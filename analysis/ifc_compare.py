import sys, json, collections, math
import ifcopenshell, ifcopenshell.util.element as ue, ifcopenshell.util.placement as up, ifcopenshell.util.unit as uu
import ifcopenshell.geom, ifcopenshell.validate

SPEC_GF = [(x, y) for x in (100, 19100) for y in (1250, 6000, 10750, 15500, 20250)] + \
          [(x, y) for x in (4850, 9600, 14350) for y in (1250,)] + [(4850, 6000), (14350, 6000)] + \
          [(8300, 6000), (10900, 6000), (4850, 8300), (8300, 8300), (8300, 12660), (14350, 13600), (8300, 17030), (9600, 20250)]
SPEC_FF = [(4850, 1250), (9600, 1250), (14350, 1250), (4850, 6000), (14350, 6000), (19100, 10750), (19100, 15500), (9600, 20250),
           (4850, 8300), (8300, 8300), (8300, 12660)]
SPEC_LEVELS = {0, 150, 3450, 6750, 9450}

def analyse(path):
    f = ifcopenshell.open(path)
    s = uu.calculate_unit_scale(f) * 1000  # -> mm
    out = {"file": path.split("/")[-1], "schema": f.schema,
           "mvd": f.header.file_description.description[0],
           "app": f.header.file_name.originating_system}
    classes = ["IfcWall", "IfcSlab", "IfcColumn", "IfcBeam", "IfcDoor", "IfcWindow", "IfcSpace", "IfcStair", "IfcStairFlight",
               "IfcRamp", "IfcRampFlight", "IfcRailing", "IfcRoof", "IfcCovering", "IfcCurtainWall", "IfcPlate", "IfcMember",
               "IfcFooting", "IfcBuildingElementProxy", "IfcOpeningElement", "IfcGrid", "IfcBuildingStorey"]
    cnt = {}
    for c in classes:
        try:
            n = len([e for e in f.by_type(c) if e.is_a() == c or c in ("IfcWall",)])
        except RuntimeError:
            n = 0
        cnt[c] = n
    out["counts"] = cnt
    pt = collections.Counter()
    for e in f.by_type("IfcSlab") + f.by_type("IfcFooting"):
        pt[(e.is_a(), str(e.PredefinedType))] += 1
    out["slab_types"] = {f"{k[0]}:{k[1]}": v for k, v in pt.items()}
    out["storeys"] = sorted([(st.Name, round((st.Elevation or 0) * s)) for st in f.by_type("IfcBuildingStorey")], key=lambda t: t[1])
    # containment
    prods = [p for p in f.by_type("IfcElement") if not p.is_a("IfcOpeningElement") and not p.is_a("IfcFeatureElement")]
    nocont = [p for p in prods if ue.get_container(p) is None and not ue.get_aggregate(p)]
    out["elements"] = len(prods)
    out["not_contained"] = len(nocont)
    out["with_material"] = sum(1 for p in prods if ue.get_material(p) is not None)
    out["with_type"] = sum(1 for p in prods if ue.get_type(p) is not None)
    out["with_qto"] = sum(1 for p in prods if any(k.startswith("Qto_") or k == "BaseQuantities" for k in ue.get_psets(p, qtos_only=True)))
    out["with_common_pset"] = sum(1 for p in prods if any(k.startswith("Pset_") and k.endswith("Common") for k in ue.get_psets(p, psets_only=True)))
    # geometry
    st = ifcopenshell.geom.settings()
    st.set("use-world-coords", True)
    ok = fail = 0
    cols = []
    xs, ys, zs = [], [], []
    for p in prods:
        if not p.Representation:
            continue
        try:
            sh = ifcopenshell.geom.create_shape(st, p)
            v = sh.geometry.verts
            X, Y, Z = v[0::3], v[1::3], v[2::3]
            xs += [min(X), max(X)]; ys += [min(Y), max(Y)]; zs += [min(Z), max(Z)]
            ok += 1
            if p.is_a("IfcColumn"):
                cols.append(((min(X) + max(X)) / 2 * 1000, (min(Y) + max(Y)) / 2 * 1000, min(Z) * 1000, (max(X) - min(X)) * 1000))
        except Exception:
            fail += 1
    out["geom_ok"], out["geom_fail"] = ok, fail
    if xs:
        out["bbox_mm"] = [round(min(xs) * 1000), round(max(xs) * 1000), round(min(ys) * 1000), round(max(ys) * 1000), round(min(zs) * 1000), round(max(zs) * 1000)]
    # columns vs spec
    gf = [c for c in cols if c[2] < 1500]
    ff = [c for c in cols if c[2] >= 1500]
    def match(found, spec):
        errs = []
        for sx, sy in spec:
            d = min((math.hypot(c[0] - sx, c[1] - sy) for c in found), default=1e9)
            errs.append(d)
        return sum(1 for d in errs if d <= 10), round(max(errs), 1) if errs else None
    out["cols_gf"] = (len(gf),) + match(gf, SPEC_GF)
    out["cols_ff"] = (len(ff),) + match(ff, SPEC_FF)
    out["col_diam"] = sorted(set(round(c[3]) for c in cols))
    # spaces
    sp = []
    for e in f.by_type("IfcSpace"):
        q = ue.get_psets(e)
        area = None
        for k, d in q.items():
            for kk, vv in d.items():
                if kk in ("NetFloorArea", "GrossFloorArea", "Area") and isinstance(vv, (int, float)):
                    area = vv; break
            if area: break
        sp.append((e.LongName or e.Name, round(area, 1) if area else None))
    out["spaces"] = sp
    # grids
    out["grid_axes"] = sorted(a.AxisTag for g in f.by_type("IfcGrid") for a in list(g.UAxes or []) + list(g.VAxes or []))
    # validation
    log = ifcopenshell.validate.json_logger()
    try:
        ifcopenshell.validate.validate(f, log, express_rules=False)
        out["schema_errors"] = len(log.statements)
        out["schema_error_samples"] = list({str(x.get("message", x))[:140] for x in log.statements})[:6]
    except Exception as ex:
        out["schema_errors"] = f"validator failed: {ex}"
    return out

if __name__ == "__main__":
    res = [analyse(p) for p in sys.argv[1:]]
    print(json.dumps(res, indent=1, default=str))

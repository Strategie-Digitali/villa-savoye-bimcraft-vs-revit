# Villa Savoye – Data sheet for the BIM test

Source: FreeCAD model of Villa Savoye by paullee0, https://github.com/paullee0/FreeCAD_Villa-Savoye (extracted by script on 27 Oct 2026), cross-checked against web sources.
Legend: **[M]** read from the model · **[M+W]** model confirmed by web sources · **[A]** accepted simplification (the model differs from the real building; kept on purpose for a fair test).
Units: mm. Origin and axes are those of the FreeCAD model, so results can be compared numerically against it.
Convention: side y=0 = entrance front (ground-floor curved glazing); x increases to the right when facing the entrance.

## 1. Grids [M+W]
- Square 5×5 grid, spacing **4750** (reduced from 5000 in 1928).
- Numbered grids along X: **1** x=100 · **2** x=4850 · **3** x=9600 · **4** x=14350 · **5** x=19100
- Lettered grids along Y: **A** y=1250 · **B** y=6000 · **C** y=10750 · **D** y=15500 · **E** y=20250
- Grid length: at least 1500 beyond the building footprint on each side.

## 2. Levels [M]
| Level | Elevation (top of slab) | Notes |
|---|---|---|
| Ground | 0 | |
| Ground Floor | +150 | slab 150 |
| First Floor (piano nobile) | +3450 | slab 200, underside +3250 |
| Roof Terrace / Solarium | +6750 | slab 200 |
| Solarium Top | +9450 | top of curved walls +9550 |

Floor-to-floor 3300. Overall height ~9.55 m.

## 3. Pilotis [M] (diameter [A])
- Round columns **Ø190** (as in the model; the real ones are probably larger).
- Ground floor, perimeter: every grid intersection on grids 1 and 5 (A–E) + rows A and B on grids 2, 3, 4 (B3 excluded).
- Off-grid columns (ground floor): (8300, 6000) · (10900, 6000) either side of the entrance · (4850, 8300) · (8300, 8300) · (8300, 12660) · (14350, 13600) · (8300, 17030) · (9600, 20250).
- Note: the centre C3 (9600, 10750) has **no** column, because the ramp is there. The grid is deliberately irregular.
- First floor: columns at A2, A3, A4, B2, B4, C5, D5, E3 + (4850, 8300), (8300, 8300), (8300, 12660).

## 4. Ground floor (+150) [M]
- Set-back volume: x 3050–16160, y ~4100–21500.
- Curved (U-shaped) façade wall towards the entrance: **centre (9605, 10750), outer R 6555, thickness 200**, height 3250. It continues with straight segments to the rear front (y 21500, white wall x 4750–14460).
- Curved entrance glazing: frame on the same centre, R ~6530, height 3100 (two segments: x 3060–8118 and x 11081–14046).
- Entrance door: glazed, on the axis, x 8155–11045, at y 4700, up to +3250.
- Rear ribbon window: x 5100–14110, z 1000–3100.
- Interior partitions 100 thick, height 3100. Curved segments: R 340–440 (bathrooms), R 2284–2384 centre (12010, 15921).

## 5. First floor (+3450) [M+W]
- Outer box: **x 0–19200 · y 0–21500**, wall 200, height 3800 (from +3250 to +7050). Cantilever beyond grids A and E of ~1150–1250 [M+W: 19 × 21.5 m].
- **Ribbon windows**: sill **+1055** above floor (z 4505), height **1040** (up to z 5545).
  - Front (y=0): continuous, x 205–18994.
  - Rear (y=21500): continuous, x 206–18995.
  - Left (x=0): 4 segments, y 1351–5892 · 6102–10643 · 10853–15394 · 15604–20145.
  - Right (x=19200): y 1355–5896; the rest of this side opens onto the terrace (unglazed openings at the same height).
- Roof garden / terrace: the area x ~9700–19000, y ~6300–15400.
- Living room glazing onto the terrace: y 6300, x 9701–18995, **height 3090** (from +3455 to +6545) [M+W: "9 m × 3 m"].
- Terrace planter: low wall height 400, x 11490–14450, y 6300–15400.
- Interior doors 1100×2100 (12 in the model).
- Rooms (net areas from the model): 26.8 · 82.1 · 18.5 · 41.4 m²; gross floor area ~397 m² [W: ~480 m² gross overall].

## 6. Ramp [M]
Two side-by-side flights with a landing; repeated identically between the first floor and the terrace.
- Flight 1 (up): x 9700–10800 (width 1100), from y 8390 to y 16930, from +150 to +1800 (slope ~19%).
- Landing: x 8400–10800, y 16930–18210, at +1800.
- Flight 2 (return): x 8400–9500 (width 1100), from y 16930 to y 8390, from +1800 to +3450.
- Spine wall between the flights: x 9550–9650, thickness 100.
- First floor to terrace: same geometry, +3450 → +5100 → +6750.
- Guardrails: height 900.

## 7. Stair [M] / [A]
- Footprint: x 5050–7450, y 8490–10290 (2400 × 1800).
- Three straight flights with landings per storey, as in the model. **[A] The real stair is helical**; the flights version is kept because it is fair to both tools and comparable with the model.
- Arrival at roof level: cylindrical stair tower R 900–1000, centre (6551, 9390).

## 8. Solarium (+6750) [M]
- Curved walls height 2800 (up to +9550), thickness 100:
  - centre (4431, 7819), R 6245–6345
  - centre (4160, 4312), R 2727–2827
  - centre (15070, 3050), R 1900–2000
- Wall extents: x 1335–17055, y 1050–10390.
- Planters height 400 along the curved walls; built-in table height ~900 [M].

## 9. Expected views (for the drawings)
- **Longitudinal section** along the ramp axis: x = 10250, from y –2000 to y 23500, looking west.
- **Cross section** through terrace and living room: y = 10750 (grid C), from x –2000 to x 21000, looking north.
- 4 elevations, 3D axonometric view from the south-west (entrance side).

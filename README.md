# Villa Savoye: BIMCraft vs Revit, driven by the same AI agent

Same prompt, same Claude model, same data sheet. One run in [BIMCraft](https://github.com/IPedrax/BIMCraft), one in Revit 2026, each connected to Claude through MCP (Model Context Protocol). The agent worked alone: no questions, no human help.

Everything the agent produced is in this repository, so you can check the results yourself.

## Results

| | BIMCraft 0.8.0 | Revit 2026 |
|---|---|---|
| Time to finish | **11:26** | 31:33 |
| Tokens used | **~255k** | ~338k |
| Columns placed as specified (34) | 34/34, max error 0.2 mm | 34/34, max error 0.2 mm |
| Levels | 7 (2 helper levels added for the ramp) | **5, as specified** |
| Ramp in IFC | **IfcRamp + 4 IfcRampFlight** | 4 IfcRampFlight, no IfcRamp |
| Floor slabs in IFC | **IfcSlab FLOOR** | IfcSlab BASESLAB (modelled as foundation slabs) |
| Elements with type, common Pset, quantities | 0% | **~100%** |
| IFC schema validation | 2 errors | **0 errors** |
| A0 sheet | 12 views, coloured 3D, sparse elevations | 12 views, cleaner elevations, title block drawn with lines |

In short: BIMCraft was 2.8× faster with cleaner BIM semantics, because it gives the agent a native command for every element. Revit still produced richer information and more mature drawings, but the agent had to write C# and work around missing tools to model.

The IFC figures come from `analysis/ifc_compare.py` (IfcOpenShell 0.9); raw output in `analysis/ifc_compare_results.json`.

## What's inside

| Folder | Content |
|---|---|
| `prompt/` | The exact prompts sent to both runs and the data sheet with all dimensions |
| `bimcraft/` | Native `.bimcraft` model, IFC4 export, A0 sheet as PDF, the agent's final report |
| `revit/` | Native `.rvt` model, IFC4 export, A0 sheet as PDF, the agent's final report |
| `analysis/` | The IFC comparison script and its results |
| `video/` | The side-by-side video, 16:9 and 4:5 |

## How the test was run

- **Model:** Claude Opus 5.5, same effort setting, fresh session for each run.
- **Prompt:** identical for both runs (`prompt/prompts.txt`). Message 1 checked the connection; message 2 asked for the full model and drawings.
- **Data sheet:** dimensions extracted from the FreeCAD model of Villa Savoye by paullee0 ([FreeCAD_Villa-Savoye](https://github.com/paullee0/FreeCAD_Villa-Savoye)): 5×5 grid at 4750 mm, levels, pilotis, ribbon windows, ramp, stair, solarium. The FreeCAD model itself is not included here; get it from its repository.
- **Deliverables asked:** grid-based model, dimensioned plans, 2 sections, 4 elevations, 3D view, one A0 sheet, IFC and PDF export.
- **Timing:** from the first message to the end of the work, read on the screen recording.

## Limits of this test

- The two runs were recorded separately and aligned at the start in the video. It was not a live race.
- One run per tool: results may vary between runs.
- The comparison is "tool + its MCP server". The Revit MCP used here has no native modelling commands, so the agent wrote C# through the Revit API; part of the gap comes from that.
- The data sheet simplifies the building on purpose: straight-flight stair instead of the helical one, 190 mm columns as in the reference model. It was ambiguous on the start and end of the solarium arcs, and the two runs interpreted them differently.
- Around minute 5 of the BIMCraft recording the screen-capture window moved and the app was out of frame for about 1.5 minutes. BIMCraft kept working; the 11:26 includes that stretch.

## License

Content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Analysis script: MIT. See `LICENSE`.

## Credits

Test by [Strategie Digitali](https://strategiedigitali.io). BIMCraft is an open-source project by IPedrax. The reference geometry comes from [paullee0's FreeCAD model of Villa Savoye](https://github.com/paullee0/FreeCAD_Villa-Savoye).

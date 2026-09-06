# Render Autodesk VRED scenes on Deadline Cloud

The
[vred\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vred_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vred_render")
job bundle on the GitHub website renders VRED scenes using either VRED Core or VRED Pro in
headless mode. It uses VRED's Python API through the
`VRED_RenderScript_DeadlineCloud.py` script, which controls the
rendering process, converts job template parameters into VRED API calls, and
manages settings such as quality, resolution, and tiling.

The bundle provides two template options:

- **Basic template**
  (`template.yaml`): Standard rendering functionality.
- **Tiling template**
  (`template_tiling.yaml`): Adds region/tile-based rendering
  and a tile assembly step that combines rendered tiles into final images.
  To use this template, rename it to `template.yaml`.
  The job parameters cover input and output paths, render settings such as
  image dimensions and DPI, render quality presets (Analytic, Realistic,
  Raytracing, NPR), NVIDIA DLSS options, frame control, animation settings,
  and tile-based rendering. When you use tile-based rendering, you must also
  enable GPU raytracing to prevent solid black tile outputs.

To run this bundle on a service-managed fleet, your queue needs access
to the `deadline-cloud` conda channel and a GPU-enabled worker.
The
[vredcore-2026
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026") on the GitHub website builds a VRED Core conda
package. For tile assembly, the rendering environment must include the
`imagemagick` conda package from the `conda-forge`
channel.

Submit the bundle:

```
deadline bundle gui-submit vred_render/
```

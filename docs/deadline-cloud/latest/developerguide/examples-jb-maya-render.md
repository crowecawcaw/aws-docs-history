# Render Autodesk Maya scenes on Deadline Cloud

The deadline-cloud-samples repository on the GitHub website includes the
[maya\_cli\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/maya_cli_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/maya_cli_render")
job bundle, which renders a Maya software renderer scene with the Maya CLI
`Render` command. It runs one task per frame using an Open Job
Description parameter space and restricts execution to Linux workers through
host requirements.

The bundle includes a sample scene with falling gears that uses the
Bullet physics plugin, along with instructions for creating similar scenes.
The same repository on the GitHub website includes the
[maya\_arnold\_ass\_export\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/maya_arnold_ass_export_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/maya_arnold_ass_export_render")
bundle, a related two-step pipeline: a single export task opens the Maya
scene with `mayapy` and writes per-frame Arnold `.ass`
files, then a render step distributes per-frame `kick` tasks
across workers. Job attachments automatically synchronizes the exported
`.ass` files from the export worker to the render workers.

To run these bundles, your queue needs Maya available through a queue
environment. The
[maya
conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026") on the GitHub website build conda packages you can
publish to your queue's S3 conda channel. The
`maya-mtoa` recipes also provide the
`kick` binary used by the export-and-render pipeline.

Submit the bundle:

```
deadline bundle gui-submit maya_cli_render/
```

For an example that exports `.ass` files from Maya and renders
them in a single job, use:

```
deadline bundle submit maya_arnold_ass_export_render/ \
    -p MayaSceneFile=`path-to-scene.ma` \
    -p Frames=1-100 \
    -p OutputDir=`path-for-outputs`
```

For more information about job bundles, see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md").

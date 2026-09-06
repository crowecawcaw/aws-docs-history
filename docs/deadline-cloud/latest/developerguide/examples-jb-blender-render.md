# Render Blender scenes on Deadline Cloud

The
[blender\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_render")
job bundle on the GitHub website shows how to support a CLI application in
about 100 lines of YAML. Most of the template is parameter metadata that
defines parameter names, types, defaults, and user interface controls. The
step definition includes a parameter space that creates a task for each
frame in the Frames job parameter, and a short script that substitutes job
parameters and the Frame task parameter into a command for each task.

Submit the bundle with the GUI submitter:

```
deadline bundle gui-submit blender_render/
```

Or submit from the CLI with parameter values:

```
deadline bundle submit blender_render/ \
    -p BlenderSceneFile=`path-to-scene.blend` \
    -p OutputDir=`path-for-outputs`
```

To run this bundle, your queue needs Blender available through a queue
environment. The samples repository on the GitHub website includes the
[blender-4.5
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5") and other Blender recipes that build conda packages you
can publish to your queue's S3 conda channel.

For more information about job bundles, see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md").

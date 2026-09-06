# Render Foundry Nuke scripts on Deadline Cloud

The
[nuke\_render
job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/nuke_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/nuke_render") on the GitHub website renders Nuke scripts in headless
mode with the `nuke -x` command. The job creates one task per
frame using the Open Job Description parameter space feature, and is
restricted to Linux workers through host requirements.

The bundle includes a sample `motionblur3d_10.nk` Nuke script
based on Foundry's MotionBlur3D example, configured with relative file paths
and a pre-configured Write node.

To run this bundle, your queue needs Nuke available through a queue
environment that installs the `nuke` and `nuke-openjd`
conda packages. The
[nuke-16.0
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0") on the GitHub website builds a Nuke conda package you
can publish to your queue's S3 conda channel.

Submit the bundle with custom parameters:

```
deadline bundle submit nuke_render/ \
  --name "My Nuke Render" \
  -p Frames="1-10" \
  -p NukeScript=`path-to-script.nk` \
  -p OutputDir=`path-for-outputs`
```

Or open the GUI submitter:

```
deadline bundle gui-submit nuke_render/
```

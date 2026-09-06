# Render a turntable video with Maya and Arnold on Deadline Cloud

The
[turntable\_with\_maya\_arnold job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold")
on the GitHub website takes an OBJ geometry file as input and outputs a turntable
render video. A turntable render is a 360-degree rotation of a rendered
3D model that allows inspection of the geometry without a 3D viewer.

This bundle demonstrates how to create utility jobs that are easy to
submit from a GUI. The job template defines a pipeline of three steps
connected with a dependency chain:

1. A scene preparation task runs as a single MayaPy task that loads a
   base Maya scene, imports the input geometry file, and adjusts scene
   properties.
2. An image sequence rendering step runs a separate task per frame
   across many worker hosts.
3. A video encoding task runs a single FFmpeg task that combines the
   rendered frames into a video.
   The bundle embeds a base Maya scene file with a camera, lighting, and
   default geometry, and provides job parameters that you can use for either
   GUI submission or automation scripting. By specifying conda channel and
   package parameter values, the job runs successfully on a farm created with
   the Deadline Cloud default onboarding.

You can launch the GUI submitter by creating a desktop shortcut. On
Windows, create a file called
`Submit Turntable to Deadline Cloud.bat` with content like the
following:

```
@call C:\`DEADLINE_CLI_INSTALLATION`\deadline bundle gui-submit C:\`DEADLINE_CLOUD_SAMPLES`\turntable_with_maya_arnold
```

If you accept all default settings, the job renders a turntable with
placeholder geometry. You can also download an OBJ file such as
[stanford-bunny.obj](https://github.com/alecjacobson/common-3d-test-models/blob/master/data/stanford-bunny.obj "https://github.com/alecjacobson/common-3d-test-models/blob/master/data/stanford-bunny.obj")
from the common-3d-test-models repository on the GitHub website, and select
it for the input geometry parameter.

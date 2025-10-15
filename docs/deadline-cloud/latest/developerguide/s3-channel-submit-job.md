# Test your package with a Blender 4.2 render job

After you have the Blender 4.2 package built and your production queue configured to use
 the S3 conda channel, you can submit jobs to render with the package. If you don't have a
 Blender scene, download the Blender 3.5 - Cozy Kitchen scene from the [Blender demo files](https://www.blender.org/download/demo-files "https://www.blender.org/download/demo-files") page.

The Deadline Cloud samples GitHub repository that you downloaded earlier contains a sample job to
 render a Blender scene using the following commands:


```
deadline bundle submit blender_render \
     -p CondaPackages=blender=4.2 \
     -p BlenderSceneFile=/path/to/downloaded/blender-3.5-splash.blend \
     -p Frames=1
```
You can use the Deadline Cloud monitor to track the progress of your job:

1. In the monitor, select the task for the job you submitted, then select the option to
 view the log.
2. On the right side of the log view, select the **Launch Conda**
 session action.
You can see that the action searched for Blender 4.2 in the two conda channels
 configured for the queue environment, and that it found the package in the S3
 channel.

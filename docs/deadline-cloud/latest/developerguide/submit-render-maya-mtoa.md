# Test your package with a Maya render job

After you have the Maya 2025 and MtoA packages built, you can submit 
 jobs to render with the package. The [turntable with Maya/Arnold](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold") job bundle sample renders an animation with 
 Maya and Arnold. This sample also uses FFmpeg to encode a video. You can 
 add the conda-forge channel to the list of default `CondaChannels` in your conda queue 
 environment to provide a source for the `ffmpeg` package.

From the `job_bundles` directory in your git clone of [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples"), run 
 the following command.


```
deadline bundle submit turntable_with_maya_arnold
```
You can use the Deadline Cloud monitor to track the progress of your job:

1. In the monitor, select the task for the job you submitted, then select the option to
 view the log.
2. On the right side of the log view, select the **Launch Conda**
 session action.
You can see that the action searched for maya and maya-mtoa in the conda 
 channels configured for the queue environment, and that it found the packages in the S3 channel.

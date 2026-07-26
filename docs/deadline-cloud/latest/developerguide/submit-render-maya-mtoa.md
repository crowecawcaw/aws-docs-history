# Test your packages with a Maya render job

After you build the Maya, MtoA, and
`maya-openjd` packages, you can test them with a render job. The Deadline Cloud
samples repository contains a [turntable with Maya/Arnold](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold") job bundle that
renders an animation using Maya and Arnold. The job
bundle also uses FFmpeg to encode a video, which is available from the
`conda-forge` channel.

## Testing locally

You can run the job template on your workstation using the [Open Job Description
CLI](https://github.com/OpenJobDescription/openjd-cli#readme "https://github.com/OpenJobDescription/openjd-cli#readme"). Install the CLI with `pip`.

```
pip install openjd-cli
```

From the `job_bundles` directory in the samples repository, run the
following command. The `ErrorOnArnoldLicenseFail=false` parameter tells
Arnold to render with watermarks instead of failing when no license is
available.

```
openjd run turntable_with_maya_arnold/template.yaml \
    --environment ../queue_environments/conda_queue_env_pyrattler.yaml \
    -p CondaPackages="maya maya-mtoa maya-openjd ffmpeg" \
    -p CondaChannels="file://$HOME/my-conda-channel conda-forge" \
    -p ErrorOnArnoldLicenseFail=false \
    -p FrameRange=1-5
```

The `--environment` option applies the conda queue environment, which
creates a conda virtual environment with the packages specified in
`CondaPackages`. The `CondaChannels` parameter includes both
the local channel for your custom packages and `conda-forge` for
`ffmpeg`. If you published to an Amazon S3 channel instead of a local channel,
replace the `file://` path with your `s3://` channel
URL.

When the job completes, the rendered output is in the
`turntable_with_maya_arnold/output/` directory.

## Testing on Deadline Cloud

After you configure your production queue to use the Amazon S3 conda channel, submit
the render job to Deadline Cloud. Add the `conda-forge` channel to the
`CondaChannels` parameter in your conda queue environment to provide a
source for `ffmpeg` and the Python dependencies that the adaptor
requires. From the `job_bundles`
directory in the samples repository, run the following command.

```
deadline bundle submit turntable_with_maya_arnold
```

Use the Deadline Cloud monitor to track the progress of the job. In the monitor,
select the task for the job and choose **View logs**. Select the
**Launch conda** session action to verify that the
`maya`, `maya-mtoa`, and `maya-openjd` packages
were found in the Amazon S3 channel.

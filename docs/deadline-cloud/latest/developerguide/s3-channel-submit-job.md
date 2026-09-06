

# Test your package with a Blender render job
<a name="s3-channel-submit-job"></a>

After you build the Blender 4.5 package, you can test it with a render job. If you do not have a Blender scene, download the Blender 3.5 - Cozy Kitchen scene from the [Blender demo files page](https://www.blender.org/download/demo-files) on the Blender website. The Deadline Cloud samples repository contains a `blender_render` job bundle and a conda queue environment that you can use for both local and cloud testing.

## Testing locally
<a name="blender-test-locally"></a>

You can run the job template on your workstation using the [Open Job Description CLI](https://github.com/OpenJobDescription/openjd-cli#readme) on the GitHub website. Install the CLI with `pip`.

```
pip install openjd-cli
```

From the `job_bundles` directory in the samples repository, run the following command. Replace {{/path/to/scene.blend}} with the path to your Blender scene file.

```
openjd run blender_render/template.yaml \
    --environment ../queue_environments/conda_queue_env_pyrattler.yaml \
    -p CondaPackages=blender=4.5 \
    -p CondaChannels=file://$HOME/my-conda-channel \
    -p BlenderSceneFile={{/path/to/scene.blend}} \
    -p Frames=1
```

The `--environment` option applies the conda queue environment, which creates a conda virtual environment with the packages specified in `CondaPackages`. The `CondaChannels` parameter tells the queue environment where to find the packages. If you published to an Amazon S3 channel instead of a local channel, replace the `file://` path with your `s3://` channel URL.

## Testing on Deadline Cloud
<a name="blender-test-deadline-cloud"></a>

After you configure your production queue to use the Amazon S3 conda channel, you can submit the render job to Deadline Cloud. From the `job_bundles` directory in the samples repository, run the following command.

```
deadline bundle submit blender_render \
    -p CondaPackages=blender=4.5 \
    -p BlenderSceneFile={{/path/to/scene.blend}} \
    -p Frames=1
```

Use the Deadline Cloud monitor to track the progress of the job. In the monitor, select the task for the job and choose **View logs**. Select the **Launch conda** session action to verify that the package was found in the Amazon S3 channel.
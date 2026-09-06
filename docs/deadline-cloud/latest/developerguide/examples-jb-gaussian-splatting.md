

# Train 3D Gaussian Splatting from video on Deadline Cloud
<a name="examples-jb-gaussian-splatting"></a>

The [gsplat\_pipeline job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline) on the GitHub website runs a [3D Gaussian Splatting pipeline](https://aws.amazon.com/blogs/spatial/3d-gaussian-splatting-performant-3d-scene-reconstruction-at-scale/). The bundle takes a video file as input and produces a Gaussian Splatting `.ply` file as output. After downloading the output, you can view it in any Gaussian Splatting viewer such as [SuperSplat](https://github.com/playcanvas/supersplat) on the GitHub website.

The pipeline runs a single task that performs the following steps:

1. Extracts video frames with [FFmpeg](https://www.ffmpeg.org/) on the FFmpeg website.

1. Solves Structure-from-Motion with [COLMAP](https://colmap.github.io/) on the COLMAP website and [GLOMAP](https://github.com/colmap/glomap) on the GitHub website, saving the pinhole model and undistorted images.

1. Trains Gaussian Splatting with one of three trainers: [NeRF Studio splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html) on the Nerfstudio website, [Splatfacto in the Wild](https://docs.nerf.studio/nerfology/methods/splatw.html) on the Nerfstudio website, or the [simple\_trainer.py gsplat library example](https://docs.gsplat.studio/main/examples/colmap.html) on the gsplat website. Output is saved to the `.ply` file you specify.

To run this bundle, deploy the [CUDA farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm) on the GitHub website to create a Deadline Cloud farm with a CUDA GPU fleet. Then build the [NeRF Studio conda package](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio) on the GitHub website and publish it to your S3 conda channel.

If you only need the default `NERFSTUDIO` (splatfacto) trainer, you don't need the CUDA farm template or the custom NeRF Studio conda package. The minimum requirements are a Deadline Cloud farm with a GPU fleet, a queue environment that includes `conda-forge`, and the following conda packages: `ffmpeg colmap glomap nerfstudio cuda`.

To capture a usable video, follow these tips:
+ Use a wide field of view so that more objects are common between image pairs for Structure-from-Motion to use.
+ Turn off video stabilization to preserve identical lens optics between frames.
+ Capture with slow and steady motion. Keep moving the camera and avoid stopping and panning from a single location.

From the `job_bundles` directory of the samples repository, submit the job:

```
deadline bundle gui-submit gsplat_pipeline
```

On the *Job-specific settings* tab, select paths for both the input video file and the output `.ply` file.

For a complete walkthrough that covers capturing a video, submitting and monitoring the job, and viewing the trained result, see [Train 3D Gaussian Splatting from your own video](tutorial-gsplat-pipeline.md).
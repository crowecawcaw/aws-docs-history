# Train 3D Gaussian Splatting from your own video

This tutorial walks you through training your own 3D Gaussian
Splatting point cloud from a video that you capture. You submit the
[Gaussian Splatting pipeline job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline")
on the GitHub website to your Deadline Cloud farm. The job takes a video file as input and
produces a Gaussian Splatting `.ply` file as output. When the
job completes, you can view the result in any Gaussian Splatting viewer,
such as [SuperSplat](https://github.com/playcanvas/supersplat "https://github.com/playcanvas/supersplat")
on the GitHub website.

The pipeline runs a single task that:

1. Extracts video frames with
   [FFmpeg](https://www.ffmpeg.org/ "https://www.ffmpeg.org/") on the FFmpeg website.
2. Solves Structure-from-Motion with
   [COLMAP](https://colmap.github.io/ "https://colmap.github.io/") on the COLMAP website and
   [GLOMAP](https://github.com/colmap/glomap "https://github.com/colmap/glomap") on the GitHub website, saving
   the pinhole model and undistorted images.
3. Trains Gaussian Splatting with
   [NeRF Studio splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html "https://docs.nerf.studio/nerfology/methods/splat.html") on the Nerfstudio website,
   [Splatfacto in the Wild](https://docs.nerf.studio/nerfology/methods/splatw.html "https://docs.nerf.studio/nerfology/methods/splatw.html") on the Nerfstudio website, or the
   [simple\_trainer.py gsplat library example](https://docs.gsplat.studio/main/examples/colmap.html "https://docs.gsplat.studio/main/examples/colmap.html") on the gsplat website, and saves the output to the
   `.ply` file you specify.
   The following video demonstrates the Gaussian Splatting pipeline
   workflow on Deadline Cloud.

**Estimated time:** A few hours,
including farm setup. Depending on the input video and the settings you
select, the job itself can finish in 10 minutes or take hours.

Running this tutorial incurs charges for the GPU worker instances
that process the job. The [Understand the cost of your training jobs](#tutorial-gsplat-cost "#tutorial-gsplat-cost") section shows how to review those
costs.

## Overview

To complete this tutorial, follow these steps:

1. Complete the prerequisites.
2. Set up your farm.
3. Capture a video of a subject.
4. Submit the `gsplat_pipeline` job.
5. Monitor the job.
6. Download and view the Gaussian Splatting `.ply`
   file.
7. Clean up resources.

## Prerequisites

Before you begin, complete the following setup:

1. [Create an AWS account](https://aws.amazon.com/resources/create-account/ "https://aws.amazon.com/resources/create-account/") if you do not already have one.

## Set up your farm

You need a Deadline Cloud farm with a CUDA GPU fleet to run the Gaussian
Splatting job. To set one up, complete the following steps:

1. Follow the
   [CUDA farm sample CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm") instructions on the GitHub website to create a Deadline Cloud
   farm that has a CUDA GPU fleet and can build conda packages.
2. Follow the
   [NeRF Studio sample conda package recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio") instructions on the GitHub website to build a
   NeRF Studio conda
   package into the Amazon S3 channel of your CUDA farm. For more information, see [NeRF Studio](https://docs.nerf.studio/ "https://docs.nerf.studio/") on the Nerfstudio website.

###### Note

If you only need the default `NERFSTUDIO` (splatfacto)
trainer, you don't need to deploy the CUDA farm CloudFormation template or
build the custom NeRF Studio conda package. The minimum requirements
are a Deadline Cloud farm with a GPU fleet, a queue environment with
`conda-forge` included in the conda channels, and the
conda packages `ffmpeg colmap glomap nerfstudio cuda`. The
`GSPLAT_SIMPLE_TRAINER` and
`NERFSTUDIO_SPLATFACTOW` trainer options depend on
commands that are only available in the custom-built NeRF Studio
conda package.

## Capture a video of a subject

You can use a video-capable camera like your smartphone to capture
a video of a subject for your Gaussian Splatting. Consider the
following tips:

- Use a wide field of view, such as zoom level 0.5 in your camera
  app. With a wider field of view, more objects are common between
  image pairs for Structure-from-Motion to use.
- Turn off video stabilization. Turning it off preserves
  identical lens optics between all frames, and can increase the
  quality of solves.
- Plan your camera motion depending on the subject. To capture an
  object, like a bench or a bicycle, orbit around the subject a few
  times at different heights and distances. To capture a room
  interior, follow around the outside of the room with the camera
  facing inwards, and repeat at different camera heights. To capture
  less structured spaces such as outside terrain, think about how to
  include everything you want in your Gaussian Splatting, and how to
  capture all of it from multiple different angles.
- Capture the video with slow and steady motion.
- Keep moving the camera. Avoid stopping and panning from a
  single location.

Copy the video you captured from your camera to your computer for
submitting to the farm.

## Submit the gsplat\_pipeline job

###### To submit the Gaussian Splatting job

1. If you don't have a local copy of the
   [deadline-cloud-samples repository](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples") on the GitHub website, clone it or
   [download it as a ZIP](https://github.com/aws-deadline/deadline-cloud-samples/archive/refs/heads/mainline.zip "https://github.com/aws-deadline/deadline-cloud-samples/archive/refs/heads/mainline.zip"):

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
cd deadline-cloud-samples/job_bundles
```

2. From the `job_bundles` directory, run the
   following command:

```
deadline bundle gui-submit gsplat_pipeline
```

3. Switch to the **Job-specific settings** tab
   and select paths for both the **Input Video File**
   and the **Output Ply File**.
4. Choose **Submit**, or customize the settings
   first. If the input video has higher complexity, you may need to
   increase the **Approximate Image Count**
   value.

You can also select which Gaussian Splatting trainer to use and
customize the CLI options for it. For example, to use the Monte Carlo
Markov chain (MCMC) trainer with the bilateral grid option to produce
up to 2 million splats, make the following changes:

1. Switch the **Gaussian Splatting Trainer** from
   `NERFSTUDIO` to `GSPLAT_SIMPLE_TRAINER`.
2. Modify the **GSplat Simple Trainer Options**
   text from `--strategy.cap-max 1000000` to
   `--strategy.cap-max 2000000` to get 2 million splats,
   and from `--no-use-bilateral-grid` to
   `--use-bilateral-grid` to enable the bilateral grid
   option.

###### Note

If you select an input video or options that require higher
memory usage than the CUDA fleet provides, you need to update the
fleet's minimum settings. Re-deploy your CloudFormation template with updated
parameter values, or edit the settings from the Deadline Cloud console.

## Monitor the job

After you submit the job, you can monitor its status from the
Deadline Cloud monitor job table. Depending on the input video and the settings you
selected, the job might finish in 10 minutes or take hours.

When the job is running, open the context menu for the task and
choose **View logs** to open the log view. As the
pipeline goes through its steps, it updates the status message visible
in the task run details.

If you encounter errors, the log output in this view helps you
track down the cause. Common causes include running out of memory or
failing to solve for the camera poses. The pipeline can fail during any
of these steps: FFmpeg frame extraction, GLOMAP Structure-from-Motion
solving, or NeRF Studio training. To resolve errors, either adjust the
fleet infrastructure or use a lower image resolution or image
count.

## Download and view the Gaussian Splatting .ply

###### To download and view the output

1. When the job completes successfully, open the context menu for
   the completed task in the **Tasks** table of
   Deadline Cloud monitor and choose
   **Download output**. Depending on your settings,
   it either shows the download progress or presents a CLI command you
   can use to download. Deadline Cloud saves the `.ply` file to the
   location you selected when submitting the job.
2. To view the result in your browser, open the
   [SuperSplat Editor](https://superspl.at/editor "https://superspl.at/editor") on the SuperSplat website
   and drag the file from your operating system's file browser
   onto the SuperSplat page.
3. Toggle the **Show/Hide Splats** option, then
   rotate and move around the scene to find the subject of your
   capture.

With SuperSplat, you can also edit your Gaussian Splatting. For
example, you can select a sphere, invert the selection, and delete the
splats outside it to crop the scene. The
[SuperSplat documentation](https://github.com/playcanvas/supersplat/wiki "https://github.com/playcanvas/supersplat/wiki") on the GitHub website explains how to use the editor, or you can import
your `.ply` file into your tool of choice.

## Understand the cost of your training jobs

Deadline Cloud monitor includes a usage explorer feature that estimates the cost of
the jobs you run, showing how much each training costs. If you're
comfortable running your tests during off-peak hours when CUDA-capable
instances are available with low enough interruption rates, a spot CUDA
fleet costs less than an on-demand fleet. Usage explorer does not show
costs outside of your job run time, such as idle worker instance time
or storage on your Amazon S3 bucket.

## Clean up

To avoid ongoing charges, clean up the resources that you created
for this tutorial:

###### To clean up tutorial resources

1. If you deployed the CUDA farm CloudFormation template, delete the CloudFormation
   stack from the CloudFormation console.
2. If you used an existing farm and created a GPU fleet
   specifically for this tutorial, stop or delete that fleet. If you
   used a pre-existing shared fleet, leave it in place.

## Next steps

You can pull apart, edit, and remix the
`gsplat_pipeline` job bundle to suit your needs. You can
customize your own 3D reconstruction pipeline, or follow the same
patterns to run different CUDA workloads on your Deadline Cloud CUDA farm. The following directions are documented in the
[sample README](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline#this-sample-is-a-starting-point "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline#this-sample-is-a-starting-point") on the GitHub website:

- Run the job anywhere with the
  [Open Job Description CLI](https://github.com/OpenJobDescription/openjd-cli "https://github.com/OpenJobDescription/openjd-cli") on the GitHub website, such as locally or on an Amazon EC2
  instance, instead of on your farm.
- Decompose the pipeline's single task into multiple Open Job
  Description steps connected by dependencies, following the pattern
  in the
  [Job Development Progression sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_dev_progression "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_dev_progression") on the GitHub website. Separate steps can run on
  different fleets, such as a CPU-only fleet for frame extraction and
  a GPU fleet for training.
- Split the pipeline into multiple jobs with different structure.
  For example, one job to solve Structure-from-Motion once, and a
  second job to iteratively try different variations of Gaussian
  Splatting training parameters.

## Related resources

The following resources provide additional information:

- [Sample source code](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gsplat_pipeline") on the GitHub website
- [CUDA farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm") on the GitHub website
- [NeRF Studio conda package recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio") on the GitHub website
- [3D Gaussian Splatting blog post](https://aws.amazon.com/blogs/spatial/3d-gaussian-splatting-performant-3d-scene-reconstruction-at-scale/ "https://aws.amazon.com/blogs/spatial/3d-gaussian-splatting-performant-3d-scene-reconstruction-at-scale/")
- [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md")

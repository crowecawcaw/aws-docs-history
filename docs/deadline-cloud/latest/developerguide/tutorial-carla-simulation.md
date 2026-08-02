# Run an autonomous driving simulation sweep with CARLA

This tutorial walks you through running a
[CARLA](https://carla.org/ "https://carla.org/") autonomous driving
simulation parameter sweep with configurable multi-sensor capture. You
build a Docker image, push it to Amazon Elastic Container Registry (Amazon ECR), and submit the
[autonomous driving CARLA job bundle on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla")
to a GPU fleet on your Deadline Cloud farm.

The job runs a lane-change cut-in scenario where an NPC vehicle
starts behind the ego vehicle, accelerates to position itself 20 meters
ahead of the ego during a 105-second get-ahead phase, then cuts into the
ego's lane. It sweeps across configurable ego speeds, NPC speeds, and NPC
starting distances, creating a task for each parameter combination
(default 2×2×2 = 8 tasks). Each task captures multi-sensor
data from the camera viewpoints you select and produces the following
output:

- RGB frames from each selected camera viewpoint
- Semantic segmentation frames
- LiDAR point clouds (`.ply`)
- 2D and 3D bounding boxes (KITTI format)
- Per-camera scenario videos (H.264 MP4)
- Stitched grid video (if you select multiple cameras)
  The following video demonstrates the CARLA simulation sweep workflow
  on Deadline Cloud.

**Estimated time:** 1–2 hours,
including the Docker image build. Tasks typically complete in about
13 minutes each.

Running this tutorial incurs charges for the GPU worker instances
that process the tasks and for Amazon ECR image storage.

## Overview

To complete this tutorial, follow these steps:

1. Complete the prerequisites.
2. Set up your farm.
3. Build and push the Docker image.
4. Submit the simulation job.
5. Monitor the job.
6. Review the output.
7. Clean up resources.

## Prerequisites

Before you begin, complete the following setup:

1. [Create an AWS account](https://aws.amazon.com/resources/create-account/ "https://aws.amazon.com/resources/create-account/") if you do not already have one, ensuring
   it has access to GPU instances (`g6.4xlarge`
   recommended).
2. Install
   [Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/")
   locally for building the CARLA image.
3. Create an
   [Amazon ECR](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/") repository
   in your account to host the built image.
4. Install the
   [Deadline Cloud CLI](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") locally.

## Set up your farm

You need a Deadline Cloud farm with a queue that has a conda queue
environment (channels: `conda-forge`, packages:
`ffmpeg`) and a GPU fleet (minimum: 1 NVIDIA GPU with
16 vCPU and 64 GiB memory).

**IAM permissions** – Your
queue role needs Amazon ECR pull permissions, because the task script runs
`docker pull` under queue role credentials. Attach a policy
like the following:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "arn:aws:ecr:`REGION`:`ACCOUNT_ID`:repository/*"
    },
    {
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
```

**Fleet host configuration** –
Your fleet workers need Docker and the NVIDIA Container Toolkit. Attach
the
[Docker and NVIDIA Container Toolkit host configuration script on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit")
to your fleet. For more information, see
[Run Docker containers with NVIDIA GPUs on Deadline Cloud workers](examples-host-config-docker-nvidia.md "examples-host-config-docker-nvidia.md").

## Build and push the Docker image

The job runs inside a Docker container based on the
[carlasim/carla:0.9.16 base image on Docker Hub](https://hub.docker.com/r/carlasim/carla "https://hub.docker.com/r/carlasim/carla").
The base CARLA image includes the simulator but lacks the Python
environment, scenario runner, and sensor capture scripts needed for
this job. The custom image layers on Python 3.10,
`scenario_runner`, and the entrypoint and capture scripts so
each Deadline Cloud task can boot CARLA, execute the driving scenario, and
record sensor data in a single container.

###### To build and push the Docker image

1. Create an Amazon ECR repository if you don't have one:

```
aws ecr create-repository --repository-name carla-deadline --region `REGION`
```

2. From the `docker/` directory of the
   `autonomous_driving_carla` bundle, build the
   image:

```
cd docker/
docker build -t carla-deadline:0.9.16 .
```

###### Note

The Dockerfile pulls `carlasim/carla:0.9.16` from
Docker Hub as the base image. The first build downloads
approximately 8 GB. 3. Push the image to Amazon ECR:

```
aws ecr get-login-password --region `REGION` | \
  docker login --username AWS --password-stdin `ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com

docker tag carla-deadline:0.9.16 \
  `ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com/carla-deadline:0.9.16

docker push `ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com/carla-deadline:0.9.16
```

## Submit the simulation job

###### To submit the job with the GUI submitter

1. From the bundle directory, open the submitter:

```
cd autonomous_driving_carla
deadline bundle gui-submit .
```

2. On the **Job-specific settings** tab, under
   **Scenario Settings**, configure ego speeds, NPC
   speeds, and NPC distances as comma-separated integers. The
   cross-product creates your task grid.
3. Under **Camera Viewpoints**, select which
   cameras to capture. **Front** is the default
   selection. Available positions are Front, Front Left, Front Right,
   Rear, Rear Left, and Rear Right.
4. Under **Advanced**, set your
   **Container Image URI** to
   ``ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com/carla-deadline:0.9.16`
   and the AWS Region where your Amazon ECR repository lives.
5. Choose **Submit**.

Alternatively, submit with the CLI:

```
deadline bundle submit . \
  --farm-id `FARM_ID` \
  --queue-id `QUEUE_ID` \
  --name "CARLA Lane Change Demo" \
  -p ImageURI=`ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com/carla-deadline:0.9.16 \
  -p AwsRegion=`REGION`
```

## Monitor the job

Monitor progress in the Deadline Cloud console. Each task shows its
parameter values (`EgoSpeed`, `NpcSpeed`,
`NpcDistance`) in the task table. Tasks typically complete
in about 13 minutes each.

The log output shows:

- Scenario generation and parameter values
- CARLA server boot and readiness
- Sensor capture progress (frame count per camera)
- Video encoding for each camera
- Grid video stitching (if you selected multiple cameras)

## Review the output

###### To download the output

1. After the job completes, run the download command from the
   same directory you used at submit time, so the
   `OutputDir` path (default `./outputs`)
   resolves to the same place:

```
deadline job download-output --job-id `job-id`
```

2. Deadline Cloud restores the output to the `OutputDir`
   directory that you selected when submitting the job.

Each task produces output in a subdirectory named for its
parameters:

```
outputs/
└── ego20_npc30_dist10/
    ├── rgb/
    │   ├── front/frame_000001.png ... frame_000062.png
    │   └── rear/frame_000001.png ... frame_000062.png
    ├── semantic/
    │   ├── front/...
    │   └── rear/...
    ├── lidar/frame_000001.ply ...
    ├── bbox_2d/{front,rear}/frame_*.txt
    ├── bbox_3d/frame_*.txt
    └── video/
        ├── front_scenario.mp4
        ├── rear_scenario.mp4
        └── grid_scenario.mp4
```

## Known limitations

- **Linux only** – The CARLA
  Docker image requires a Linux host with NVIDIA GPU drivers. Workers
  must run on Linux fleets.
- **x86\_64 only** – The CARLA
  Docker image does not support ARM architectures.
- **Mosaic images** –
  The job generates RGB/semantic mosaic images when you select 2 or
  more cameras. The layout is 2×3 when all 6 are active, or a
  smaller grid otherwise.
- **Capture rate scales with camera
  count** – The capture script writes PNGs
  synchronously per flush. With all 6 cameras, each flush writes
  14 PNGs instead of 2 with a single camera, and the increased I/O
  slows flushes below the 7 FPS target. The video encoder is fixed at
  7 FPS, so the same scenario produces a longer per-camera video with
  few cameras enabled and a shorter, denser multi-view video with
  many cameras enabled. This synchronous design is a deliberate
  tradeoff to keep the sample's architecture small and easy to adapt.
  A production pipeline would parallelize sensor I/O.

## Clean up

To avoid ongoing charges, clean up the resources that you created
for this tutorial:

###### To clean up tutorial resources

1. If you created a GPU fleet specifically for this tutorial,
   stop or delete it. If you used a pre-existing shared fleet, leave
   it in place.
2. Delete the `carla-deadline` Amazon ECR repository if you
   no longer need the image.

## Related resources

The following resources provide additional information:

- [Sample source code on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla")
- [CARLA simulator](https://carla.org/ "https://carla.org/")
- [Docker and NVIDIA Container Toolkit host configuration script on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit")
- [Run Docker containers with NVIDIA GPUs on Deadline Cloud workers](examples-host-config-docker-nvidia.md "examples-host-config-docker-nvidia.md")
- [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md")

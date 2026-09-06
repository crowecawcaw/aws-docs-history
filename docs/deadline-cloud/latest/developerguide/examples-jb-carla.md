# Run autonomous driving simulations with CARLA on Deadline Cloud

The
[autonomous\_driving\_carla](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/autonomous_driving_carla")
job bundle on the GitHub website runs an autonomous driving simulation parameter
sweep on AWS Deadline Cloud with configurable multi-sensor capture, using the [CARLA simulator](https://carla.org/ "https://carla.org/") on the CARLA website. The job runs a lane-change cut-in scenario and sweeps
across configurable ego speeds, NPC speeds, and NPC starting distances.
Each parameter combination creates a task (default 2×2×2 =
8 tasks).

Each task captures multi-sensor data from user-selected camera
viewpoints and produces per-camera videos, RGB and semantic segmentation
frames, LiDAR point clouds (`.ply`), and 2D/3D bounding boxes
in KITTI format.

The job runs inside a Docker container based on
`carlasim/carla:0.9.16`. Before submitting, build the custom
Docker image from the `docker/` directory in the bundle and
push it to Amazon Elastic Container Registry (Amazon ECR). Attach the
[docker\_nvidia\_container\_toolkit](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit")
host configuration script on the GitHub website to your fleet to provide Docker and
the NVIDIA Container Toolkit.

To run this bundle, you need a Deadline Cloud farm with a GPU fleet (minimum
1 NVIDIA GPU, 16 vCPU, 64 GiB memory) and a conda queue environment with
`ffmpeg`. The queue role needs Amazon ECR pull permissions.

From the `job_bundles` directory, submit the job:

```
deadline bundle gui-submit autonomous_driving_carla
```

On the _Job-specific settings_ tab, set the
Container Image URI to your Amazon ECR image and configure the scenario
parameters (ego speeds, NPC speeds, NPC distances) and camera
viewpoints.

For a complete walkthrough that covers building the Docker image,
submitting and monitoring the job, and reviewing the captured sensor
output, see
[Run an autonomous driving simulation sweep with CARLA](tutorial-carla-simulation.md "tutorial-carla-simulation.md").

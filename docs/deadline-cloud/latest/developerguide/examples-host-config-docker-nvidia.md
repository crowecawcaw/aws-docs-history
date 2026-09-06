# Run Docker containers with NVIDIA GPUs on Deadline Cloud workers

The
[docker\_nvidia\_container\_toolkit](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/docker_nvidia_container_toolkit")
host configuration script on the GitHub website installs Docker and the NVIDIA Container Toolkit
on Linux service-managed fleet workers, which lets jobs run GPU containers
directly with `docker run`. Many GPU workloads, such as ComfyUI
and Stable Diffusion inference servers, ship as container images and
require Docker with GPU passthrough. Containers also provide a clean way
to package complex dependency stacks (CUDA, Python, application-specific
libraries) without polluting the host or conflicting with other jobs on
the fleet.

The script does the following:

1. Installs Docker through `dnf` and starts the
   service.
2. Adds `job-user` to the `docker` group so
   that jobs can run containers without sudo.
3. Installs the NVIDIA Container Toolkit from the official
   repository.
4. Configures the Docker daemon to use the NVIDIA runtime.
5. Generates the CDI (Container Device Interface) spec for GPU
   access.
6. Restarts Docker and verifies the setup.
   The fleet AMI must have NVIDIA GPU drivers already installed, which
   Deadline Cloud GPU AMIs provide, and the fleet must use a GPU instance type such as
   `g6.xlarge`, `g6e.xlarge`, or
   `p4d.24xlarge`.

Once the host configuration has run, jobs can launch GPU containers.
The following example runs a container with GPU access, host networking,
and the standard Deadline Cloud usage-based license environment variables passed
through:

```
docker run --rm \
  --runtime=nvidia \
  --gpus all \
  --network host \
  -e ADSKFLEX_LICENSE_FILE \
  -e FLEXLM_TIMEOUT \
  -e foundry_LICENSE \
  -e PIXAR_LICENSE_FILE \
  -e g_licenseServerRLM \
  -e redshift_LICENSE \
  -e SESI_LMHOST \
  -e VRAY_AUTH_CLIENT_FILE_PATH \
  -e VRAY_AUTH_CLIENT_SETTINGS \
  `your-image:latest`
```

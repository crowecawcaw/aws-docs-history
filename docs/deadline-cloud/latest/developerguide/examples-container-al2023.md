

# Build a worker-equivalent Amazon Linux 2023 Docker image for Deadline Cloud
<a name="examples-container-al2023"></a>

The [al2023-deadline](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/containers/al2023-deadline) Dockerfile on the GitHub website replicates the package set of the Deadline Cloud service-managed fleet (SMF) worker AMI on top of the base Amazon Linux 2023 image. Use the image to:
+ Build and test conda packages with the same GLIBC version, system libraries, and runtime environment as real workers.
+ Reproduce worker-side build or runtime failures locally.
+ Validate that your software dependencies are satisfied by the worker environment before submitting jobs.

The image installs packages in layered groups that match the worker AMI: core system tools, build toolchain, X11/Mesa/OpenGL, image and media libraries, networking and security utilities, Python 3.11, Docker and containerd, AWS CLI v2, Boost, jemalloc, and TBB.

Build the image:

```
docker build -f Dockerfile.worker-equivalent -t al2023-deadline:latest .
```

Build a conda package inside the container:

```
docker run --rm -v "$PWD":/work -w /work al2023-deadline:latest \
    bash -c "pip3.11 install conda-build && conda build my-recipe/"
```

**Important**  
This image is a point-in-time snapshot. The actual SMF worker AMI may have newer or additional packages. For NVIDIA GPU support, add the NVIDIA Container Toolkit repository to the Dockerfile and run with `--gpus all`.
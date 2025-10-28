# How Amazon SageMaker Processing Runs Your Processing Container

Image

Amazon SageMaker Processing runs your processing container image in a similar way as the following
command, where `AppSpecification.ImageUri` is the Amazon ECR image URI that
you specify in a `CreateProcessingJob` operation.

```
docker run [AppSpecification.ImageUri]
```

This command runs the `ENTRYPOINT` command configured in your Docker
image.

You can also override the entrypoint command in the image or give command-line
arguments to your entrypoint command using the
`AppSpecification.ContainerEntrypoint` and
`AppSpecification.ContainerArgument` parameters in your
`CreateProcessingJob` request. Specifying these parameters configures
Amazon SageMaker Processing to run the container similar to the way that the following command does.

```
 docker run --entry-point [AppSpecification.ContainerEntrypoint] [AppSpecification.ImageUri] [AppSpecification.ContainerArguments]
```

For example, if you specify the `ContainerEntrypoint` to be
`[python3, -v, /processing_script.py]` in your
`CreateProcessingJob` request, and `ContainerArguments` to
be `[data-format, csv]`, Amazon SageMaker Processing runs your container with the following
command.

```
 python3 -v /processing_script.py data-format csv
```

When building your processing container, consider the following details:

- Amazon SageMaker Processing decides whether the job completes or fails depending on the exit
  code of the command run. A processing job completes if all of the processing
  containers exit successfully with an exit code of 0, and fails if any of the
  containers exits with a non-zero exit code.
- Amazon SageMaker Processing lets you override the processing container's entrypoint and set
  command-line arguments just like you can with the Docker API. Docker images
  can also configure the entrypoint and command-line arguments using the
  `ENTRYPOINT` and CMD instructions. The way
  `CreateProcessingJob`'s `ContainerEntrypoint` and
  `ContainerArgument` parameters configure a Docker image's
  entrypoint and arguments mirrors how Docker overrides the entrypoint and
  arguments through the Docker API:
  - If neither `ContainerEntrypoint` nor
    `ContainerArguments` are provided, Processing uses the
    default `ENTRYPOINT` or CMD in the image.
  - If `ContainerEntrypoint` is provided, but not
    `ContainerArguments`, Processing runs the image with the
    given entrypoint, and ignores the `ENTRYPOINT` and CMD in
    the image.
  - If `ContainerArguments` is provided, but not
    `ContainerEntrypoint`, Processing runs the image with the
    default `ENTRYPOINT` in the image and with the provided
    arguments.
  - If both `ContainerEntrypoint` and
    `ContainerArguments` are provided, Processing runs the
    image with the given entrypoint and arguments, and ignores the
    `ENTRYPOINT` and CMD in the image.

- You must use the exec form of the `ENTRYPOINT` instruction in
  your Dockerfile (`ENTRYPOINT`
  `["executable", "param1", "param2"])` instead of the shell form
  (`ENTRYPOINT` `command param1 param2`). This lets
  your processing container receive `SIGINT` and
  `SIGKILL` signals, which Processing uses to stop processing jobs
  with the `StopProcessingJob` API.
- `/opt/ml` and all its subdirectories are reserved by SageMaker AI. When
  building your Processing Docker image, don't place any data required by your
  processing container in these directories.
- If you plan to use GPU devices, make sure that your containers are
  nvidia-docker compatible. Include only the CUDA toolkit in containers. Don't
  bundle NVIDIA drivers with the image. For more information about
  nvidia-docker, see [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker "https://github.com/NVIDIA/nvidia-docker").

# Dockerfile specifications

To bring your own image (BYOI), ensure that the following specifications are satisfied
when you create your `Dockerfile`.

- **Base image specifications**: You must use one of
  the base images from Amazon SageMaker AI Distribution ([`sagemaker-distribution`](https://gallery.ecr.aws/sagemaker/sagemaker-distribution "https://gallery.ecr.aws/sagemaker/sagemaker-distribution")), with the following
  specifications. These contain important extensions that are required to execute an
  image on Amazon SageMaker Unified Studio.
  - The base image must be `FROM
public.ecr.aws/sagemaker/sagemaker-distribution:`version``.
You can copy the Image URI of an image from the Image tags tab in [`sagemaker-distribution`](https://gallery.ecr.aws/sagemaker/sagemaker-distribution "https://gallery.ecr.aws/sagemaker/sagemaker-distribution").
  - The chosen image `version` must be
    greater or equal to the following.
    - For CPU, `2.6-cpu`
    - For GPU: `2.6-gpu`

- Follow the [Custom image
  specifications](../../../sagemaker/latest/dg/studio-updated-byoi-specs.md "../../../sagemaker/latest/dg/studio-updated-byoi-specs.md") in the _SageMaker AI Developer
  Guide_.

## Dockerfile example

The following is an example `Dockerfile` that meets the above
criteria. The `version` in this example must
satisfy the specification above.

###### Note

Adding `ENTRYPOINT` in the `Dockerfile` will not
work as expected. If you would like to configure a custom entrypoint, you will need
to update your [`ContainerConfig`](../../../sagemaker/latest/APIReference/API_ContainerConfig.md "../../../sagemaker/latest/APIReference/API_ContainerConfig.md"). For an example, see [Update container configuration](../../../sagemaker/latest/dg/studio-updated-byoi-how-to-container-configuration.md "../../../sagemaker/latest/dg/studio-updated-byoi-how-to-container-configuration.md") in the _SageMaker AI Developer
Guide_.

```
FROM public.ecr.aws/sagemaker/sagemaker-distribution:`version`

ARG NB_USER="sagemaker-user"
ARG NB_UID=1000
ARG NB_GID=100

ENV MAMBA_USER=$NB_USER

USER root

RUN apt-get update
RUN micromamba install sagemaker-inference --freeze-installed --yes --channel conda-forge --name base

USER $MAMBA_USER
```

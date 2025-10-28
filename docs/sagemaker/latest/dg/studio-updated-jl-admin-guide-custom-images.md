# Custom images

If you need functionality that is different than what's provided by SageMaker distribution,
you can bring your own image with your custom extensions and packages. You can also use
it to personalize the JupyterLab UI for your own branding or compliance needs.

The following page will provide JupyterLab-specific information and templates to
create your own custom SageMaker AI images. This is meant to supplement the Amazon SageMaker Studio
information and instructions on creating your own SageMaker AI image and bringing your own image
to Studio. To learn about custom Amazon SageMaker AI images and how to bring your own image to
Studio, see [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md").

###### Topics

- [Health
  check and URL for applications](#studio-updated-jl-admin-guide-custom-images-app-healthcheck "#studio-updated-jl-admin-guide-custom-images-app-healthcheck")
- [Dockerfile
  examples](#studio-updated-jl-custom-images-dockerfile-templates "#studio-updated-jl-custom-images-dockerfile-templates")

## Health

check and URL for applications

- `Base URL` – The base URL for the BYOI application must
  be `jupyterlab/default`. You can only have one application and it
  must always be named `default`.
- `HealthCheck API` – SageMaker AI uses the health check endpoint
  at port `8888` to check the health of the JupyterLab
  application. `jupyterlab/default/api/status` is the endpoint for
  the health check.
- `Home/Default URL` – The
  `/opt/.sagemakerinternal` and `/opt/ml`
  directories that are used by AWS. The metadata file in
  `/opt/ml` contains metadata about resources such as
  `DomainId`.
- Authentication – To enable authentication for your users, turn off
  the Jupyter notebooks token or password based authentication and allow all
  origins.

## Dockerfile

examples

The following examples are `Dockerfile`s that meets the above
information and [Custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md").

###### Note

If you are bringing your own image to SageMaker Unified Studio, you will need to follow the [Dockerfile
specifications](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md") in the _Amazon SageMaker Unified Studio User Guide_.

`Dockerfile` examples for SageMaker Unified Studio can be found in [Dockerfile example](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example") in the _Amazon SageMaker Unified Studio User
Guide_.

Example AL2023 Dockerfile
The following is an example AL2023
Dockerfile that meets the above information and [Custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md").

```
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

ARG NB_USER="sagemaker-user"
ARG NB_UID=1000
ARG NB_GID=100

# Install Python3, pip, and other dependencies
RUN yum install -y \
    python3 \
    python3-pip \
    python3-devel \
    gcc \
    shadow-utils && \
    useradd --create-home --shell /bin/bash --gid "${NB_GID}" --uid ${NB_UID} ${NB_USER} && \
    yum clean all

RUN python3 -m pip install --no-cache-dir \
    'jupyterlab>=4.0.0,<5.0.0' \
    urllib3 \
    jupyter-activity-monitor-extension \
    --ignore-installed

# Verify versions
RUN python3 --version && \
    jupyter lab --version

USER ${NB_UID}
CMD jupyter lab --ip 0.0.0.0 --port 8888 \
    --ServerApp.base_url="/jupyterlab/default" \
    --ServerApp.token='' \
    --ServerApp.allow_origin='*'
```

Example Amazon SageMaker Distribution Dockerfile
The following is a example Amazon SageMaker Distribution
Dockerfile that meets the above information and [Custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md").

```
FROM public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu
ARG NB_USER="sagemaker-user"
ARG NB_UID=1000
ARG NB_GID=100

ENV MAMBA_USER=$NB_USER

USER root

RUN apt-get update
RUN micromamba install sagemaker-inference --freeze-installed --yes --channel conda-forge --name base

USER $MAMBA_USER

ENTRYPOINT ["jupyter-lab"]
CMD ["--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888", "--ServerApp.allow_origin=*", "--ServerApp.token=''", "--ServerApp.base_url=/jupyterlab/default"]

```

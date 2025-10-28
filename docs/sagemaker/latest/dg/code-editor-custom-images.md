# Custom images

If you need functionality that is different than what's provided by SageMaker distribution,
you can bring your own image with your custom extensions and packages. You can also use it
to personalize the Code Editor UI for your own branding or compliance needs.

The following page will provide Code Editor-specific information and templates to create your
own custom SageMaker AI images. This is meant to supplement the Amazon SageMaker Studio information and
instructions on creating your own SageMaker AI image and bringing your own image to Studio. To
learn about custom Amazon SageMaker AI images and how to bring your own image to Studio, see [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md").

###### Topics

- [Health check and URL for
  applications](#code-editor-custom-images-app-healthcheck "#code-editor-custom-images-app-healthcheck")
- [Dockerfile
  examples](#code-editor-custom-images-dockerfile-templates "#code-editor-custom-images-dockerfile-templates")

## Health check and URL for

applications

- `Base URL` – The base URL for the BYOI application must be
  `CodeEditor/default`. You can only have one application and it must
  always be named `default`.
- Health check endpoint – You must host your Code Editor server at 0.0.0.0 port 8888
  for SageMaker AI to detect it.
- Authentication – You must pass `--without-connection-token` when
  opening `sagemaker-code-editor` to allow SageMaker AI to authenticate your
  users.

###### Note

If you are using Amazon SageMaker Distribution as the base image, these requirements are
already taken care of as part of the included `entrypoint-code-editor`
script.

## Dockerfile

examples

The following examples are `Dockerfile`s that meets the above
information and [Custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md").

###### Note

If you are bringing your own image to SageMaker Unified Studio, you will need to follow the [Dockerfile
specifications](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md") in the _Amazon SageMaker Unified Studio User Guide_.

`Dockerfile` examples for SageMaker Unified Studio can be found in [Dockerfile example](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example") in the _Amazon SageMaker Unified Studio User
Guide_.

Example micromamba Dockerfile
The following is an example Dockerfile to create an image from scratch using a
[`micromamba`](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html "https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html") base environment:

```
FROM mambaorg/micromamba:latest
ARG NB_USER="sagemaker-user"
ARG NB_UID=1000
ARG NB_GID=100

USER root

RUN micromamba install -y --name base -c conda-forge sagemaker-code-editor

USER $NB_UID

CMD eval "$(micromamba shell hook --shell=bash)"; \
    micromamba activate base; \
    sagemaker-code-editor --host 0.0.0.0 --port 8888 \
        --without-connection-token \
        --base-path "/CodeEditor/default"
```

Example SageMaker AI Distribution Dockerfile
The following is an example Dockerfile to create an image based on [Amazon SageMaker AI
Distribution](https://github.com/aws/sagemaker-distribution/tree/main "https://github.com/aws/sagemaker-distribution/tree/main"):

```
FROM public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu
ARG NB_USER="sagemaker-user"
ARG NB_UID=1000
ARG NB_GID=100
ENV MAMBA_USER=$NB_USER

USER root

 # install scrapy in the base environment
RUN micromamba install -y --name base -c conda-forge scrapy

 # download VSCodeVim
RUN \
  wget https://github.com/VSCodeVim/Vim/releases/download/v1.27.2/vim-1.27.2.vsix \
  -P /tmp/exts/ --no-check-certificate

 # Install the extension
RUN \
  extensionloc=/opt/amazon/sagemaker/sagemaker-code-editor-server-data/extensions \
  && sagemaker-code-editor \
    --install-extension "/tmp/exts/vim-1.27.2.vsix" \
    --extensions-dir "${extensionloc}"

USER $MAMBA_USER
ENTRYPOINT ["entrypoint-code-editor"]
```

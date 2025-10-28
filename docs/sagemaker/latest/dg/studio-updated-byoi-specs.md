# Custom image specifications

The image that you specify in your Dockerfile must match the specifications in the following
sections to create the image successfully.

###### Topics

- [Running the image](#studio-updated-byoi-specs-run "#studio-updated-byoi-specs-run")
- [Specifications for the user and
  file system](#studio-updated-byoi-specs-user-and-filesystem "#studio-updated-byoi-specs-user-and-filesystem")
- [Health check and URL for
  applications](#studio-updated-byoi-specs-app-healthcheck "#studio-updated-byoi-specs-app-healthcheck")
- [Dockerfile samples](#studio-updated-byoi-specs-dockerfile-templates "#studio-updated-byoi-specs-dockerfile-templates")

## Running the image

The following configurations can be made by updating your [`ContainerConfig`](../APIReference/API_ContainerConfig.md "../APIReference/API_ContainerConfig.md"). For an example, see [Update container
configuration](studio-updated-byoi-how-to-container-configuration.md "studio-updated-byoi-how-to-container-configuration.md").

- `Entrypoint` – You can configure `ContainerEntrypoint` and
  `ContainerArguments` that are passed to the container at runtime. We recommend
  configuring your entry point using `ContainerConfig`. See the above link for an
  example.
- `EnvVariables` – When using Studio, you can define custom
  `ContainerEnvironment` variables for your container. You can optionally update your
  environmental variables using `ContainerConfig`. See the above link for an
  example.

SageMaker AI-specific environment variables take precedence and will override any variables with
the same names. For example, SageMaker AI automatically provides environment variables prefixed with
`AWS_` and `SAGEMAKER_` to ensure proper integration with AWS
services and SageMaker AI functionality. The following are a few example SageMaker AI-specific environment
variables:

    + `AWS_ACCOUNT_ID`
    + `AWS_REGION`
    + `AWS_DEFAULT_REGION`
    + `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI`
    + `SAGEMAKER_SPACE_NAME`
    + `SAGEMAKER_APP_TYPE`

## Specifications for the user and

file system

- `WorkingDirectory` – The Amazon EBS volume for your space is mounted on the
  path `/home/sagemaker-user`. You can't change the mount path. Use the
  `WORKDIR` instruction to set the working directory of your image to a folder within
  `/home/sagemaker-user`.
- `UID` – The user ID of the Docker container. UID=1000 is a
  supported value. You can add sudo access to your users. The IDs are remapped to prevent a
  process running in the container from having more privileges than necessary.
- `GID` – The group ID of the Docker container. GID=100 is a
  supported value. You can add sudo access to your users. The IDs are remapped to prevent a
  process running in the container from having more privileges than necessary.
- Metadata directories – The `/opt/.sagemakerinternal` and
  `/opt/ml` directories that are used by AWS. The metadata file in
  `/opt/ml` contains metadata about resources such as
  `DomainId`.

Use the following command to show the file system contents:

```
cat /opt/ml/metadata/resource-metadata.json
```

- Logging directories – `/var/log/studio` are reserved for the
  logging directories of your applications and the extensions associated with it. We recommend
  that you don't use these folders in creating your image.

## Health check and URL for

applications

The health check and URL depend on the applications. Choose the following link associated
with the application you are building the image for.

- [Health check and URL for
  applications](code-editor-custom-images.md#code-editor-custom-images-app-healthcheck "code-editor-custom-images.md#code-editor-custom-images-app-healthcheck") for Code Editor
- [Health
  check and URL for applications](studio-updated-jl-admin-guide-custom-images.md#studio-updated-jl-admin-guide-custom-images-app-healthcheck "studio-updated-jl-admin-guide-custom-images.md#studio-updated-jl-admin-guide-custom-images-app-healthcheck") for
  JupyterLab

## Dockerfile samples

For Dockerfile samples that meet both the requirements on this page and your specific
application needs, navigate to the sample Dockerfiles in the respective application's section.
The following options include Amazon SageMaker Studio applications.

- [Dockerfile
  examples](code-editor-custom-images.md#code-editor-custom-images-dockerfile-templates "code-editor-custom-images.md#code-editor-custom-images-dockerfile-templates") for Code Editor
- [Dockerfile
  examples](studio-updated-jl-admin-guide-custom-images.md#studio-updated-jl-custom-images-dockerfile-templates "studio-updated-jl-admin-guide-custom-images.md#studio-updated-jl-custom-images-dockerfile-templates") for JupyterLab

###### Note

If you are bringing your own image to SageMaker Unified Studio, you will need to follow the [Dockerfile
specifications](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md") in the _Amazon SageMaker Unified Studio User Guide_.

`Dockerfile` examples for SageMaker Unified Studio can be found in [Dockerfile example](../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example "../../../sagemaker-unified-studio/latest/userguide/byoi-specifications.md#byoi-specifications-example") in the _Amazon SageMaker Unified Studio User
Guide_.

# Update container

configuration

You can bring custom Docker images into your machine learning workflows. A key aspect of
customizing these images is configuring the container configurations, or [`ContainerConfig`](../APIReference/API_ContainerConfig.md "../APIReference/API_ContainerConfig.md"). The following page provides an example on how to
configure your `ContainerConfig`.

An entrypoint is the command or script that runs when the container starts. Custom
entrypoints enable you to set up your environment, initialize services, or perform any
necessary setup before your application launches.

This example provides instructions on how to configure a custom entrypoint, for your
JupyterLab application, using the AWS CLI. This example assumes that you have already
created a custom image and domain. For instructions, see [Attach your custom image to your
domain](studio-updated-byoi-how-to-attach-to-domain.md "studio-updated-byoi-how-to-attach-to-domain.md").

1. First set your variables for the AWS CLI commands that follow.

```
APP_IMAGE_CONFIG_NAME=`app-image-config-name`
ENTRYPOINT_FILE=`entrypoint-file-name`
ENV_KEY=`environment-key`
ENV_VALUE=`environment-value`
REGION=`aws-region`
DOMAIN_ID=`domain-id`
IMAGE_NAME=`custom-image-name`
IMAGE_VERSION=`custom-image-version`
```

    * ``app-image-config-name`` is the name of your
     application image configuration.
    * ``entrypoint-file-name`` is the name of your
     container's entrypoint script. For example, `entrypoint.sh`.
    * ``environment-key`` is the name of your
     environment variable.
    * ``environment-value`` is the value assigned to
     your environment variable.
    * ``aws-region`` is the AWS Region of your Amazon SageMaker AI domain. You can
     find this at the top right of any AWS console page.
    * ``domain-id`` is your domain ID. To view
     your domains, see [View domains](domain-view.md "domain-view.md").
    * ``custom-image-name`` is the name of your
     custom image. To view your custom image details, see [View custom image details
     (console)](studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console "studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console").


    If you followed the instructions in [Attach your custom image to your
     domain](studio-updated-byoi-how-to-attach-to-domain.md "studio-updated-byoi-how-to-attach-to-domain.md"), you may want to use
     the same image name you used in that process.
    * ``custom-image-version`` is the version number
     of your custom image. This should be an integer, representing the version of your
     image. To view your custom image details, see [View custom image details
     (console)](studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console "studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console").

2. Use the [`CreateAppImageConfig`](../APIReference/API_CreateAppImageConfig.md "../APIReference/API_CreateAppImageConfig.md") API to create an image
   configuration.

```
aws sagemaker create-app-image-config \
    --region ${REGION} \
    --app-image-config-name "${APP_IMAGE_CONFIG_NAME}" \
    --jupyter-lab-app-image-config "ContainerConfig = {
        ContainerEntrypoint = "${ENTRYPOINT_FILE}",
        ContainerEnvironmentVariables = {
            "${ENV_KEY}"="${ENV_VALUE}"
        }
    }"
```

3. Use the [`UpdateDomain`](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") API to update the default settings for your
   domain. This will attach the custom image as well as the application image
   configuration.

```
aws sagemaker update-domain \
    --region ${REGION} \
    --domain-id "${DOMAIN_ID}" \
    --default-user-settings "{
        \"JupyterLabAppSettings\": {
            \"CustomImages\": [
                {
                    \"ImageName\": \"${IMAGE_NAME}\",
                    \"ImageVersionNumber\": ${IMAGE_VERSION},
                    \"AppImageConfigName\": \"${APP_IMAGE_CONFIG_NAME}\"
                }
            ]
        }
    }"
```

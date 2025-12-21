# Integrate SOCI-indexed images with

Studio example

You must reference the SOCI-indexed image tag to use SOCI-indexed images in Studio,
rather than the original container image tag. Use the tag you specified during the SOCI
conversion process (e.g., `SOCI_IMAGE_TAG` in the [Create SOCI indexes with nerdctl and
SOCI CLI example](soci-indexing-example-create-indexes.md "soci-indexing-example-create-indexes.md")).

###### Integrate SOCI-indexed images example

1. First set your variables for the AWS CLI commands that follow. The following is an
   example of setting up your variables.

```
ACCOUNT_ID="`111122223333`"
REGION="`us-east-1`"
IMAGE_NAME="`sagemaker-image-name`"
IMAGE_CONFIG_NAME="`sagemaker-image-config-name`"
ROLE_ARN="`your-role-arn`"
DOMAIN_ID="`domain-id`"
SOCI_IMAGE_TAG="`soci-indexed-image-tag`"
```

Variable definitions:

    * `ACCOUNT_ID` is your AWS account ID
    * `REGION` is the AWS Region of your Amazon ECR private registry
    * `IMAGE_NAME` is the name of your SageMaker image
    * `IMAGE_CONFIG_NAME` is the name of your SageMaker image
     configuration
    * `ROLE_ARN` is the ARN of your execution role with the permissions
     listed in [Required IAM
     permissions](soci-indexing-setup.md#soci-indexing-setup-iam-permissions "soci-indexing-setup.md#soci-indexing-setup-iam-permissions")
    * `DOMAIN_ID` is the [domain ID](domain-view.md "domain-view.md")


    ###### Note

    If you are attaching the image to a SageMaker Unified Studio project and you need clarification
     on which domain to use, see [View the SageMaker AI domain details associated with your project](../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain "../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain").
    * `SOCI_IMAGE_TAG` is the tag of your SOCI-indexed image

2. Export your region:

```
export AWS_REGION=$REGION
```

3. Create a SageMaker image:

```
aws sagemaker create-image \
    --image-name "$IMAGE_NAME" \
    --role-arn "$ROLE_ARN"
```

4. Create a SageMaker Image Version using your SOCI index URI:

```
IMAGE_INDEX_URI="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$IMAGE_NAME:$SOCI_IMAGE_TAG"

aws sagemaker create-image-version \
    --image-name "$IMAGE_NAME" \
    --base-image "$IMAGE_INDEX_URI"
```

5. Create an application image configuration and update your Amazon SageMaker AI domain to include
   the custom image for your app. You can do this for Code Editor, based on Code-OSS, Visual Studio Code - Open Source (Code Editor) and JupyterLab
   applications. Choose the application option below to view the steps.

Code Editor
Create an application image configuration for Code Editor:

```
aws sagemaker create-app-image-config \
    --app-image-config-name "$IMAGE_CONFIG_NAME" \
    --code-editor-app-image-config '{ "FileSystemConfig": { "MountPath": "/home/sagemaker-user", "DefaultUid": 1000, "DefaultGid": 100 } }'
```

Update your Amazon SageMaker AI domain to include the custom image for Code Editor:

```
aws sagemaker update-domain \
    --domain-id "$DOMAIN_ID" \
    --default-user-settings '{
        "CodeEditorAppSettings": {
        "CustomImages": [{
            "ImageName": "$IMAGE_NAME",
            "AppImageConfigName": "$IMAGE_CONFIG_NAME"
        }]
    }
}'
```

JupyterLab
Create an application image configuration for JupyterLab:

```
aws sagemaker create-app-image-config \
    --app-image-config-name "$IMAGE_CONFIG_NAME" \
    --jupyter-lab-app-image-config '{ "FileSystemConfig": { "MountPath": "/home/sagemaker-user", "DefaultUid": 1000, "DefaultGid": 100 } }'
```

Update your Amazon SageMaker AI domain to include the custom image for JupyterLab:

```
aws sagemaker update-domain \
    --domain-id "$DOMAIN_ID" \
    --default-user-settings '{
        "JupyterLabAppSettings": {
        "CustomImages": [{
            "ImageName": "$IMAGE_NAME",
            "AppImageConfigName": "$IMAGE_CONFIG_NAME"
        }]
    }
}'
```

6. After you update your domain to include your custom image, you can create an
   application in Studio using your custom image. When you [Launch a custom image in
   Studio](studio-updated-byoi-how-to-launch.md "studio-updated-byoi-how-to-launch.md") ensure that you are using your
   custom image.

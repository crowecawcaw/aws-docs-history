# Create a custom RStudio image

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

This topic describes how you can create a custom RStudio image using the SageMaker AI console and
the AWS CLI. If you use the AWS CLI, you must run the steps from your local machine. The
following steps do not work from within Amazon SageMaker Studio Classic.

When you create an image, SageMaker AI also creates an initial image version. The image version
represents a container image in [Amazon Elastic Container Registry (ECR)](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
The container image must satisfy the requirements to be used in RStudio. For more
information, see [Custom RStudio image specifications](rstudio-byoi-specs.md "rstudio-byoi-specs.md").

For information about testing your image locally and resolving common issues, see the
[SageMaker Studio Custom Image Samples repo](https://github.com/aws-samples/sagemaker-studio-custom-image-samples/blob/main/DEVELOPMENT.md "https://github.com/aws-samples/sagemaker-studio-custom-image-samples/blob/main/DEVELOPMENT.md").

###### Topics

- [Add a SageMaker AI-compatible RStudio
  Docker container image to Amazon ECR](#rstudio-byoi-sdk-add-container-image "#rstudio-byoi-sdk-add-container-image")
- [Create a SageMaker image from the
  console](#rstudio-byoi-create-console "#rstudio-byoi-create-console")
- [Create an image from the AWS CLI](#rstudio-byoi-create-cli "#rstudio-byoi-create-cli")

## Add a SageMaker AI-compatible RStudio

Docker container image to Amazon ECR

Use the following steps to add a Docker container image to Amazon ECR:

- Create an Amazon ECR repository.
- Authenticate to Amazon ECR.
- Build a SageMaker AI-compatible RStudio Docker image.
- Push the image to the Amazon ECR repository.

###### Note

The Amazon ECR repository must be in the same AWS Region as your domain.

###### To build and add a Docker image to Amazon ECR

1. Create an Amazon ECR repository using the AWS CLI. To create the repository using
   the Amazon ECR console, see
   [Creating a repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md").

```
aws ecr create-repository \
    --repository-name rstudio-custom \
    --image-scanning-configuration scanOnPush=true
```

Response:

```
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:acct-id:repository/rstudio-custom",
        "registryId": "acct-id",
        "repositoryName": "rstudio-custom",
        "repositoryUri": "acct-id.dkr.ecr.us-east-2.amazonaws.com/rstudio-custom",
        ...
    }
}
```

2. Authenticate to Amazon ECR using the repository URI returned as a response from the
   `create-repository` command. Make sure that the Docker
   application is running. For more information, see [Registry
   Authentication](../../../AmazonECR/latest/userguide/Registries.md#registry_auth "../../../AmazonECR/latest/userguide/Registries.md#registry_auth").

```
aws ecr get-login-password | \
    docker login --username AWS --password-stdin `<repository-uri>`
```

Response:

```
Login Succeeded
```

3. Build the Docker image. Run the following command from the directory that
   includes your Dockerfile.

```
docker build .
```

4. Tag your built image with a unique tag.

```
docker tag `<image-id>` "`<repository-uri>`:`<tag>`"
```

5. Push the container image to the Amazon ECR repository. For more information, see
   [ImagePush](https://docs.docker.com/engine/api/v1.40/#operation/ImagePush "https://docs.docker.com/engine/api/v1.40/#operation/ImagePush") and
   [Pushing an image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md").

```
docker push `<repository-uri>`:`<tag>`
```

Response:

```
The push refers to repository [`<account-id>`.dkr.ecr.us-east-2.amazonaws.com/rstudio-custom]
r: digest: `<digest>` size: 3066
```

## Create a SageMaker image from the

console

###### To create an image

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **Images**.
4. On the **Custom images** page, choose
   **Create image**.
5. For **Image source**, enter the registry path to the container image
   in Amazon ECR. The path is in the following format:

``acct-id`.dkr.ecr.`region`.amazonaws.com/`repo-name[:tag] or [@digest]`` 6. Choose **Next**. 7. Under **Image properties**, enter the following:

    * Image name – The name must be unique to your account in the current
     AWS Region.
    * (Optional) Image display name – The name displayed in the domain
     user interface. When not provided, `Image name` is
     displayed.
    * (Optional) Description – A description of the image.
    * IAM role – The role must have the
     [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess")
     policy attached. Use the dropdown menu to choose one of the following options:




    	+ Create a new role – Specify any additional Amazon Simple Storage Service (Amazon S3) buckets that you want
    	 your notebooks users to access. If you don't want to allow access to additional
    	 buckets, choose **None**.


    	SageMaker AI attaches the `AmazonSageMakerFullAccess` policy to
    	 the role. The role allows your notebook users to access the
    	 Amazon S3 buckets listed next to the check marks.
    	+ Enter a custom IAM role ARN – Enter the Amazon Resource Name (ARN) of
    	 your IAM role.
    	+ Use existing role – Choose one of your existing roles from the list.
    * (Optional) Image tags – Choose **Add new tag**.
     You can add up to 50 tags. Tags are searchable using the SageMaker AI console or
     the SageMaker AI `Search` API.

8. Under **Image type**, select RStudio image.
9. Choose **Submit**.

The new image is displayed in the **Custom images** list and briefly
highlighted. After the image has been successfully created, you can choose the image name to
view its properties or choose **Create version** to create another version.

###### To create another image version

1. Choose **Create version** on the same row as the image.
2. For **Image source**, enter the registry path to the Amazon ECR image.
   The image shouldn't be the same image as used in a previous version of the SageMaker AI
   image.

To use the custom image in RStudio, you must attach it to your domain. For more
information, see [Attach a custom SageMaker image](rstudio-byoi-attach.md "rstudio-byoi-attach.md").

## Create an image from the AWS CLI

This section shows how to create a custom Amazon SageMaker image using the AWS CLI.

Use the following steps to create a SageMaker image:

- Create an `Image`.
- Create an `ImageVersion`.
- Create a configuration file.
- Create an `AppImageConfig`.

###### To create the SageMaker image entities

1. Create a SageMaker image. The role ARN must have at least the
   `AmazonSageMakerFullAccessPolicy` policy attached.

```
aws sagemaker create-image \
    --image-name rstudio-custom-image \
    --role-arn arn:aws:iam::`<acct-id>`:role/service-role/`<execution-role>`
```

Response:

```
{
    "ImageArn": "arn:aws:sagemaker:us-east-2:acct-id:image/rstudio-custom-image"
}
```

2. Create a SageMaker image version from the image. Pass the unique tag value that you
   chose when you pushed the image to Amazon ECR.

```
aws sagemaker create-image-version \
    --image-name rstudio-custom-image \
    --base-image `<repository-uri>`:`<tag>`
```

Response:

```
{
    "ImageVersionArn": "arn:aws:sagemaker:us-east-2:acct-id:image-version/rstudio-image/1"
}
```

3. Check that the image version was successfully created.

```
aws sagemaker describe-image-version \
    --image-name rstudio-custom-image \
    --version 1
```

Response:

```
{
    "ImageVersionArn": "arn:aws:sagemaker:us-east-2:acct-id:image-version/rstudio-custom-image/1",
    "ImageVersionStatus": "CREATED"
}
```

###### Note

If the response is `"ImageVersionStatus": "CREATED_FAILED"`,
the response also includes the failure reason. A permissions issue is a
common cause of failure. You also can check your Amazon CloudWatch Logs. The name of
the log group is `/aws/sagemaker/studio`. The name of the log
stream is
`$domainID/$userProfileName/KernelGateway/$appName`. 4. Create a configuration file, named
`app-image-config-input.json`. The app image config
is used to configuration for running a SageMaker image as a Kernel Gateway
application.

```
{
    "AppImageConfigName": "rstudio-custom-config"
}
```

5. Create the AppImageConfig using the file that you created in the previous
   step.

```
aws sagemaker create-app-image-config \
    --cli-input-json file://app-image-config-input.json
```

Response:

```
{
    "AppImageConfigArn": "arn:aws:sagemaker:us-east-2:acct-id:app-image-config/r-image-config"
}
```

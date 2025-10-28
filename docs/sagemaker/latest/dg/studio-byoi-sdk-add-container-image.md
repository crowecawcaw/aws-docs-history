# Add a Docker Image Compatible with

Amazon SageMaker Studio Classic to Amazon ECR

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You perform the following steps to add a container image to Amazon ECR:

- Create an Amazon ECR repository.
- Authenticate to Amazon ECR.
- Build a Docker image compatible with Studio Classic.
- Push the image to the Amazon ECR repository.

###### Note

The Amazon ECR repository must be in the same AWS Region as Studio Classic.

###### To build and add a container image to Amazon ECR

1. Create an Amazon ECR repository using the AWS CLI. To create the repository using
   the Amazon ECR console, see
   [Creating a repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md").

```
aws ecr create-repository \
    --repository-name smstudio-custom \
    --image-scanning-configuration scanOnPush=true
```

The response should look similar to the following.

```
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:acct-id:repository/smstudio-custom",
        "registryId": "acct-id",
        "repositoryName": "smstudio-custom",
        "repositoryUri": "acct-id.dkr.ecr.us-east-2.amazonaws.com/smstudio-custom",
        ...
    }
}
```

2. Build the `Dockerfile` using the Studio Classic image build CLI. The period (.)
   specifies that the Dockerfile should be in the context of the build command. This command
   builds the image and uploads the built image to the ECR repo. It then outputs the image
   URI.

```
sm-docker build . --repository smstudio-custom:custom
```

The response should look similar to the following.

```
Image URI: `<acct-id>`.dkr.ecr.`<region>`.amazonaws.com/`<image_name>`
```

# Prerequisites for Custom Images in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You must satisfy the following prerequisites to bring your own container for use with Amazon SageMaker Studio Classic.

- The Docker application. For information about setting up Docker, see [Orientation and setup](https://docs.docker.com/get-started/ "https://docs.docker.com/get-started/").
- Install the AWS CLI by following the steps in [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- A local copy of any Dockerfile for creating a Studio Classic compatible image. For sample
  custom images, see the [SageMaker AI
  Studio Classic custom image samples](https://github.com/aws-samples/sagemaker-studio-custom-image-samples/ "https://github.com/aws-samples/sagemaker-studio-custom-image-samples/") repository.
- Permissions to access the Amazon Elastic Container Registry (Amazon ECR) service. For more information, see [Amazon ECR Managed
  Policies](../../../AmazonECR/latest/userguide/ecr_managed_policies.md "../../../AmazonECR/latest/userguide/ecr_managed_policies.md").
- An AWS Identity and Access Management execution role that has the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy attached. If you have onboarded to Amazon SageMaker AI
  domain, you can get the role from the **Domain Summary** section of the
  SageMaker AI control panel.
- Install the Studio Classic image build CLI by following the steps in [SageMaker Docker
  Build](https://github.com/aws-samples/sagemaker-studio-image-build-cli "https://github.com/aws-samples/sagemaker-studio-image-build-cli"). This CLI enables you to build a Dockerfile using AWS CodeBuild.

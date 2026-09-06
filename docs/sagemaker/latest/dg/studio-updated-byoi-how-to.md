

# How to bring your own image
<a name="studio-updated-byoi-how-to"></a>

The following pages will provide instructions on how to bring your own custom image. Ensure that the following prerequisites are satisfied before continuing.

## Prerequisites
<a name="studio-updated-byoi-how-to-prerequisites"></a>

You will need to complete the following prerequisites to bring your own image to Amazon SageMaker AI.
+ Set up the Docker application. For more information, see [Get started](https://docs.docker.com/get-started/) in the *Docker documentation*.
+ Install the latest AWS CLI by following the steps in [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS Command Line Interface User Guide for Version 2*.
+ Permissions to access the Amazon Elastic Container Registry (Amazon ECR) service. For more information, see [Amazon ECR Managed Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr_managed_policies.html) in the *Amazon ECR User Guide*.
+ An AWS Identity and Access Management role that has the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess) policy attached.

**Topics**
+ [Prerequisites](#studio-updated-byoi-how-to-prerequisites)
+ [Create a custom image and push to Amazon ECR](studio-updated-byoi-how-to-prepare-image.md)
+ [Attach your custom image to your domain](studio-updated-byoi-how-to-attach-to-domain.md)
+ [Update container configuration](studio-updated-byoi-how-to-container-configuration.md)
# How to bring your own image

The following pages will provide instructions on how to bring your own custom image. Ensure
that the following prerequisites are satisfied before continuing.

## Prerequisites

You will need to complete the following prerequisites to bring your own image to
Amazon SageMaker AI.

- Set up the Docker application. For more information, see [Get started](https://docs.docker.com/get-started/ "https://docs.docker.com/get-started/") in the _Docker
  documentation_.
- Install the latest AWS CLI by following the steps in [Getting started with the
  AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User Guide for Version 2_.
- Permissions to access the Amazon Elastic Container Registry (Amazon ECR) service. For more information, see [Amazon ECR Managed Policies](../../../AmazonECR/latest/userguide/ecr_managed_policies.md "../../../AmazonECR/latest/userguide/ecr_managed_policies.md") in the
  _Amazon ECR User Guide_.
- An AWS Identity and Access Management role that has the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy attached.

###### Topics

- [Create a custom image and push to
  Amazon ECR](studio-updated-byoi-how-to-prepare-image.md "studio-updated-byoi-how-to-prepare-image.md")
- [Attach your custom image to your
  domain](studio-updated-byoi-how-to-attach-to-domain.md "studio-updated-byoi-how-to-attach-to-domain.md")
- [Update container
  configuration](studio-updated-byoi-how-to-container-configuration.md "studio-updated-byoi-how-to-container-configuration.md")

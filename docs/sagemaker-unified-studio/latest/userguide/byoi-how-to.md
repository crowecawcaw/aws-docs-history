# How to BYOI

When you bring your own image (BYOI) to Amazon SageMaker Unified Studio, you attach a custom image to an
Amazon SageMaker Unified Studio project. The following page provides instructions on how to bring your custom
image to your Amazon SageMaker Unified Studio project.

###### Topics

- [Prerequisites](#byoi-how-to-prerequisites "#byoi-how-to-prerequisites")
- [Step 1: Create your custom
  image](#byoi-how-to-step-1-create-custom-image "#byoi-how-to-step-1-create-custom-image")
- [Step 2: Get the SageMaker AI domain name
  associated with your Amazon SageMaker Unified Studio project](#byoi-how-to-step-2-get-domain-name "#byoi-how-to-step-2-get-domain-name")
- [Step 3: Attach your custom
  image using the SageMaker AI domain](#byoi-how-to-step-3-attach-custom-image "#byoi-how-to-step-3-attach-custom-image")
- [Step 4: Access your custom
  image in Amazon SageMaker Unified Studio](#byoi-how-to-step-4-access-custom-image "#byoi-how-to-step-4-access-custom-image")

## Prerequisites

You will need to complete the following prerequisites to bring your own image to
Amazon SageMaker Unified Studio.

- Create an Amazon SageMaker Unified Studio project. For more information, see [Create a new project](create-new-project.md "create-new-project.md").
- Set up the Docker application. For more information, see [Get started](https://docs.docker.com/get-started/ "https://docs.docker.com/get-started/") in the
  _Docker documentation_.
- Install the latest AWS CLI by following the steps in [Getting started with the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User
  Guide for Version 2_.
- Permissions to access the Amazon Elastic Container Registry (Amazon ECR) service. For more information, see [Amazon ECR Managed
  Policies](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _Amazon ECR User Guide_.
- An AWS Identity and Access Management role that has the [AmazonSageMakerFullAccess](../../../sagemaker/latest/dg/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "../../../sagemaker/latest/dg/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess") policy attached.

## Step 1: Create your custom

image

###### Important

Ensure that you are using the [Dockerfile specifications](byoi-specifications.md "byoi-specifications.md") in the following instructions.

Follow the steps in [Create a
custom image and push to Amazon ECR](../../../sagemaker/latest/dg/studio-updated-byoi-how-to-prepare-image.md "../../../sagemaker/latest/dg/studio-updated-byoi-how-to-prepare-image.md") in the _SageMaker AI Developer
Guide_.

## Step 2: Get the SageMaker AI domain name

associated with your Amazon SageMaker Unified Studio project

An associated SageMaker AI domain is created when you create a Amazon SageMaker Unified Studio project. You will
need the SageMaker AI domain name before proceeding to the next step. For instructions, see
[View the SageMaker AI domain details associated
with your project](view-project-details.md#view-project-details-smai-domain "view-project-details.md#view-project-details-smai-domain").

## Step 3: Attach your custom

image using the SageMaker AI domain

To attach your custom image to your Amazon SageMaker Unified Studio project, you must attach your custom
image to your SageMaker AI domain. Follow the steps in [Attach
your custom image to your domain](../../../sagemaker/latest/dg/studio-updated-byoi-how-to-attach-to-domain.md "../../../sagemaker/latest/dg/studio-updated-byoi-how-to-attach-to-domain.md") in the _SageMaker AI Developer
Guide_, using the SageMaker AI domain obtained from above.

## Step 4: Access your custom

image in Amazon SageMaker Unified Studio

Once your custom image is attached to your Amazon SageMaker Unified Studio project, the users with access to
your project can access it. For instructions on how users can access the custom images,
see [Launch your custom image in Amazon SageMaker Unified Studio](byoi-launch-custom-image.md "byoi-launch-custom-image.md").

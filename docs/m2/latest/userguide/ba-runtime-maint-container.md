AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Upgrade the AWS Blu Age Runtime on container

This guide describes how to upgrade the AWS Blu Age Runtime on container. To do this, you need to first complete some prerequisites,
and then work with Docker image to upgrade the AWS Blu Age Runtime.

###### Topics

- [Prerequisites](#ba-runtime-maint-prereq "#ba-runtime-maint-prereq")
- [Upgrade the AWS Blu Age Runtime](#ba-runtime-maint-copy-files "#ba-runtime-maint-copy-files")

## Prerequisites

Before you begin, make sure you meet the following prerequisites.

- Complete [AWS Blu Age Runtime prerequisites](ba-runtime-setup-prereq.md "ba-runtime-setup-prereq.md") and [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") .
- Download the version of the AWS Blu Age Runtime that you want to upgrade to. For more information, see
  [Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md") . The framework consists of two binary files:
  `aws-bluage-runtime-x.y.z.zip` and
  `aws-bluage-webapps-x.y.z.zip`.

## Upgrade the AWS Blu Age Runtime

Complete the following steps to upgrade the AWS Blu Age Runtime.

1. Rebuild your Docker image with the desired AWS Blu Age Runtime version. For instructions, see [Set up AWS Blu Age Runtime on container](ba-runtime-deploy-container.md "ba-runtime-deploy-container.md").
2. Push your Docker image to your Amazon ECR repository.
3. Stop and restart your Amazon ECS or Amazon EKS service.
4. Verify the logs.

The AWS Blu Age Runtime is successfully upgraded.

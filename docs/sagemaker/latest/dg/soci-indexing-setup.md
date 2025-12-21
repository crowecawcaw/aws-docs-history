# Permissions for SOCI indexing

Create SOCI indexes for your container images and store them in Amazon ECR before using SOCI
indexing with [Amazon SageMaker Studio](studio-updated.md "studio-updated.md") or [Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md "../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md").

###### Topics

- [Prerequisites](#soci-indexing-setup-prerequisites "#soci-indexing-setup-prerequisites")
- [Required IAM permissions](#soci-indexing-setup-iam-permissions "#soci-indexing-setup-iam-permissions")

## Prerequisites

- AWS account with an [AWS Identity and Access Management](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md") (IAM) role with
  permissions to manage
  - [Amazon ECR](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md")
  - [Amazon SageMaker AI](gs.md "gs.md")

- [Amazon ECR
  private repositories](../../../AmazonECR/latest/userguide/Repositories.md "../../../AmazonECR/latest/userguide/Repositories.md") for storing your container images
- [AWS CLI v2.0+](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") configured with appropriate credentials
- The following container tools:
  - Required: [soci-snapshotter](https://github.com/awslabs/soci-snapshotter "https://github.com/awslabs/soci-snapshotter")
  - Options:
    - [nerdctl](https://github.com/containerd/nerdctl "https://github.com/containerd/nerdctl")
    - [finch](https://github.com/runfinch/finch "https://github.com/runfinch/finch")

## Required IAM permissions

Your IAM role needs permissions to:

- Create and manage SageMaker AI resources (domains, images, app configs).
  - You may use the [SageMakerFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") AWS managed policy. For more permission details,
    see [AWS managed policy:
    AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").

- [IAM permissions for pushing an image to an Amazon ECR private repository](../../../AmazonECR/latest/userguide/image-push-iam.md "../../../AmazonECR/latest/userguide/image-push-iam.md").

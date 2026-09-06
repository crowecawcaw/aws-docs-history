

# Permissions for SOCI indexing
<a name="soci-indexing-setup"></a>

Create SOCI indexes for your container images and store them in Amazon ECR before using SOCI indexing with [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html).

**Topics**
+ [Prerequisites](#soci-indexing-setup-prerequisites)
+ [Required IAM permissions](#soci-indexing-setup-iam-permissions)

## Prerequisites
<a name="soci-indexing-setup-prerequisites"></a>
+ AWS account with an [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html) (IAM) role with permissions to manage
  + [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
  + [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)
+ [Amazon ECR private repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) for storing your container images
+ [AWS CLI v2.0\+](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) configured with appropriate credentials
+ The following container tools:
  + Required: [soci-snapshotter](https://github.com/awslabs/soci-snapshotter)
  + Options:
    + [nerdctl](https://github.com/containerd/nerdctl)
    + [finch](https://github.com/runfinch/finch)

## Required IAM permissions
<a name="soci-indexing-setup-iam-permissions"></a>

Your IAM role needs permissions to:
+ Create and manage SageMaker AI resources (domains, images, app configs).
  + You may use the [SageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) AWS managed policy. For more permission details, see [AWS managed policy: AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess).
+ [IAM permissions for pushing an image to an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push-iam.html).
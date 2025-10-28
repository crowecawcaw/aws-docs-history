# AWS policy:

SageMakerStudioProjectRoleMachineLearningPolicy

Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial
intelligence, and machine learning actions, and uses this policy when creating these
roles to define the permissions related to Amazon SageMaker.

This is the SageMaker policy for the SageMakerUnifiedStudioProjectRole role. This
policy grants read and write access for Amazon SageMaker Unified Studio users to services such as Amazon
SageMaker, Amazon CloudWatch, and AWS Resource Groups. The policy also gives read and
write permissions to some infrastructure resources that are required to use these
services such as network interfaces and AWS KMS keys.

An administrator can disable certain permissions in this policy by tagging the role to
which the policy is attached to. The tag EnableSageMakerMLWorkloads=false disables all
SageMaker ML workloads related permissions.

To view the permissions for this policy, see [SageMakerStudioProjectRoleMachineLearningPolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioProjectRoleMachineLearningPolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioProjectRoleMachineLearningPolicy.md") in the _AWS Managed Policy Reference_.

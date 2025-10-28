# AWS policy:

SageMakerStudioBedrockEvaluationJobServiceRolePolicy

This policy allows Amazon Bedrock to access Amazon Bedrock models and datasets for
evaluation jobs in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE evaluation job service role. This
role is part of the AmazonBedrockEvaluation environment blueprint.

This policy grants the Amazon Bedrock service access to resources for an Amazon
Bedrock model evaluation job, including Amazon Bedrock models, Amazon S3 objects, and an
AWS KMS key.

- Amazon Bedrock permissions are required for Amazon Bedrock evaluation jobs to
  invoke Amazon Bedrock models enabled at the project level. This policy also
  grants access to Amazon Bedrock resources managed within Amazon SageMaker
  Unified Studio.
- Amazon S3 permissions are required for Amazon Bedrock evaluation jobs to
  access the project's Amazon S3 bucket.
- AWS KMS permissions are required to access Amazon S3 data encrypted with a
  customer managed key.
  This policy allows the Amazon Bedrock service to access specific resources tagged with
  the same project ID as the service role. This tag restriction effectively only permits
  access to resources in the same project. By default, project users are not allowed to
  change service role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockEvaluationJobServiceRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

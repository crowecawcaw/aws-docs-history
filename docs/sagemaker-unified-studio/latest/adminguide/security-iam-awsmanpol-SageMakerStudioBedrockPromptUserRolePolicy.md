# AWS policy: SageMakerStudioBedrockPromptUserRolePolicy

This policy provides access to an Amazon Bedrock prompt and its configuration in
Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE prompt user role. This role is part
of the AmazonBedrockPrompt environment blueprint.

This policy grants users access to a shared Amazon Bedrock IDE prompt, including the
Amazon Bedrock prompt, its configuration in Amazon S3, and an AWS KMS key.

- Amazon Bedrock permissions are required for prompt users to read Amazon
  Bedrock prompts.
- Amazon S3 permissions are required for prompt users to read an object in the
  project's Amazon S3 bucket.
- AWS KMS permissions are required to access Amazon Bedrock and Amazon S3 data
  encrypted with a customer managed key.
  This policy allows users to access individually shared Amazon Bedrock IDE prompts. By
  default, domain users and project users are not allowed to change user role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockPromptUserRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockPromptUserRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockPromptUserRolePolicy.md") in the _AWS Managed Policy Reference_.

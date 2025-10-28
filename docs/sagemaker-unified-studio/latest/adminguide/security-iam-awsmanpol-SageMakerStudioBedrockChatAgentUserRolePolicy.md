# AWS policy: SageMakerStudioBedrockChatAgentUserRolePolicy

This policy provides access to an Amazon Bedrock chat agent app's configuration and
Amazon Bedrock agent in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE chat agent user role. This role is
part of the AmazonBedrockChatAgent environment blueprint.

This policy grants users access to a shared Amazon Bedrock IDE chat agent app,
including the permission to invoke an Amazon Bedrock agent, get its configuration from
Amazon S3, and use an AWS KMS key.

- Amazon Bedrock permissions are required for app users to read and invoke an
  Amazon Bedrock agent.
- Amazon S3 permissions are required for app users to read an object in the
  project's Amazon S3 bucket.
- AWS KMS permissions are required to access Amazon Bedrock and Amazon S3 data
  encrypted with a customer managed key.
  This policy allows users to access individually shared Amazon Bedrock IDE chat agent
  apps. By default, domain users and project users are not allowed to change user role
  tags.

To view the permissions for this policy, see [SageMakerStudioBedrockChatAgentUserRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockChatAgentUserRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockChatAgentUserRolePolicy.md") in the _AWS Managed Policy Reference_.

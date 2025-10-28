# AWS policy: SageMakerStudioBedrockAgentServiceRolePolicy

This policy allows Amazon Bedrock Agents to access Amazon Bedrock models and other
resources attached to an agent in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE agent service role. This role is
part of the AmazonBedrockChatAgent environment blueprint.

This policy grants the Amazon Bedrock service access to resources attached to a Amazon
Bedrock IDE chat agent app, including Amazon Bedrock models, guardrails, knowledge
bases; AWS Lambda functions; Amazon S3 objects; and an AWS KMS key.

- Amazon Bedrock permissions are required for Amazon Bedrock agents to invoke
  Amazon Bedrock models enabled at the project level. This policy also grants
  access to Amazon Bedrock resources managed within Amazon SageMaker Unified
  Studio.
- AWS Lambda permissions are required for Amazon Bedrock agents to run
  functions attached to an Amazon Bedrock IDE chat agent app.
- Amazon S3 permissions are required for Amazon Bedrock agents to access the
  project's Amazon S3 bucket.
- AWS KMS permissions are required to access Amazon Bedrock and Amazon S3 data
  encrypted with a customer managed key.
  This policy allows the Amazon Bedrock service to access specific resources tagged with
  the same project ID as the service role. This tag restriction effectively only permits
  access to resources in the same project. By default, project users are not allowed to
  change service role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockAgentServiceRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockAgentServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockAgentServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

# AWS policy:

SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy

This policy provides access to configure vector stores and Amazon Bedrock knowledge
bases in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE knowledge base custom resource
service role. This role is part of the AmazonBedrockKnowledgeBase environment
blueprint.

This policy grants AWS Lambda-backed CloudFormation custom resources access to
Amazon Bedrock IDE knowledge bases and their Amazon OpenSearch Serverless
collections.

- Amazon Bedrock permissions are required for the custom resource to start and
  query Amazon Bedrock knowledge base ingestion jobs.
- Amazon OpenSearch Serverless permissions for the custom resource to prepare
  Amazon OpenSearch Serverless collections for use with Amazon Bedrock knowledge
  bases.
  This policy allows the Amazon Bedrock service to access specific resources tagged with
  the same project ID as the service role. This tag restriction effectively only permits
  access to resources in the same project. By default, project users are not allowed to
  change service role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md") in the _AWS Managed Policy Reference_.

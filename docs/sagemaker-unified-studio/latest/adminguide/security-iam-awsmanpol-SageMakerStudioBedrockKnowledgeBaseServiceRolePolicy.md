# AWS policy:

SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy

This policy allows Amazon Bedrock Knowledge Bases to access Amazon Bedrock models and
data sources in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE knowledge base service role. This
role is part of the AmazonBedrockKnowledgeBase environment blueprint.

This policy grants the Amazon Bedrock service access to resources attached to Amazon
Bedrock IDE knowledge bases, including Amazon Bedrock models, Amazon OpenSearch
Serverless collections, Amazon S3 objects, and an AWS KMS key.

- Amazon Bedrock permissions are required for Amazon Bedrock knowledge bases to
  invoke Amazon Bedrock models enabled at the project level and generate
  queries.
- AWS SQL Workbench permissions are required to generate SQL recommendations
  for querying structured data sources.
- Amazon OpenSearch Serverless permissions are required for Amazon Bedrock
  knowledge bases to access the vector search collections that store knowledge
  base embeddings.
- Amazon S3 permissions are required for Amazon Bedrock agents to access the
  project's Amazon S3 bucket.
- AWS KMS permissions are required to access Amazon Bedrock and Amazon S3 data
  encrypted with a customer managed key.
  This policy allows the Amazon Bedrock service to access specific resources tagged with
  the same project ID as the service role. This tag restriction effectively only permits
  access to resources in the same project. By default, project users are not allowed to
  change service role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

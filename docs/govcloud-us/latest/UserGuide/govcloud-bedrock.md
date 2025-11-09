# Amazon Bedrock in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) and AWS GovCloud (US-East).

Amazon Bedrock provides a broad set of capabilities you need to build generative AI applications, simplifying development while maintaining privacy and security. You can easily experiment with Foundation Models (FMs) and privately customize them. Since Amazon Bedrock is serverless, you don’t have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications.

## How Amazon Bedrock differs for AWS GovCloud (US)

- Model availability for all regions, including AWS GovCloud (US), is available at [Model support by AWS Region](../../../bedrock/latest/userguide/models-regions.md "../../../bedrock/latest/userguide/models-regions.md").
- The following models have FedRAMP and IL4/5 authorization
  - All Titan Models
  - Claude 3.5 Sonnet v1
  - Claude 3 Haiku
  - Llama 3 8B
  - Llama 3 70B

- Feature support for all regions, including AWS GovCloud (US), is available at [Feature support by AWS Region](../../../bedrock/latest/userguide/features-regions.md "../../../bedrock/latest/userguide/features-regions.md").
- Bedrock Data Automation is currently available in AWS GovCloud (US-West).

## Documentation for Amazon Bedrock

[Amazon Bedrock documentation](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

The following customer-defined metadata may leave the AWS GovCloud (US) Regions only when the customer asks AWS to investigate a reported issue:

- Custom model metadata
- Provisioned throughput metadata for the no-commit option

Amazon Bedrock model evaluation metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating an Amazon Bedrock model evaluation job, such as the following:

- Inference configuration
- Evaluation configuration
- IAM role Amazon Resource Names
- Amazon S3 bucket names and object prefixes
- Resource tags

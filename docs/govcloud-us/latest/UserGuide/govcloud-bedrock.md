# Amazon Bedrock in AWS GovCloud (US)

Amazon Bedrock provides a broad set of capabilities you need to build generative AI applications, simplifying development while maintaining privacy and security. You can easily experiment with Foundation Models (FMs) and privately customize them. Since Amazon Bedrock is serverless, you don’t have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Amazon Bedrock differs

The following differences apply to Amazon Bedrock:

- Model availability for all regions, including AWS GovCloud (US), is available at [Regional availability by models](../../../bedrock/latest/userguide/models-region-compatibility.md "../../../bedrock/latest/userguide/models-region-compatibility.md").
- FedRAMP Class D certification and DoD CSP SRG IL-4 and IL-5 approvals are available at [Amazon Bedrock models - FedRAMP and DoD CSP SRG (IL4/IL5) certification status](https://aws.amazon.com/compliance/services-in-scope/FedRAMP/amazon-bedrock-models/ "https://aws.amazon.com/compliance/services-in-scope/FedRAMP/amazon-bedrock-models/").

## Documentation

- [Amazon Bedrock documentation](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md")

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

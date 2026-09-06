

# Security Hub CSPM controls for Amazon Bedrock
<a name="bedrock-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Bedrock service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [Bedrock.1] Amazon Bedrock data sources should be encrypted with customer managed AWS KMS keys
<a name="bedrock-1"></a>

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::Bedrock::DataSource`

**AWS Config rule:** [bedrock-data-source-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/bedrock-data-source-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock data source is encrypted at rest with a customer managed AWS KMS key. The control fails if the data source isn't encrypted with a customer managed KMS key.

By default, Amazon Bedrock encrypts data source content with AWS managed keys. Using a customer managed KMS key gives you full control over the encryption key lifecycle, including rotation, access policies, and auditing through AWS CloudTrail. This helps meet compliance requirements that mandate customer-controlled encryption for sensitive data ingested into knowledge bases.

### Remediation
<a name="bedrock-1-remediation"></a>

To encrypt your Amazon Bedrock data source with a customer managed KMS key, see [Modify a data source for your Amazon Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-update.html) in the *Amazon Bedrock User Guide*.
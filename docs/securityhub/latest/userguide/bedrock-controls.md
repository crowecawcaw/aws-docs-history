# Security Hub CSPM controls for Amazon Bedrock

These AWS Security Hub CSPM controls evaluate the Amazon Bedrock service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Bedrock.1] Amazon Bedrock data sources should be encrypted with customer managed AWS KMS keys

**Category:** Protect > Data protection >
Encryption of data at rest

**Severity:** Medium

**Resource type:**
`AWS::Bedrock::DataSource`

**AWS Config rule:**
[bedrock-data-source-encryption-enabled](../../../config/latest/developerguide/bedrock-data-source-encryption-enabled.md "../../../config/latest/developerguide/bedrock-data-source-encryption-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock data source is encrypted at rest with a
customer managed AWS KMS key. The control fails if the data source isn't encrypted with a
customer managed KMS key.

By default, Amazon Bedrock encrypts data source content with AWS managed keys. Using
a customer managed KMS key gives you full control over the encryption key lifecycle,
including rotation, access policies, and auditing through AWS CloudTrail. This helps meet
compliance requirements that mandate customer-controlled encryption for sensitive data
ingested into knowledge bases.

### Remediation

To encrypt your Amazon Bedrock data source with a customer managed KMS key, see
[Modify a data source for your
Amazon Bedrock knowledge base](../../../bedrock/latest/userguide/kb-ds-update.md "../../../bedrock/latest/userguide/kb-ds-update.md") in the _Amazon
Bedrock User Guide_.

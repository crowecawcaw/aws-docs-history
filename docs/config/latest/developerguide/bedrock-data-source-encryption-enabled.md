# bedrock-data-source-encryption-enabled

Checks whether an Amazon Bedrock data source is encrypted with a customer-managed KMS key. The rule is NON\_COMPLIANT if the data source does not have ServerSideEncryptionConfiguration.KmsKeyArn configured.

**Identifier:** BEDROCK\_DATA\_SOURCE\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::Bedrock::DataSource

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hong Kong), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

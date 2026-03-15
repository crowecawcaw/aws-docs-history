# transfer-connector-as2-encryption-algorithm-check

Checks that AWS Transfer Family AS2 connectors are not configured with a weak encryption algorithm. The rule is NON_COMPLIANT if configuration.As2Config.EncryptionAlgorithm is 'DES_EDE3_CBC'.

**Identifier:** TRANSFER_CONNECTOR_AS2_ENCRYPTION_ALGORITHM_CHECK

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedEncryptionAlgorithms (Optional)
Type: CSV

Comma-separated list of approved encryption algorithms for the rule to check. If provided, the rule is NON_COMPLIANT if configuration.As2Config.EncryptionAlgorithm is configured with a value not specified in this parameter. Valid values include: 'AES128_CBC', 'AES192_CBC', 'AES256_CBC', 'NONE', and 'DES_EDE3_CBC'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

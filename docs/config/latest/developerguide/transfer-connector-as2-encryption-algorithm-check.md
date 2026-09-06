

# transfer-connector-as2-encryption-algorithm-check
<a name="transfer-connector-as2-encryption-algorithm-check"></a>

Checks that AWS Transfer Family AS2 connectors are not configured with a weak encryption algorithm. The rule is NON\_COMPLIANT if configuration.As2Config.EncryptionAlgorithm is 'DES\_EDE3\_CBC'. 



**Identifier:** TRANSFER\_CONNECTOR\_AS2\_ENCRYPTION\_ALGORITHM\_CHECK

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedEncryptionAlgorithms (Optional)Type: CSV  
Comma-separated list of approved encryption algorithms for the rule to check. If provided, the rule is NON\_COMPLIANT if configuration.As2Config.EncryptionAlgorithm is configured with a value not specified in this parameter. Valid values include: 'AES128\_CBC', 'AES192\_CBC', 'AES256\_CBC', 'NONE', and 'DES\_EDE3\_CBC'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1575c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
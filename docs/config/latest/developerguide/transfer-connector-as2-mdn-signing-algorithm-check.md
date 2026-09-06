

# transfer-connector-as2-mdn-signing-algorithm-check
<a name="transfer-connector-as2-mdn-signing-algorithm-check"></a>

Checks if AWS Transfer Family AS2 connectors are configured with a specified MDN signing algorithm for MDN responses. The rule is NON\_COMPLIANT if configuration.As2Config.MdnSigningAlgorithm is a value not specified in the required rule parameter. 



**Identifier:** TRANSFER\_CONNECTOR\_AS2\_MDN\_SIGNING\_ALGORITHM\_CHECK

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedMdnSigningAlgorithmsType: CSV  
Comma-separated list of approved MDN signing algorithms for the rule to check. The rule is NON\_COMPLIANT if configuration.As2Config.MdnSigningAlgorithm is configured with a value not specified in this parameter. Valid values include: 'SHA256', 'SHA384', 'SHA512', 'SHA1', 'DEFAULT', and 'NONE'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1577c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
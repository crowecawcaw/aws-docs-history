

# transfer-connector-as2-signing-algorithm-check
<a name="transfer-connector-as2-signing-algorithm-check"></a>

Checks if AWS Transfer Family AS2 connectors are configured with a signing algorithm. The rule is NON\_COMPLIANT if configuration.As2Config.SigningAlgorithm is 'NONE'. 



**Identifier:** TRANSFER\_CONNECTOR\_AS2\_SIGNING\_ALGORITHM\_CHECK

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedSigningAlgorithms (Optional)Type: CSV  
Comma-separated list of approved signing algorithms for the rule to check. If provided, the rule is NON\_COMPLIANT if configuration.As2Config.SigningAlgorithm is configured with a value not specified in this parameter. Valid values include: 'SHA256', 'SHA384', 'SHA512', 'SHA1', and 'NONE'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1579c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
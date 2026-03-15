# transfer-connector-as2-mdn-signing-algorithm-check

Checks if AWS Transfer Family AS2 connectors are configured with a specified MDN signing algorithm for MDN responses. The rule is NON_COMPLIANT if configuration.As2Config.MdnSigningAlgorithm is a value not specified in the required rule parameter.

**Identifier:** TRANSFER_CONNECTOR_AS2_MDN_SIGNING_ALGORITHM_CHECK

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedMdnSigningAlgorithms
Type: CSV

Comma-separated list of approved MDN signing algorithms for the rule to check. The rule is NON_COMPLIANT if configuration.As2Config.MdnSigningAlgorithm is configured with a value not specified in this parameter. Valid values include: 'SHA256', 'SHA384', 'SHA512', 'SHA1', 'DEFAULT', and 'NONE'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

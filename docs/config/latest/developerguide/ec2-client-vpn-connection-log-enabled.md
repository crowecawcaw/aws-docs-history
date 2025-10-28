# ec2-client-vpn-connection-log-enabled

Checks if AWS Client VPN endpoint has client connection logging enabled. The rule is NON_COMPLIANT if 'Configuration.ConnectionLogOptions.Enabled' is set to false.

**Identifier:** EC2_CLIENT_VPN_CONNECTION_LOG_ENABLED

**Resource Types:** AWS::EC2::ClientVpnEndpoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

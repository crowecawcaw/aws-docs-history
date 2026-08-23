# ec2-transit-gateway-auto-vpc-attach-disabled

Checks if Amazon Elastic Compute Cloud (Amazon EC2) Transit Gateways have 'AutoAcceptSharedAttachments' enabled. The rule is NON\_COMPLIANT for a Transit Gateway if 'AutoAcceptSharedAttachments' is set to 'enable'.

**Identifier:** EC2\_TRANSIT\_GATEWAY\_AUTO\_VPC\_ATTACH\_DISABLED

**Resource Types:** AWS::EC2::TransitGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Osaka), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

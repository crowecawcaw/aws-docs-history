# ec2-vpn-connection-ike-version-check

Checks if an Amazon EC2 VPN connection is configured to use only IKEv2 protocol. The rule is NON\_COMPLIANT if the VPN connection's tunnel allows IKE versions other than IKEv2.

**Identifier:** EC2\_VPN\_CONNECTION\_IKE\_VERSION\_CHECK

**Resource Types:** AWS::EC2::VPNConnection

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), China (Beijing), Middle East (UAE), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

# vpc-sg-open-only-to-authorized-ports

Checks if security groups allowing unrestricted incoming traffic ('0.0.0.0/0' or '::/0') only allow inbound TCP or UDP connections on authorized ports. The rule is NON_COMPLIANT if such security groups do not have ports specified in the rule parameters.

###### Note

This rule evaluates Amazon EC2 security groups with ingress rule set to IPv4='0.0.0.0/0' or IPv6='::/'.
If the security group does not have one of those destinations, this rule returns `NOT_APPLICABLE`.

**Identifier:** VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

authorizedTcpPorts (Optional)
Type: String

Comma-separated list of TCP ports authorized to be open to 0.0.0.0/0 or ::/0. Ranges are defined by dash, for example, "443,1020-1025".

authorizedUdpPorts (Optional)
Type: String

Comma-separated list of UDP ports authorized to be open to 0.0.0.0/0 or ::/0. Ranges are defined by dash, for example, "500,1020-1025".

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

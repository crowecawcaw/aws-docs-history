# ec2-security-group-attached-to-eni

Checks if non-default security groups are attached to elastic network interfaces. The rule is NON\_COMPLIANT if the security group is not associated with a network interface.

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

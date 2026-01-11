# vpc-default-security-group-closed

Checks if the default security group of any Amazon Virtual Private Cloud (Amazon VPC) does not allow inbound or outbound traffic. The rule is NON_COMPLIANT if the default security group has one or more inbound or outbound traffic rules.

###### Note

There may be a delay between when AWS Config records the deletion of related resources such as default security groups, which are deleted as part of the Amazon VPC deletion. As a result,
even if all default security groups or other related resources have been deleted or remediated,
the rule may report NON_COMPLIANT until the next account baselining process.

**Identifier:** VPC_DEFAULT_SECURITY_GROUP_CLOSED

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** Only available in Middle East (Bahrain), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), US West (Oregon) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

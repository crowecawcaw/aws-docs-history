# ec2-instance-launched-with-allowed-ami

Checks if running or stopped EC2 instances were launched with Amazon Machine Images (AMIs) that meet your Allowed AMIs criteria. The rule is NON_COMPLIANT if an AMI doesn't meet the Allowed AMIs criteria and the Allowed AMIs settings isn't disabled.

**Identifier:** EC2_INSTANCE_LAUNCHED_WITH_ALLOWED_AMI

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

InstanceStateNameList (Optional)
Type: CSV

Comma-separate list of Amazon EC2 instance states for the rule to check. Valid values are "running" and "stopped".

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

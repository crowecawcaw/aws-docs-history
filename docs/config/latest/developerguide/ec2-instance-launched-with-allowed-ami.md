

# ec2-instance-launched-with-allowed-ami
<a name="ec2-instance-launched-with-allowed-ami"></a>

Checks if running or stopped EC2 instances were launched with Amazon Machine Images (AMIs) that meet your Allowed AMIs criteria. The rule is NON\_COMPLIANT if an AMI doesn't meet the Allowed AMIs criteria and the Allowed AMIs settings isn't disabled. 



**Identifier:** EC2\_INSTANCE\_LAUNCHED\_WITH\_ALLOWED\_AMI

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

InstanceStateNameList (Optional)Type: CSV  
Comma-separate list of Amazon EC2 instance states for the rule to check. Valid values are "running" and "stopped".

## AWS CloudFormation template
<a name="w2aac20c16c17b7d555c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
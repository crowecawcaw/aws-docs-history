# ec2-instance-managed-by-systems-manager

###### Important

For this rule, the rule identifier (EC2_INSTANCE_MANAGED_BY_SSM) and rule name (ec2-instance-managed-by-systems-manager) are different.

Checks if your Amazon EC2 instances are managed by AWS Systems Manager Agent (SSM Agent).
The rule is NON_COMPLIANT if an EC2 instance is running and the SSM Agent is stopped, or if an EC2 instance is running and the SSM Agent is terminated.

###### Note

The rule will not return NON_COMPLIANT if an EC2 instance is stopped and the SSM Agent is running.

**Identifier:** EC2_INSTANCE_MANAGED_BY_SSM

**Resource Types:** AWS::EC2::Instance, AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

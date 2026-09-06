

# ec2-instance-managed-by-systems-manager
<a name="ec2-instance-managed-by-systems-manager"></a>

**Important**  
For this rule, the rule identifier (EC2\_INSTANCE\_MANAGED\_BY\_SSM) and rule name (ec2-instance-managed-by-systems-manager) are different.

Checks if your Amazon EC2 instances are managed by AWS Systems Manager Agent (SSM Agent). The rule is NON\_COMPLIANT if an EC2 instance is running and the SSM Agent is stopped, or if an EC2 instance is running and the SSM Agent is terminated.

**Note**  
The rule will not return NON\_COMPLIANT if an EC2 instance is stopped and the SSM Agent is running.



**Identifier:** EC2\_INSTANCE\_MANAGED\_BY\_SSM

**Resource Types:** AWS::EC2::Instance, AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d557c23"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
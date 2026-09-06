

# desired-instance-type
<a name="desired-instance-type"></a>

Checks if your EC2 instances are of a specific instance type. The rule is NON\_COMPLIANT if an EC2 instance is not specified in the parameter list. For a list of supported EC2 instance types, see Instance types in the EC2 User Guide for Linux Instances. 



**Identifier:** DESIRED\_INSTANCE\_TYPE

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

instanceTypeType: CSV  
 Comma-separated list of EC2 instance types (for example, "t2.small, m4.large, i2.xlarge").

## AWS CloudFormation template
<a name="w2aac20c16c17b7d455c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
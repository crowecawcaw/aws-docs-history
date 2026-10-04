

# ebs-optimized-instance
<a name="ebs-optimized-instance"></a>

Checks if Amazon EBS optimization is enabled for your Amazon Elastic Compute Cloud (Amazon EC2) instances that can be Amazon EBS-optimized. The rule is NON\_COMPLIANT if EBS optimization is not enabled for an Amazon EC2 instance that can be EBS-optimized. 

**Note**  
EC2 instances which are EBS-optimized by default always result in rule evaluations returning `COMPLIANT`.

**Identifier:** EBS\_OPTIMIZED\_INSTANCE

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d523c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
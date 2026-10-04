

# ec2-instance-profile-attached
<a name="ec2-instance-profile-attached"></a>

Checks if an EC2 instance has an AWS Identity and Access Management (IAM) profile attached to it. The rule is NON\_COMPLIANT if no IAM profile is attached to the EC2 instance. 



**Identifier:** EC2\_INSTANCE\_PROFILE\_ATTACHED

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

IamInstanceProfileArnList (Optional)Type: CSV  
Comma-separated list of IAM profile Amazon Resource Names (ARNs) that can be attached to Amazon EC2 instances.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d563c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).


# ec2-launch-templates-ebs-volume-encrypted
<a name="ec2-launch-templates-ebs-volume-encrypted"></a>

Checks whether Amazon EC2 launch templates have encryption enabled for all attached EBS volumes.The rule is NON\_COMPLIANT if encryption is set to False for any EBS volume configured in the launch template. 



**Identifier:** EC2\_LAUNCH\_TEMPLATES\_EBS\_VOLUME\_ENCRYPTED

**Resource Types:** AWS::EC2::LaunchTemplate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d571c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
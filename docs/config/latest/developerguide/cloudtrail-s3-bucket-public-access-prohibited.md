

# cloudtrail-s3-bucket-public-access-prohibited
<a name="cloudtrail-s3-bucket-public-access-prohibited"></a>

Checks if the S3 bucket configurations for your AWS CloudTrail logs block public access. The rule is NON\_COMPLIANT if at least one S3 bucket for a CloudTrail trail is publicly accessible. 



**Identifier:** CLOUDTRAIL\_S3\_BUCKET\_PUBLIC\_ACCESS\_PROHIBITED

**Resource Types:** AWS::CloudTrail::Trail

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d341c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).


# cloudtrail-s3-bucket-access-logging
<a name="cloudtrail-s3-bucket-access-logging"></a>

Checks if the S3 bucket configurations for your AWS CloudTrail logs have Amazon S3 server access logging enabled. The rule is NON\_COMPLIANT if at least one S3 bucket for a CloudTrail trail does not have S3 server access logging enabled. 



**Identifier:** CLOUDTRAIL\_S3\_BUCKET\_ACCESS\_LOGGING

**Resource Types:** AWS::CloudTrail::Trail

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d339c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
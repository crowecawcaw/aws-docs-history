

# s3-access-point-in-vpc-only
<a name="s3-access-point-in-vpc-only"></a>

Checks if an Amazon S3 access point does not allow access from the internet (NetworkOrigin is VPC). The rule is NON\_COMPLIANT if NetworkOrigin is Internet. 



**Identifier:** S3\_ACCESS\_POINT\_IN\_VPC\_ONLY

**Resource Types:** AWS::S3::AccessPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1377c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
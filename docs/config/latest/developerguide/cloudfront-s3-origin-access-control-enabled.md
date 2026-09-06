

# cloudfront-s3-origin-access-control-enabled
<a name="cloudfront-s3-origin-access-control-enabled"></a>

Checks if an Amazon CloudFront distribution with an Amazon Simple Storage Service (Amazon S3) Origin type has origin access control (OAC) enabled. The rule is NON\_COMPLIANT for CloudFront distributions with Amazon S3 origins that don't have OAC enabled. 



**Identifier:** CLOUDFRONT\_S3\_ORIGIN\_ACCESS\_CONTROL\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d319c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
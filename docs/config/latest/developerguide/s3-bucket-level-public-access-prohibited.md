

# s3-bucket-level-public-access-prohibited
<a name="s3-bucket-level-public-access-prohibited"></a>

Checks if S3 buckets are publicly accessible. The rule is NON\_COMPLIANT if an S3 bucket is not listed in the `excludedPublicBuckets` parameter and bucket level settings are public. 



**Identifier:** S3\_BUCKET\_LEVEL\_PUBLIC\_ACCESS\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

excludedPublicBuckets (Optional)Type: CSV  
Comma-separated list of known allowed public Amazon S3 bucket names.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1393c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
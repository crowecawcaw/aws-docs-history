# s3express-dir-bucket-lifecycle-rules-check

Checks if lifecycle rules are configured for an Amazon S3 Express directory bucket. The rule is NON_COMPLIANT if there is no active lifecycle configuration rules or the configuration does not match with the parameter values.

**Identifier:** S3EXPRESS_DIR_BUCKET_LIFECYCLE_RULES_CHECK

**Resource Types:** AWS::S3Express::DirectoryBucket

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), US East (Ohio), Europe (Ireland), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon) Region

**Parameters:**

targetExpirationDays (Optional)
Type: int

Number of days after creation when objects are deleted from Amazon S3 Express directory buckets.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

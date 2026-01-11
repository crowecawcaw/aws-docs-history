# s3-bucket-server-side-encryption-enabled

Checks if your Amazon S3 bucket either has the Amazon S3 default encryption enabled
or that the Amazon S3 bucket policy explicitly denies `put-object` requests without server side encryption that uses AES-256 or AWS Key Management Service.
The rule is NON_COMPLIANT if your Amazon S3 bucket is not encrypted by default.

**Identifier:** S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

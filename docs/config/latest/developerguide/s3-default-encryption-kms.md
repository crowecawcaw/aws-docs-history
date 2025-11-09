# s3-default-encryption-kms

Checks if the S3 buckets are encrypted with AWS Key Management Service (AWS KMS). The rule is NON_COMPLIANT if the S3 bucket is not encrypted with an AWS KMS key.

**Identifier:** S3_DEFAULT_ENCRYPTION_KMS

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns (Optional)
Type: CSV

Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon S3 Buckets.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

# s3-bucket-replication-enabled

Checks if S3 buckets have replication rules enabled. The rule is NON_COMPLIANT if an S3 bucket does not have a replication rule or has a replication rule that is not enabled.

**Identifier:** S3_BUCKET_REPLICATION_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

ReplicationType (Optional)
Type: String

Accepted values: 'CROSS-REGION' and 'SAME-REGION'. Enter 'CROSS-REGION' for the rule to check that all buckets have only Cross-Region Replication enabled. Enter 'SAME-REGION' for the rule to check that all buckets have only Same-Region Replication enabled.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

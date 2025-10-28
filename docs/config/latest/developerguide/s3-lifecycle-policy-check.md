# s3-lifecycle-policy-check

Checks if a lifecycle rule is configured for an Amazon Simple Storage Service (Amazon S3) bucket. The rule is NON_COMPLIANT if there is no active lifecycle configuration rules or the configuration does not match with the parameter values.

**Identifier:** S3_LIFECYCLE_POLICY_CHECK

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

targetTransitionDays (Optional)
Type: int

Number of days after object creation when objects are transitioned to a specified storage class (for example, 30 days).

targetExpirationDays (Optional)
Type: int

Number of days after object creation when objects are deleted (for example, 395 days).

targetTransitionStorageClass (Optional)
Type: String

Destination storage class type.
For example, Amazon S3 Standard-Infrequent Access (S3 Standard-IA). For more information, see [Understanding and managing Amazon S3 storage classes](../../../AmazonS3/latest/dev/storage-class-intro.md "../../../AmazonS3/latest/dev/storage-class-intro.md").

targetPrefix (Optional)
Type: String

Amazon S3 Object prefix to identify one or more objects.

bucketNames (Optional)
Type: CSV

Comma-separated list of Amazon S3 bucket names that have lifecycle policy enabled.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

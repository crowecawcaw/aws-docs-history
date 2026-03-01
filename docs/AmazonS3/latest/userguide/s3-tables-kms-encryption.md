# Using server-side encryption with AWS KMS keys (SSE-KMS) in table buckets

###### Topics

- [How SSE-KMS works for tables and table buckets](#kms-tables-how "#kms-tables-how")
- [Enforcing and scoping SSE-KMS use for tables and table buckets](tables-require-kms.md "tables-require-kms.md")
- [Monitoring and Auditing SSE-KMS encryption for tables and table buckets](#kms-tables-audit "#kms-tables-audit")
- [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md")
- [Specifying server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-specify.md "s3-tables-kms-specify.md")
  Table buckets have a default encryption configuration that automatically encrypts tables
  by using server-side encryption with Amazon S3 managed keys (SSE-S3). This encryption applies to
  all tables in your S3 table buckets, and comes at no cost to you.

If you need more control over your encryption keys, such as managing key rotation and
access policy grants, you can configure your table buckets to use server-side encryption
with AWS Key Management Service (AWS KMS) keys (SSE-KMS). The security controls in AWS KMS can help you meet
encryption-related compliance requirements. For more information about SSE-KMS, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").

## How SSE-KMS works for tables and table buckets

SSE-KMS with table buckets differs from SSE-KMS in general purpose buckets in the
following ways:

- You can specify encryption settings for table buckets and individual
  tables.
- You can only use customer managed keys with SSE-KMS. AWS managed keys aren't
  supported.
- You must grant permissions for certain roles and AWS service principals to
  access your AWS KMS key. For more information, see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md"). This includes granting access
  to:
  - The S3 maintenance principal – for performing table maintenance
    on encrypted tables
  - Your S3 Tables integration role – for working with encrypted
    tables in AWS analytics services
  - Your client access role – for direct access to encrypted tables
    from Apache Iceberg clients
  - The S3 Metadata principal – for updating encrypted S3 metadata
    tables

- Encrypted tables use table-level keys that minimize the number of requests
  made to AWS KMS to make working with SSE-KMS encrypted tables more cost effective.

**SSE-KMS encryption for table buckets**

When you create a table bucket, you can choose SSE-KMS as the default
encryption type and select a specific KMS key that will be used for
encryption. Any tables created within that bucket will automatically inherit
these encryption settings from their table bucket. You can use the AWS CLI, S3
API, or AWS SDKs to modify or remove the default encryption settings on a
table bucket at any time. When you modify the encryption settings on a table
bucket those settings apply only to new tables created in that bucket.
Encryption settings for pre-existing tables are not changed. For more
information, see [Specifying encryption for table buckets](s3-tables-kms-specify.md#specify-kms-table-bucket "s3-tables-kms-specify.md#specify-kms-table-bucket").

**SSE-KMS encryption for tables**

You also have an option to encrypt an individual table with a different
KMS key regardless of the bucket's default encryption configuration. To
set encryption for an individual table, you must specify the desired
encryption key at the time of table creation. If you want to change the
encryption for an existing table, then you'll need to create a table with
desired key and copy data from old table to the new one. For more
information, see [Specifying encryption for tables](s3-tables-kms-specify.md#specify-kms-table "s3-tables-kms-specify.md#specify-kms-table").

When using AWS KMS encryption, S3 Tables automatically creates unique table-level data
keys that encrypt new objects associated with each table. These keys are used for a
limited time period, minimizing the need for additional AWS KMS requests during encryption
operations and reducing the cost of encryption. This is similar to [S3 Bucket Keys for SSE-KMS](bucket-key.md#bucket-key-overview "bucket-key.md#bucket-key-overview").

## Monitoring and Auditing SSE-KMS encryption for tables and table buckets

To audit the usage of your AWS KMS keys for your SSE-KMS encrypted data, you can use
AWS CloudTrail logs. You can get insight into your [cryptographic
operations](../../../kms/latest/developerguide/concepts.md#cryptographic-operations "../../../kms/latest/developerguide/concepts.md#cryptographic-operations"), such as `GenerateDataKey` and `Decrypt`.
CloudTrail supports numerous [attribute
values](../../../awscloudtrail/latest/APIReference/API_LookupEvents.md "../../../awscloudtrail/latest/APIReference/API_LookupEvents.md") for filtering your search, including event name, user name, and event
source.

You can track encryption configuration requests for Amazon S3 tables and table buckets by
using CloudTrail events. The following API event names are used in CloudTrail logs:

- `s3tables:PutTableBucketEncryption`
- `s3tables:GetTableBucketEncryption`
- `s3tables:DeleteTableBucketEncryption`
- `s3tables:GetTableEncryption`
- `s3tables:CreateTable`
- `s3tables:CreateTableBucket`

###### Note

EventBridge isn't supported for table buckets.

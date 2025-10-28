# Data protection in Data Exports

Learn how the AWS shared responsibility model applies to data protection in Data Exports.

## S3 security best practices

Data Exports delivers your billing and cost management data to an Amazon S3 bucket. There are a
number of steps you can take to make sure your S3 bucket is secure. For more information,
see [Security best practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") in the _Amazon S3 User
Guide_.

## Data encryption in S3

By default, your data exports are encrypted using server-side encryption with Amazon S3
managed keys (SSE-S3). If you want to use Amazon Key Management Service (KMS) encryption
(SSE-KMS) to encrypt your exports, you need to trigger encryption with KMS after the export
has been delivered. For more information, see [Setting
default server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the
_Amazon S3 User Guide_.

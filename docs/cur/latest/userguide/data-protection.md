

# Data protection in Data Exports
<a name="data-protection"></a>

Learn how the AWS shared responsibility model applies to data protection in Data Exports.

## S3 security best practices
<a name="s3-security-best-practices"></a>

Data Exports delivers your billing and cost management data to an Amazon S3 bucket. There are a number of steps you can take to make sure your S3 bucket is secure. For more information, see [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) in the *Amazon S3 User Guide*.

## Data encryption in S3
<a name="s3-data-encryption"></a>

By default, your data exports are encrypted using server-side encryption with Amazon S3 managed keys (SSE-S3). If you want to use Amazon Key Management Service (KMS) encryption (SSE-KMS) to encrypt your exports, you need to trigger encryption with KMS after the export has been delivered. For more information, see [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the *Amazon S3 User Guide*.
# Protecting S3 table data with encryption

Data protection refers to protecting data while it's in transit (as it travels to and from
Amazon S3) and at rest (while it's stored on disks in Amazon S3 data centers). S3 Tables always protects data in transit using Transport Layer Security (1.2 and above) through HTTPS. For protecting data at rest in S3 table buckets, you have the following options:

**Server-side encryption with Amazon S3 managed keys (SSE-S3)**
All Amazon S3 table buckets have encryption configured by default. The default option for server-side encryption is with Amazon S3 managed keys (SSE-S3). This encryption comes at no cost to you and applies to all tables in your S3 table buckets unless you specify another form of encryption. Each object is encrypted with a unique key. As an additional safeguard, SSE-S3 encrypts the key itself with a root key that it regularly rotates. SSE-S3 uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.

**Server-side encryption with AWS KMS keys (SSE-KMS)**
You can choose to configure table buckets or tables to use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS). The security controls in AWS KMS can help you meet encryption-related compliance requirements. SSE-KMS gives you more control over your encryption keys by allowing you to do the following:

- Create, view, edit, monitor, enable or disable, rotate, and schedule deletion of KMS keys.
- Define the policies that control how and by whom KMS keys can be used.
- Track key usage in AWS CloudTrail to verify your KMS keys are being used correctly.

S3 Tables supports using customer managed keys in SSE-KMS to encrypt tables. AWS managed keys are not supported. For more information on using SSE-KMS for S3 tables and table buckets, see [Using server-side encryption with AWS KMS keys
(SSE-KMS) in table buckets](s3-tables-kms-encryption.md "s3-tables-kms-encryption.md").



# Security for data delivery
<a name="data-delivery-security"></a>

 Use this topic to learn about the security features and best practices for data delivery in Amazon Kinesis Data Streams, including encryption, access control, and audit logging. 

## Encryption in transit
<a name="data-delivery-security-encryption-transit"></a>

 All communication between data delivery and its destinations is encrypted in transit using TLS 1.2 or later. This includes data delivered to streaming tables on Apache Iceberg and general purpose Amazon S3 buckets, as well as communication with AWS Glue Schema Registry and the dead-letter queue. 

## Encryption at rest
<a name="data-delivery-security-encryption-rest"></a>

 Streaming tables and Amazon S3 delivery store delivered data in Amazon S3. All delivered data is encrypted at rest server-side. This applies to both destination types, because streaming tables on Apache Iceberg and general purpose Amazon S3 buckets both store data in Amazon S3. You do not need to take any action for your delivered data to be encrypted. 

### Options for encryption at rest
<a name="data-delivery-security-encryption-options"></a>

 You can choose one of the following encryption options for delivered data: 
+ **SSE-S3 (default)** – Server-side encryption with Amazon S3 managed keys. This is the default if no customer managed key is specified. No additional configuration is required.
+ **SSE-KMS with a customer managed key** – Server-side encryption with a symmetric customer managed AWS KMS key that you own and manage.

### Using a customer managed key for encryption at rest
<a name="data-delivery-security-encryption-cmk"></a>

 Because delivered data is stored in Amazon S3 for both destination types, encryption at rest works the same way as Amazon S3 server-side encryption, including how AWS KMS keys are used, the required key permissions, encryption context, and auditing. Only symmetric encryption AWS KMS keys are supported. For complete details about how Amazon S3 uses AWS KMS keys for server-side encryption, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon S3 User Guide*. 

 To encrypt delivered data with a customer managed key, specify the key in the `EncryptionConfiguration` parameter when you create the delivery with `CreateChannel`. For more information, see the [CreateChannel](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateChannel.html) operation in the *Amazon Kinesis Data Streams API Reference*. The encryption configuration is immutable after a delivery is created; to change it, delete the delivery and create a new one. 

 For the specific AWS KMS permissions the service execution role needs to use a customer managed key, see [IAM permissions for data delivery](data-delivery-iam.md). 

**Note**  
 You must use a customer managed AWS KMS key for destination encryption. An AWS managed key (the `aws/kinesis` alias) is not supported. Source streams encrypted with an AWS managed key are also not supported; see [Source stream encryption](#data-delivery-security-source-stream-encryption). 

### Monitoring AWS KMS interaction
<a name="data-delivery-security-encryption-monitoring"></a>

 You can audit how your customer managed key is used with AWS CloudTrail. AWS KMS cryptographic operations that encrypt and decrypt delivered objects, such as `GenerateDataKey` and `Decrypt`, appear in your CloudTrail event history. For more information about finding AWS KMS events, see [Auditing AWS KMS key usage](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS Key Management Service Developer Guide*. 

## Source stream encryption
<a name="data-delivery-security-source-stream-encryption"></a>

**Important**  
 If your Kinesis data stream is encrypted with an AWS managed key (the `aws/kinesis` alias), you cannot create a delivery. `CreateChannel` fails synchronously for streams encrypted with an AWS managed key. 

 To use streaming tables or Amazon S3 delivery on an encrypted stream, use a customer managed key for stream encryption. You can change the encryption key on an existing stream using `StartStreamEncryption`. Streams encrypted with a customer managed key are fully supported. 

## IAM access control
<a name="data-delivery-security-iam"></a>

 Follow these best practices for IAM access control with data delivery: 
+ **Least privilege** – Grant only the minimum permissions required for the service execution role. Scope Amazon S3 permissions to specific buckets and prefixes rather than using wildcards.
+ **Scope to specific resources** – Restrict permissions to the specific bucket, table bucket, or table that the delivery writes to. Avoid using `Resource: "*"`.
+ **Confused deputy prevention** – Always include `aws:SourceArn` and `aws:SourceAccount` conditions in the trust policy to prevent other services or accounts from assuming the execution role.

## AWS CloudTrail logging
<a name="data-delivery-security-cloudtrail"></a>

 All delivery API calls are logged by AWS CloudTrail. This includes `CreateChannel`, `UpdateChannel`, `DeleteChannel`, `DescribeChannel`, and `ListChannels`. You can use AWS CloudTrail logs to audit who created, modified, or deleted delivery resources, and when those actions occurred. 
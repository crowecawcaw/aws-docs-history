After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Data Protection in Amazon Kinesis Data Analytics for SQL Applications

You can protect your data using tools that are provided by AWS. Kinesis Data Analytics can work with services that support encrypting data, including Kinesis Data Streams, Firehose, and Amazon S3.

## Data Encryption in Kinesis Data Analytics

### Encryption at Rest

Note the following about encrypting data at rest with Kinesis Data Analytics:

- You can encrypt data on the incoming Kinesis data stream using [StartStreamEncryption](../../../kinesis/latest/APIReference/API_StartStreamEncryption.md "../../../kinesis/latest/APIReference/API_StartStreamEncryption.md").
  For more information, see [What Is Server-Side Encryption for Kinesis Data Streams?](../../../streams/latest/dev/what-is-sse.md "../../../streams/latest/dev/what-is-sse.md").
- Output data can be encrypted at rest using Firehose to store data in an encrypted Amazon S3 bucket. You can specify the encryption key that your Amazon S3 bucket uses. For more information, see
  [Protecting Data Using Server-Side Encryption with KMS–Managed Keys (SSE-KMS)](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md").
- Your application's code is encrypted at rest.
- Your application's reference data is encrypted at rest.

### Encryption In Transit

Kinesis Data Analytics encrypts all data in transit. Encryption in transit is enabled for all Kinesis Data Analytics applications and cannot be disabled.

Kinesis Data Analytics encrypts data in transit in the following scenarios:

- Data in transit from Kinesis Data Streams to Kinesis Data Analytics.
- Data in transit between internal components within Kinesis Data Analytics.
- Data in transit between Kinesis Data Analytics and Firehose.

### Key Management

Data encryption in Kinesis Data Analytics uses service-managed keys. Customer-managed keys are not supported.

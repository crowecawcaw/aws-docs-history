Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Data protection in Amazon Managed Service for Apache Flink

You can protect your data using tools that are provided by AWS. Amazon MSF can work with services that support encrypting data, including Firehose, and Amazon S3.

## Data encryption in Managed Service for Apache Flink

### Encryption at rest

Note the following about encrypting data at rest with Amazon MSF:

- You can encrypt data on the incoming Kinesis data stream using
  [StartStreamEncryption](../../../kinesis/latest/APIReference/API_StartStreamEncryption.md "../../../kinesis/latest/APIReference/API_StartStreamEncryption.md").
  For more information, see [What Is Server-Side Encryption for Kinesis Data Streams?](../../../streams/latest/dev/what-is-sse.md "../../../streams/latest/dev/what-is-sse.md").
- Output data can be encrypted at rest using Firehose to store data in an encrypted Amazon S3 bucket. You can specify the encryption key that your Amazon S3 bucket uses. For more information, see
  [Protecting Data Using Server-Side Encryption with KMS–Managed Keys (SSE-KMS)](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md").
- Amazon MSF can read from any streaming source, and write to any streaming or database destination. Ensure that your sources and destinations encrypt all data in transit and data at rest.
- Your application's code is encrypted at rest.
- Durable application storage is encrypted at rest.
- Running application storage is encrypted at rest.

### Encryption in transit

Amazon MSF encrypts all data in transit. Encryption in transit is enabled for all Amazon MSF applications and cannot be disabled.

Amazon MSF encrypts data in transit in the following scenarios:

- Data in transit from Kinesis Data Streams to Amazon MSF.
- Data in transit between internal components within Amazon MSF.
- Data in transit between Amazon MSF and Firehose.

### Key management

In Amazon MSF, you can use either service managed or your own customer managed keys to encrypt data. For more information, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md "key-management-flink.md").

# How Amazon S3 delivery works

Use this topic to learn how an Amazon S3 delivery sends records from an Amazon Kinesis Data Streams stream
to general purpose Amazon Simple Storage Service buckets, including storage configuration, compression,
storage class, record formats, and encryption.

## How delivery works

An Amazon S3 delivery sends records to general purpose Amazon S3 buckets in the
following steps:

1. **Read** – the delivery reads records
   from all shards in the Kinesis Data Streams stream.
2. **Buffer** – records are buffered until
   the data freshness interval is reached.
3. **Validate** – when the record format is
   `STRING`, each record is validated as a valid UTF-8 string; when
   the record format is `JSON`, each record is validated as a valid
   JSON payload. Records that fail validation are sent to the dead-letter queue.
4. **Compress and format** – records are
   formatted according to the configured output format and compressed using
   the specified compression algorithm.
5. **Deliver** – the resulting objects are
   written to the destination Amazon S3 bucket using the configured key template.
6. **Dead-letter queue** – records that fail
   validation are written to the dead-letter queue with error context.

## Storage configuration

When you create an Amazon S3 delivery, you specify the following storage
configuration:

- **BucketARN** – the ARN of the
  destination Amazon S3 bucket.
- **ExpectedBucketOwner** – the 12-digit
  AWS account ID of the expected owner of the destination bucket. This value
  is required and helps prevent delivery to an unintended bucket if ownership
  changes.
- **CompressionType** – the compression
  type applied to delivered objects. This value is required; specify
  `NONE` to deliver objects without compression. See [Compression options](#data-delivery-s3-compression "#data-delivery-s3-compression").
- **StorageClass** – the Amazon S3 storage
  class for delivered objects (optional). See [Storage class](#data-delivery-s3-storage-class "#data-delivery-s3-storage-class").
- **OutputKeyTemplate** – the template
  used to construct the Amazon S3 object key (optional). See [S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md "data-delivery-s3-key-template.md").

## Compression options

You must specify a compression type for delivery to general purpose Amazon S3 buckets. To
deliver objects without compression, choose `NONE`. Choose one of the
following compression types:

- **GZIP** – standard gzip compression. Good balance of compression ratio and speed.
- **ZSTD** – Zstandard compression. Higher compression ratio with faster decompression.
- **NONE** – no compression applied. Records are delivered uncompressed.

## Storage class

You can optionally specify the Amazon S3 storage class for delivered objects. If not
specified, the default storage class is STANDARD. Supported storage classes:

- **STANDARD** – general purpose storage for frequently accessed data.
- **INTELLIGENT\_TIERING** – automatically moves data between access tiers based on usage patterns.
- **GLACIER\_IR** – low-cost storage for data that requires immediate retrieval.

For more information about Amazon S3 storage classes, see
[Understanding
and managing storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in the _Amazon S3 User Guide_.

## Output key template

You can configure the output key template to control the Amazon S3 object key
structure for delivered files. The template supports dynamic placeholders for
date, time, and delivery metadata to organize your data in the destination bucket.
For the default template, supported variables, and examples, see
[S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md "data-delivery-s3-key-template.md").

## Data freshness

Data freshness defines the maximum buffering time before records are delivered.
You can configure this value between 300 and 900 seconds (5 to 15 minutes). The default is 300
seconds. Lower values provide faster delivery, while higher values produce fewer,
larger objects.

## Dead-letter queue

A dead-letter queue is optional for delivery to general purpose Amazon S3 buckets.
If you do not specify a dead-letter queue configuration, the delivery defaults
to writing error information to the same destination bucket with an error prefix.

If you specify a dead-letter queue, you provide the following:

- **BucketARN** – the ARN of the Amazon S3
  bucket that receives information about records that could not be delivered.
- **ExpectedBucketOwner** – the 12-digit
  AWS account ID of the expected owner of the dead-letter queue bucket
  (required when you specify a dead-letter queue).
- **ErrorOutputPrefix** – an optional
  prefix for organizing the failure metadata objects within the bucket.

## Record formats

Amazon S3 deliveries support the following record formats for delivery to general
purpose Amazon S3 buckets:

- **JSON** – plain JSON records.
- **STRING** – UTF-8 string records.
- **BYTE\_ARRAY** – raw binary records.

###### Note

The `GSR_JSON` record format is not supported for delivery to general
purpose Amazon S3 buckets. It is supported only for delivery to streaming tables on
Apache Iceberg, which require AWS Glue Schema Registry.

## Cross-account delivery

Amazon S3 deliveries support cross-account delivery to general purpose Amazon S3
buckets. The source stream and destination bucket must be in the same AWS Region.
Configure the destination bucket policy to grant the delivery IAM role
permission to write objects.

## Encryption

Amazon S3 deliveries support server-side encryption with customer-managed AWS KMS
keys for objects delivered to general purpose Amazon S3 buckets. You can specify a
customer-managed AWS KMS key to encrypt delivered objects.

###### Important

You cannot use the `aws/kinesis` AWS KMS alias for destination
encryption. You must use a customer-managed AWS KMS key.

If your source Kinesis data stream is encrypted, additional considerations apply. A
stream encrypted with an AWS managed key (the `aws/kinesis` alias) is
not supported, and the service execution role requires AWS KMS permissions to decrypt
source records. For source stream encryption requirements, see
[Source stream encryption](data-delivery-security.md#data-delivery-security-source-stream-encryption "data-delivery-security.md#data-delivery-security-source-stream-encryption"). For the AWS KMS
permissions the service execution role needs, see [IAM permissions for data delivery](data-delivery-iam.md "data-delivery-iam.md").

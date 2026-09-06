# Streaming tables and S3 delivery for Amazon Kinesis Data Streams

With Amazon Kinesis Data Streams, you can deliver streaming data from your Kinesis data streams to two
destination types: streaming tables on Apache Iceberg (Amazon S3 Tables), or general purpose
Amazon S3 buckets. You don't need to manage any infrastructure, and you can start delivering
within minutes. Amazon Kinesis Data Streams reads from your stream, buffers and aggregates records, and
delivers them to your configured destination. Delivery is fully managed – there are no
connectors, consumer applications, or compute resources to provision.

These capabilities are supported for streams running in On-Demand Advantage or On-Demand Standard
capacity mode. You configure delivery from your stream and specify a destination. Amazon Kinesis Data Streams then handles
scaling, retries, and delivery reliability automatically. Delivery does not consume your stream's read throughput
and has no impact on existing consumers.

###### Topics

- [How data delivery works](#data-delivery-how-it-works "#data-delivery-how-it-works")
- [Delivery destinations](#data-delivery-destinations-overview "#data-delivery-destinations-overview")
- [Data flow](#data-delivery-data-flow "#data-delivery-data-flow")
- [Key capabilities](#data-delivery-capabilities "#data-delivery-capabilities")
- [Requirements](#data-delivery-requirements-overview "#data-delivery-requirements-overview")
- [Data delivery concepts](data-delivery-concepts.md "data-delivery-concepts.md")
- [Streaming tables](data-delivery-st.md "data-delivery-st.md")
- [Amazon S3 general purpose delivery](data-delivery-s3.md "data-delivery-s3.md")
- [IAM permissions for data delivery](data-delivery-iam.md "data-delivery-iam.md")
- [Security for data delivery](data-delivery-security.md "data-delivery-security.md")
- [Monitoring data delivery](data-delivery-monitoring.md "data-delivery-monitoring.md")
- [Best practices for data delivery](data-delivery-best-practices.md "data-delivery-best-practices.md")
- [Troubleshooting data delivery](data-delivery-troubleshooting.md "data-delivery-troubleshooting.md")
- [Delivery quotas and limits](data-delivery-quotas.md "data-delivery-quotas.md")

## How data delivery works

Data delivery connects your Kinesis data stream to a delivery destination through a
managed pipeline:

1. You publish data to a Kinesis data stream in On-Demand mode.
2. You call `CreateChannel` on the stream and specify a destination
   (streaming tables on Apache Iceberg, or a general purpose Amazon S3
   bucket).
3. The delivery reads from the stream, buffers records, and aggregates them
   into optimally sized files.
4. The delivery writes the files to your configured destination within the
   data freshness window you specify.

## Delivery destinations

Data delivery supports two destination types:

Streaming tables on Apache Iceberg

Streaming tables continuously delivers your Kinesis data stream into Apache
Iceberg tables stored in Amazon S3 Tables. As data arrives, it is automatically
converted to optimized Apache Parquet format with intelligent inline compaction
that eliminates the small files problem and reduces downstream query costs.
Within minutes of being published to your stream, data becomes queryable through
Amazon Athena, Amazon EMR, Amazon Managed Service for Apache Flink, or any engine that supports Apache
Iceberg.

General purpose Amazon S3 buckets

Amazon S3 delivery writes streaming data from your Kinesis data stream directly
to an S3 bucket. Records are delivered in their original source format with no
transformation applied. Multiple records are buffered and batched into optimally
sized objects, with configurable compression and an S3 key structure you define
through the output key template. This is ideal for use cases such as raw log
archival, event replay, and downstream batch processing, where you need durable,
low-cost storage of your streaming data without the overhead of managing a
delivery pipeline.

## Data flow

The following diagram shows an end-to-end data flow for delivery to streaming tables
on Apache Iceberg. The diagram uses a card-transactions use case as an example. A
producer serializes records against a schema in AWS Glue Schema Registry and writes them to
a Kinesis data stream. Amazon Kinesis Data Streams delivers the records to Apache Iceberg tables on Amazon S3
Tables. If you enable analytics integration in S3 Tables, the table metadata is also
registered in the AWS Glue Data Catalog; this does not happen by default. The delivered data
and its metadata are then available to analytics and AI engines such as Amazon Athena,
Amazon Redshift, and Amazon EMR.

Delivery to general purpose Amazon S3 buckets follows a similar flow, with two
differences. A producer writes records to a Kinesis data stream, and Amazon Kinesis Data Streams delivers
them to your S3 bucket. Records are delivered in their original source format with no
conversion, so AWS Glue Schema Registry is not required and no table metadata is registered
in the AWS Glue Data Catalog. Amazon Kinesis Data Streams buffers and batches records into optimally sized
objects and writes them using the S3 key structure you define through the output key
template. The delivered objects are then available for downstream batch processing and
analytics.

![Architecture diagram showing card-transaction records serialized through AWS Glue Schema Registry into a Kinesis data stream, delivered to Apache Iceberg tables on Amazon S3 Tables with metadata registered in the AWS Glue Data Catalog, and consumed by analytics and AI engines including Amazon Athena, Amazon Redshift, and Amazon EMR.](images/data-delivery-architecture.png)

## Key capabilities

- **Serverless auto-scaling** – Scales
  automatically with your stream throughput, up to the stream's throughput capacity.
  No compute resources to provision.
- **Exactly-once delivery per shard** –
  Records from a shard are delivered to the destination exactly once, with no duplicates
  or omissions within the shard.
- **Near real-time delivery** –
  Configurable data freshness from 5 to 15 minutes (300 to 900 seconds).
- **Automatic Parquet conversion** –
  For streaming tables on Apache Iceberg, converts streaming records into optimized
  Apache Parquet format for efficient analytics queries.
- **Inline compaction** – Aggregates
  records into optimally sized files for analytics query
  performance.
- **Encryption** – Supports
  customer managed AWS KMS keys for server-side encryption at the destination. The
  AWS managed key (the `aws/kinesis` alias) is not supported for
  destination encryption.
- **Dead-letter queue** – Failure
  metadata for records that cannot be delivered – including stream ARN, shard ID,
  sequence number, and error context – is written to an S3-based dead-letter
  queue.
- **CloudWatch metrics and logs** – Monitor
  bytes delivered, record counts, and data freshness through Amazon CloudWatch metrics. Enable
  delivery logging to Amazon CloudWatch Logs to capture delivery batch details, failures, and
  error context for troubleshooting.
- **No impact on other consumers** –
  Does not consume enhanced fan-out slots or shared throughput.

## Requirements

- Your Kinesis data stream must use On-Demand Standard or On-Demand Advantage
  capacity mode.
- You must create an IAM service execution role that grants the delivery
  permissions to write to your destination.
- Your destination bucket or table bucket must be in the same Region as
  your Kinesis data stream. Data delivery does not support cross-Region delivery for
  either destination type.
- For streaming tables on Apache Iceberg, cross-account delivery is not
  supported. The source stream, the destination S3 table bucket, and AWS Glue Schema
  Registry must all be in the same AWS account and the same Region.
- For general purpose Amazon S3 buckets, cross-account delivery is
  supported for the destination bucket only. The channel and its source stream must be
  in the same AWS account; only the destination bucket can be in a different
  account.
- For streaming tables on Apache Iceberg, you must configure a dead-letter
  queue in Amazon S3.

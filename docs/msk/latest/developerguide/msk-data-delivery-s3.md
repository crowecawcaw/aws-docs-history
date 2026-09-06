

# data delivery to Amazon S3 general purpose buckets
<a name="msk-data-delivery-s3"></a>

With Amazon MSK Data Delivery, you can deliver Apache Kafka data in the source format to Amazon S3 general purpose buckets for downstream processing, with end-to-end reliability for mission-critical workloads. Use it to land Kafka data in Amazon S3 for use cases such as log archival, compliance retention, Kafka replay, and training AI/ML models. This approach removes the need to build self-managed connector pipelines that grow costly and operationally complex as workloads scale.

**Topics**
+ [Integrations](#msk-data-delivery-s3-integrations)
+ [Common use cases](#msk-data-delivery-s3-use-cases)
+ [Data flow](#msk-data-delivery-s3-data-flow)
+ [Benefits](#msk-data-delivery-s3-benefits)
+ [How it works](#msk-data-delivery-s3-how-it-works)
+ [Key concepts](msk-data-delivery-s3-concepts.md)
+ [Requirements and supported configurations](#msk-data-delivery-s3-requirements)
+ [Get started](msk-data-delivery-s3-getting-started.md)
+ [IAM permissions](msk-data-delivery-s3-iam.md)
+ [Manage Channels](msk-data-delivery-s3-manage.md)
+ [Output key template](msk-data-delivery-s3-output-key-template.md)
+ [Security](msk-data-delivery-s3-security.md)
+ [Monitoring](msk-data-delivery-s3-monitoring.md)
+ [Logging](msk-data-delivery-s3-logging.md)
+ [Best practices](msk-data-delivery-s3-bestpractices.md)
+ [Troubleshooting](msk-data-delivery-s3-troubleshooting.md)

## Integrations
<a name="msk-data-delivery-s3-integrations"></a>
+ **Amazon MSK Express brokers** — the data source.
+ **Amazon S3** — general-purpose object destination.
+ **Amazon CloudWatch** — metrics and operational logs.
+ **AWS CloudTrail** — API audit logging.
+ **AWS KMS** — optional customer-managed encryption at rest.

## Common use cases
<a name="msk-data-delivery-s3-use-cases"></a>
+ Archive Kafka topic data to S3 for storage, replay, or downstream batch processing.
+ Fan out a single topic to multiple destinations without adding broker load.

For the API specification, see `CreateChannel`, `DescribeChannel`, `UpdateChannel`, `DeleteChannel`, and `ListChannels` in the *Amazon MSK API Reference*.

## Data flow
<a name="msk-data-delivery-s3-data-flow"></a>

The following diagram shows how records flow from an Amazon MSK Express broker topic through a Data Delivery channel to your destination, with unprocessable records routed to a dead-letter queue.

![Data flow from an Amazon MSK Express broker topic through a Data Delivery channel to a general-purpose Amazon S3 bucket, with unprocessable records routed to a dead-letter queue.](http://docs.aws.amazon.com/msk/latest/developerguide/images/msk-data-channel-dataflow.png)


## Benefits
<a name="msk-data-delivery-s3-benefits"></a>
+ **No infrastructure to manage** — No connectors or compute clusters. You configure a Channel and the service handles delivery, scaling, and fault tolerance.
+ **No broker impact** — A channel reads from the topic without consuming broker throughput or affecting producer and consumer workloads.
+ **Scales with your data** — Supports data delivery throughput of up to 10 GBps with no manual scaling required.
+ **Data freshness in minutes** — Delivered data is available for querying or processing within 5 to 15 minutes of being produced to the topic.
+ **Built-in error handling** — Unprocessable records are routed to a dead-letter queue with error context, so delivery continues uninterrupted.

## How it works
<a name="msk-data-delivery-s3-how-it-works"></a>

To deliver data to a general-purpose S3 bucket, you create a **Channel**. You create a Channel on an Amazon MSK Provisioned cluster that uses Express brokers. The Channel reads records from a Kafka topic and delivers them to the configured destination.

For **Amazon S3 general purpose buckets**, the Channel writes records (JSON, ByteArray, or String) as objects to a general-purpose S3 bucket, using a configurable output key template.

Records that cannot be processed are routed to a required dead-letter queue (DLQ) S3 bucket.

**Note**  
A Channel does **not** backfill previously produced data — only data produced after enablement is delivered.

## Requirements and supported configurations
<a name="msk-data-delivery-s3-requirements"></a>
+ An Amazon MSK Provisioned cluster with **Express brokers**. Standard brokers and Amazon MSK Serverless are **not** supported.
+ At least one Kafka topic.
+ An Amazon S3 bucket for the dead-letter queue (DLQ). This is **required**.
+ An IAM service role that the Channel assumes to deliver data.
+ Data freshness configured between 5 and 15 minutes.
+ Topic data in **JSON**, **ByteArray**, or **String** format.
+ A general-purpose Amazon S3 bucket for delivery.
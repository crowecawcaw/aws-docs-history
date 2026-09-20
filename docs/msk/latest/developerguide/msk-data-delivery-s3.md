

# Amazon MSK data delivery to Amazon S3
<a name="msk-data-delivery-s3"></a>

Amazon MSK data delivery to Amazon S3 delivers your Apache Kafka data to general purpose Amazon S3 buckets in its source format. You choose a Kafka topic and a destination bucket, and Amazon MSK Express brokers deliver your records to Amazon S3 as a fully managed capability.

Amazon MSK scales delivery to your workload automatically and handles retries and backpressure, supporting throughput of up to 10 GBps. Routine operations such as capacity scaling and version upgrades happen without delivery gaps. Because delivery is native to Express brokers rather than a connector fleet that you run, there is no additional broker egress throughput to provision, and you pay $8.00 per TB delivered. Together this can reduce ingestion and delivery costs by up to 60% compared to self-managed alternatives.

Without this capability, delivering Apache Kafka data to Amazon S3 for log archival, compliance retention, Kafka replay, or machine learning training data means building pipelines from self-managed connectors. You source or build connector plugins, secure approvals to deploy them, scale worker capacity as throughput grows, and apply security updates across a connector fleet, and you size that capacity for peak rather than actual demand. Data delivery removes the connector fleet and the coordination it requires.

The following diagram shows how records flow from an Amazon MSK Express broker topic through a Data Delivery channel to a general purpose Amazon S3 bucket, shown as the dashed path. The solid path shows delivery to Apache Iceberg tables in Amazon S3 Tables.

![Producers publish events to a Kafka topic on Amazon MSK Express brokers. A solid path delivers records to Apache Iceberg tables on Amazon S3 Tables, which are automatically registered in the AWS Glue Data Catalog and queried by Amazon Athena, Amazon Redshift, Apache Spark on Amazon EMR, and Amazon Bedrock AI agents. A dashed path delivers raw records to a general purpose Amazon S3 bucket.](https://docs.aws.amazon.com/msk/latest/developerguide/images/msk-data-channel-dataflow.png)


**Topics**
+ [Benefits](#msk-data-delivery-s3-benefits)
+ [Pricing](#msk-data-delivery-s3-pricing)
+ [Common use cases](#msk-data-delivery-s3-use-cases)
+ [Integrations](#msk-data-delivery-s3-integrations)
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

## Benefits
<a name="msk-data-delivery-s3-benefits"></a>
+ **No infrastructure to manage** — No connectors or compute clusters. You configure a Channel and the service handles delivery, scaling, and fault tolerance.
+ **No broker impact** — A channel reads from the topic without consuming broker throughput or affecting producer and consumer workloads.
+ **Scales with your data** — Supports data delivery throughput of up to 10 GBps with no manual scaling required.
+ **Data freshness in minutes** — Delivered data is available for querying or processing within 5 to 15 minutes of being produced to the topic.
+ **Built-in error handling** — Unprocessable records are routed to a dead-letter queue with error context, so delivery continues uninterrupted.

## Pricing
<a name="msk-data-delivery-s3-pricing"></a>

You pay for the volume of data delivered from your Apache Kafka topics to the destination, billed at per-byte resolution, at $8.00 per TB. There are no setup fees, minimum commitments, or upfront costs.

Standard Amazon S3 storage, request, and data transfer charges apply to the destination bucket. There is no additional charge for broker egress used by this capability, and there are no separate connector, worker, or MSK Connect Unit (MCU) fees.

You are not charged separately for failed delivery attempts routed to the dead-letter queue. Only successfully delivered data is billed.

Rates vary by destination type and are subject to change. For current pricing, see [Amazon MSK pricing](https://aws.amazon.com/msk/pricing/).

## Common use cases
<a name="msk-data-delivery-s3-use-cases"></a>
+ Archive Kafka topic data to S3 for storage, replay, or downstream batch processing.
+ Fan out a single topic to multiple destinations without adding broker load.

For the API specification, see `CreateChannel`, `DescribeChannel`, `UpdateChannel`, `DeleteChannel`, and `ListChannels` in the *Amazon MSK API Reference*.

## Integrations
<a name="msk-data-delivery-s3-integrations"></a>
+ **Amazon MSK Express brokers** — the data source.
+ **Amazon S3** — general-purpose object destination.
+ **Amazon CloudWatch** — metrics and operational logs.
+ **AWS CloudTrail** — API audit logging.
+ **AWS KMS** — optional customer-managed encryption at rest.

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
+ The destination bucket must be in the same AWS Region as your Amazon MSK cluster. Cross-Region delivery is not supported.
+ Cross-account delivery is supported for the destination bucket only. Your Amazon MSK cluster and the dead-letter queue bucket must be in the same AWS account as the Channel; only the destination bucket can be in a different AWS account.


# Amazon MSK streaming tables to Apache Iceberg
<a name="msk-data-delivery-iceberg"></a>

Amazon MSK streaming tables continuously materialize your Apache Kafka topics as Apache Iceberg tables on Amazon S3 Tables. You choose a Kafka topic and a destination table bucket, and Amazon MSK Express brokers write your records as Apache Parquet data files and commit them to the table.

Delivered data is queryable within minutes of being produced, and a single streaming table scales to 10 GBps of delivery throughput without manual scaling. Because delivery is native to Express brokers rather than a connector that you run, there is no additional broker egress throughput to provision, and you pay $10.00 per TB delivered. Together this can reduce the cost of ingesting and delivering Apache Kafka data into Amazon S3 Tables by up to 60% compared to self-managed deployments, and inline compaction reduces downstream query costs by up to 30%.

Without this capability, unifying streaming data with Apache Iceberg means deploying and maintaining Kafka Connect clusters, Apache Flink jobs, or custom consumers, handling data format conversions, and coordinating concurrent writes from high-throughput producers. High-volume ingestion also creates large numbers of small Parquet files that slow query engines such as Apache Spark, Trino, and Apache Flink, forcing a trade-off between data freshness and query performance. Streaming tables remove that infrastructure, resolve writer conflicts for you, and compact files inline so that queries stay fast without sacrificing freshness.

The following diagram shows how records flow from an Amazon MSK Express broker topic through a Data Delivery channel to an Apache Iceberg table in Amazon S3 Tables, and how the delivered data becomes available to query. The dashed path shows delivery to general purpose Amazon S3 buckets.

![Producers publish events to a Kafka topic on Amazon MSK Express brokers. A solid path delivers records to Apache Iceberg tables on Amazon S3 Tables, which are automatically registered in the AWS Glue Data Catalog and queried by Amazon Athena, Amazon Redshift, Apache Spark on Amazon EMR, and Amazon Bedrock AI agents. A dashed path delivers raw records to a general purpose Amazon S3 bucket.](https://docs.aws.amazon.com/msk/latest/developerguide/images/msk-data-channel-dataflow.png)


**Topics**
+ [Benefits](#msk-data-delivery-iceberg-benefits)
+ [Pricing](#msk-data-delivery-iceberg-pricing)
+ [Common use cases](#msk-data-delivery-iceberg-use-cases)
+ [Integrations](#msk-data-delivery-iceberg-integrations)
+ [How it works](#msk-data-delivery-iceberg-how-it-works)
+ [Key concepts](msk-data-delivery-iceberg-concepts.md)
+ [Requirements and supported configurations](#msk-data-delivery-iceberg-requirements)
+ [Get started](msk-data-delivery-iceberg-getting-started.md)
+ [IAM permissions](msk-data-delivery-iceberg-iam.md)
+ [Manage Channels](msk-data-delivery-iceberg-manage.md)
+ [Iceberg table behaviors](msk-data-delivery-iceberg-behaviors.md)
+ [Security](msk-data-delivery-iceberg-security.md)
+ [Monitoring](msk-data-delivery-iceberg-monitoring.md)
+ [Logging](msk-data-delivery-iceberg-logging.md)
+ [Best practices](msk-data-delivery-iceberg-bestpractices.md)
+ [Troubleshooting](msk-data-delivery-iceberg-troubleshooting.md)

## Benefits
<a name="msk-data-delivery-iceberg-benefits"></a>
+ **No infrastructure to manage** — No connectors or compute clusters. You configure a Channel and the service handles delivery, scaling, and fault tolerance.
+ **No broker impact** — A channel reads from the topic without consuming broker throughput or affecting producer and consumer workloads.
+ **Scales with your data** — Supports data delivery throughput of up to 10 GBps with no manual scaling required.
+ **Data freshness in minutes** — Delivered data is available for querying or processing within 5 to 15 minutes of being produced to the topic.
+ **Built-in error handling** — Unprocessable records are routed to a dead-letter queue with error context, so delivery continues uninterrupted.

## Pricing
<a name="msk-data-delivery-iceberg-pricing"></a>

You pay for the volume of data delivered from your Apache Kafka topics to the destination, billed at per-byte resolution, at $10.00 per TB. There are no setup fees, minimum commitments, or upfront costs.

Standard Amazon S3 Tables storage, request, and maintenance charges apply to the destination table bucket, and standard AWS data transfer charges apply. There is no additional charge for broker egress, inline compaction, or writer coordination.

You are not charged separately for failed delivery attempts routed to the dead-letter queue. Only successfully delivered data is billed.

Rates vary by destination type and are subject to change. For current pricing, see [Amazon MSK pricing](https://aws.amazon.com/msk/pricing/).

## Common use cases
<a name="msk-data-delivery-iceberg-use-cases"></a>
+ Continuously land Kafka streaming data into queryable Iceberg tables for analytics (Athena, Spark, and other engines).
+ Build a streaming lakehouse on S3 Tables without managing compaction or a delivery service.
+ Fan out a single topic to multiple destinations without adding broker load.

For the API specification, see `CreateChannel`, `DescribeChannel`, `UpdateChannel`, `DeleteChannel`, and `ListChannels` in the *Amazon MSK API Reference*.

## Integrations
<a name="msk-data-delivery-iceberg-integrations"></a>
+ **Amazon MSK Express brokers** — the data source.
+ **Amazon S3 Tables** — managed Iceberg destination.
+ **AWS Glue Schema Registry** — source of truth for record schemas.
+ **Amazon CloudWatch** — metrics and operational logs.
+ **AWS CloudTrail** — API audit logging.
+ **AWS KMS** — optional customer-managed encryption at rest.

## How it works
<a name="msk-data-delivery-iceberg-how-it-works"></a>

To establish a table on Iceberg, you create a **Channel**. You create a Channel on an Amazon MSK Provisioned cluster that uses Express brokers. The Channel reads records from a Kafka topic and delivers them to the configured destination.

For **streaming tables for Apache Iceberg**, the Channel converts JSON records using a schema in the AWS Glue Schema Registry, writes them as Apache Parquet data files, and registers them in a new Iceberg table stored in an S3 Table bucket.

Records that cannot be processed are routed to a required dead-letter queue (DLQ) S3 bucket.

**Note**  
A Channel does **not** backfill previously produced data — only data produced after enablement is delivered. For streaming tables for Apache Iceberg, a Channel creates a **new** Iceberg table for each configuration; delivery to existing Iceberg tables is not supported.

## Requirements and supported configurations
<a name="msk-data-delivery-iceberg-requirements"></a>
+ An Amazon MSK Provisioned cluster with **Express brokers**. Standard brokers and Amazon MSK Serverless are **not** supported.
+ At least one Kafka topic.
+ An Amazon S3 bucket for the dead-letter queue (DLQ). This is **required**.
+ An IAM service role that the Channel assumes to deliver data.
+ Data freshness configured between 5 and 15 minutes.
+ Topic data in **JSON** (plain JSON, with a GSR schema ARN) or **JSON\_SCHEMA\_GSR** (GSR-serialized JSON with an embedded schema ID).
+ A schema registered in the AWS Glue Schema Registry that matches your topic data.
+ An Amazon S3 Table bucket in the same AWS Region as your Amazon MSK cluster.
+ Cross-account delivery is **not** supported for streaming tables. Your Amazon MSK cluster, the destination S3 Table bucket, the AWS Glue Schema Registry, and the dead-letter queue bucket must all be in the same AWS account and the same AWS Region. Cross-Region delivery is not supported.
+ For the minimum 5-minute data freshness, the topic should produce at least 2.4 MBps of uncompressed data. For lower-throughput topics, use a higher data freshness value (up to 15 minutes).
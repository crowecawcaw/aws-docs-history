# data delivery for streaming tables to Apache Iceberg

With Amazon MSK Data Delivery, you can continuously materialize Apache Kafka topics as Apache Iceberg tables on Amazon S3 Tables. Intelligent inline compaction eliminates the performance impact of small files and keeps query performance predictable without sacrificing data freshness. Built-in coordination resolves concurrent writer conflicts across high-throughput consumers. Amazon S3 Tables automatically handles ongoing table maintenance, including compaction, snapshot expiration, and unreferenced file cleanup.

###### Topics

- [Integrations](#msk-data-delivery-iceberg-integrations "#msk-data-delivery-iceberg-integrations")
- [Common use cases](#msk-data-delivery-iceberg-use-cases "#msk-data-delivery-iceberg-use-cases")
- [Data flow](#msk-data-delivery-iceberg-data-flow "#msk-data-delivery-iceberg-data-flow")
- [Benefits](#msk-data-delivery-iceberg-benefits "#msk-data-delivery-iceberg-benefits")
- [How it works](#msk-data-delivery-iceberg-how-it-works "#msk-data-delivery-iceberg-how-it-works")
- [Key concepts](msk-data-delivery-iceberg-concepts.md "msk-data-delivery-iceberg-concepts.md")
- [Requirements and supported configurations](#msk-data-delivery-iceberg-requirements "#msk-data-delivery-iceberg-requirements")
- [Get started](msk-data-delivery-iceberg-getting-started.md "msk-data-delivery-iceberg-getting-started.md")
- [IAM permissions](msk-data-delivery-iceberg-iam.md "msk-data-delivery-iceberg-iam.md")
- [Manage Channels](msk-data-delivery-iceberg-manage.md "msk-data-delivery-iceberg-manage.md")
- [Iceberg table behaviors](msk-data-delivery-iceberg-behaviors.md "msk-data-delivery-iceberg-behaviors.md")
- [Security](msk-data-delivery-iceberg-security.md "msk-data-delivery-iceberg-security.md")
- [Monitoring](msk-data-delivery-iceberg-monitoring.md "msk-data-delivery-iceberg-monitoring.md")
- [Logging](msk-data-delivery-iceberg-logging.md "msk-data-delivery-iceberg-logging.md")
- [Best practices](msk-data-delivery-iceberg-bestpractices.md "msk-data-delivery-iceberg-bestpractices.md")
- [Troubleshooting](msk-data-delivery-iceberg-troubleshooting.md "msk-data-delivery-iceberg-troubleshooting.md")

## Integrations

- **Amazon MSK Express brokers** — the data source.
- **Amazon S3 Tables** — managed Iceberg destination.
- **AWS Glue Schema Registry** — source of truth for record schemas.
- **Amazon CloudWatch** — metrics and operational logs.
- **AWS CloudTrail** — API audit logging.
- **AWS KMS** — optional customer-managed encryption at rest.

## Common use cases

- Continuously land Kafka streaming data into queryable Iceberg tables for analytics (Athena, Spark, and other engines).
- Build a streaming lakehouse on S3 Tables without managing compaction or a delivery service.
- Fan out a single topic to multiple destinations without adding broker load.

For the API specification, see `CreateChannel`, `DescribeChannel`, `UpdateChannel`, `DeleteChannel`, and `ListChannels` in the _Amazon MSK API Reference_.

## Data flow

The following diagram shows how records flow from an Amazon MSK Express broker topic through a Data Delivery channel to your destination, with unprocessable records routed to a dead-letter queue.

![Data flow from an Amazon MSK Express broker topic through a Data Delivery channel to an Apache Iceberg table in Amazon S3 Tables, with unprocessable records routed to a dead-letter queue.](images/msk-data-channel-dataflow.png)

## Benefits

- **No infrastructure to manage** — No connectors or compute clusters. You configure a Channel and the service handles delivery, scaling, and fault tolerance.
- **No broker impact** — A channel reads from the topic without consuming broker throughput or affecting producer and consumer workloads.
- **Scales with your data** — Supports data delivery throughput of up to 10 GBps with no manual scaling required.
- **Data freshness in minutes** — Delivered data is available for querying or processing within 5 to 15 minutes of being produced to the topic.
- **Built-in error handling** — Unprocessable records are routed to a dead-letter queue with error context, so delivery continues uninterrupted.

## How it works

To establish a table on Iceberg, you create a **Channel**. You create a Channel on an Amazon MSK Provisioned cluster that uses Express brokers. The Channel reads records from a Kafka topic and delivers them to the configured destination.

For **streaming tables for Apache Iceberg**, the Channel converts JSON records using a schema in the AWS Glue Schema Registry, writes them as Apache Parquet data files, and registers them in a new Iceberg table stored in an S3 Table bucket.

Records that cannot be processed are routed to a required dead-letter queue (DLQ) S3 bucket.

###### Note

A Channel does **not** backfill previously produced data — only data produced after enablement is delivered. For streaming tables for Apache Iceberg, a Channel creates a **new** Iceberg table for each configuration; delivery to existing Iceberg tables is not supported.

## Requirements and supported configurations

- An Amazon MSK Provisioned cluster with **Express brokers**. Standard brokers and Amazon MSK Serverless are **not** supported.
- At least one Kafka topic.
- An Amazon S3 bucket for the dead-letter queue (DLQ). This is **required**.
- An IAM service role that the Channel assumes to deliver data.
- Data freshness configured between 5 and 15 minutes.
- Topic data in **JSON** (plain JSON, with a GSR schema ARN) or **JSON\_SCHEMA\_GSR** (GSR-serialized JSON with an embedded schema ID).
- A schema registered in the AWS Glue Schema Registry that matches your topic data.
- An Amazon S3 Table bucket in the same AWS Region as your Amazon MSK cluster.
- For the minimum 5-minute data freshness, the topic should produce at least 2.4 MBps of uncompressed data. For lower-throughput topics, use a higher data freshness value (up to 15 minutes).

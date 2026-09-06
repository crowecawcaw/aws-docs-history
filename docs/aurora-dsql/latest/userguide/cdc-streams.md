

# Change data capture streams
<a name="cdc-streams"></a>

For pricing information, see the [Aurora DSQL pricing page](https://aws.amazon.com/rds/aurora/dsql/pricing/).

Amazon Aurora DSQL change data capture (CDC) streams committed database changes in near real time directly to Amazon Kinesis Data Streams. Aurora DSQL delivers the final committed state of each changed row as a structured JSON record to a Kinesis data stream that you configure.

CDC is useful when you want to:
+ **Keep downstream systems in sync** – Replicate changes to a search index, cache, data warehouse, or analytics system without batch jobs.
+ **Build event-driven architectures** – Trigger workflows, notifications, or microservice actions in response to database changes.
+ **Maintain an audit trail** – Capture the committed net effect of every transaction for compliance, debugging, or historical analysis.
+ **Decouple producers from consumers** – Let the database focus on transactions while downstream systems process changes at their own pace.

## How it works
<a name="cdc-how-it-works"></a>

Aurora DSQL reads committed transactions, formats the net row-level change as a structured JSON record, and delivers it to a Kinesis data stream that you configure. CDC automatically captures the committed effect of every `INSERT`, `UPDATE`, and `DELETE` across all user tables in the cluster. Apply filtering logic in your downstream apps by using the `source.schema` and `source.table` fields in each CDC record to focus on the tables or changes your app needs.

Aurora DSQL compacts the write set of each transaction before publishing CDC records and emits a single record for each row with a net change, reflecting the final state. For details, see [Write-set compaction](cdc-record-format.md#cdc-write-set-compaction).

CDC streams are fully managed. Aurora DSQL manages all infrastructure required to capture change events, monitors stream health, and reports the status through the `GetStream` API operation and CloudWatch metrics.

CDC streams use a bring-your-own-target model. You create and manage the Kinesis data stream in your account, and Aurora DSQL assumes an IAM role that you configure to write CDC records on your behalf. You're responsible for the target's capacity, encryption, and retention settings. For the latest supported targets, see the `TargetDefinition` parameter in [CreateStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateStream.html) in the Amazon Aurora DSQL API Reference. For a complete list of CDC stream API operations, see the [Amazon Aurora DSQL API Reference](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html).

## Topics on this page
<a name="cdc-topics-on-page"></a>
+ [Ordering and delivery semantics](#cdc-ordering-delivery)
+ [Multi-Region CDC stream configuration](#cdc-multi-region)
+ [Processing CDC records downstream](#cdc-downstream-processing)

## Related topics
<a name="cdc-related-topics"></a>
+ [Getting started with CDC streams](cdc-setup.md)
+ [Configuring IAM](cdc-iam.md)
+ [Understanding CDC records](cdc-record-format.md)
+ [Monitoring streams](cdc-monitoring.md)

## Ordering and delivery semantics
<a name="cdc-ordering-delivery"></a>

### Delivery guarantees
<a name="cdc-delivery-guarantees"></a>

Aurora DSQL produces one CDC record for each row with a net change at commit time. For details about how Aurora DSQL compacts multiple operations on the same row, see [Write-set compaction](cdc-record-format.md#cdc-write-set-compaction).

Aurora DSQL guarantees at-least-once delivery for every record it produces. Aurora DSQL can deliver the same record more than one time, so design your app to handle duplicates. You can identify a duplicate by comparing `source.ts_ns` and the primary key values—a duplicate has the same values as the original delivery.

### Ordering
<a name="cdc-ordering"></a>

CDC streams use `UNORDERED` mode. In practice, records arrive in approximate commit order because Aurora DSQL reads and publishes changes sequentially. However, Aurora DSQL doesn't guarantee strict ordering. Specifically:
+ Aurora DSQL can deliver records from different transactions in any order.
+ Records for the same primary key from different transactions can arrive out of commit order.
+ Records from a single transaction can interleave with records from other transactions. Use the `source.txId` field to group records by transaction when your workflow requires it.

Each CDC record includes a `source.ts_ns` field that contains the transaction commit timestamp in nanoseconds. Use this field to establish commit order on the receiving side.

### Consumer strategies
<a name="cdc-consumer-strategies"></a>

Because records can arrive out of commit order and can appear more than one time, your app must account for both conditions.

**Important**  
Define a primary key on all tables that participate in CDC. Without a primary key, your app can't deduplicate records or correlate deletes with the affected row.

**Last-writer-wins (materialized views, caches)**  
Track the highest `source.ts_ns` value per primary key. Discard any record with a `source.ts_ns` less than or equal to the tracked value. This filters both duplicates and out-of-order records, keeping the most recent state for each key. When you process a delete (`op: "d"`), store a tombstone for the primary key that preserves the `source.ts_ns` value instead of removing the entry. The tombstone ensures that an insert or update with an earlier `source.ts_ns` that arrives after the delete doesn't incorrectly restore the row.

**Every-change processing (audit logging, event sourcing)**  
Remove duplicates by comparing `source.ts_ns` combined with the primary key values. Buffer incoming records and sort by `source.ts_ns` before processing to reconstruct commit order. CDC delivers only the final state of each row per committed transaction (after [Write-set compaction](cdc-record-format.md#cdc-write-set-compaction)). If your audit workflow requires a record for every SQL statement, perform each statement in its own transaction.

## Multi-Region CDC stream configuration
<a name="cdc-multi-region"></a>

A CDC stream is a regional resource. Each stream belongs to a single AWS Region and delivers changes to a Kinesis data stream in the same Region. On a multi-Region cluster, a CDC stream in any one Region captures committed writes from **all Regions** in the cluster. This means you only need one stream to capture every change, regardless of where the write originated. To deliver CDC records in more than one Region, create a separate stream in each Region. Each stream independently captures the full set of committed changes across the cluster.

All resources—the Aurora DSQL cluster, Kinesis data stream, IAM service role, and calling principal—must be in the same AWS account and Region.

## Processing CDC records downstream
<a name="cdc-downstream-processing"></a>

After CDC records arrive in your Kinesis data stream, you can process them directly or route them to other destinations by using AWS integration services. The following table summarizes common processing patterns.


**Common processing patterns for CDC records**  

| Pattern | How it works | 
| --- |--- |
| Direct consumption | Read records from Kinesis by using the Amazon Kinesis Client Library (KCL), the AWS SDK, or a Kinesis Data Streams consumer. See [Developing KCL consumers](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html) in the Amazon Kinesis Data Streams Developer Guide. | 
| AWS Lambda | Configure a Lambda function as an event source for your Kinesis data stream to process each batch of CDC records as they arrive. See [Using AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html) in the AWS Lambda Developer Guide. | 
| Amazon Data Firehose | Deliver CDC records from Kinesis to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, or other destinations for analytics and archival. See [Sending data to a delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html) in the Amazon Data Firehose Developer Guide. | 
| Self-managed consumers | Run Apache Kafka Connect with the Kinesis source connector, Apache Flink, or other stream processing frameworks to transform and route records. For Apache Flink on AWS, see [Configuring app input](https://docs.aws.amazon.com/managed-flink/latest/java/how-it-works-input.html) in the Amazon Managed Service for Apache Flink Developer Guide. | 

Each CDC record includes fields such as `source.schema`, `source.table`, and `op` that you can use to route and filter records in your processing logic. For the full record schema, see [Understanding CDC records](cdc-record-format.md).
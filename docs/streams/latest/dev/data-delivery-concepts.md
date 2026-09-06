# Data delivery concepts

Use this topic to review key concepts for streaming tables and Amazon S3 delivery in
Amazon Kinesis Data Streams.

## Data freshness

Data freshness defines the maximum time (in seconds) that Kinesis Data Streams buffers incoming
records before delivering them to the destination. You can configure data freshness
between 300 and 900 seconds (5 to 15 minutes). The default value is 300 seconds.

- **Lower values** – Faster delivery to
  your destination with smaller batch sizes.
- **Higher values** – More efficient
  batching, which produces fewer, larger files at the destination.

## Input formats for streaming tables

When delivering to streaming tables on Apache Iceberg, data delivery supports the
following input record formats. Both formats require AWS Glue Schema Registry.

- **JSON** – plain JSON records. You must
  provide a `GSRSchemaARN` (the of a AWS Glue Schema Registry
  schema) that references a schema registered in
  AWS Glue Schema Registry.
- **GSR\_JSON** (AWS Glue Schema Registry JSON) –
  JSON records with the schema ID embedded in each record. The schema is resolved
  automatically from AWS Glue Schema Registry.

## Input formats for general purpose Amazon S3 buckets

When delivering to general purpose Amazon S3 buckets, data delivery supports the
following input record formats. No schema registry is required.

- **JSON** – plain JSON records.
- **STRING** – UTF-8 string records.
- **BYTE\_ARRAY** – raw binary records.

###### Note

The `GSR_JSON` format is not supported for general purpose Amazon S3
buckets. It is available only for delivery to streaming tables on Apache Iceberg.

## Schema enforcement

For streaming tables on Apache Iceberg, every record is validated against
the schema registered in AWS Glue Schema Registry. Records that do not conform to
the schema are not delivered to your streaming table. Failure metadata is written
to the dead-letter queue for troubleshooting. Data delivery does not support schema evolution.
This includes adding new fields, removing existing fields, renaming fields, or
changing field data types.

## No backfill

Your destination receives only records produced after you create the streaming table or
configure the S3 delivery. Existing records in the stream are not backfilled.

## New table per delivery

Each streaming table delivery creates its own Iceberg table at the destination. Delivery to
existing tables is not supported. You specify the table bucket ARN, namespace, and
table name when calling `CreateChannel`.

## Dead-letter queue

A dead-letter queue captures information about records that could not be delivered
successfully.

- **Streaming tables on Apache Iceberg** –
  a dead-letter queue is required. You must specify an S3 bucket and prefix
  for failed records.
- **General purpose Amazon S3 buckets** –
  a dead-letter queue is optional. If not specified, it defaults to the same
  destination bucket with an error prefix.

The dead-letter queue contains record identifiers and error context, not full
record payloads.

## Inline compaction

Data delivery performs inline compaction by aggregating records across shards into
optimally sized files. This reduces the number of small files at the destination
and improves query performance.

## Delivery states

A delivery transitions through the following states during its lifecycle:

- **CREATING** – the delivery is being provisioned.
- **ACTIVE** – the delivery is delivering records.
- **UPDATING** – a configuration change is in progress.
- **DELETING** – the delivery is being removed.
- **FAILED** – the delivery encountered an unrecoverable error.

## Append-only delivery

Delivery is append-only. Updates and upserts are not supported.
Each record from the stream is written as a new row at the destination.

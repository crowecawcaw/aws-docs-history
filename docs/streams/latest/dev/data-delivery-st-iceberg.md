

# Iceberg behaviors for streaming table
<a name="data-delivery-st-iceberg"></a>

 Use this topic to learn how streaming table maps data from AWS Glue Schema Registry schemas to Apache Iceberg tables, including type mapping, field handling, table maintenance, and format specifications. 

## AWS Glue Schema Registry to Iceberg type mapping
<a name="data-delivery-iceberg-type-mapping"></a>

 Streaming table maps JSON Schema types from AWS Glue Schema Registry to Apache Iceberg types as follows: 


**Schema Registry to Iceberg type mapping**  

| JSON Schema type | Iceberg type | Notes | 
| --- | --- | --- | 
| string (plain) | string | Default string mapping. | 
| string with format date-time | timestamptz | Timestamp with timezone. | 
| string with format date | date | Calendar date. | 
| string with format time | time | Time of day. | 
| string with format uuid | uuid | Universally unique identifier. | 
| string with encoding byte or base64 | binary | Binary data encoded as base64. | 
| integer (32-bit or less) | int | Values with maximum or exclusiveMaximum <= 2^31. | 
| integer (greater than 32-bit) | long | Values that exceed 32-bit range. | 
| number with multipleOf | decimal | Fixed-point decimal with precision derived from multipleOf. | 
| number (plain) | double | IEEE 754 double-precision floating point. | 
| boolean | boolean | True or false. | 
| object with named properties | struct | Named fields map to struct fields. | 
| object with additionalProperties | map | Key-value map with string keys. | 
| array | list | Ordered collection of elements. | 
| enum | string | Enum values stored as strings. | 

## Required columns
<a name="data-delivery-iceberg-required-columns"></a>

 Fields listed in the JSON Schema `required` array become required (non-nullable) columns in the Iceberg table. If a required field is missing from a record, the record is sent to the dead-letter queue. 

## Partition key column
<a name="data-delivery-iceberg-partition-key"></a>

 Your table must include a `timestamptz` column that can be used for time-based partitioning by hour (the `TIME_HOUR` transform). In the AWS Glue Schema Registry schema, this is a `string` field with the `date-time` format, which maps to the Iceberg `timestamptz` type. 

 The source column referenced by the partition is automatically marked as required, regardless of whether it appears in the schema's `required` array. Records missing the partition key value are sent to the dead-letter queue. 

 You can enable an Amazon S3 Tables record-expiration job based on the table's partition column. For more information, see [Record expiration](#data-delivery-iceberg-record-expiration). 

## Field handling
<a name="data-delivery-iceberg-field-handling"></a>

 Streaming table handles mismatches between incoming records and the Iceberg table schema as follows: 
+ **Extra fields** – Fields present in the record but not defined in the schema are dropped and not written to the Iceberg table.
+ **Missing optional fields** – Optional fields not present in the record are written as `null` in the Iceberg table.
+ **Missing required fields** – If a required field is missing from a record, the entire record is sent to the dead-letter queue.

## Nesting limit
<a name="data-delivery-iceberg-nesting"></a>

 Streaming table supports a maximum nesting depth of 16 levels for complex types (structs, maps, and lists). Schemas that exceed 16 levels of nesting are rejected at delivery creation time. 

## Managed table properties
<a name="data-delivery-iceberg-table-properties"></a>

 Streaming table manages Iceberg table properties automatically. These properties are set when the table is created and should not be modified externally. Streaming table uses these properties to control write behavior, compaction, and metadata management. 

 Because the table is managed by Amazon Kinesis Data Streams, you should not update its schema, modify its table properties, or write to or delete its data directly. You can query the table with AWS analytics services and any compatible Apache Iceberg query engine. For more information about managed table buckets, see [Using AWS managed table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-aws-managed-buckets.html) in the *Amazon S3 User Guide*. 

## S3 Tables maintenance
<a name="data-delivery-iceberg-maintenance"></a>

 When delivering to streaming tables on Apache Iceberg backed by S3 Tables, the following maintenance operations are handled automatically: 
+ **Compaction** – Small data files are periodically compacted into larger files to improve query performance and reduce metadata overhead.
+ **Snapshot expiration** – Expired snapshots are cleaned up to reclaim metadata storage and reduce table metadata size.
+ **Unreferenced file cleanup** – Orphaned data files that are no longer referenced by any snapshot are removed to reclaim storage.

## Record expiration
<a name="data-delivery-iceberg-record-expiration"></a>

 You can configure a record expiration period for your Iceberg table. When enabled, Amazon S3 Tables automatically removes records older than the specified retention period during maintenance operations, based on the table's `timestamptz` partition column. For more information, see [Managing Amazon S3 Tables record expiration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html) in the *Amazon S3 User Guide*. 

## Format specifications
<a name="data-delivery-iceberg-format"></a>

 Streaming table uses the following format specifications for Iceberg tables: 
+ **Iceberg format version** – v2
+ **Iceberg spec version** – 1.9.0
+ **File format** – Apache Parquet
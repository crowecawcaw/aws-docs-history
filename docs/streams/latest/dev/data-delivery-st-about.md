

# How streaming table delivery works
<a name="data-delivery-st-about"></a>

 Use this topic to learn how a streaming table delivery sends records from your Amazon Kinesis Data Streams stream to streaming tables on Apache Iceberg backed by S3 table buckets, including record conversion, destination table creation, partitioning, data freshness, the dead-letter queue, and encryption. 

## How delivery works
<a name="data-delivery-st-how-it-works"></a>

 A streaming table delivery sends records to a streaming table on Apache Iceberg in the following steps: 

1.  **Read** – the delivery reads records from all shards in the Kinesis Data Streams stream. 

1.  **Buffer** – the delivery buffers records until the data freshness interval is reached. 

1.  **Validate and convert** – the delivery validates each record against the schema in AWS Glue Schema Registry and converts it to the Apache Iceberg table schema. Records that fail validation go to the dead-letter queue. 

1.  **Compact and write** – the delivery converts records to optimized Apache Parquet files with inline compaction and writes them to the destination Iceberg table. 

1.  **Commit** – the delivery commits the new files to the Iceberg table so that the data becomes queryable. 

## Record conversion
<a name="data-delivery-st-record-conversion"></a>

 Streaming table delivery requires a schema registered in AWS Glue Schema Registry. The delivery uses the schema to convert incoming records to the Apache Iceberg table schema. It supports the following input record formats: 
+ **JSON** – plain JSON records. You provide a `GSRSchemaARN` that references a schema registered in AWS Glue Schema Registry.
+ **GSR\_JSON** – JSON records with the schema ID embedded in each record by the AWS Glue Schema Registry serializer. The schema is resolved automatically from AWS Glue Schema Registry.

 For the full AWS Glue Schema Registry to Iceberg type mapping and field-handling rules, see [Iceberg behaviors for streaming table](data-delivery-st-iceberg.md). 

## Destination table
<a name="data-delivery-st-destination-table"></a>

 When you create a streaming table delivery, Amazon Kinesis Data Streams creates the destination Iceberg table in the S3 table bucket you specify. You provide the following: 
+ **Table bucket ARN** – the ARN of the S3 table bucket where the table is created.
+ **Namespace** – the namespace for the table.
+ **Table name** – the name of the table to create. Each delivery creates its own table. You cannot deliver to an existing table.
+ **Partition column** – a `timestamptz` column used to partition the table by hour. For partitioning requirements, see [Iceberg behaviors for streaming table](data-delivery-st-iceberg.md).

## Data freshness
<a name="data-delivery-st-data-freshness"></a>

 Data freshness defines the maximum buffering time before records are delivered. You can configure this value between 300 and 900 seconds (5 to 15 minutes). The default is 300 seconds. Lower values provide faster delivery, while higher values produce fewer, larger files at the destination. 

## Dead-letter queue
<a name="data-delivery-st-dead-letter-queue"></a>

 A dead-letter queue is required for streaming table delivery. You specify an Amazon S3 bucket that receives information about records that fail validation. You provide the bucket ARN, the expected bucket owner, and an optional error output prefix. The dead-letter queue contains record identifiers and error context, not full record payloads. 

## Encryption
<a name="data-delivery-st-encryption"></a>

 Streaming table delivery encrypts delivered data at rest in Amazon S3. By default, data is encrypted with Amazon S3 managed keys (SSE-S3). You can instead use a customer managed AWS KMS key (SSE-KMS). 

**Important**  
 You cannot use an AWS managed key (the `aws/kinesis` alias) for destination encryption. You must use a customer managed AWS KMS key. In addition, if your source Kinesis data stream is encrypted with an AWS managed key, you cannot create a delivery. For source stream encryption requirements, see [Source stream encryption](data-delivery-security.md#data-delivery-security-source-stream-encryption). For the AWS KMS permissions the service execution role needs, see [IAM permissions for data delivery](data-delivery-iam.md). 

## Cross-account and cross-Region delivery
<a name="data-delivery-st-cross-account-region"></a>

 Streaming table delivery does not support cross-account or cross-Region delivery. The source stream, the destination S3 table bucket, and the AWS Glue Schema Registry must all be in the same AWS account and the same Region. 
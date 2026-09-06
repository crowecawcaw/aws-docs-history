

# Streaming tables
<a name="data-delivery-st"></a>

 Streaming tables continuously delivers records from a Amazon Kinesis Data Streams stream into streaming tables on Apache Iceberg backed by Amazon S3 Tables. As data arrives, it is automatically converted to optimized Apache Parquet format with inline compaction, and becomes queryable through engines such as Amazon Athena, Amazon EMR, and Amazon Managed Service for Apache Flink. This capability requires a schema in AWS Glue Schema Registry and a dead-letter queue. 

**Topics**
+ [How streaming table delivery works](data-delivery-st-about.md)
+ [Getting started with streaming tables](data-delivery-st-getting-started.md)
+ [Manage streaming table deliveries](data-delivery-st-manage.md)
+ [Iceberg behaviors for streaming table](data-delivery-st-iceberg.md)


# Considerations and limitations
<a name="apache-iceberg-considerations"></a>

**Note**  
Firehose supports Apache Iceberg Tables as a destination in all [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#region) except China Regions, AWS GovCloud (US) Regions, Asia Pacific (Taipei), Asia Pacific (Malaysia), Asia Pacific (New Zealand), and Mexico (Central).

Firehose support for Apache Iceberg tables has the following considerations and limitations.
+ **Throughput **– If you use **Direct PUT** as the source to deliver data to Apache Iceberg tables, then the maximum throughput per stream is 5 MiB/second in US East (N. Virginia), US West (Oregon), and Europe (Ireland) Regions and 1 MiB/second in all other AWS Regions. If you want to insert data to Iceberg tables with no updates and deletes and you want higher throughput for your stream, then you can use the [Firehose Limits form](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits) to request a throughput limit increase.

  You can also set the `AppendOnly` flag to `True` if you want to only insert data and not perform updates and deletes. By setting the `AppendOnly` flag to `True`, Firehose automatically scales to match your throughput. Currently, you can set this flag only with the [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html) API operation.

  If a **Direct PUT** stream experiences throttling due to higher data ingest volumes that exceed the throughput capacity of a Firehose stream, then Firehose automatically increases the throughput limit of the stream until the throttling is contained. Depending on increased throughput and throttling, it might take longer for Firehose to increase the throughput of a stream to the desired levels. Because of this, continue to retry the failed data ingest records. If you expect the data volume to increase in sudden large bursts, or if your new stream needs a higher throughput than the default throughput limit, request to increase the throughput limit.
+ **Throughput and Partition Scaling** – The service is optimized to support either a large number of Iceberg partitions or very high ingest throughput. As ingest throughput increases, the number of partitions that can be actively written to decreases.

  Here are the limits for ingest throughput and max active partitions supported.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-considerations.html)
**Note**  
Ingest throughput here refers to the volume of data Firehose processes and writes to your Iceberg tables, measured *after* any Lambda transformation – not the volume of data sent to the stream at the source. If you use a Lambda function that expands your records, your processed throughput can be significantly higher than your source ingest volume, and the applicable max active partitions limit is based on the larger, post-transformation throughput.
+ **S3 Transaction Per Second (TPS) **– To optimize S3 performance, if you are using Kinesis Data Streams or Amazon MSK as a source, we recommend that you partition the source record using a proper partition key. In that way, data records that are routed to the same Iceberg table are mapped to one or a few source partitions know as shards. If possible, spread data records belonging to different target Iceberg tables into different partitions/shards, so that you can use all the aggregate throughput available across all the partitions/shards of the source topic/stream.
+ **Columns** – For column names and values, Firehose takes only the first level of nodes in a multi-level nested JSON. For example, Firehose selects the nodes that are available in the first level including the position field. The column names and the data types of the source data must exactly match those of the target tables for Firehose to deliver successfully. In this case, Firehose expects that you have either struct or map data type column in your Iceberg tables to match the position field. Firehose supports 16 levels of nesting. Following is an example of a nested JSON.

  ```
  {
     "version":"2016-04-01",
     "deviceId":"<solution_unique_device_id>",
     "sensorId":"<device_sensor_id>",
     "timestamp":"2024-01-11T20:42:45.000Z",
     "value":"<actual_value>",
     "position":{
        "x":143.595901,
        "y":476.399628,
        "z":0.24234876
     }
  }
  ```

  If the column names or data types do not match, then Firehose throws an error and delivers data to the S3 error bucket. If all the column names and data types match in the Apache Iceberg tables, but you have an additional field present in the source record, Firehose skips the new field. 
+ **One JSON object per record** – You can send only one JSON object in one Firehose record. If you aggregate and send multiple JSON objects inside a record, Firehose throws an error and delivers data to the S3 error bucket. If you aggregate records with [KPL](https://docs.aws.amazon.com/streams/latest/dev/kpl-with-firehose.html) and ingest data into Firehose with Amazon Kinesis Data Streams as source, then Firehose automatically de-aggregates and uses one JSON object per record. 
+ **Compaction and storage optimization** – Every time you write to Iceberg Tables using Firehose, it commits and generates snapshots, data files and delete files. Having many data files increases metadata overhead and affects read performance. To get efficient query performance, you might want to consider a solution that periodically takes small data files and rewrites them into fewer larger data files. This process is called compaction. AWS Glue Data Catalog supports automatic compaction of your Apache Iceberg Tables. For more information, see [Compaction management](https://docs.aws.amazon.com/glue/latest/dg/compaction-management.html) in the *AWS Glue User Guide*. For additional information, see [Automatic compaction of Apache Iceberg Tables](https://aws.amazon.com/blogs/aws/aws-glue-data-catalog-now-supports-automatic-compaction-of-apache-iceberg-tables/). Alternatively, you can run the Athena Optimize command to perform compaction manually. For more information about the Optimize command, see [Athena Optimize](https://docs.aws.amazon.com/athena/latest/ug/optimize-statement.html).

  Besides compaction of data files, you can also optimize storage consumption with the [VACUUM](https://docs.aws.amazon.com/athena/latest/ug/vacuum-statement.html) statement that performs table maintenance on Apache Iceberg tables, such as snapshot expiration and orphan file removal. Alternatively, you can use AWS Glue Data Catalog that also supports managed table optimization of Apache Iceberg tables by automatically removing the data files, orphaned files, and expire snapshots that are no longer needed. For more information, see this blog post on [Storage optimization of Apache Iceberg Tables](https://aws.amazon.com/blogs/big-data/the-aws-glue-data-catalog-now-supports-storage-optimization-of-apache-iceberg-tables/).
+ We do not support Amazon MSK Serverless source for Apache Iceberg Tables as a destination.
+ For an update operation, Firehose puts a delete file followed by an insert operation. Putting delete files incurs Amazon S3 put charges.
+ Firehose does not recommend using multiple Firehose streams to write data to the same Apache Iceberg table. This is because Apache Iceberg relies on [Optimistic Concurrency Control (OCC)](https://iceberg.apache.org/docs/1.6.0/reliability/#concurrent-write-operations). If multiple Firehose streams attempt to write to a single Iceberg table concurrently, then only one stream is succeed in committing the data at a given time. The other streams that fail to commit back-off, and retry the commit operation until the configured retry duration expires. Once the retry duration is exhausted, the data and delete file keys (Amazon S3 paths) are sent to the configured Amazon S3 error prefix.
+ The current Iceberg Library version that Firehose supports is version 1.5.2.
+ For delivering encrypted data to Amazon S3 Tables, you should configure AWS Key Management Service parameters in Amazon S3 Tables, and not in the Firehose configuration. If you configure AWS Key Management Service parameters in Firehose for delivering encrypted data to Amazon S3 Tables, then Firehose cannot use those parameters to encrypt. For more information, see [Using server-side encryption with AWS KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-encryption.html).
+ Firehose streams only support delivery to databases and tables that are created through Iceberg’s GlueCatalog API. Delivery to databases and tables that are created through the Glue SDK are not supported. Note that a hyphen (`-`) is not a supported character for the database and the table name in the Iceberg library. For more details, see the [Glue Database Regex](https://github.com/apache/iceberg/blob/main/aws/src/main/java/org/apache/iceberg/aws/glue/IcebergToGlueConverter.java#L62) and the [Glue Table Regex](https://github.com/apache/iceberg/blob/main/aws/src/main/java/org/apache/iceberg/aws/glue/IcebergToGlueConverter.java#L63]) that are supported by the Iceberg library.
+ All files written by Firehose are computed using the partition that is present in the record. This also applies to deleted files. Global deletes, such as writing unpartitioned delete files for a partitioned table, is not supported.
+ Firehose does not currently support bloom filter properties when delivering data to Apache Iceberg tables. When bloom filter properties are configured on Iceberg tables, Firehose will ignore these properties during data delivery operations.
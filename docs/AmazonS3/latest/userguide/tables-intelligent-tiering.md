# Cost optimization for tables with Intelligent-Tiering

You can automatically optimize storage costs for tables by using S3 Intelligent-Tiering. The S3 Tables Intelligent-Tiering storage class automatically moves data to the most cost-effective access tier when access patterns change. When you use S3 Intelligent-Tiering, data accessed less frequently is automatically moved to lower-cost tiers, and moved back to the Frequent Access tier whenever you access it again.

All data is moved between tiers without retrieval fees, performance impact, or changes to availability. Additionally, table maintenance operations such as compaction are optimized based on access patterns, processing only actively accessed data in the Frequent Access tier while reducing maintenance costs on less frequently accessed data in lower-cost tiers.

###### Topics

- [S3 Tables Intelligent-Tiering access tiers](#tables-intelligent-tiering-access-tiers "#tables-intelligent-tiering-access-tiers")
- [Auto-tiering behavior with S3 Intelligent-Tiering](#tables-intelligent-tiering-auto-tiering-behavior "#tables-intelligent-tiering-auto-tiering-behavior")
- [Specifying S3 Intelligent-Tiering as your storage class](#tables-intelligent-tiering-specifying-storage-class "#tables-intelligent-tiering-specifying-storage-class")
- [Monitoring storage usage](#tables-intelligent-tiering-monitoring-storage "#tables-intelligent-tiering-monitoring-storage")

## S3 Tables Intelligent-Tiering access tiers

When your table is stored in the S3 Intelligent-Tiering storage class, Amazon S3 continuously monitors access patterns and automatically moves table data between access tiers.

Tiering happens at the individual file level, so a single table can have files in different tiers based on access patterns. Table data is automatically moved to one of the following access tiers based on access patterns:

- **Frequent Access**: The default tier for all files. Files in other tiers automatically move back to the Frequent Access tier when accessed.
- **Infrequent Access**: If you do not access a file for 30 consecutive days, it moves to the Infrequent Access tier.
- **Archive Instant Access**: If you do not access a file for 90 consecutive days, it moves to the Archive Instant Access tier.

All tiers provide millisecond latency, high throughput performance, and are designed for 99.9% availability and 99.999999999% durability.

## Auto-tiering behavior with S3 Intelligent-Tiering

The following actions constitute access that automatically moves files from the Infrequent Access tier or the Archive Instant Access tier back to the Frequent Access tier:

- Any read or write operations on table data or metadata files using `GetObject`, `PutObject`, or `CompleteMultipartUpload` actions
- `LoadTable` or `UpdateTable` actions using [Iceberg REST API Operations](s3-tables-integrating-open-source.md#endpoint-supported-api "s3-tables-integrating-open-source.md#endpoint-supported-api")
- S3 Tables replication operations

Other actions don't constitute access that automatically moves files from the Infrequent Access tier or the Archive Instant Access tier back to the Frequent Access tier.

###### Note

Files smaller than 128 KB are not eligible for auto-tiering and remain in the Frequent Access tier. Compaction may combine these files into fewer, larger objects and commit them back to your table as a new snapshot. The newly compacted files become eligible for auto-tiering if the new file is 128 KB or larger.

### Table maintenance behavior

Automatic table maintenance operations performed by Amazon S3, such as snapshot management, unreferenced file removal, and record expiration, continue to run on your tables regardless of tier. Compaction runs only on files in the Frequent Access tier, optimizing performance for frequently accessed data while reducing maintenance costs on data in lower-cost tiers.

Maintenance operations do not affect the access tier of files in your table. Reads performed by maintenance operations do not cause files to change tiers. However, if a maintenance operation, such as compaction or record expiration, writes a new file, that file is created in the Frequent Access tier.

###### Note

Because compaction only processes files in the Frequent Access tier, delete operations on data in lower-cost tiers create delete files that are not automatically compacted. These delete files become eligible for compaction when the associated data files are accessed and move back to the Frequent Access tier. For tables that are not frequently accessed, you can manually run compaction using Amazon EMR to compact these delete files with their associated data files. For more information, see [Maintaining tables by using compaction](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-compaction.md#compaction-emr-glue "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-compaction.md#compaction-emr-glue"). You can monitor file growth in your table using Amazon CloudWatch metrics to determine when manual compaction may be beneficial.

## Specifying S3 Intelligent-Tiering as your storage class

By default, all tables are created in the S3 Standard storage class and cannot be moved to S3 Intelligent-Tiering. To use S3 Intelligent-Tiering, you must specify it at table creation. You can also set S3 Intelligent-Tiering as the default storage class for your table bucket to automatically store any new tables created there in the S3 Intelligent-Tiering storage class.

### Specifying S3 Intelligent-Tiering for table buckets

You can specify S3 Intelligent-Tiering as the default storage class when creating a new table bucket by using the `storage-class-configuration` header with the `CreateTableBucket` operation.

To check the default storage class on an existing table bucket, use the `GetTableBucketStorageClass` operation. To modify the default storage class of an existing table bucket, use the `PutTableBucketStorageClass` operation.

###### Note

When you modify the default storage class on a table bucket, that setting applies only to new tables created in that bucket. The storage class for pre-existing tables is not changed.

### Specifying S3 Intelligent-Tiering for tables

You can specify S3 Intelligent-Tiering as the storage class when creating a new table using the `storage-class-configuration` header with the `CreateTable` operation.

If you do not specify a storage class at table creation, the table is created in the default storage class configured on the table bucket at that time. Once a table is created, you cannot modify its storage class.

To check the default storage class on an existing table bucket, use the `GetTableBucketStorageClass` operation.

## Monitoring storage usage

You can view your storage usage breakdown by access tier in the AWS Cost and Usage Reports for your account. For more information, see [Creating Cost and Usage Reports](../../../cur/latest/userguide/creating-cur.md "../../../cur/latest/userguide/creating-cur.md") in the _AWS Data Exports User Guide_.

The following usage types are available in your billing reports:

| Usage Type                                     | Unit     | Granularity | Description                                                                                                                         |
| ---------------------------------------------- | -------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| ``region`-Tables-TimedStorage-INT-FA-ByteHrs`  | GB-Month | Daily       | The number of GB-months that data was stored in the S3 Intelligent-Tiering Frequent Access of S3 Intelligent-Tiering storage        |
| ``region`-Tables-TimedStorage-INT-IA-ByteHrs`  | GB-Month | Daily       | The number of GB-months that data was stored in the S3 Intelligent-Tiering Infrequent Access of S3 Intelligent-Tiering storage      |
| ``region`-Tables-TimedStorage-INT-AIA-ByteHrs` | GB-Month | Daily       | The number of GB-months that data was stored in the S3 Intelligent-Tiering Archive Instant Access of S3 Intelligent-Tiering storage |
| ``region`-Tables-Requests-INT-Tier1`           | Count    | Hourly      | The number of `PUT`, `COPY`, or `POST` requests on S3 Tables Intelligent-Tiering objects                                            |
| ``region`-Tables-Requests-INT-Tier2`           | Count    | Hourly      | The number of `GET` and all other non-Tier1 requests for S3 Tables Intelligent-Tiering objects                                      |

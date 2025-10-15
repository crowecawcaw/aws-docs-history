# Maintenance for tables

S3 Tables offers maintenance operations to enhance the management and performance of your individual 
 tables. The following options are enabled by default for all tables in table buckets. You can edit or
 disable these by specifying maintenance configuration files for your S3 table.

Editing this configuration requires the
 `s3tables:GetTableMaintenanceConfiguration` and
 `s3tables:PutTableMaintenanceConfiguration` permissions.

###### Topics

* [Compaction](#s3-tables-maintenance-compaction "#s3-tables-maintenance-compaction")
* [Snapshot management](#s3-tables-maintenance-snapshot "#s3-tables-maintenance-snapshot")
* [Consideration and limitations](#s3-tables-considerations-see-more "#s3-tables-considerations-see-more")

## Compaction


Compaction is configured at the table level and combines multiple smaller objects into fewer, larger objects to improve Apache Iceberg
 query performance. When combining objects, compaction also applies the effects of
 row-level deletes in your table.


Compaction is enabled by default for all tables, with a default target file size of 512MB, or a custom value you specify between 64MB to 512MB. The compacted files are
 written as the most recent snapshot of your table.


###### Note

Compaction is supported on Apache Parquet, Avro, and ORC file types.


### Compaction Strategies


You can choose from multiple compaction strategies which can further increase query performance depending on your query patterns and table sort order.


S3 Tables supports these compaction strategies for tables:



* **Auto (Default)**




	+ Amazon S3 selects the best compaction strategy based on your table sort order. This is the default compaction strategy for all tables.
	+ For tables with a defined sort order in their metadata, `auto` will automatically apply `sort` compaction.
	+ For tables without a sort order, `auto` will default to using `binpack` compaction.
* **Binpack**




	+ Combines small files into larger files, typically targeting sizes over 100MB, while applying any pending deletes. This is the default compaction strategy for unsorted tables.
* **Sort**




	+ Organizes data based on specified columns which are sorted automatically by hierarchy during compaction, improving query performance for filtered operations. This strategy is recommended when your queries frequently filter on specific columns. When you use this strategy, S3 Tables automatically applies hierarchical sorting on columns when a `sort_order` is defined in table properties.
* **Z-order**




	+ Optimizes data organization by blending multiple attributes into a single scalar value that can be used for sorting, allowing efficient querying across multiple dimensions. This strategy is recommended when you need to query data across multiple dimensions simultaneously. This strategy requires you to define a sort order in your Iceberg table properties using the `sort_order` table property.

Compaction will incur additional costs. The `z-order` and `sort` compaction strategies may incur a higher cost than `binpack`. For more information, see the pricing information in the .[Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


### 
 Compaction Examples


The following examples show configurations for table compaction.




**To configure the compaction target file size by using the AWS CLI**

The minimum target compaction file size is 64MB; the maximum is 512MB.


The following example will change the target file size to 256MB using the
 `PutTableMaintenanceConfiguration` API.



```
aws s3tables put-table-maintenance-configuration \
   --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1` \
   --type icebergCompaction \
   --namespace `mynamespace` \
   --name `testtable` \
   --value='{"status":"enabled","settings":{"icebergCompaction":{"targetFileSizeMB":256}}}'
```

For more information, see [put-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html") in the *AWS CLI Command Reference*.



**To configure the compaction strategy by using the AWS CLI**

The following example will change the compaction strategy to `sort` using the
 `PutTableMaintenanceConfiguration` API. When setting compaction you can choose from the following compaction strategies: `auto`,`binpack`,`sort`, or `z-order`


###### Note

To set the compaction strategy to `sort` or `z-order` you need the following prerequisites:


* A sort order defined in your Iceberg table properties.
* The `s3tables:GetTableData` permission.


```
aws s3tables put-table-maintenance-configuration \
   --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
   --type icebergCompaction \
   --namespace `mynamespace` \
   --name `testtable` \
   --value='{"status":"enabled","settings":{"icebergCompaction":{"strategy":"sort"}}}'
```

For more information, see [put-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html") in the *AWS CLI Command Reference*.



**To disable compaction by using the AWS CLI**

The following example will disable compaction using the
 `PutTableMaintenanceConfiguration` API.



```
aws s3tables put-table-maintenance-configuration \
   --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
   --type icebergCompaction \
   --namespace `mynamespace` \
   --name `testtable` \
   --value='{"status":"disabled","settings":{"icebergCompaction":{"targetFileSizeMB":256}}}'
```

For more information, see [put-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html") in the *AWS CLI Command Reference*.




## Snapshot management


Snapshot management determines the number of active snapshots for your table.
 This is based on the `MinimumSnapshots` (1 by default) and
 `MaximumSnapshotAge` (120 hours by default). Snapshot management expires
 and removes table snapshots based on these configurations.


When a snapshot expires, Amazon S3 marks any objects referenced only by that snapshot as noncurrent. These
 noncurrent objects are deleted after the number of days specified by the `NoncurrentDays`
 property in your unreferenced file removal policy.


###### Note

Deletes of noncurrent objects are permanent with no way to recover these objects.


To view or recover objects that has been marked as noncurrent you must contact AWS Support. For
 information about contacting AWS Support, see [Contact AWS](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") or the [AWS Support
 Documentation](https://aws.amazon.com/documentation/aws-support/ "https://aws.amazon.com/documentation/aws-support/").


Snapshot management determines the objects to delete from your table with
 references only to that table. References to these objects from outside the table will not prevent snapshot management from deleting them.


###### Note

Snapshot management does not support retention values you configure as Iceberg
 table properties in the `metadata.json` file or through an
 `ALTER TABLE SET TBLPROPERTIES` SQL command, including branch or
 tag-based retention. Snapshot management is disabled when you
 configure a branch or tag-based retention policy, or configure a retention policy on
 the `metadata.json` file that is longer than the values
 configured through the `PutTableMaintenanceConfiguration` API. In these
 cases S3 will not expire or remove snapshots and you will need to manually delete
 snapshots or remove the properties from your Iceberg table to avoid storage
 charges.


You can only configure snapshot management at the table level. For more information,
 see the pricing information in the [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


### 
 Snapshot Management Examples


The following examples show configurations for table snapshot management.




**To configure the snapshot management by using the AWS CLI**

The following example will set the `MinimumSnapshots` to 10 and
 the `MaximumSnapshotAge` to 2500 hours using the
 `PutTableMaintenanceConfiguration` API.



```
aws s3tables put-table-maintenance-configuration \
--table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
--namespace `my_namespace` \
--name `my_table` \
--type icebergSnapshotManagement \
--value '{"status":"enabled","settings":{"icebergSnapshotManagement":{"minSnapshotsToKeep":10,"maxSnapshotAgeHours":2500}}}' 
```


**To disable snapshot management by using the AWS CLI**

The following example will disable snapshot management using the
 `PutTableMaintenanceConfiguration` API.



```
aws s3tables put-table-maintenance-configuration \
--table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
--namespace `my_namespace` \
--name `my_table` \
--type icebergSnapshotManagement \
--value '{"status":"disabled","settings":{"icebergSnapshotManagement":{"minSnapshotsToKeep":1,"maxSnapshotAgeHours":120}}}' 
```



For more information, see [put-table-maintenance-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/put-table-maintenance-configuration.html") in the *AWS CLI Command Reference*.


## Consideration and limitations


To learn more about additional consideration and limits for compaction and snapshot
 management, see [Considerations and limitations for maintenance jobs](s3-tables-considerations.md "s3-tables-considerations.md").


###### Note

S3 Tables applies the parquets row-group-default size of 128 MB.

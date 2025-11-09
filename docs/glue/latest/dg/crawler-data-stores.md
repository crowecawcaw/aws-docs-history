# Supported data sources for crawling

Crawlers can crawl the following file-based and table-based data
stores.

| Access type that crawler uses | Data stores                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Native client                 | • Amazon Simple Storage Service (Amazon S3)<br>• Amazon DynamoDB<br>• Delta Lake 2.0.x<br>• Apache Iceberg 1.5<br>• Apache Hudi 0.14                                                                               |
| JDBC                          | Amazon Redshift<br>Snowflake<br>Within Amazon Relational Database Service (Amazon RDS) or external to Amazon RDS:<br>• Amazon Aurora<br>• MariaDB<br>• Microsoft SQL Server<br>• MySQL<br>• Oracle<br>• PostgreSQL |
| MongoDB client                | • MongoDB<br>• MongoDB Atlas<br>• Amazon DocumentDB (with MongoDB compatibility)                                                                                                                                   |

###### Note

Currently AWS Glue does not support crawlers for data streams.

For JDBC, MongoDB, MongoDB Atlas, and Amazon DocumentDB (with MongoDB compatibility) data stores, you must specify
an AWS Glue _connection_ that the crawler can use to connect to
the data store. For Amazon S3, you can optionally specify a connection of type Network. A
connection is a Data Catalog object that stores connection information, such as credentials, URL,
Amazon Virtual Private Cloud information, and more. For
more information, see [Connecting to data](glue-connections.md "glue-connections.md").

The following are the versions of drivers supported by the crawler:

| Product              | Crawler supported driver       |
| -------------------- | ------------------------------ |
| PostgreSQL           | 42.2.1                         |
| Amazon Aurora        | Same as native crawler drivers |
| MariaDB              | 8.0.13                         |
| Microsoft SQL Server | 6.1.0                          |
| MySQL                | 8.0.13                         |
| Oracle               | 11.2.2                         |
| Amazon Redshift      | 4.1                            |
| Snowflake            | 3.13.20                        |
| MongoDB              | 4.7.2                          |
| MongoDB Atlas        | 4.7.2                          |

The following are notes about the various data stores.

**Amazon S3**

You can choose to crawl a path in your account or in another account. If all the
Amazon S3 files in a folder have the same schema, the crawler creates one table. Also, if the
Amazon S3 object is partitioned, only one metadata table is created and partition information
is added to the Data Catalog for that
table.

**Amazon S3 and Amazon DynamoDB**

Crawlers use an AWS Identity and Access Management (IAM) role for permission to access your data stores.
_The role you pass to the crawler must have permission to access Amazon S3 paths
and Amazon DynamoDB tables that are crawled_.

**Amazon DynamoDB**

When defining a crawler using the AWS Glue console, you specify one DynamoDB table. If
you're using the AWS Glue API, you can specify a list of tables. You can choose to crawl
only a small sample of the data to reduce crawler run times.

**Delta Lake**

For each Delta Lake data store, you specify how to create the Delta tables:

- **Create Native tables**: Allow integration with query engines that support querying of the Delta transaction log directly. For more information, see [Querying Delta Lake tables](../../../athena/latest/ug/delta-lake-tables.md "../../../athena/latest/ug/delta-lake-tables.md").
- **Create Symlink tables**: Create a `_symlink_manifest` folder with manifest files partitioned by the partition keys, based on the specified configuration parameters.

**Iceberg**

For each Iceberg data store, you specify an Amazon S3 path that contains the metadata for your Iceberg tables. If crawler discovers Iceberg table metadata, it registers it in the Data Catalog. You can set a schedule for the crawler to keep the tables updated.

You can define these parameters for the data store:

- **Exclusions**: Allows you to skip certain folders.
- **Maximum Traversal Depth**: Sets the depth limit the crawler can crawl in your Amazon S3 bucket. The default maximum traversal depth is 10 and the maximum depth you can set is 20.

**Hudi**

For each Hudi data store, you specify an Amazon S3 path that contains the metadata for your Hudi tables. If crawler discovers Hudi table metadata, it registers it in the Data Catalog. You can set a schedule for the crawler to keep the tables updated.

You can define these parameters for the data store:

- **Exclusions**: Allows you to skip certain folders.
- **Maximum Traversal Depth**: Sets the depth limit the crawler can crawl in your Amazon S3 bucket. The default maximum traversal depth is 10 and the maximum depth you can set is 20.

###### Note

Timestamp columns with `millis` as logical types will be interpreted as `bigint`, due to an incompatibility with Hudi 0.13.1 and timestamp types. A resolution may be provided in the upcoming Hudi release.

Hudi tables are categorized as follows, with specific implications for each:

- Copy on Write (CoW): Data is stored in a columnar format (Parquet), and each update creates a new version of files during a write.
- Merge on Read (MoR): Data is stored using a combination of columnar (Parquet) and row-based (Avro) formats. Updates are logged to row-based delta files and are compacted as needed to create new versions of the columnar files.

With CoW datasets, each time there is an update to a record, the file that contains the record is rewritten with the updated values. With a MoR dataset, each time there is an update, Hudi writes only the row for the changed record. MoR is better suited for write- or change-heavy workloads with fewer reads. CoW is better suited for read-heavy workloads on data that change less frequently.

Hudi provides three query types for accessing the data:

- Snapshot queries: Queries that see the latest snapshot of the table as of a given commit or compaction action. For MoR tables, snapshot queries expose the most recent state of the table by merging the base and delta files of the latest file slice at the time of the query.
- Incremental queries: Queries only see new data written to the table, since a given commit/compaction. This effectively provides change streams to enable incremental data pipelines.
- Read optimized queries: For MoR tables, queries see the latest data compacted. For CoW tables, queries see the latest data committed.

For Copy-On-Write tables, the crawlers creates a single table in the Data Catalog with the ReadOptimized serde `org.apache.hudi.hadoop.HoodieParquetInputFormat`.

For Merge-On-Read tables, the crawler creates two tables in the Data Catalog for the same table location:

- A table with suffix `_ro` which uses the ReadOptimized serde `org.apache.hudi.hadoop.HoodieParquetInputFormat`.
- A table with suffix `_rt` which uses the RealTime Serde allowing for Snapshot queries: `org.apache.hudi.hadoop.realtime.HoodieParquetRealtimeInputFormat`.

**MongoDB and Amazon DocumentDB (with MongoDB compatibility)**

MongoDB versions 3.2 and later are supported. You can choose to crawl only a small
sample of the data to reduce crawler run times.

**Relational database**

Authentication is with a database user name and password. Depending on the type of
database engine, you can choose which objects are crawled, such as databases, schemas,
and tables.

**Snowflake**

The Snowflake JDBC crawler supports crawling the Table, External Table, View, and Materialized View. The Materialized View Definition will not be populated.

For Snowflake external tables, the crawler only will crawl if it points to an Amazon S3 location. In addition to the the table schema, the crawler will also crawl the Amazon S3 location, file format and output as table parameters in the Data Catalog table. Note that the partition information of the partitioned external table is not populated.

ETL is currently not supported for Data Catalog tables created using the Snowflake crawler.

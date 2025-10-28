# Crawler API

The Crawler API describes AWS Glue crawler data types, along
with the API for creating, deleting, updating, and listing crawlers.

## Data types

- [Crawler structure](#aws-glue-api-crawler-crawling-Crawler "#aws-glue-api-crawler-crawling-Crawler")
- [Schedule structure](#aws-glue-api-crawler-crawling-Schedule "#aws-glue-api-crawler-crawling-Schedule")
- [CrawlerTargets structure](#aws-glue-api-crawler-crawling-CrawlerTargets "#aws-glue-api-crawler-crawling-CrawlerTargets")
- [S3Target structure](#aws-glue-api-crawler-crawling-S3Target "#aws-glue-api-crawler-crawling-S3Target")
- [S3DeltaCatalogTarget structure](#aws-glue-api-crawler-crawling-S3DeltaCatalogTarget "#aws-glue-api-crawler-crawling-S3DeltaCatalogTarget")
- [S3DeltaDirectTarget structure](#aws-glue-api-crawler-crawling-S3DeltaDirectTarget "#aws-glue-api-crawler-crawling-S3DeltaDirectTarget")
- [JdbcTarget structure](#aws-glue-api-crawler-crawling-JdbcTarget "#aws-glue-api-crawler-crawling-JdbcTarget")
- [MongoDBTarget structure](#aws-glue-api-crawler-crawling-MongoDBTarget "#aws-glue-api-crawler-crawling-MongoDBTarget")
- [DynamoDBTarget structure](#aws-glue-api-crawler-crawling-DynamoDBTarget "#aws-glue-api-crawler-crawling-DynamoDBTarget")
- [DeltaTarget structure](#aws-glue-api-crawler-crawling-DeltaTarget "#aws-glue-api-crawler-crawling-DeltaTarget")
- [IcebergTarget structure](#aws-glue-api-crawler-crawling-IcebergTarget "#aws-glue-api-crawler-crawling-IcebergTarget")
- [HudiTarget structure](#aws-glue-api-crawler-crawling-HudiTarget "#aws-glue-api-crawler-crawling-HudiTarget")
- [CatalogTarget structure](#aws-glue-api-crawler-crawling-CatalogTarget "#aws-glue-api-crawler-crawling-CatalogTarget")
- [CrawlerMetrics structure](#aws-glue-api-crawler-crawling-CrawlerMetrics "#aws-glue-api-crawler-crawling-CrawlerMetrics")
- [CrawlerHistory structure](#aws-glue-api-crawler-crawling-CrawlerHistory "#aws-glue-api-crawler-crawling-CrawlerHistory")
- [CrawlsFilter structure](#aws-glue-api-crawler-crawling-CrawlsFilter "#aws-glue-api-crawler-crawling-CrawlsFilter")
- [SchemaChangePolicy structure](#aws-glue-api-crawler-crawling-SchemaChangePolicy "#aws-glue-api-crawler-crawling-SchemaChangePolicy")
- [LastCrawlInfo structure](#aws-glue-api-crawler-crawling-LastCrawlInfo "#aws-glue-api-crawler-crawling-LastCrawlInfo")
- [RecrawlPolicy structure](#aws-glue-api-crawler-crawling-RecrawlPolicy "#aws-glue-api-crawler-crawling-RecrawlPolicy")
- [LineageConfiguration structure](#aws-glue-api-crawler-crawling-LineageConfiguration "#aws-glue-api-crawler-crawling-LineageConfiguration")
- [LakeFormationConfiguration structure](#aws-glue-api-crawler-crawling-LakeFormationConfiguration "#aws-glue-api-crawler-crawling-LakeFormationConfiguration")

## Crawler structure

Specifies a crawler program that examines a data source and uses classifiers
to try to determine its schema. If successful, the crawler records metadata concerning
the data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler.

- `Role` – UTF-8 string.

The Amazon Resource Name (ARN) of an IAM role that's used to access customer
resources, such as Amazon Simple Storage Service (Amazon S3) data.

- `Targets` – A [CrawlerTargets](#aws-glue-api-crawler-crawling-CrawlerTargets "#aws-glue-api-crawler-crawling-CrawlerTargets") object.

A collection of targets to crawl.

- `DatabaseName` – UTF-8 string.

The name of the database in which the crawler's output is stored.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the crawler.

- `Classifiers` – An array of UTF-8 strings.

A list of UTF-8 strings that specify the custom classifiers that are associated
with the crawler.

- `RecrawlPolicy` – A [RecrawlPolicy](#aws-glue-api-crawler-crawling-RecrawlPolicy "#aws-glue-api-crawler-crawling-RecrawlPolicy") object.

A policy that specifies whether to crawl the entire dataset again, or to
crawl only folders that were added since the last crawler run.

- `SchemaChangePolicy` – A [SchemaChangePolicy](#aws-glue-api-crawler-crawling-SchemaChangePolicy "#aws-glue-api-crawler-crawling-SchemaChangePolicy") object.

The policy that specifies update and delete behaviors for the crawler.

- `LineageConfiguration` – A [LineageConfiguration](#aws-glue-api-crawler-crawling-LineageConfiguration "#aws-glue-api-crawler-crawling-LineageConfiguration") object.

A configuration that specifies whether data lineage is enabled for the
crawler.

- `State` – UTF-8 string (valid values: `READY` | `RUNNING` | `STOPPING`).

Indicates whether the crawler is running, or whether a run is pending.

- `TablePrefix` – UTF-8 string, not more than 128 bytes long.

The prefix added to the names of tables that are created.

- `Schedule` – A [Schedule](aws-glue-api-crawler-scheduler.md#aws-glue-api-crawler-scheduler-Schedule "aws-glue-api-crawler-scheduler.md#aws-glue-api-crawler-scheduler-Schedule") object.

For scheduled crawlers, the schedule when the crawler runs.

- `CrawlElapsedTime` – Number (long).

If the crawler is running, contains the total time elapsed since the last
crawl began.

- `CreationTime` – Timestamp.

The time that the crawler was created.

- `LastUpdated` – Timestamp.

The time that the crawler was last updated.

- `LastCrawl` – A [LastCrawlInfo](#aws-glue-api-crawler-crawling-LastCrawlInfo "#aws-glue-api-crawler-crawling-LastCrawlInfo") object.

The status of the last crawl, and potentially error information if an error
occurred.

- `Version` – Number (long).

The version of the crawler.

- `Configuration` – UTF-8 string.

Crawler configuration information. This versioned JSON string allows
users to specify aspects of a crawler's behavior. For more information, see [Setting
crawler configuration options](crawler-configuration.md "crawler-configuration.md").

- `CrawlerSecurityConfiguration` – UTF-8 string, not more than 128 bytes long.

The name of the `SecurityConfiguration` structure to be
used by this crawler.

- `LakeFormationConfiguration` – A [LakeFormationConfiguration](#aws-glue-api-crawler-crawling-LakeFormationConfiguration "#aws-glue-api-crawler-crawling-LakeFormationConfiguration") object.

Specifies whether the crawler should use AWS Lake Formation credentials
for the crawler instead of the IAM role credentials.

## Schedule structure

A scheduling object using a `cron` statement to schedule
an event.

###### Fields

- `ScheduleExpression` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `State` – UTF-8 string (valid values: `SCHEDULED` | `NOT_SCHEDULED` | `TRANSITIONING`).

The state of the schedule.

## CrawlerTargets structure

Specifies data stores to crawl.

###### Fields

- `S3Targets` – An array of [S3Target](#aws-glue-api-crawler-crawling-S3Target "#aws-glue-api-crawler-crawling-S3Target") objects.

Specifies Amazon Simple Storage Service (Amazon S3) targets.

- `JdbcTargets` – An array of [JdbcTarget](#aws-glue-api-crawler-crawling-JdbcTarget "#aws-glue-api-crawler-crawling-JdbcTarget") objects.

Specifies JDBC targets.

- `MongoDBTargets` – An array of [MongoDBTarget](#aws-glue-api-crawler-crawling-MongoDBTarget "#aws-glue-api-crawler-crawling-MongoDBTarget") objects.

Specifies Amazon DocumentDB or MongoDB targets.

- `DynamoDBTargets` – An array of [DynamoDBTarget](#aws-glue-api-crawler-crawling-DynamoDBTarget "#aws-glue-api-crawler-crawling-DynamoDBTarget") objects.

Specifies Amazon DynamoDB targets.

- `CatalogTargets` – An array of [CatalogTarget](#aws-glue-api-crawler-crawling-CatalogTarget "#aws-glue-api-crawler-crawling-CatalogTarget") objects.

Specifies AWS Glue Data Catalog targets.

- `DeltaTargets` – An array of [DeltaTarget](#aws-glue-api-crawler-crawling-DeltaTarget "#aws-glue-api-crawler-crawling-DeltaTarget") objects.

Specifies Delta data store targets.

- `IcebergTargets` – An array of [IcebergTarget](#aws-glue-api-crawler-crawling-IcebergTarget "#aws-glue-api-crawler-crawling-IcebergTarget") objects.

Specifies Apache Iceberg data store targets.

- `HudiTargets` – An array of [HudiTarget](#aws-glue-api-crawler-crawling-HudiTarget "#aws-glue-api-crawler-crawling-HudiTarget") objects.

Specifies Apache Hudi data store targets.

## S3Target structure

Specifies a data store in Amazon Simple Storage Service (Amazon S3).

###### Fields

- `Path` – UTF-8 string.

The path to the Amazon S3 target.

- `Exclusions` – An array of UTF-8 strings.

A list of glob patterns used to exclude from the crawl. For more information,
see [Catalog
Tables with a Crawler](add-crawler.md "add-crawler.md").

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of a connection which allows a job or crawler to access data in Amazon
S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).

- `SampleSize` – Number (integer).

Sets the number of files in each leaf folder to be crawled when crawling
sample files in a dataset. If not set, all the files are crawled. A valid value is
an integer between 1 and 249.

- `EventQueueArn` – UTF-8 string.

A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.

- `DlqEventQueueArn` – UTF-8 string.

A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.

## S3DeltaCatalogTarget structure

Specifies a target that writes to a Delta Lake data source in the AWS Glue Data Catalog.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Table` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the table in the database to write to.

- `Database` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The name of the database to write to.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [CatalogSchemaChangePolicy](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-CatalogSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-AutoDataQuality "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Delta catalog target. When set to `true`, data quality checks
are performed automatically during the write operation.

- `OutputSchemas` – An array of [GlueSchema](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-GlueSchema "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-GlueSchema") objects.

Specifies the data schema for the S3 Delta catalog target.

## S3DeltaDirectTarget structure

Specifies a target that writes to a Delta Lake data source in Amazon S3.

###### Fields

- `Name` – _Required:_ UTF-8 string, matching the [Custom string pattern #63](aws-glue-api-common.md#regex_63 "aws-glue-api-common.md#regex_63").

The name of the data target.

- `Inputs` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 1 strings.

The nodes that are inputs to the data target.

- `PartitionKeys` – An array of UTF-8 strings.

Specifies native partitioning using a sequence of keys.

- `Path` – _Required:_ UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

The Amazon S3 path of your Delta Lake data source to write to.

- `Compression` – _Required:_ UTF-8 string (valid values: `uncompressed="UNCOMPRESSED"` | `snappy="SNAPPY"`).

Specifies how the data is compressed. This is generally not necessary
if the data has a standard file extension. Possible values are `"gzip"`
and `"bzip"`).

- `NumberTargetPartitions` – UTF-8 string.

Specifies the number of target partitions for distributing Delta Lake
dataset files across Amazon S3.

- `Format` – _Required:_ UTF-8 string (valid values: `json="JSON"` | `csv="CSV"` | `avro="AVRO"` | `orc="ORC"` | `parquet="PARQUET"` | `hudi="HUDI"` | `delta="DELTA"` | `iceberg="ICEBERG"` | `hyper="HYPER"` | `xml="XML"`).

Specifies the data output format for the target.

- `AdditionalOptions` – A map array of key-value pairs.

Each key is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Each value is a UTF-8 string, matching the [Custom string pattern #61](aws-glue-api-common.md#regex_61 "aws-glue-api-common.md#regex_61").

Specifies additional connection options for the connector.

- `SchemaChangePolicy` – A [DirectSchemaChangePolicy](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-DirectSchemaChangePolicy "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-DirectSchemaChangePolicy") object.

A policy that specifies update behavior for the crawler.

- `AutoDataQuality` – An [AutoDataQuality](aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-AutoDataQuality "aws-glue-api-visual-job-api.md#aws-glue-api-visual-job-api-AutoDataQuality") object.

Specifies whether to automatically enable data quality evaluation for
the S3 Delta direct target. When set to `true`, data quality checks
are performed automatically during the write operation.

## JdbcTarget structure

Specifies a JDBC data store to crawl.

###### Fields

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection to use to connect to the JDBC target.

- `Path` – UTF-8 string.

The path of the JDBC target.

- `Exclusions` – An array of UTF-8 strings.

A list of glob patterns used to exclude from the crawl. For more information,
see [Catalog
Tables with a Crawler](add-crawler.md "add-crawler.md").

- `EnableAdditionalMetadata` – An array of UTF-8 strings.

Specify a value of `RAWTYPES` or `COMMENTS`
to enable additional metadata in table responses. `RAWTYPES` provides
the native-level datatype. `COMMENTS` provides comments associated
with a column or table in the database.

If you do not need additional metadata, keep the field empty.

## MongoDBTarget structure

Specifies an Amazon DocumentDB or MongoDB data store to crawl.

###### Fields

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection to use to connect to the Amazon DocumentDB or
MongoDB target.

- `Path` – UTF-8 string.

The path of the Amazon DocumentDB or MongoDB target (database/collection).

- `ScanAll` – Boolean.

Indicates whether to scan all the records, or to sample rows from the table.
Scanning all the records can take a long time when the table is not a high throughput
table.

A value of `true` means to scan all records, while a value of
`false` means to sample the records. If no value is specified, the
value defaults to `true`.

## DynamoDBTarget structure

Specifies an Amazon DynamoDB table to crawl.

###### Fields

- `Path` – UTF-8 string.

The name of the DynamoDB table to crawl.

- `scanAll` – Boolean.

Indicates whether to scan all the records, or to sample rows from the table.
Scanning all the records can take a long time when the table is not a high throughput
table.

A value of `true` means to scan all records, while a value of
`false` means to sample the records. If no value is specified, the
value defaults to `true`.

- `scanRate` – Number (double).

The percentage of the configured read capacity units to use by the AWS Glue crawler. Read capacity units is a term defined by DynamoDB, and is
a numeric value that acts as rate limiter for the number of reads that can be performed
on that table per second.

The valid values are null or a value between 0.1 to 1.5. A null value is used
when user does not provide a value, and defaults to 0.5 of the configured Read Capacity
Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit
(for tables using on-demand mode).

## DeltaTarget structure

Specifies a Delta data store to crawl one or more Delta tables.

###### Fields

- `DeltaTables` – An array of UTF-8 strings.

A list of the Amazon S3 paths to the Delta tables.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection to use to connect to the Delta table target.

- `WriteManifest` – Boolean.

Specifies whether to write the manifest files to the Delta table path.

- `CreateNativeDeltaTable` – Boolean.

Specifies whether the crawler will create native tables, to allow integration
with query engines that support querying of the Delta transaction log directly.

## IcebergTarget structure

Specifies an Apache Iceberg data source where Iceberg tables are stored
in Amazon S3.

###### Fields

- `Paths` – An array of UTF-8 strings.

One or more Amazon S3 paths that contains Iceberg metadata folders
as `s3://bucket/prefix`.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection to use to connect to the Iceberg target.

- `Exclusions` – An array of UTF-8 strings.

A list of glob patterns used to exclude from the crawl. For more information,
see [Catalog
Tables with a Crawler](add-crawler.md "add-crawler.md").

- `MaximumTraversalDepth` – Number (integer).

The maximum depth of Amazon S3 paths that the crawler can traverse
to discover the Iceberg metadata folder in your Amazon S3 path. Used
to limit the crawler run time.

## HudiTarget structure

Specifies an Apache Hudi data source.

###### Fields

- `Paths` – An array of UTF-8 strings.

An array of Amazon S3 location strings for Hudi, each indicating
the root folder with which the metadata files for a Hudi table resides. The Hudi
folder may be located in a child folder of the root folder.

The crawler will scan all folders underneath a path for a Hudi folder.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection to use to connect to the Hudi target. If your Hudi
files are stored in buckets that require VPC authorization, you can set their
connection properties here.

- `Exclusions` – An array of UTF-8 strings.

A list of glob patterns used to exclude from the crawl. For more information,
see [Catalog
Tables with a Crawler](add-crawler.md "add-crawler.md").

- `MaximumTraversalDepth` – Number (integer).

The maximum depth of Amazon S3 paths that the crawler can traverse
to discover the Hudi metadata folder in your Amazon S3 path. Used to limit
the crawler run time.

## CatalogTarget structure

Specifies an AWS Glue Data Catalog target.

###### Fields

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database to be synchronized.

- `Tables` – _Required:_ An array of UTF-8 strings, at least 1 string.

A list of the tables to be synchronized.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The name of the connection for an Amazon S3-backed Data Catalog table to
be a target of the crawl when using a `Catalog` connection type paired
with a `NETWORK` Connection type.

- `EventQueueArn` – UTF-8 string.

A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.

- `DlqEventQueueArn` – UTF-8 string.

A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.

## CrawlerMetrics structure

Metrics for a specified crawler.

###### Fields

- `CrawlerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler.

- `TimeLeftSeconds` – Number (double), not more than None.

The estimated time left to complete a running crawl.

- `StillEstimating` – Boolean.

True if the crawler is still estimating how long it will take to complete
this run.

- `LastRuntimeSeconds` – Number (double), not more than None.

The duration of the crawler's most recent run, in seconds.

- `MedianRuntimeSeconds` – Number (double), not more than None.

The median duration of this crawler's runs, in seconds.

- `TablesCreated` – Number (integer), not more than None.

The number of tables created by this crawler.

- `TablesUpdated` – Number (integer), not more than None.

The number of tables updated by this crawler.

- `TablesDeleted` – Number (integer), not more than None.

The number of tables deleted by this crawler.

## CrawlerHistory structure

Contains the information for a run of a crawler.

###### Fields

- `CrawlId` – UTF-8 string.

A UUID identifier for each crawl.

- `State` – UTF-8 string (valid values: `RUNNING` | `COMPLETED` | `FAILED` | `STOPPED`).

The state of the crawl.

- `StartTime` – Timestamp.

The date and time on which the crawl started.

- `EndTime` – Timestamp.

The date and time on which the crawl ended.

- `Summary` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A run summary for the specific crawl in JSON. Contains the catalog tables
and partitions that were added, updated, or deleted.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

If an error occurred, the error message associated with the crawl.

- `LogGroup` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log group string pattern](aws-glue-api-common.md#aws-glue-api-regex-logGroup-id "aws-glue-api-common.md#aws-glue-api-regex-logGroup-id").

The log group associated with the crawl.

- `LogStream` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log-stream string pattern](aws-glue-api-common.md#aws-glue-api-regex-logStream-id "aws-glue-api-common.md#aws-glue-api-regex-logStream-id").

The log stream associated with the crawl.

- `MessagePrefix` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The prefix for a CloudWatch message about this crawl.

- `DPUHour` – Number (double), not more than None.

The number of data processing units (DPU) used in hours for the crawl.

## CrawlsFilter structure

A list of fields, comparators and value that you can use to filter the crawler
runs for a specified crawler.

###### Fields

- `FieldName` – UTF-8 string (valid values: `CRAWL_ID` | `STATE` | `START_TIME` | `END_TIME` | `DPU_HOUR`).

A key used to filter the crawler runs for a specified crawler. Valid values
for each of the field names are:

    + `CRAWL_ID`: A string representing the UUID identifier for
     a crawl.
    + `STATE`: A string representing the state of the crawl.
    + `START_TIME` and `END_TIME`: The epoch timestamp
     in milliseconds.
    + `DPU_HOUR`: The number of data processing unit (DPU) hours
     used for the crawl.

- `FilterOperator` – UTF-8 string (valid values: `GT` | `GE` | `LT` | `LE` | `EQ` | `NE`).

A defined comparator that operates on the value. The available operators
are:

    + `GT`: Greater than.
    + `GE`: Greater than or equal to.
    + `LT`: Less than.
    + `LE`: Less than or equal to.
    + `EQ`: Equal to.
    + `NE`: Not equal to.

- `FieldValue` – UTF-8 string.

The value provided for comparison on the crawl field.

## SchemaChangePolicy structure

A policy that specifies update and deletion behaviors for the crawler.

###### Fields

- `UpdateBehavior` – UTF-8 string (valid values: `LOG` | `UPDATE_IN_DATABASE`).

The update behavior when the crawler finds a changed schema.

- `DeleteBehavior` – UTF-8 string (valid values: `LOG` | `DELETE_FROM_DATABASE` | `DEPRECATE_IN_DATABASE`).

The deletion behavior when the crawler finds a deleted object.

## LastCrawlInfo structure

Status and error information about the most recent crawl.

###### Fields

- `Status` – UTF-8 string (valid values: `SUCCEEDED` | `CANCELLED` | `FAILED`).

Status of the last crawl.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

If an error occurred, the error information about the last crawl.

- `LogGroup` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log group string pattern](aws-glue-api-common.md#aws-glue-api-regex-logGroup-id "aws-glue-api-common.md#aws-glue-api-regex-logGroup-id").

The log group for the last crawl.

- `LogStream` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log-stream string pattern](aws-glue-api-common.md#aws-glue-api-regex-logStream-id "aws-glue-api-common.md#aws-glue-api-regex-logStream-id").

The log stream for the last crawl.

- `MessagePrefix` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The prefix for a message about this crawl.

- `StartTime` – Timestamp.

The time at which the crawl started.

## RecrawlPolicy structure

When crawling an Amazon S3 data source after the first crawl is complete,
specifies whether to crawl the entire dataset again or to crawl only folders that
were added since the last crawler run. For more information, see [Incremental Crawls in AWS Glue](incremental-crawls.md "incremental-crawls.md") in the developer guide.

###### Fields

- `RecrawlBehavior` – UTF-8 string (valid values: `CRAWL_EVERYTHING` | `CRAWL_NEW_FOLDERS_ONLY` | `CRAWL_EVENT_MODE`).

Specifies whether to crawl the entire dataset again or to crawl only folders
that were added since the last crawler run.

A value of `CRAWL_EVERYTHING` specifies crawling the entire
dataset again.

A value of `CRAWL_NEW_FOLDERS_ONLY` specifies crawling
only folders that were added since the last crawler run.

A value of `CRAWL_EVENT_MODE` specifies crawling only the
changes identified by Amazon S3 events.

## LineageConfiguration structure

Specifies data lineage configuration settings for the crawler.

###### Fields

- `CrawlerLineageSettings` – UTF-8 string (valid values: `ENABLE` | `DISABLE`).

Specifies whether data lineage is enabled for the crawler. Valid values
are:

    + ENABLE: enables data lineage for the crawler
    + DISABLE: disables data lineage for the crawler

## LakeFormationConfiguration structure

Specifies AWS Lake Formation configuration settings for the crawler.

###### Fields

- `UseLakeFormationCredentials` – Boolean.

Specifies whether to use AWS Lake Formation credentials for the crawler
instead of the IAM role credentials.

- `AccountId` – UTF-8 string, not more than 12 bytes long.

Required for cross account crawls. For same account crawls as the target
data, this can be left as null.

## Operations

- [CreateCrawler action (Python: create_crawler)](#aws-glue-api-crawler-crawling-CreateCrawler "#aws-glue-api-crawler-crawling-CreateCrawler")
- [DeleteCrawler action (Python: delete_crawler)](#aws-glue-api-crawler-crawling-DeleteCrawler "#aws-glue-api-crawler-crawling-DeleteCrawler")
- [GetCrawler action (Python: get_crawler)](#aws-glue-api-crawler-crawling-GetCrawler "#aws-glue-api-crawler-crawling-GetCrawler")
- [GetCrawlers action (Python: get_crawlers)](#aws-glue-api-crawler-crawling-GetCrawlers "#aws-glue-api-crawler-crawling-GetCrawlers")
- [GetCrawlerMetrics action (Python: get_crawler_metrics)](#aws-glue-api-crawler-crawling-GetCrawlerMetrics "#aws-glue-api-crawler-crawling-GetCrawlerMetrics")
- [UpdateCrawler action (Python: update_crawler)](#aws-glue-api-crawler-crawling-UpdateCrawler "#aws-glue-api-crawler-crawling-UpdateCrawler")
- [StartCrawler action (Python: start_crawler)](#aws-glue-api-crawler-crawling-StartCrawler "#aws-glue-api-crawler-crawling-StartCrawler")
- [StopCrawler action (Python: stop_crawler)](#aws-glue-api-crawler-crawling-StopCrawler "#aws-glue-api-crawler-crawling-StopCrawler")
- [BatchGetCrawlers action (Python: batch_get_crawlers)](#aws-glue-api-crawler-crawling-BatchGetCrawlers "#aws-glue-api-crawler-crawling-BatchGetCrawlers")
- [ListCrawlers action (Python: list_crawlers)](#aws-glue-api-crawler-crawling-ListCrawlers "#aws-glue-api-crawler-crawling-ListCrawlers")
- [ListCrawls action (Python: list_crawls)](#aws-glue-api-crawler-crawling-ListCrawls "#aws-glue-api-crawler-crawling-ListCrawls")

## CreateCrawler action (Python: create_crawler)

Creates a new crawler with specified targets, role, configuration, and
optional schedule. At least one crawl target must be specified, in the `s3Targets`
field, the `jdbcTargets` field, or the `DynamoDBTargets`
field.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the new crawler.

- `Role` – _Required:_ UTF-8 string.

The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler
to access customer resources.

- `DatabaseName` – UTF-8 string.

The AWS Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*`.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the new crawler.

- `Targets` – _Required:_ A [CrawlerTargets](#aws-glue-api-crawler-crawling-CrawlerTargets "#aws-glue-api-crawler-crawling-CrawlerTargets") object.

A list of collection of targets to crawl.

- `Schedule` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `Classifiers` – An array of UTF-8 strings.

A list of custom classifiers that the user has registered. By default,
all built-in classifiers are included in a crawl, but these custom classifiers
always override the default classifiers for a given classification.

- `TablePrefix` – UTF-8 string, not more than 128 bytes long.

The table prefix used for catalog tables that are created.

- `SchemaChangePolicy` – A [SchemaChangePolicy](#aws-glue-api-crawler-crawling-SchemaChangePolicy "#aws-glue-api-crawler-crawling-SchemaChangePolicy") object.

The policy for the crawler's update and deletion behavior.

- `RecrawlPolicy` – A [RecrawlPolicy](#aws-glue-api-crawler-crawling-RecrawlPolicy "#aws-glue-api-crawler-crawling-RecrawlPolicy") object.

A policy that specifies whether to crawl the entire dataset again, or to
crawl only folders that were added since the last crawler run.

- `LineageConfiguration` – A [LineageConfiguration](#aws-glue-api-crawler-crawling-LineageConfiguration "#aws-glue-api-crawler-crawling-LineageConfiguration") object.

Specifies data lineage configuration settings for the crawler.

- `LakeFormationConfiguration` – A [LakeFormationConfiguration](#aws-glue-api-crawler-crawling-LakeFormationConfiguration "#aws-glue-api-crawler-crawling-LakeFormationConfiguration") object.

Specifies AWS Lake Formation configuration settings for the crawler.

- `Configuration` – UTF-8 string.

Crawler configuration information. This versioned JSON string allows
users to specify aspects of a crawler's behavior. For more information, see [Setting
crawler configuration options](crawler-configuration.md "crawler-configuration.md").

- `CrawlerSecurityConfiguration` – UTF-8 string, not more than 128 bytes long.

The name of the `SecurityConfiguration` structure to be
used by this crawler.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to use with this crawler request. You may use tags to limit access
to the crawler. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") in the developer guide.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `AlreadyExistsException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`

## DeleteCrawler action (Python: delete_crawler)

Removes a specified crawler from the AWS Glue Data Catalog, unless
the crawler state is `RUNNING`.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler to remove.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `CrawlerRunningException`
- `SchedulerTransitioningException`
- `OperationTimeoutException`

## GetCrawler action (Python: get_crawler)

Retrieves metadata for a specified crawler.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler to retrieve metadata for.

###### Response

- `Crawler` – A [Crawler](#aws-glue-api-crawler-crawling-Crawler "#aws-glue-api-crawler-crawling-Crawler") object.

The metadata for the specified crawler.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`

## GetCrawlers action (Python: get_crawlers)

Retrieves metadata for all crawlers defined in the customer account.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The number of crawlers to return on each call.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

###### Response

- `Crawlers` – An array of [Crawler](#aws-glue-api-crawler-crawling-Crawler "#aws-glue-api-crawler-crawling-Crawler") objects.

A list of crawler metadata.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list has not reached the end of those
defined in this customer account.

###### Errors

- `OperationTimeoutException`

## GetCrawlerMetrics action (Python: get_crawler_metrics)

Retrieves metrics about specified crawlers.

###### Request

- `CrawlerNameList` – An array of UTF-8 strings, not more than 100 strings.

A list of the names of crawlers about which to retrieve metrics.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of a list to return.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `CrawlerMetricsList` – An array of [CrawlerMetrics](#aws-glue-api-crawler-crawling-CrawlerMetrics "#aws-glue-api-crawler-crawling-CrawlerMetrics") objects.

A list of metrics for the specified crawler.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list does not contain the last metric
available.

###### Errors

- `OperationTimeoutException`

## UpdateCrawler action (Python: update_crawler)

Updates a crawler. If a crawler is running, you must stop it using `StopCrawler`
before updating it.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the new crawler.

- `Role` – UTF-8 string.

The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the
new crawler to access customer resources.

- `DatabaseName` – UTF-8 string.

The AWS Glue database where results are stored, such as: `arn:aws:daylight:us-east-1::database/sometable/*`.

- `Description` – UTF-8 string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the new crawler.

- `Targets` – A [CrawlerTargets](#aws-glue-api-crawler-crawling-CrawlerTargets "#aws-glue-api-crawler-crawling-CrawlerTargets") object.

A list of targets to crawl.

- `Schedule` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `Classifiers` – An array of UTF-8 strings.

A list of custom classifiers that the user has registered. By default,
all built-in classifiers are included in a crawl, but these custom classifiers
always override the default classifiers for a given classification.

- `TablePrefix` – UTF-8 string, not more than 128 bytes long.

The table prefix used for catalog tables that are created.

- `SchemaChangePolicy` – A [SchemaChangePolicy](#aws-glue-api-crawler-crawling-SchemaChangePolicy "#aws-glue-api-crawler-crawling-SchemaChangePolicy") object.

The policy for the crawler's update and deletion behavior.

- `RecrawlPolicy` – A [RecrawlPolicy](#aws-glue-api-crawler-crawling-RecrawlPolicy "#aws-glue-api-crawler-crawling-RecrawlPolicy") object.

A policy that specifies whether to crawl the entire dataset again, or to
crawl only folders that were added since the last crawler run.

- `LineageConfiguration` – A [LineageConfiguration](#aws-glue-api-crawler-crawling-LineageConfiguration "#aws-glue-api-crawler-crawling-LineageConfiguration") object.

Specifies data lineage configuration settings for the crawler.

- `LakeFormationConfiguration` – A [LakeFormationConfiguration](#aws-glue-api-crawler-crawling-LakeFormationConfiguration "#aws-glue-api-crawler-crawling-LakeFormationConfiguration") object.

Specifies AWS Lake Formation configuration settings for the crawler.

- `Configuration` – UTF-8 string.

Crawler configuration information. This versioned JSON string allows
users to specify aspects of a crawler's behavior. For more information, see [Setting
crawler configuration options](crawler-configuration.md "crawler-configuration.md").

- `CrawlerSecurityConfiguration` – UTF-8 string, not more than 128 bytes long.

The name of the `SecurityConfiguration` structure to be
used by this crawler.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `VersionMismatchException`
- `EntityNotFoundException`
- `CrawlerRunningException`
- `OperationTimeoutException`

## StartCrawler action (Python: start_crawler)

Starts a crawl using the specified crawler, regardless of what is scheduled.
If the crawler is already running, returns a [CrawlerRunningException](aws-glue-api-exceptions.md#aws-glue-api-exceptions-CrawlerRunningException "aws-glue-api-exceptions.md#aws-glue-api-exceptions-CrawlerRunningException").

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the crawler to start.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `CrawlerRunningException`
- `OperationTimeoutException`

## StopCrawler action (Python: stop_crawler)

If the specified crawler is running, stops the crawl.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the crawler to stop.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `CrawlerNotRunningException`
- `CrawlerStoppingException`
- `OperationTimeoutException`

## BatchGetCrawlers action (Python: batch_get_crawlers)

Returns a list of resource metadata for a given list of crawler names. After
calling the `ListCrawlers` operation, you can call this operation
to access the data to which you have been granted permissions. This operation
supports all IAM permissions, including permission conditions that uses tags.

###### Request

- `CrawlerNames` – _Required:_ An array of UTF-8 strings, not more than 100 strings.

A list of crawler names, which might be the names returned from the `ListCrawlers`
operation.

###### Response

- `Crawlers` – An array of [Crawler](#aws-glue-api-crawler-crawling-Crawler "#aws-glue-api-crawler-crawling-Crawler") objects.

A list of crawler definitions.

- `CrawlersNotFound` – An array of UTF-8 strings, not more than 100 strings.

A list of names of crawlers that were not found.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`

## ListCrawlers action (Python: list_crawlers)

Retrieves the names of all crawler resources in this AWS account, or the resources with the specified tag. This operation allows you
to see which resources are available in your account, and their names.

This operation takes the optional `Tags` field, which you
can use as a filter on the response so that tagged resources can be retrieved as
a group. If you choose to use tags filtering, only resources with the tag are retrieved.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of a list to return.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Specifies to return only these tagged resources.

###### Response

- `CrawlerNames` – An array of UTF-8 strings, not more than 100 strings.

The names of all crawlers in the account, or the crawlers with the specified
tags.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list does not contain the last metric
available.

###### Errors

- `OperationTimeoutException`

## ListCrawls action (Python: list_crawls)

Returns all the crawls of a specified crawler. Returns only the crawls
that have occurred since the launch date of the crawler history feature, and only
retains up to 12 months of crawls. Older crawls will not be returned.

You may use this API to:

- Retrive all the crawls of a specified crawler.
- Retrieve all the crawls of a specified crawler within a limited count.
- Retrieve all the crawls of a specified crawler in a specific time range.
- Retrieve all the crawls of a specified crawler with a particular state,
  crawl ID, or DPU hour value.

###### Request

- `CrawlerName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler whose runs you want to retrieve.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return. The default is 20, and maximum
is 100.

- `Filters` – An array of [CrawlsFilter](#aws-glue-api-crawler-crawling-CrawlsFilter "#aws-glue-api-crawler-crawling-CrawlsFilter") objects.

Filters the crawls by the criteria you specify in a list of `CrawlsFilter`
objects.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `Crawls` – An array of [CrawlerHistory](#aws-glue-api-crawler-crawling-CrawlerHistory "#aws-glue-api-crawler-crawling-CrawlerHistory") objects.

A list of `CrawlerHistory` objects representing the crawl
runs that meet your criteria.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`

# GlueContext class

Wraps the Apache Spark [SparkContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html "https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html") object, and thereby provides mechanisms for interacting with the Apache
Spark platform.

## \_\_init\_\_

###### `__init__(sparkContext)`

- `sparkContext` – The Apache Spark context to use.

## Creating

- [\_\_init\_\_](#aws-glue-api-crawler-pyspark-extensions-glue-context-__init__ "#aws-glue-api-crawler-pyspark-extensions-glue-context-__init__")
- [getSource](#aws-glue-api-crawler-pyspark-extensions-glue-context-get-source "#aws-glue-api-crawler-pyspark-extensions-glue-context-get-source")
- [create_dynamic_frame_from_rdd](#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_rdd "#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_rdd")
- [create_dynamic_frame_from_catalog](#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog "#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_catalog")
- [create_dynamic_frame_from_options](#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options "#aws-glue-api-crawler-pyspark-extensions-glue-context-create_dynamic_frame_from_options")
- [create_sample_dynamic_frame_from_catalog](#aws-glue-api-crawler-pyspark-extensions-glue-context-create-sample-dynamic-frame-from-catalog "#aws-glue-api-crawler-pyspark-extensions-glue-context-create-sample-dynamic-frame-from-catalog")
- [create_sample_dynamic_frame_from_options](#aws-glue-api-crawler-pyspark-extensions-glue-context-create-sample-dynamic-frame-from-options "#aws-glue-api-crawler-pyspark-extensions-glue-context-create-sample-dynamic-frame-from-options")
- [add_ingestion_time_columns](#aws-glue-api-crawler-pyspark-extensions-glue-context-add-ingestion-time-columns "#aws-glue-api-crawler-pyspark-extensions-glue-context-add-ingestion-time-columns")
- [create_data_frame_from_catalog](#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-catalog "#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-catalog")
- [create_data_frame_from_options](#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options "#aws-glue-api-crawler-pyspark-extensions-glue-context-create-dataframe-from-options")
- [forEachBatch](#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch "#aws-glue-api-crawler-pyspark-extensions-glue-context-forEachBatch")

## getSource

###### `getSource(connection_type, transformation_ctx = "", **options)`

Creates a `DataSource` object that can be used to read
`DynamicFrames` from external sources.

- `connection_type` – The connection type to use, such as Amazon Simple Storage Service (Amazon S3),
  Amazon Redshift, and JDBC. Valid values include `s3`, `mysql`,
  `postgresql`, `redshift`, `sqlserver`,
  `oracle`, and `dynamodb`.
- `transformation_ctx` – The transformation context to use (optional).
- `options` – A collection of optional name-value pairs.
  For more information, see [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").

The following is an example of using `getSource`.

```
>>> data_source = context.getSource("file", paths=["/in/path"])
>>> data_source.setFormat("json")
>>> myFrame = data_source.getFrame()

```

## create_dynamic_frame_from_rdd

###### `create_dynamic_frame_from_rdd(data, name, schema=None, sample_ratio=None, transformation_ctx="")`

Returns a `DynamicFrame` that is created from an Apache Spark Resilient Distributed
Dataset (RDD).

- `data` – The data source to use.
- `name` – The name of the data to use.
- `schema` – The schema to use (optional).
- `sample_ratio` – The sample ratio to use (optional).
- `transformation_ctx` – The transformation context to use (optional).

## create_dynamic_frame_from_catalog

###### `create_dynamic_frame_from_catalog(database, table_name, redshift_tmp_dir, transformation_ctx = "", push_down_predicate= "", additional_options = {}, catalog_id = None)`

Returns a `DynamicFrame` that is created using a Data Catalog database and table name. When using this
method, you provide `format_options` through table properties on the specified AWS Glue Data Catalog
table and other options through the `additional_options` argument.

- `Database` – The database to read from.
- `table_name` – The name of the table to read from.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – The transformation context to use (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset. For supported sources and limitations, see [Optimizing reads with pushdown in AWS Glue ETL](aws-glue-programming-pushdown.md "aws-glue-programming-pushdown.md").
  For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").
- `additional_options` – A collection of optional name-value pairs. The
  possible options include those listed in [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") except for `endpointUrl`,
  `streamName`, `bootstrap.servers`, `security.protocol`,
  `topicName`, `classification`, and `delimiter`. Another supported option is `catalogPartitionPredicate`:

`catalogPartitionPredicate` — You can pass a catalog expression to filter based on the index columns. This pushes down the filtering to the server side. For more information, see [AWS Glue Partition Indexes](partition-indexes.md "partition-indexes.md"). Note that `push_down_predicate` and `catalogPartitionPredicate` use different syntaxes. The former one uses Spark SQL standard syntax and the later one uses JSQL parser.

- `catalog_id` — The catalog ID (account ID) of the Data Catalog being accessed. When None, the default account ID of the caller is used.

## create_dynamic_frame_from_options

###### `create_dynamic_frame_from_options(connection_type, connection_options={},

format=None, format_options={}, transformation_ctx = "")`

Returns a `DynamicFrame` created with the specified connection and
format.

- `connection_type` – The connection type, such as Amazon S3, Amazon Redshift, and JDBC.
  Valid values include `s3`, `mysql`, `postgresql`, `redshift`, `sqlserver`, `oracle`, and `dynamodb`.
- `connection_options` – Connection options, such as paths and database table
  (optional). For a `connection_type` of `s3`, a list of Amazon S3 paths is
  defined.

```
connection_options = {"paths": ["`s3://aws-glue-target/temp`"]}
```

For JDBC connections, several properties must be defined. Note that the database name must be part of the URL. It can optionally be included in the connection options.

###### Warning

Storing passwords in your script is not recommended. Consider using `boto3` to retrieve them from AWS Secrets Manager or the AWS Glue Data Catalog.

```
connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`"}
```

The `dbtable` property is the name of the JDBC table. For JDBC data stores that support schemas within a database, specify `schema.table-name`. If a schema is not provided, then the default "public" schema is used.

For more information, see [Connection types and options for ETL in
AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").

- `format` – A format specification. This is used for an Amazon S3 or an
  AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are
  supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – The transformation context to use (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset. For supported sources and limitations, see [Optimizing reads with pushdown in AWS Glue ETL](aws-glue-programming-pushdown.md "aws-glue-programming-pushdown.md"). For more information, see [Pre-Filtering Using Pushdown Predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").

## create_sample_dynamic_frame_from_catalog

###### `create_sample_dynamic_frame_from_catalog(database, table_name, num, redshift_tmp_dir, transformation_ctx = "", push_down_predicate= "", additional_options = {}, sample_options = {}, catalog_id = None)`

Returns a sample `DynamicFrame` that is created using a Data Catalog database and table name. The `DynamicFrame` only contains first `num` records from a datasource.

- `database` – The database to read from.
- `table_name` – The name of the table to read from.
- `num` – The maximum number of records in the returned sample dynamic frame.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – The transformation context to use
  (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset.
  For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").
- `additional_options` – A collection of optional name-value pairs. The
  possible options include those listed in [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") except for `endpointUrl`,
  `streamName`, `bootstrap.servers`, `security.protocol`,
  `topicName`, `classification`, and `delimiter`.
- `sample_options` – Parameters to control sampling behavior (optional). Current available parameters for Amazon S3 sources:
  - `maxSamplePartitions` – The maximum number of partitions the sampling will read. Default value is 10
  - `maxSampleFilesPerPartition` – The maximum number of files the sampling will read in one partition. Default value is 10.

  These parameters help to reduce the time consumed by file listing. For example, suppose the dataset has 1000 partitions, and each partition has 10 files. If you set `maxSamplePartitions` = 10, and `maxSampleFilesPerPartition` = 10, instead of listing all 10,000 files, the sampling will only list and read the first 10 partitions with the first 10 files in each: 10\*10 = 100 files in total.

- `catalog_id` – The catalog ID of the Data Catalog being accessed (the
  account ID of the Data Catalog). Set to `None` by default. `None`
  defaults to the catalog ID of the calling account in the service.

## create_sample_dynamic_frame_from_options

###### `create_sample_dynamic_frame_from_options(connection_type, connection_options={}, num, sample_options={}, format=None, format_options={}, transformation_ctx = "")`

Returns a sample `DynamicFrame` created with the specified connection and format. The `DynamicFrame` only contains first `num` records from a datasource.

- `connection_type` – The connection type, such as Amazon S3, Amazon Redshift, and JDBC.
  Valid values include `s3`, `mysql`, `postgresql`, `redshift`, `sqlserver`, `oracle`, and `dynamodb`.
- `connection_options` – Connection options, such as paths and database table
  (optional). For more information, see [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `num` – The maximum number of records in the returned sample dynamic frame.
- `sample_options` – Parameters to control sampling behavior (optional). Current available parameters for Amazon S3 sources:
  - `maxSamplePartitions` – The maximum number of partitions the sampling will read. Default value is 10
  - `maxSampleFilesPerPartition` – The maximum number of files the sampling will read in one partition. Default value is 10.

  These parameters help to reduce the time consumed by file listing. For example, suppose the dataset has 1000 partitions, and each partition has 10 files. If you set `maxSamplePartitions` = 10, and `maxSampleFilesPerPartition` = 10, instead of listing all 10,000 files, the sampling will only list and read the first 10 partitions with the first 10 files in each: 10\*10 = 100 files in total.

- `format` – A format specification. This is used for an Amazon S3 or an
  AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are
  supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – The transformation context to use
  (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset.
  For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").

## add_ingestion_time_columns

###### `add_ingestion_time_columns(dataFrame, timeGranularity = "")`

Appends ingestion time columns like `ingest_year`, `ingest_month`,
`ingest_day`, `ingest_hour`, `ingest_minute` to the input
`DataFrame`. This function is automatically generated in the script generated
by the AWS Glue when you specify a Data Catalog table with Amazon S3 as the target. This
function automatically updates the partition with ingestion time columns on the output
table. This allows the output data to be automatically partitioned on ingestion time without
requiring explicit ingestion time columns in the input data.

- `dataFrame` – The `dataFrame` to append the ingestion time
  columns to.
- `timeGranularity` – The granularity of the time columns. Valid values
  are "`day`", "`hour`" and "`minute`". For example, if
  "`hour`" is passed in to the function, the original `dataFrame`
  will have "`ingest_year`", "`ingest_month`",
  "`ingest_day`", and "`ingest_hour`" time columns appended.

Returns the data frame after appending the time granularity columns.

Example:

```
dynamic_frame = DynamicFrame.fromDF(glueContext.add_ingestion_time_columns(dataFrame, "hour"))
```

## create_data_frame_from_catalog

###### `create_data_frame_from_catalog(database, table_name, transformation_ctx = "",

additional_options = {})`

Returns a `DataFrame` that is created using information from a Data Catalog
table.

- `database` – The Data Catalog database to read from.
- `table_name` – The name of the Data Catalog table to read from.
- `transformation_ctx` – The transformation context to use
  (optional).
- `additional_options` – A collection of optional name-value pairs. The
  possible options include those listed in [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") for streaming sources, such as
  `startingPosition`, `maxFetchTimeInMs`, and
  `startingOffsets`.
  - `useSparkDataSource`
    – When set to true, forces AWS Glue to use the native Spark Data Source API to read
    the table. The Spark Data Source API supports the following formats: AVRO, binary,
    CSV, JSON, ORC, Parquet, and text. In a Data Catalog table, you specify the format using
    the `classification` property. To learn more about the Spark Data Source
    API, see the official [Apache Spark documentation](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html "https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html").

  Using `create_data_frame_from_catalog` with
  `useSparkDataSource` has the following benefits:

      - Directly returns a `DataFrame` and provides an alternative to
       `create_dynamic_frame.from_catalog().toDF()`.
      - Supports AWS Lake Formation table-level permission control for native formats.
      - Supports reading data lake formats without AWS Lake Formation table-level permission
       control. For more information, see [Using data lake
       frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

  When you enable `useSparkDataSource`, you can also add any of the
  [Spark Data
  Source options](https://spark.apache.org/docs/latest/sql-data-sources.html "https://spark.apache.org/docs/latest/sql-data-sources.html") in `additional_options` as needed. AWS Glue passes
  these options directly to the Spark reader.
  - `useCatalogSchema` – When set to true, AWS Glue applies the Data Catalog
    schema to the resulting `DataFrame`. Otherwise, the reader infers the
    schema from the data. When you enable `useCatalogSchema`, you must also set
    `useSparkDataSource` to true.

**Limitations**

Consider the following limitations when you use the `useSparkDataSource`
option:

- When you use `useSparkDataSource`, AWS Glue creates a new
  `DataFrame` in a separate Spark session that is different from the original
  Spark session.
- Spark DataFrame partition filtering doesn't work with the following AWS Glue features.

      + [Job bookmarks](monitor-continuations.md "monitor-continuations.md")
      + [Excluding Amazon S3 storage classes](aws-glue-programming-etl-storage-classes.md#aws-glue-programming-etl-storage-classes-dynamic-frame "aws-glue-programming-etl-storage-classes.md#aws-glue-programming-etl-storage-classes-dynamic-frame")
      + [Catalog partition predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates")

  To use partition filtering with these features, you can use the AWS Glue pushdown
  predicate. For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns"). Filtering on
  non-partitioned columns is not affected.

The following example script demonstrates the incorrect way to perform partition
filtering with the `excludeStorageClasses` option.

```
// Incorrect partition filtering using Spark filter with excludeStorageClasses
read_df = glueContext.create_data_frame.from_catalog(
    database=database_name,
    table_name=table_name,
    additional_options = {
      "useSparkDataSource": True,
      "excludeStorageClasses" : ["GLACIER", "DEEP_ARCHIVE"]
    }
)

//  Suppose year and month are partition keys.
//  Filtering on year and month won't work, the filtered_df will still
//  contain data with other year/month values.
filtered_df = read_df.filter("year == '2017 and month == '04' and 'state == 'CA'")
```

The following example script demonstrates the correct way to use a pushdown predicate
in order to perform partition filtering with the `excludeStorageClasses`
option.

```
// Correct partition filtering using the AWS Glue pushdown predicate
// with excludeStorageClasses
read_df = glueContext.create_data_frame.from_catalog(
    database=database_name,
    table_name=table_name,
    //  Use AWS Glue pushdown predicate to perform partition filtering
    push_down_predicate = "(year=='2017' and month=='04')"
    additional_options = {
      "useSparkDataSource": True,
      "excludeStorageClasses" : ["GLACIER", "DEEP_ARCHIVE"]
    }
)

//  Use Spark filter only on non-partitioned columns
filtered_df = read_df.filter("state == 'CA'")
```

**Example: Creating a CSV table using the Spark data source
reader**

```
//  Read a CSV table with '\t' as separator
read_df = glueContext.create_data_frame.from_catalog(
    database=`<database_name>`,
    table_name=`<table_name>`,
    additional_options = {"useSparkDataSource": True,  "sep": '\t'}
)
```

## create_data_frame_from_options

###### `create_data_frame_from_options(connection_type, connection_options={},

format=None, format_options={}, transformation_ctx = "")`

This API is now deprecated. Instead use the `getSource()` API. Returns a `DataFrame` created with the specified connection and format. Use
this function only with AWS Glue streaming sources.

- `connection_type` – The streaming connection type. Valid values
  include `kinesis` and `kafka`.
- `connection_options` – Connection options, which are different for
  Kinesis and Kafka. You can find the list of all connection options for each streaming data
  source at [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md"). Note the following differences in
  streaming connection options:
  - Kinesis streaming sources require `streamARN`,
    `startingPosition`, `inferSchema`, and
    `classification`.
  - Kafka streaming sources require `connectionName`,
    `topicName`, `startingOffsets`, `inferSchema`, and
    `classification`.

- `format` – A format specification. This is used for an
  Amazon S3 or an AWS Glue connection that supports multiple formats. For information about the
  supported formats, see [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").
- `format_options` – Format options for the specified format. For
  information about the supported format options, see [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").
- `transformation_ctx` – The transformation context to use
  (optional).

Example for Amazon Kinesis streaming source:

```
kinesis_options =
   { "streamARN": "arn:aws:kinesis:us-east-2:777788889999:stream/fromOptionsStream",
     "startingPosition": "TRIM_HORIZON",
     "inferSchema": "true",
     "classification": "json"
   }
data_frame_datasource0 = glueContext.create_data_frame.from_options(connection_type="kinesis", connection_options=kinesis_options)
```

Example for Kafka streaming source:

```
kafka_options =
    { "connectionName": "ConfluentKafka",
      "topicName": "kafka-auth-topic",
      "startingOffsets": "earliest",
      "inferSchema": "true",
      "classification": "json"
    }
data_frame_datasource0 = glueContext.create_data_frame.from_options(connection_type="kafka", connection_options=kafka_options)
```

## forEachBatch

###### `forEachBatch(frame, batch_function, options)`

Applies the `batch_function` passed in to every micro batch that is read from
the Streaming source.

- `frame` – The DataFrame containing the current micro batch.
- `batch_function` – A function that will be applied for every micro
  batch.
- `options` – A collection of key-value pairs that holds information
  about how to process micro batches. The following options are required:
  - `windowSize` – The amount of time to spend processing each
    batch.
  - `checkpointLocation` – The location where checkpoints are stored
    for the streaming ETL job.
  - `batchMaxRetries` – The maximum number of times to retry the batch if it fails. The default value is 3. This option is only configurable for Glue version 2.0 and above.

**Example:**

```
glueContext.forEachBatch(
    frame = data_frame_datasource0,
    batch_function = processBatch,
    options = {
        "windowSize": "100 seconds",
        "checkpointLocation": "s3://kafka-auth-dataplane/confluent-test/output/checkpoint/"
    }
)

def processBatch(data_frame, batchId):
    if (data_frame.count() > 0):
        datasource0 = DynamicFrame.fromDF(
          glueContext.add_ingestion_time_columns(data_frame, "hour"),
          glueContext, "from_data_frame"
        )
        additionalOptions_datasink1 = {"enableUpdateCatalog": True}
        additionalOptions_datasink1["partitionKeys"] = ["ingest_yr", "ingest_mo", "ingest_day"]
        datasink1 = glueContext.write_dynamic_frame.from_catalog(
          frame = datasource0,
          database = "tempdb",
          table_name = "kafka-auth-table-output",
          transformation_ctx = "datasink1",
          additional_options = additionalOptions_datasink1
        )

```

## Working with datasets in Amazon S3

- [purge_table](#aws-glue-api-crawler-pyspark-extensions-glue-context-purge_table "#aws-glue-api-crawler-pyspark-extensions-glue-context-purge_table")
- [purge_s3_path](#aws-glue-api-crawler-pyspark-extensions-glue-context-purge_s3_path "#aws-glue-api-crawler-pyspark-extensions-glue-context-purge_s3_path")
- [transition_table](#aws-glue-api-crawler-pyspark-extensions-glue-context-transition_table "#aws-glue-api-crawler-pyspark-extensions-glue-context-transition_table")
- [transition_s3_path](#aws-glue-api-crawler-pyspark-extensions-glue-context-transition_s3_path "#aws-glue-api-crawler-pyspark-extensions-glue-context-transition_s3_path")

## purge_table

###### `purge_table(catalog_id=None, database="", table_name="", options={},

transformation_ctx="")`

Deletes files from Amazon S3 for the specified catalog's database and table. If all files in
a partition are deleted, that partition is also deleted from the catalog. We don't support purge_table action on tables registered with Lake Formation.

If you want to be able to recover deleted objects, you can turn on [object
versioning](../../../AmazonS3/latest/dev/ObjectVersioning.md "../../../AmazonS3/latest/dev/ObjectVersioning.md") on the Amazon S3 bucket. When an object is deleted from a bucket that
doesn't have object versioning enabled, the object can't be recovered. For more information
about how to recover deleted objects in a version-enabled bucket, see [How can I retrieve an Amazon S3 object that was deleted?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-undelete-configuration/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-undelete-configuration/") in the AWS Support
Knowledge Center.

- `catalog_id` – The catalog ID of the Data Catalog being accessed (the
  account ID of the Data Catalog). Set to `None` by default. `None`
  defaults to the catalog ID of the calling account in the service.
- `database` – The database to use.
- `table_name` – The name of the table to use.
- `options` – Options to filter files to be deleted and for manifest file generation.
  - `retentionPeriod` – Specifies a period in number of hours to retain files.
    Files newer than the retention period are retained. Set to 168 hours (7 days) by
    default.
  - `partitionPredicate` – Partitions satisfying this predicate are deleted.
    Files within the retention period in these partitions are not deleted. Set to
    `""` – empty by default.
  - `excludeStorageClasses` – Files with storage class in the
    `excludeStorageClasses` set are not deleted. The default is
    `Set()` – an empty set.
  - `manifestFilePath` – An optional path for manifest file generation. All files
    that were successfully purged are recorded in `Success.csv`, and those that
    failed in `Failed.csv`

- `transformation_ctx` – The transformation context to use (optional). Used in the manifest file path.

```
glueContext.purge_table("database", "table", {"partitionPredicate": "(month=='march')", "retentionPeriod": 1, "excludeStorageClasses": ["STANDARD_IA"], "manifestFilePath": "s3://bucketmanifest/"})
```

## purge_s3_path

###### `purge_s3_path(s3_path, options={}, transformation_ctx="")`

Deletes files from the specified Amazon S3 path recursively.

If you want to be able to recover
deleted objects, you can turn on [object
versioning](../../../AmazonS3/latest/dev/ObjectVersioning.md "../../../AmazonS3/latest/dev/ObjectVersioning.md") on the Amazon S3 bucket. When an object is deleted
from a bucket that doesn't have object versioning turned on, the
object can't be recovered. For more information about how
to recover deleted objects in a bucket with versioning, see
[How can I retrieve an Amazon S3 object that was deleted?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-undelete-configuration/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-undelete-configuration/") in
the Support Knowledge Center.

- `s3_path` – The path in Amazon S3 of the files to be deleted in the format `s3://<`bucket`>/<`prefix`>/`
- `options` – Options to filter files to be deleted and for manifest file generation.
  - `retentionPeriod` – Specifies a period in number of hours to retain files.
    Files newer than the retention period are retained. Set to 168 hours (7 days) by
    default.
  - `excludeStorageClasses` – Files with storage class in the
    `excludeStorageClasses` set are not deleted. The default is
    `Set()` – an empty set.
  - `manifestFilePath` – An optional path for manifest file generation. All files
    that were successfully purged are recorded in `Success.csv`, and those that
    failed in `Failed.csv`

- `transformation_ctx` – The transformation context to use (optional). Used in the manifest file path.

```
glueContext.purge_s3_path("s3://bucket/path/", {"retentionPeriod": 1, "excludeStorageClasses": ["STANDARD_IA"], "manifestFilePath": "s3://bucketmanifest/"})
```

## transition_table

###### `transition_table(database, table_name, transition_to, options={}, transformation_ctx="", catalog_id=None)`

Transitions the storage class of the files stored on Amazon S3 for the specified catalog's database and table.

You can transition between any two storage classes. For the `GLACIER` and `DEEP_ARCHIVE` storage classes, you can transition to these classes. However, you would use an `S3 RESTORE` to transition from `GLACIER` and `DEEP_ARCHIVE` storage classes.

If you're running AWS Glue ETL jobs that read files or partitions from Amazon S3, you can exclude
some Amazon S3 storage class types. For more information, see [Excluding Amazon S3 Storage
Classes](aws-glue-programming-etl-storage-classes.md "aws-glue-programming-etl-storage-classes.md").

- `database` – The database to use.
- `table_name` – The name of the table to use.
- `transition_to` – The [Amazon S3 storage class](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/StorageClass.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/StorageClass.md") to transition to.
- `options` – Options to filter files to be deleted and for manifest file generation.
  - `retentionPeriod` – Specifies a period in number of hours to retain files.
    Files newer than the retention period are retained. Set to 168 hours (7 days) by
    default.
  - `partitionPredicate` – Partitions satisfying this predicate are transitioned.
    Files within the retention period in these partitions are not transitioned. Set to
    `""` – empty by default.
  - `excludeStorageClasses` – Files with storage class in the `excludeStorageClasses` set are not transitioned. The default is `Set()` – an empty set.
  - `manifestFilePath` – An optional path for manifest file generation. All files
    that were successfully transitioned are recorded in `Success.csv`, and
    those that failed in `Failed.csv`
  - `accountId` – The Amazon Web Services account ID to run the transition transform. Mandatory for this transform.
  - `roleArn` – The AWS role to run the transition transform. Mandatory for this transform.

- `transformation_ctx` – The transformation context to use (optional). Used in the manifest file path.
- `catalog_id` – The catalog ID of the Data Catalog being accessed (the account ID of the Data Catalog). Set to `None` by default. `None` defaults to the catalog ID of the calling account in the service.

```
glueContext.transition_table("database", "table", "STANDARD_IA", {"retentionPeriod": 1, "excludeStorageClasses": ["STANDARD_IA"], "manifestFilePath": "s3://bucketmanifest/", "accountId": "12345678901", "roleArn": "arn:aws:iam::123456789012:user/example-username"})
```

## transition_s3_path

###### `transition_s3_path(s3_path, transition_to, options={}, transformation_ctx="")`

Transitions the storage class of the files in the specified Amazon S3 path
recursively.

You can transition between any two storage classes. For the `GLACIER` and `DEEP_ARCHIVE` storage classes, you can transition to these classes. However, you would use an `S3 RESTORE` to transition from `GLACIER` and `DEEP_ARCHIVE` storage classes.

If you're running AWS Glue ETL jobs that read files or partitions from Amazon S3, you can exclude
some Amazon S3 storage class types. For more information, see [Excluding Amazon S3 Storage
Classes](aws-glue-programming-etl-storage-classes.md "aws-glue-programming-etl-storage-classes.md").

- `s3_path` – The path in Amazon S3 of the files to be transitioned in the format `s3://<`bucket`>/<`prefix`>/`
- `transition_to` – The [Amazon S3 storage class](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/StorageClass.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/StorageClass.md") to transition to.
- `options` – Options to filter files to be deleted and for manifest file generation.
  - `retentionPeriod` – Specifies a period in number of hours to retain files.
    Files newer than the retention period are retained. Set to 168 hours (7 days) by
    default.
  - `partitionPredicate` – Partitions satisfying this predicate are transitioned.
    Files within the retention period in these partitions are not transitioned. Set to
    `""` – empty by default.
  - `excludeStorageClasses` – Files with storage class in the `excludeStorageClasses` set are not transitioned. The default is `Set()` – an empty set.
  - `manifestFilePath` – An optional path for manifest file generation. All files
    that were successfully transitioned are recorded in `Success.csv`, and
    those that failed in `Failed.csv`
  - `accountId` – The Amazon Web Services account ID to run the transition transform. Mandatory for this transform.
  - `roleArn` – The AWS role to run the transition transform. Mandatory for this transform.

- `transformation_ctx` – The transformation context to use (optional). Used in the manifest file path.

```
glueContext.transition_s3_path("s3://bucket/prefix/", "STANDARD_IA", {"retentionPeriod": 1, "excludeStorageClasses": ["STANDARD_IA"], "manifestFilePath": "s3://bucketmanifest/", "accountId": "12345678901", "roleArn": "arn:aws:iam::123456789012:user/example-username"})
```

## Extracting

- [extract_jdbc_conf](#aws-glue-api-crawler-pyspark-extensions-glue-context-extract_jdbc_conf "#aws-glue-api-crawler-pyspark-extensions-glue-context-extract_jdbc_conf")

## extract_jdbc_conf

###### `extract_jdbc_conf(connection_name, catalog_id = None)`

Returns a `dict` with keys with the configuration properties from the AWS Glue connection object in the Data Catalog.

- `user` – The database user name.
- `password` – The database password.
- `vendor` – Specifies a vendor (`mysql`, `postgresql`, `oracle`, `sqlserver`, etc.).
- `enforceSSL` – A boolean string indicating if a secure connection is required.
- `customJDBCCert` – Use a specific client certificate from the Amazon S3 path indicated.
- `skipCustomJDBCCertValidation` – A boolean string indicating if the `customJDBCCert` must be validated by a CA.
- `customJDBCCertString` – Additional information about the custom certificate, specific for the driver type.
- `url` – (Deprecated) JDBC URL with only protocol, server and port.
- `fullUrl` – JDBC URL as entered when the connection was created (Available in AWS Glue version 3.0 or later).

Example retrieving JDBC configurations:

```
jdbc_conf = glueContext.extract_jdbc_conf(connection_name="your_glue_connection_name")
print(jdbc_conf)
>>> {'enforceSSL': 'false', 'skipCustomJDBCCertValidation': 'false', 'url': 'jdbc:mysql://myserver:3306', 'fullUrl': 'jdbc:mysql://myserver:3306/mydb', 'customJDBCCertString': '', 'user': 'admin', 'customJDBCCert': '', 'password': '1234', 'vendor': 'mysql'}
```

## Transactions

- [start_transaction](#aws-glue-api-pyspark-extensions-glue-context-start-transaction "#aws-glue-api-pyspark-extensions-glue-context-start-transaction")
- [commit_transaction](#aws-glue-api-pyspark-extensions-glue-context-commit-transaction "#aws-glue-api-pyspark-extensions-glue-context-commit-transaction")
- [cancel_transaction](#aws-glue-api-pyspark-extensions-glue-cancel-transaction "#aws-glue-api-pyspark-extensions-glue-cancel-transaction")

## start_transaction

###### `start_transaction(read_only)`

Start a new transaction. Internally calls the Lake Formation [startTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-StartTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-StartTransaction") API.

- `read_only` – (Boolean) Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed.

Returns the transaction ID.

## commit_transaction

###### `commit_transaction(transaction_id, wait_for_commit = True)`

Attempts to commit the specified transaction. `commit_transaction` may return before the transaction has finished committing. Internally calls the Lake Formation [commitTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CommitTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CommitTransaction") API.

- `transaction_id` – (String) The transaction to commit.
- `wait_for_commit` – (Boolean) Determines whether the `commit_transaction` returns immediately. The default value is true. If false, `commit_transaction` polls and waits until the transaction is committed. The amount of wait time is restricted to 1 minute using exponential backoff with a maximum of 6 retry attempts.

Returns a Boolean to indicate whether the commit is done or not.

## cancel_transaction

###### `cancel_transaction(transaction_id)`

Attempts to cancel the specified transaction. Returns a `TransactionCommittedException` exception if the transaction was previously committed. Internally calls the Lake Formation [CancelTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CancelTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CancelTransaction") API.

- `transaction_id` – (String) The transaction to cancel.

## Writing

- [getSink](#aws-glue-api-crawler-pyspark-extensions-glue-context-get-sink "#aws-glue-api-crawler-pyspark-extensions-glue-context-get-sink")
- [write_dynamic_frame_from_options](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_options")
- [write_from_options](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_from_options "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_from_options")
- [write_dynamic_frame_from_catalog](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_catalog "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_catalog")
- [write_data_frame_from_catalog](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_data_frame_from_catalog "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_data_frame_from_catalog")
- [write_dynamic_frame_from_jdbc_conf](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_jdbc_conf "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_dynamic_frame_from_jdbc_conf")
- [write_from_jdbc_conf](#aws-glue-api-crawler-pyspark-extensions-glue-context-write_from_jdbc_conf "#aws-glue-api-crawler-pyspark-extensions-glue-context-write_from_jdbc_conf")

## getSink

###### `getSink(connection_type, format = None, transformation_ctx = "", **options)`

Gets a `DataSink` object that can be used to write `DynamicFrames`
to external sources. Check the SparkSQL `format` first to be sure to get the expected sink.

- `connection_type` – The connection type to use, such as Amazon S3, Amazon Redshift, and JDBC.
  Valid values include `s3`, `mysql`, `postgresql`,
  `redshift`, `sqlserver`, `oracle`, `kinesis`, and
  `kafka`.
- `format` – The SparkSQL format to use (optional).
- `transformation_ctx` – The transformation context to use (optional).
- `options` – A collection of name-value pairs used to specify the connection
  options. Some of the possible values are:
  - `user` and `password`: For authorization
  - `url`: The endpoint for the data store
  - `dbtable`: The name of the target table
  - `bulkSize`: Degree of parallelism for insert operations

The options that you can specify depends on the connection type. See [Connection types and options for ETL in
AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") for additional values and examples.

Example:

```
>>> data_sink = context.getSink("s3")
>>> data_sink.setFormat("json"),
>>> data_sink.writeFrame(myFrame)

```

## write_dynamic_frame_from_options

###### `write_dynamic_frame_from_options(frame, connection_type, connection_options={}, format=None,

format_options={}, transformation_ctx = "")`

Writes and returns a `DynamicFrame` using the specified connection and
format.

- `frame` – The `DynamicFrame` to write.
- `connection_type` – The connection type, such as Amazon S3, Amazon Redshift, and JDBC. Valid
  values include `s3`, `mysql`, `postgresql`,
  `redshift`, `sqlserver`, `oracle`, `kinesis`, and
  `kafka`.
- `connection_options` – Connection options, such as path and database table
  (optional).
  For a `connection_type` of `s3`, an Amazon S3 path is defined.

```
connection_options = {"path": "`s3://aws-glue-target/temp`"}
```

For JDBC connections, several properties must be defined. Note that the database name must be part of the URL. It can optionally be included in the connection options.

###### Warning

Storing passwords in your script is not recommended. Consider using `boto3` to retrieve them from AWS Secrets Manager or the AWS Glue Data Catalog.

```
connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`"}
```

The `dbtable` property is the name of the JDBC table. For JDBC data stores that support schemas within a database, specify `schema.table-name`. If a schema is not provided, then the default "public" schema is used.

For more information, see [Connection types and options for ETL in
AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").

- `format` – A format specification. This is used for an Amazon S3 or an
  AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are
  supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – A transformation context to use (optional).

## write_from_options

###### `write_from_options(frame_or_dfc, connection_type,

connection_options={}, format={}, format_options={}, transformation_ctx = "")`

Writes and returns a `DynamicFrame` or `DynamicFrameCollection`
that is created with the specified connection and format information.

- `frame_or_dfc` – The `DynamicFrame` or
  `DynamicFrameCollection` to write.
- `connection_type` – The connection type, such as Amazon S3, Amazon Redshift, and JDBC.
  Valid values include `s3`, `mysql`, `postgresql`, `redshift`, `sqlserver`, and `oracle`.
- `connection_options` – Connection options, such as path and database table
  (optional).
  For a `connection_type` of `s3`, an Amazon S3 path is defined.

```
connection_options = {"path": "`s3://aws-glue-target/temp`"}
```

For JDBC connections, several properties must be defined. Note that the database name must be part of the URL. It can optionally be included in the connection options.

###### Warning

Storing passwords in your script is not recommended. Consider using `boto3` to retrieve them from AWS Secrets Manager or the AWS Glue Data Catalog.

```
connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`"}
```

The `dbtable` property is the name of the JDBC table. For JDBC data stores that support schemas within a database, specify `schema.table-name`. If a schema is not provided, then the default "public" schema is used.

For more information, see [Connection types and options for ETL in
AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").

- `format` – A format specification. This is used for an Amazon S3 or an
  AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") for the formats that are
  supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – A transformation context to use (optional).

## write_dynamic_frame_from_catalog

###### `write_dynamic_frame_from_catalog(frame, database, table_name, redshift_tmp_dir, transformation_ctx = "", additional_options = {}, catalog_id = None)`

Writes and returns a `DynamicFrame` using information from a Data Catalog database
and table.

- `frame` – The `DynamicFrame` to write.
- `Database` – The Data Catalog database that contains the table.
- `table_name` – The name of the Data Catalog table associated with the
  target.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – The transformation context to use (optional).
- `additional_options` – A collection of optional name-value
  pairs.
- `catalog_id` — The catalog ID (account ID) of the Data Catalog being accessed. When None, the default account ID of the caller is used.

## write_data_frame_from_catalog

###### `write_data_frame_from_catalog(frame, database, table_name, redshift_tmp_dir,

transformation_ctx = "", additional_options = {}, catalog_id = None)`

Writes and returns a `DataFrame` using information from a Data Catalog database
and table. This method supports writing to data lake formats (Hudi, Iceberg, and Delta
Lake). For more information, see [Using data lake
frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

- `frame` – The `DataFrame` to write.
- `Database` – The Data Catalog database that contains the table.
- `table_name` – The name of the Data Catalog table that is associated with the
  target.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – The transformation context to use (optional).
- `additional_options` – A collection of optional name-value
  pairs.
  - `useSparkDataSink` – When set to true, forces AWS Glue to use the
    native Spark Data Sink API to write to the table. When you enable this option, you can
    add any [Spark
    Data Source options](https://spark.apache.org/docs/latest/sql-data-sources.html "https://spark.apache.org/docs/latest/sql-data-sources.html") to `additional_options` as needed. AWS Glue
    passes these options directly to the Spark writer.

- `catalog_id` – The catalog ID (account ID) of the Data Catalog being accessed.
  When you don't specify a value, the default account ID of the caller is used.

**Limitations**

Consider the following limitations when you use the `useSparkDataSink`
option:

- The [enableUpdateCatalog](update-from-job.md "update-from-job.md") option isn't supported when you use
  the `useSparkDataSink` option.

**Example: Writing to a Hudi table using the Spark Data Source
writer**

```
hudi_options = {
    'useSparkDataSink': True,
    'hoodie.table.name': `<table_name>`,
    'hoodie.datasource.write.storage.type': 'COPY_ON_WRITE',
    'hoodie.datasource.write.recordkey.field': 'product_id',
    'hoodie.datasource.write.table.name': `<table_name>`,
    'hoodie.datasource.write.operation': 'upsert',
    'hoodie.datasource.write.precombine.field': 'updated_at',
    'hoodie.datasource.write.hive_style_partitioning': 'true',
    'hoodie.upsert.shuffle.parallelism': 2,
    'hoodie.insert.shuffle.parallelism': 2,
    'hoodie.datasource.hive_sync.enable': 'true',
    'hoodie.datasource.hive_sync.database': `<database_name>`,
    'hoodie.datasource.hive_sync.table': `<table_name>`,
    'hoodie.datasource.hive_sync.use_jdbc': 'false',
    'hoodie.datasource.hive_sync.mode': 'hms'}

glueContext.write_data_frame.from_catalog(
    frame = `<df_product_inserts>`,
    database = `<database_name>`,
    table_name = `<table_name>`,
    additional_options = hudi_options
)
```

## write_dynamic_frame_from_jdbc_conf

###### `write_dynamic_frame_from_jdbc_conf(frame, catalog_connection, connection_options={},

redshift_tmp_dir = "", transformation_ctx = "", catalog_id = None)`

Writes and returns a `DynamicFrame` using the specified JDBC connection
information.

- `frame` – The `DynamicFrame` to write.
- `catalog_connection` – A catalog connection to use.
- `connection_options` – Connection options, such as path and database table
  (optional). For more information, see [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – A transformation context to use (optional).
- `catalog_id` — The catalog ID (account ID) of the Data Catalog being accessed. When None, the default account ID of the caller is used.

## write_from_jdbc_conf

###### `write_from_jdbc_conf(frame_or_dfc, catalog_connection, connection_options={}, redshift_tmp_dir = "", transformation_ctx = "", catalog_id = None)`

Writes and returns a `DynamicFrame` or `DynamicFrameCollection`
using the specified JDBC connection information.

- `frame_or_dfc` – The `DynamicFrame` or
  `DynamicFrameCollection` to write.
- `catalog_connection` – A catalog connection to use.
- `connection_options` – Connection options, such as path and database table
  (optional). For more information, see [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – A transformation context to use (optional).
- `catalog_id` — The catalog ID (account ID) of the Data Catalog being accessed. When None, the default account ID of the caller is used.

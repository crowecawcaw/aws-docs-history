# AWS Glue Scala GlueContext APIs

**Package: com.amazonaws.services.glue**

```
class GlueContext extends SQLContext(sc) (
           @transient val sc : SparkContext,
           val defaultSourcePartitioner : PartitioningStrategy )
```

`GlueContext` is the entry point for reading and writing a [DynamicFrame](glue-etl-scala-apis-glue-dynamicframe.md "glue-etl-scala-apis-glue-dynamicframe.md") from and to Amazon Simple Storage Service (Amazon S3), the
AWS Glue Data Catalog, JDBC, and so on. This class provides utility functions to create [DataSource trait](glue-etl-scala-apis-glue-datasource-trait.md "glue-etl-scala-apis-glue-datasource-trait.md") and [DataSink](glue-etl-scala-apis-glue-datasink-class.md "glue-etl-scala-apis-glue-datasink-class.md") objects that can in turn be
used to read and write `DynamicFrame`s.

You can also use `GlueContext` to set a target number of partitions (default 20)
in the `DynamicFrame` if the number of partitions created from the source is less
than a minimum threshold for partitions (default 10).

## def addIngestionTimeColumns

```
def addIngestionTimeColumns(
         df : DataFrame,
         timeGranularity : String = "") : dataFrame
```

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
glueContext.addIngestionTimeColumns(dataFrame, "hour")
```

## def createDataFrameFromOptions

```
def createDataFrameFromOptions( connectionType : String,
                         connectionOptions : JsonOptions,
                         transformationContext : String = "",
                         format : String = null,
                         formatOptions : JsonOptions = JsonOptions.empty
                       ) : DataSource
```

Returns a `DataFrame` created with the specified connection and format. Use this function only with AWS Glue streaming sources.

- `connectionType` – The streaming connection type. Valid values include `kinesis` and `kafka`.
- `connectionOptions` – Connection options, which are different for
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

- `transformationContext` – The transformation context to use (optional).
- `format` – A format specification (optional). This is used for an
  Amazon S3 or an AWS Glue connection that supports multiple formats. For information about the
  supported formats, see [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
- `formatOptions` – Format options for the specified format. For information about the supported format options, see [Data format options](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").

Example for Amazon Kinesis streaming source:

```
val data_frame_datasource0 =
glueContext.createDataFrameFromOptions(transformationContext = "datasource0", connectionType = "kinesis",
connectionOptions = JsonOptions("""{"streamName": "example_stream", "startingPosition": "TRIM_HORIZON", "inferSchema": "true", "classification": "json"}}"""))
```

Example for Kafka streaming source:

```
val data_frame_datasource0 =
glueContext.createDataFrameFromOptions(transformationContext = "datasource0", connectionType = "kafka",
connectionOptions = JsonOptions("""{"connectionName": "example_connection", "topicName": "example_topic", "startingPosition": "earliest", "inferSchema": "false", "classification": "json", "schema":"`column1` STRING, `column2` STRING"}"""))
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
glueContext.forEachBatch(data_frame_datasource0, (dataFrame: Dataset[Row], batchId: Long) =>
   {
      if (dataFrame.count() > 0)
        {
          val datasource0 = DynamicFrame(glueContext.addIngestionTimeColumns(dataFrame, "hour"), glueContext)
          // @type: DataSink
          // @args: [database = "tempdb", table_name = "fromoptionsoutput", stream_batch_time = "100 seconds",
          //      stream_checkpoint_location = "s3://from-options-testing-eu-central-1/fromOptionsOutput/checkpoint/",
          //      transformation_ctx = "datasink1"]
          // @return: datasink1
          // @inputs: [frame = datasource0]
          val options_datasink1 = JsonOptions(
             Map("partitionKeys" -> Seq("ingest_year", "ingest_month","ingest_day", "ingest_hour"),
             "enableUpdateCatalog" -> true))
          val datasink1 = glueContext.getCatalogSink(
             database = "tempdb",
             tableName = "fromoptionsoutput",
             redshiftTmpDir = "",
             transformationContext = "datasink1",
             additionalOptions = options_datasink1).writeDynamicFrame(datasource0)
        }
   }, JsonOptions("""{"windowSize" : "100 seconds",
         "checkpointLocation" : "s3://from-options-testing-eu-central-1/fromOptionsOutput/checkpoint/"}"""))
```

## def getCatalogSink

```
def getCatalogSink( database : String,
        tableName : String,
        redshiftTmpDir : String = "",
        transformationContext : String = ""
        additionalOptions: JsonOptions = JsonOptions.empty,
        catalogId: String = null
) : DataSink
```

Creates a [DataSink](glue-etl-scala-apis-glue-datasink-class.md "glue-etl-scala-apis-glue-datasink-class.md") that writes to a location
specified in a table that is defined in the Data Catalog.

- `database` — The database name in the Data Catalog.
- `tableName` — The table name in the Data Catalog.
- `redshiftTmpDir` — The temporary staging directory to be used with
  certain data sinks. Set to empty by default.
- `transformationContext` — The transformation context that is
  associated with the sink to be used by job bookmarks. Set to empty by default.
- `additionalOptions` – Additional options provided to AWS Glue.
- `catalogId` — The catalog ID (account ID) of the Data Catalog being accessed. When null, the default account ID of the caller is used.

Returns the `DataSink`.

## def getCatalogSource

```
def getCatalogSource( database : String,
                      tableName : String,
                      redshiftTmpDir : String = "",
                      transformationContext : String = ""
                      pushDownPredicate : String = " "
                      additionalOptions: JsonOptions = JsonOptions.empty,
                      catalogId: String = null
                    ) : DataSource
```

Creates a [DataSource trait](glue-etl-scala-apis-glue-datasource-trait.md "glue-etl-scala-apis-glue-datasource-trait.md") that reads data from a
table definition in the Data Catalog.

- `database` — The database name in the Data Catalog.
- `tableName` — The table name in the Data Catalog.
- `redshiftTmpDir` — The temporary staging directory to be used with
  certain data sinks. Set to empty by default.
- `transformationContext` — The transformation context that is
  associated with the sink to be used by job bookmarks. Set to empty by default.
- `pushDownPredicate` – Filters partitions without having to list and read all the files in your dataset.
  For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").
- `additionalOptions` – A collection of optional name-value pairs. The possible
  options include those listed in [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") except for `endpointUrl`,
  `streamName`, `bootstrap.servers`, `security.protocol`,
  `topicName`, `classification`, and `delimiter`. Another supported option is `catalogPartitionPredicate`:

`catalogPartitionPredicate` — You can pass a catalog expression to filter based on the index columns. This pushes down the filtering to the server side. For more information, see [AWS Glue Partition Indexes](partition-indexes.md "partition-indexes.md"). Note that `push_down_predicate` and `catalogPartitionPredicate` use different syntaxes. The former one uses Spark SQL standard syntax and the later one uses JSQL parser.

- `catalogId` — The catalog ID (account ID) of the Data Catalog being accessed. When null, the default account ID of the caller is used.

Returns the `DataSource`.

**Example for streaming source**

```
val data_frame_datasource0 = glueContext.getCatalogSource(
    database = "tempdb",
    tableName = "test-stream-input",
    redshiftTmpDir = "",
    transformationContext = "datasource0",
    additionalOptions = JsonOptions("""{
        "startingPosition": "TRIM_HORIZON", "inferSchema": "false"}""")
    ).getDataFrame()
```

## def getJDBCSink

```
def getJDBCSink( catalogConnection : String,
                 options : JsonOptions,
                 redshiftTmpDir : String = "",
                 transformationContext : String = "",
                 catalogId: String = null
               ) : DataSink
```

Creates a [DataSink](glue-etl-scala-apis-glue-datasink-class.md "glue-etl-scala-apis-glue-datasink-class.md") that writes to a JDBC
database that is specified in a `Connection` object in the Data Catalog. The
`Connection` object has information to connect to a JDBC sink, including the URL,
user name, password, VPC, subnet, and security groups.

- `catalogConnection` — The name of the connection in the
  Data Catalog that contains the JDBC URL to write to.
- `options` — A string of JSON name-value pairs that provide
  additional information that is required to write to a JDBC data store. This includes:
  - _dbtable_ (required) — The name of the JDBC table. For JDBC data stores that support schemas within a database, specify `schema.table-name`.
    If a schema is not provided, then the default "public" schema is used.
    The following example shows an options parameter that points to a schema named `test` and a table named `test_table` in database `test_db`.

  ```
  options = JsonOptions("""{"dbtable": "test.test_table", "database": "test_db"}""")
  ```

  - _database_ (required) — The name of the JDBC database.
  - Any additional options passed directly to the SparkSQL JDBC writer.
    For more information, see [Redshift data source for Spark](https://github.com/databricks/spark-redshift "https://github.com/databricks/spark-redshift").

- `redshiftTmpDir` — A temporary staging directory to be used with
  certain data sinks. Set to empty by default.
- `transformationContext` — The transformation context that is
  associated with the sink to be used by job bookmarks. Set to empty by default.
- `catalogId` — The catalog ID (account ID) of the Data Catalog being accessed. When null, the default account ID of the caller is used.

Example code:

```

getJDBCSink(catalogConnection = "my-connection-name", options = JsonOptions("""{"dbtable": "my-jdbc-table", "database": "my-jdbc-db"}"""), redshiftTmpDir = "", transformationContext = "datasink4")

```

Returns the `DataSink`.

## def getSink

```
def getSink( connectionType : String,
             connectionOptions : JsonOptions,
             transformationContext : String = ""
           ) : DataSink
```

Creates a [DataSink](glue-etl-scala-apis-glue-datasink-class.md "glue-etl-scala-apis-glue-datasink-class.md") that writes data to a
destination like Amazon Simple Storage Service (Amazon S3), JDBC, or the AWS Glue Data Catalog, or an Apache Kafka or Amazon
Kinesis data stream.

- `connectionType` — The type of the connection. See [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `connectionOptions` — A string of JSON name-value pairs
  that provide additional information to establish the connection with the data sink. See
  [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `transformationContext` — The transformation context that
  is associated with the sink to be used by job bookmarks. Set to empty by default.

Returns the `DataSink`.

## def getSinkWithFormat

```
def getSinkWithFormat( connectionType : String,
                       options : JsonOptions,
                       transformationContext : String = "",
                       format : String = null,
                       formatOptions : JsonOptions = JsonOptions.empty
                     ) : DataSink
```

Creates a [DataSink](glue-etl-scala-apis-glue-datasink-class.md "glue-etl-scala-apis-glue-datasink-class.md") that writes data to a
destination like Amazon S3, JDBC, or the Data Catalog, or an Apache Kafka or Amazon Kinesis data stream.
Also sets the format for the data to be written out to the destination.

- `connectionType` — The type of the connection. See [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `options` — A string of JSON name-value pairs that provide
  additional information to establish a connection with the data sink. See [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `transformationContext` — The transformation context that is
  associated with the sink to be used by job bookmarks. Set to empty by default.
- `format` — The format of the data to be written out to the
  destination.
- `formatOptions` — A string of JSON name-value pairs that provide
  additional options for formatting data at the destination. See [Data format options](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").

Returns the `DataSink`.

## def getSource

```
def getSource( connectionType : String,
               connectionOptions : JsonOptions,
               transformationContext : String = ""
               pushDownPredicate
             ) : DataSource
```

Creates a [DataSource trait](glue-etl-scala-apis-glue-datasource-trait.md "glue-etl-scala-apis-glue-datasource-trait.md") that reads data from a
source like Amazon S3, JDBC, or the AWS Glue Data Catalog. Also supports Kafka and Kinesis streaming data
sources.

- `connectionType` — The type of the data source. See [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").
- `connectionOptions` — A string of JSON name-value pairs
  that provide additional information for establishing a connection with the data source.
  For more information, see [Connection types and options for ETL in
  AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md").

A Kinesis streaming source requires the following connection options:
`streamARN`, `startingPosition`, `inferSchema`, and
`classification`.

A Kafka streaming source requires the following connection options:
`connectionName`, `topicName`, `startingOffsets`,
`inferSchema`, and `classification`.

- `transformationContext` — The transformation context that is
  associated with the sink to be used by job bookmarks. Set to empty by default.
- `pushDownPredicate` — Predicate on partition columns.

Returns the `DataSource`.

Example for Amazon Kinesis streaming source:

````
val kinesisOptions = jsonOptions()
data_frame_datasource0 = glueContext.getSource("kinesis", kinesisOptions).getDataFrame()

private def jsonOptions(): JsonOptions = {
    new JsonOptions(
      s"""{"streamARN": "arn:aws:kinesis:eu-central-1:123456789012:stream/fromOptionsStream",
|"startingPosition": "TRIM_HORIZON",
|"inferSchema": "true",
|"classification": "json"}""".stripMargin) } ``` Example for Kafka streaming source: ``` val kafkaOptions = jsonOptions() val data_frame_datasource0 = glueContext.getSource("kafka", kafkaOptions).getDataFrame() private def jsonOptions(): JsonOptions = { new JsonOptions( s"""{"connectionName": "ConfluentKafka",
|"topicName": "kafka-auth-topic",
|"startingOffsets": "earliest",
|"inferSchema": "true",
|"classification": "json"}""".stripMargin) } ``` ## def getSourceWithFormat ``` def getSourceWithFormat( connectionType : String, options : JsonOptions, transformationContext : String = "", format : String = null, formatOptions : JsonOptions = JsonOptions.empty ) : DataSource ``` Creates a [DataSource trait](glue-etl-scala-apis-glue-datasource-trait.md "glue-etl-scala-apis-glue-datasource-trait.md") that reads data from a source like Amazon S3, JDBC, or the AWS Glue Data Catalog, and also sets the format of data stored in the source. <br>• `connectionType` – The type of the data source. See [Connection types and options for ETL in AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md"). <br>• `options` – A string of JSON name-value pairs that provide additional information for establishing a connection with the data source. See [Connection types and options for ETL in AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md"). <br>• `transformationContext` – The transformation context that is associated with the sink to be used by job bookmarks. Set to empty by default. <br>• `format` – The format of the data that is stored at the source. When the `connectionType` is "s3", you can also specify `format`. Can be one of “avro”, “csv”, “grokLog”, “ion”, “json”, “xml”, “parquet”, or “orc”. <br>• `formatOptions` – A string of JSON name-value pairs that provide additional options for parsing data at the source. See [Data format options](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md"). Returns the `DataSource`. **Examples** Create a DynamicFrame from a data source that is a comma-separated values (CSV) file on Amazon S3: ``` val datasource0 = glueContext.getSourceWithFormat( connectionType="s3", options =JsonOptions(s"""{"paths": [ "`s3://csv/nycflights.csv`"]}"""), transformationContext = "datasource0", format = "csv", formatOptions=JsonOptions(s"""{"withHeader":"true","separator": ","}""") ).getDynamicFrame() ``` Create a DynamicFrame from a data source that is a PostgreSQL using a JDBC connection: ``` val datasource0 = glueContext.getSourceWithFormat( connectionType="postgresql", options =JsonOptions(s"""{ "url":"jdbc:postgresql://`databasePostgres-1`.rds.amazonaws.com:`5432`/`testdb`", "dbtable": "`public.company`", "redshiftTmpDir":"", "user":"`username`", "password":"`password123`" }"""), transformationContext = "datasource0").getDynamicFrame() ``` Create a DynamicFrame from a data source that is a MySQL using a JDBC connection: ``` val datasource0 = glueContext.getSourceWithFormat( connectionType="mysql", options =JsonOptions(s"""{ "url":"jdbc:mysql://`databaseMysql-1`.rds.amazonaws.com:`3306`/`testdb`", "dbtable": "`athenatest_nycflights13_csv`", "redshiftTmpDir":"", "user":"`username`", "password":"`password123`" }"""), transformationContext = "datasource0").getDynamicFrame() ``` ## def getSparkSession ``` def getSparkSession : SparkSession ``` Gets the `SparkSession` object associated with this GlueContext. Use this SparkSession object to register tables and UDFs for use with `DataFrame` created from DynamicFrames. Returns the SparkSession. ## def startTransaction ``` def startTransaction(readOnly: Boolean):String ``` Start a new transaction. Internally calls the Lake Formation [startTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-StartTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-StartTransaction") API. <br>• `readOnly` – (Boolean) Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed. Returns the transaction ID. ## def commitTransaction ``` def commitTransaction(transactionId: String, waitForCommit: Boolean): Boolean ``` Attempts to commit the specified transaction. `commitTransaction` may return before the transaction has finished committing. Internally calls the Lake Formation [commitTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CommitTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CommitTransaction") API. <br>• `transactionId` – (String) The transaction to commit. <br>• `waitForCommit` – (Boolean) Determines whether the `commitTransaction` returns immediately. The default value is true. If false, `commitTransaction` polls and waits until the transaction is committed. The amount of wait time is restricted to 1 minute using exponential backoff with a maximum of 6 retry attempts. Returns a Boolean to indicate whether the commit is done or not. ## def cancelTransaction ``` def cancelTransaction(transactionId: String): Unit ``` Attempts to cancel the specified transaction. Internally calls the Lake Formation [CancelTransaction](../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CancelTransaction "../../../lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-transactions.md#aws-lake-formation-api-aws-lake-formation-api-transactions-CancelTransaction") API. <br>• `transactionId` – (String) The transaction to cancel. Returns a `TransactionCommittedException` exception if the transaction was previously committed. ## def this ``` def this( sc : SparkContext, minPartitions : Int, targetPartitions : Int ) ``` Creates a `GlueContext` object using the specified `SparkContext`, minimum partitions, and target partitions. <br>• `sc` — The `SparkContext`. <br>• `minPartitions` — The minimum number of partitions. <br>• `targetPartitions` — The target number of partitions. Returns the `GlueContext`. ## def this ``` def this( sc : SparkContext ) ``` Creates a `GlueContext` object with the provided `SparkContext`. Sets the minimum partitions to 10 and target partitions to 20. <br>• `sc` — The `SparkContext`. Returns the `GlueContext`. ## def this ``` def this( sparkContext : JavaSparkContext ) ``` Creates a `GlueContext` object with the provided `JavaSparkContext`. Sets the minimum partitions to 10 and target partitions to 20. <br>• `sparkContext` — The `JavaSparkContext`. Returns the `GlueContext`.
````

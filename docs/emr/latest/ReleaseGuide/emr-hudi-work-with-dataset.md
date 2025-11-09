# Work with a Hudi dataset

Hudi supports inserting, updating, and deleting data in Hudi datasets
through Spark. For more information, see [Writing Hudi tables](https://hudi.apache.org/docs/writing_data.html "https://hudi.apache.org/docs/writing_data.html") in
Apache Hudi documentation.

The following examples demonstrate how to launch the interactive Spark shell, use
Spark submit, or use Amazon EMR Notebooks to work with Hudi on Amazon EMR. You can also use
the Hudi DeltaStreamer utility or other tools to write to a dataset. Throughout
this section, the examples demonstrate working with datasets using the Spark shell while
connected to the master node using SSH as the default `hadoop` user.

When running `spark-shell`, `spark-submit`, or
`spark-sql` using Amazon EMR 6.7.0 or later, pass the following
commands.

###### Note

Amazon EMR 6.7.0 uses [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.0-amzn-0, which contains significant improvements over previous Hudi versions. For more information, see the [Apache Hudi 0.11.0 Migration Guide](https://hudi.apache.org/releases/release-0.11.0/#migration-guide "https://hudi.apache.org/releases/release-0.11.0/#migration-guide"). The examples on this tab reflect these changes.

###### To open the Spark shell on the primary node

1. Connect to the primary node using SSH. For more information, see
   [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management Guide_.
2. Enter the following command to launch the Spark shell. To use the
   PySpark shell, replace `spark-shell` with
   `pyspark`.

```
`spark-shell` --jars /usr/lib/hudi/hudi-spark-bundle.jar \
--conf "spark.serializer=org.apache.spark.serializer.KryoSerializer" \
--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog"  \
--conf "spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension"
```

When running `spark-shell`, `spark-submit`, or
`spark-sql` using Amazon EMR 6.6.x or earlier, pass the following
commands.

###### Note

- Amazon EMR 6.2 and 5.31 and later (Hudi 0.6.x and later) can omit the
  `spark-avro.jar` from the configuration.
- Amazon EMR 6.5 and 5.35 and later (Hudi 0.9.x and later)
  can omit
  `spark.sql.hive.convertMetastoreParquet=false`
  from the configuration.
- Amazon EMR 6.6 and 5.36 and later (Hudi 0.10.x and later)
  must include the
  `HoodieSparkSessionExtension` config as described in the [Version: 0.10.0 Spark Guide](https://hudi.apache.org/docs/0.10.0/quick-start-guide/ "https://hudi.apache.org/docs/0.10.0/quick-start-guide/"):

```
--conf  "spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension" \

```

###### To open the Spark shell on the primary node

1. Connect to the primary node using SSH. For more information, see
   [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management Guide_.
2. Enter the following command to launch the Spark shell. To use the
   PySpark shell, replace `spark-shell` with
   `pyspark`.

```
`spark-shell` \
--conf "spark.serializer=org.apache.spark.serializer.KryoSerializer" \
--conf "spark.sql.hive.convertMetastoreParquet=false" \
--jars /usr/lib/hudi/hudi-spark-bundle.jar,/usr/lib/spark/external/lib/spark-avro.jar
```

To use Hudi with Amazon EMR Notebooks, you must first copy the Hudi
jar files from the local file system to HDFS on the master node of the
notebook cluster. You then use the notebook editor to configure your
EMR notebook to use Hudi.

###### To use Hudi with Amazon EMR Notebooks

1. Create and launch a cluster for Amazon EMR Notebooks. For more
   information, see [Creating Amazon EMR clusters for notebooks](../ManagementGuide/emr-managed-notebooks-cluster.md "../ManagementGuide/emr-managed-notebooks-cluster.md") in the
   _Amazon EMR Management Guide_.
2. Connect to the master node of the cluster using SSH and then copy
   the jar files from the local filesystem to HDFS as shown in the
   following examples. In the example, we create a directory in HDFS
   for clarity of file management. You can choose your own destination
   in HDFS, if desired.

```
hdfs dfs -mkdir -p /apps/hudi/lib
```

```
hdfs dfs -copyFromLocal /usr/lib/hudi/hudi-spark-bundle.jar /apps/hudi/lib/hudi-spark-bundle.jar
```

3. Open the notebook editor, enter the code from the following
   example, and run it.

```
%%configure
{ "conf": {
            "spark.jars":"hdfs:///apps/hudi/lib/hudi-spark-bundle.jar",
            "spark.serializer":"org.apache.spark.serializer.KryoSerializer",
            "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
            "spark.sql.extensions":"org.apache.spark.sql.hudi.HoodieSparkSessionExtension"
          }}
```

To use Hudi with Amazon EMR Notebooks, you must first copy the Hudi
jar files from the local file system to HDFS on the master node of the
notebook cluster. You then use the notebook editor to configure your
EMR notebook to use Hudi.

###### To use Hudi with Amazon EMR Notebooks

1. Create and launch a cluster for Amazon EMR Notebooks. For more
   information, see [Creating Amazon EMR clusters for notebooks](../ManagementGuide/emr-managed-notebooks-cluster.md "../ManagementGuide/emr-managed-notebooks-cluster.md") in the
   _Amazon EMR Management Guide_.
2. Connect to the master node of the cluster using SSH and then copy
   the jar files from the local filesystem to HDFS as shown in the
   following examples. In the example, we create a directory in HDFS
   for clarity of file management. You can choose your own destination
   in HDFS, if desired.

```
hdfs dfs -mkdir -p /apps/hudi/lib
```

```
hdfs dfs -copyFromLocal /usr/lib/hudi/hudi-spark-bundle.jar /apps/hudi/lib/hudi-spark-bundle.jar
```

```
hdfs dfs -copyFromLocal /usr/lib/spark/external/lib/spark-avro.jar /apps/hudi/lib/spark-avro.jar
```

3. Open the notebook editor, enter the code from the following
   example, and run it.

```
{ "conf": {
            "spark.jars":"hdfs:///apps/hudi/lib/hudi-spark-bundle.jar,hdfs:///apps/hudi/lib/spark-avro.jar",
            "spark.serializer":"org.apache.spark.serializer.KryoSerializer",
            "spark.sql.hive.convertMetastoreParquet":"false"
          }}
```

## Initialize a Spark session for

Hudi

When you use Scala, you must import the following classes in your Spark session.
This needs to be done once per Spark session.

```
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.functions._
import org.apache.hudi.DataSourceWriteOptions
import org.apache.hudi.DataSourceReadOptions
import org.apache.hudi.config.HoodieWriteConfig
import org.apache.hudi.hive.MultiPartKeysValueExtractor
import org.apache.hudi.hive.HiveSyncConfig
import org.apache.hudi.sync.common.HoodieSyncConfig
```

## Write to a Hudi dataset

The following examples show how to create a DataFrame and write it as a Hudi
dataset.

###### Note

To paste code samples into the Spark shell, type `:paste`
at the prompt, paste the example, and then press `CTRL` +
`D`.

Each time you write a DataFrame to a Hudi dataset, you must specify
`DataSourceWriteOptions`. Many of these options are likely to be
identical between write operations. The following example specifies common options
using the `hudiOptions` variable, which
subsequent examples use.

###### Note

Amazon EMR 6.7.0 uses [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.0-amzn-0, which contains significant improvements over previous Hudi versions. For more information, see the [Apache Hudi 0.11.0 Migration Guide](https://hudi.apache.org/releases/release-0.11.0/#migration-guide "https://hudi.apache.org/releases/release-0.11.0/#migration-guide"). The examples on this tab reflect these changes.

```
// Create a DataFrame
val inputDF = Seq(
 ("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
 ("101", "2015-01-01", "2015-01-01T12:14:58.597216Z"),
 ("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
 ("103", "2015-01-01", "2015-01-01T13:51:40.519832Z"),
 ("104", "2015-01-02", "2015-01-01T12:15:00.512679Z"),
 ("105", "2015-01-02", "2015-01-01T13:51:42.248818Z")
 ).toDF("id", "creation_date", "last_update_time")

//Specify common DataSourceWriteOptions in the single hudiOptions variable
val hudiOptions = Map[String,String](
  HoodieWriteConfig.TBL_NAME.key -> "`tableName`",
  DataSourceWriteOptions.TABLE_TYPE.key -> "COPY_ON_WRITE",
  DataSourceWriteOptions.RECORDKEY_FIELD_OPT_KEY -> "id",
  DataSourceWriteOptions.PARTITIONPATH_FIELD_OPT_KEY -> "creation_date",
  DataSourceWriteOptions.PRECOMBINE_FIELD_OPT_KEY -> "last_update_time",
  DataSourceWriteOptions.HIVE_SYNC_ENABLED_OPT_KEY -> "true",
  DataSourceWriteOptions.HIVE_TABLE_OPT_KEY -> "`tableName`",
  DataSourceWriteOptions.HIVE_PARTITION_FIELDS_OPT_KEY -> "creation_date",
  HoodieSyncConfig.META_SYNC_PARTITION_EXTRACTOR_CLASS.key -> "org.apache.hudi.hive.MultiPartKeysValueExtractor",
  HoodieSyncConfig.META_SYNC_ENABLED.key -> "true",
  HiveSyncConfig.HIVE_SYNC_MODE.key -> "hms",
  HoodieSyncConfig.META_SYNC_TABLE_NAME.key -> "`tableName`",
  HoodieSyncConfig.META_SYNC_PARTITION_FIELDS.key -> "creation_date"
)

// Write the DataFrame as a Hudi dataset
(inputDF.write
    .format("hudi")
    .options(hudiOptions)
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY,"insert")
    .mode(SaveMode.Overwrite)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))

```

```
// Create a DataFrame
val inputDF = Seq(
 ("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
 ("101", "2015-01-01", "2015-01-01T12:14:58.597216Z"),
 ("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
 ("103", "2015-01-01", "2015-01-01T13:51:40.519832Z"),
 ("104", "2015-01-02", "2015-01-01T12:15:00.512679Z"),
 ("105", "2015-01-02", "2015-01-01T13:51:42.248818Z")
 ).toDF("id", "creation_date", "last_update_time")

//Specify common DataSourceWriteOptions in the single hudiOptions variable
val hudiOptions = Map[String,String](
  HoodieWriteConfig.TABLE_NAME -> "`tableName`",
  DataSourceWriteOptions.TABLE_TYPE_OPT_KEY -> "COPY_ON_WRITE",
  DataSourceWriteOptions.RECORDKEY_FIELD_OPT_KEY -> "id",
  DataSourceWriteOptions.PARTITIONPATH_FIELD_OPT_KEY -> "creation_date",
  DataSourceWriteOptions.PRECOMBINE_FIELD_OPT_KEY -> "last_update_time",
  DataSourceWriteOptions.HIVE_SYNC_ENABLED_OPT_KEY -> "true",
  DataSourceWriteOptions.HIVE_TABLE_OPT_KEY -> "`tableName`",
  DataSourceWriteOptions.HIVE_PARTITION_FIELDS_OPT_KEY -> "creation_date",
  DataSourceWriteOptions.HIVE_PARTITION_EXTRACTOR_CLASS_OPT_KEY -> classOf[MultiPartKeysValueExtractor].getName
)

// Write the DataFrame as a Hudi dataset
(inputDF.write
    .format("org.apache.hudi")
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY, DataSourceWriteOptions.INSERT_OPERATION_OPT_VAL)
    .options(hudiOptions)
    .mode(SaveMode.Overwrite)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))

```

```
# Create a DataFrame
inputDF = spark.createDataFrame(
    [
        ("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
        ("101", "2015-01-01", "2015-01-01T12:14:58.597216Z"),
        ("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
        ("103", "2015-01-01", "2015-01-01T13:51:40.519832Z"),
        ("104", "2015-01-02", "2015-01-01T12:15:00.512679Z"),
        ("105", "2015-01-02", "2015-01-01T13:51:42.248818Z"),
    ],
    ["id", "creation_date", "last_update_time"]
)

# Specify common DataSourceWriteOptions in the single hudiOptions variable
hudiOptions = {
'hoodie.table.name': '`tableName`',
'hoodie.datasource.write.recordkey.field': 'id',
'hoodie.datasource.write.partitionpath.field': 'creation_date',
'hoodie.datasource.write.precombine.field': 'last_update_time',
'hoodie.datasource.hive_sync.enable': 'true',
'hoodie.datasource.hive_sync.table': '`tableName`',
'hoodie.datasource.hive_sync.partition_fields': 'creation_date',
'hoodie.datasource.hive_sync.partition_extractor_class': 'org.apache.hudi.hive.MultiPartKeysValueExtractor'
}

# Write a DataFrame as a Hudi dataset
inputDF.write \
.format('org.apache.hudi') \
.option('hoodie.datasource.write.operation', 'insert') \
.options(**hudiOptions) \
.mode('overwrite') \
.save('`s3://amzn-s3-demo-bucket/myhudidataset/`')
```

###### Note

You might see "hoodie" instead of Hudi in code examples and notifications. The
Hudi codebase widely uses the old "hoodie" spelling.

| DataSourceWriteOptions reference for Hudi | Option                                                                                                                                                                                                                                                             | Description |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| TABLE_NAME                                | The table name under which to register the dataset.                                                                                                                                                                                                                |
| TABLE_TYPE_OPT_KEY                        | Optional. Specifies whether the dataset is created as<br>`"COPY_ON_WRITE"` or<br>`"MERGE_ON_READ"`. The default is<br>`"COPY_ON_WRITE"`.                                                                                                                           |
| RECORDKEY_FIELD_OPT_KEY                   | The record key field whose value will be used as<br>the `recordKey` component<br>of `HoodieKey`. Actual value will be obtained by<br>invoking `.toString()` on the field value. Nested<br>fields can be specified using the dot notation, for<br>example, `a.b.c`. |
| PARTITIONPATH_FIELD_OPT_KEY               | The partition path field whose value will be used as the<br>`partitionPath` component<br>of `HoodieKey`. The actual value will be obtained<br>by invoking `.toString()` on the field value.                                                                        |
| PRECOMBINE_FIELD_OPT_KEY                  | The field used in pre-combining before actual write. When two<br>records have the same key value, Hudi picks the one with<br>the largest value for the precombine field as determined by<br>`Object.compareTo(..)`.                                                |

The following options are required only to register the Hudi dataset table in
your metastore. If you do not register your Hudi dataset as a table in the Hive
metastore, these options are not required.

| DataSourceWriteOptions reference for Hive | Option                                                                                                      | Description |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| HIVE_DATABASE_OPT_KEY                     | The Hive database to sync to. The default is<br>`"default"`.                                                |
| HIVE_PARTITION_EXTRACTOR_CLASS_OPT_KEY    | The class used to extract partition field values into Hive<br>partition columns.                            |
| HIVE_PARTITION_FIELDS_OPT_KEY             | The field in the dataset to use for determining Hive partition<br>columns.                                  |
| HIVE_SYNC_ENABLED_OPT_KEY                 | When set to `"true"`, registers the dataset with<br>the Apache Hive metastore. The default is<br>`"false"`. |
| HIVE_TABLE_OPT_KEY                        | Required. The name of the table in Hive to sync to. For<br>example, `"my_hudi_table_cow"`.                  |
| HIVE_USER_OPT_KEY                         | Optional. The Hive user name to use when syncing. For example,<br>`"hadoop"`.                               |
| HIVE_PASS_OPT_KEY                         | Optional. The Hive password for the user specified by<br>`HIVE_USER_OPT_KEY`.                               |
| HIVE_URL_OPT_KEY                          | The Hive metastore URL.                                                                                     |

## Upsert data

The following example demonstrates how to upsert data by writing a DataFrame.
Unlike the previous insert example, the `OPERATION_OPT_KEY` value is set
to `UPSERT_OPERATION_OPT_VAL`. In addition,
`.mode(SaveMode.Append)` is specified to indicate that the record
should be appended.

###### Note

Amazon EMR 6.7.0 uses [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.0-amzn-0, which contains significant improvements over previous Hudi versions. For more information, see the [Apache Hudi 0.11.0 Migration Guide](https://hudi.apache.org/releases/release-0.11.0/#migration-guide "https://hudi.apache.org/releases/release-0.11.0/#migration-guide"). The examples on this tab reflect these changes.

```
// Create a new DataFrame from the first row of inputDF with a different creation_date value
val updateDF = inputDF.limit(1).withColumn("creation_date", lit("new_value"))

(updateDF.write
    .format("hudi")
    .options(hudiOptions)
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY, "upsert")
    .mode(SaveMode.Append)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))

```

```
// Create a new DataFrame from the first row of inputDF with a different creation_date value
val updateDF = inputDF.limit(1).withColumn("creation_date", lit("`new_value`"))

(updateDF.write
    .format("org.apache.hudi")
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY, DataSourceWriteOptions.UPSERT_OPERATION_OPT_VAL)
    .options(hudiOptions)
    .mode(SaveMode.Append)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))
```

```
from pyspark.sql.functions import lit

# Create a new DataFrame from the first row of inputDF with a different creation_date value
updateDF = inputDF.limit(1).withColumn('creation_date', lit('`new_value`'))

updateDF.write \
    .format('org.apache.hudi') \
    .option('hoodie.datasource.write.operation', 'upsert') \
    .options(**hudiOptions) \
    .mode('append') \
    .save('`s3://amzn-s3-demo-bucket/myhudidataset/`')
```

## Delete a record

To hard delete a record, you can upsert an empty payload. In this case, the
`PAYLOAD_CLASS_OPT_KEY` option specifies the
`EmptyHoodieRecordPayload` class. The example uses the same
DataFrame, `updateDF`, used in the upsert example to specify the same
record.

###### Note

Amazon EMR 6.7.0 uses [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.0-amzn-0, which contains significant improvements over previous Hudi versions. For more information, see the [Apache Hudi 0.11.0 Migration Guide](https://hudi.apache.org/releases/release-0.11.0/#migration-guide "https://hudi.apache.org/releases/release-0.11.0/#migration-guide"). The examples on this tab reflect these changes.

```
(updateDF.write
    .format("hudi")
    .options(hudiOptions)
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY, "delete")
    .mode(SaveMode.Append)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))
```

```
(updateDF.write
    .format("org.apache.hudi")
    .option(DataSourceWriteOptions.OPERATION_OPT_KEY, DataSourceWriteOptions.UPSERT_OPERATION_OPT_VAL)
    .option(DataSourceWriteOptions.PAYLOAD_CLASS_OPT_KEY, "org.apache.hudi.common.model.EmptyHoodieRecordPayload")
    .mode(SaveMode.Append)
    .save("`s3://amzn-s3-demo-bucket/myhudidataset/`"))
```

```
updateDF.write \
    .format('org.apache.hudi') \
    .option('hoodie.datasource.write.operation', 'upsert') \
    .option('hoodie.datasource.write.payload.class', 'org.apache.hudi.common.model.EmptyHoodieRecordPayload') \
    .options(**hudiOptions) \
    .mode('append') \
    .save('`s3://amzn-s3-demo-bucket/myhudidataset/`')
```

You can also hard delete data by setting `OPERATION_OPT_KEY` to
`DELETE_OPERATION_OPT_VAL` to remove all records in the dataset you
submit. For instructions on performing soft deletes, and for more information about
deleting data stored in Hudi tables, see [Deletes](https://hudi.apache.org/docs/writing_data.html#deletes "https://hudi.apache.org/docs/writing_data.html#deletes") in
the Apache Hudi documentation.

## Read from a Hudi dataset

To retrieve data at the present point in time, Hudi performs snapshot queries by
default. Following is an example of querying the dataset written to S3 in [Write to a Hudi dataset](#emr-hudi-dataframe "#emr-hudi-dataframe"). Replace
`s3://amzn-s3-demo-bucket/myhudidataset` with your table
path, and add wildcard asterisks for each partition level, _plus one additional asterisk_. In this example, there is one
partition level, so we've added two wildcard symbols.

###### Note

Amazon EMR 6.7.0 uses [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.0-amzn-0, which contains significant improvements over previous Hudi versions. For more information, see the [Apache Hudi 0.11.0 Migration Guide](https://hudi.apache.org/releases/release-0.11.0/#migration-guide "https://hudi.apache.org/releases/release-0.11.0/#migration-guide"). The examples on this tab reflect these changes.

```
val snapshotQueryDF = spark.read
    .format("hudi")
    .load(`"s3://amzn-s3-demo-bucket/myhudidataset"`)
    .show()
```

```
(val snapshotQueryDF = spark.read
    .format("org.apache.hudi")
    .load("`s3://amzn-s3-demo-bucket/myhudidataset`" + "/*/*"))

snapshotQueryDF.show()
```

```
snapshotQueryDF = spark.read \
    .format('org.apache.hudi') \
    .load('`s3://amzn-s3-demo-bucket/myhudidataset`' + '/*/*')

snapshotQueryDF.show()
```

### Incremental queries

You can also perform incremental queries with Hudi to get a stream of records
that have changed since a given commit timestamp. To do so, set the
`QUERY_TYPE_OPT_KEY` field to
`QUERY_TYPE_INCREMENTAL_OPT_VAL`. Then, add a value for
`BEGIN_INSTANTTIME_OPT_KEY` to obtain all records written since
the specified time. Incremental queries are typically ten times more efficient
than their batch counterparts since they only process changed records.

When you perform incremental queries, use the root (base) table path without
the wildcard asterisks used for Snapshot queries.

###### Note

Presto does not support incremental queries.

```
val incQueryDF = spark.read
    .format("org.apache.hudi")
    .option(DataSourceReadOptions.QUERY_TYPE_OPT_KEY, DataSourceReadOptions.QUERY_TYPE_INCREMENTAL_OPT_VAL)
    .option(DataSourceReadOptions.BEGIN_INSTANTTIME_OPT_KEY, `<beginInstantTime>`)
    .load("`s3://amzn-s3-demo-bucket/myhudidataset`")

incQueryDF.show()
```

```
readOptions = {
  'hoodie.datasource.query.type': 'incremental',
  'hoodie.datasource.read.begin.instanttime': `<beginInstantTime>`,
}

incQueryDF = spark.read \
    .format('org.apache.hudi') \
    .options(**readOptions) \
    .load('`s3://amzn-s3-demo-bucket/myhudidataset`')

incQueryDF.show()
```

For more information about reading from Hudi datasets, see [Querying Hudi
tables](https://hudi.apache.org/docs/querying_data.html "https://hudi.apache.org/docs/querying_data.html") in the Apache Hudi documentation.

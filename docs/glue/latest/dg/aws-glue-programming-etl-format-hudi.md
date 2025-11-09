# Using the Hudi framework in

AWS Glue

AWS Glue 3.0 and later supports Apache Hudi framework for data lakes. Hudi is an open-source
data lake storage framework that simplifies incremental data processing and data pipeline
development. This topic covers available features for using your data in AWS Glue when you
transport or store your data in a Hudi table. To learn more about Hudi, see the official
[Apache Hudi documentation](https://hudi.apache.org/docs/overview/ "https://hudi.apache.org/docs/overview/").

You can use AWS Glue to perform read and write operations on Hudi tables in Amazon S3, or work
with Hudi tables using the AWS Glue Data Catalog. Additional operations including insert, update, and
all of the [Apache Spark
operations](https://hudi.apache.org/docs/quick-start-guide/ "https://hudi.apache.org/docs/quick-start-guide/") are also supported.

###### Note

The Apache Hudi 0.15.0 implementation in AWS Glue 5.0 internally reverts
[HUDI-7001](https://github.com/apache/hudi/pull/9936 "https://github.com/apache/hudi/pull/9936"). It does not
exhibit the regression related to Complex Key gen when the record key consists of a single
field. However this behavior differs from OSS Apache Hudi 0.15.0.

Apache Hudi 0.10.1 for AWS Glue 3.0 doesn't support Hudi Merge on Read (MoR)
tables.

The following table lists the Hudi version that is included in each AWS Glue version.

| AWS Glue version | Supported Hudi version |
| ---------------- | ---------------------- |
| 5.0              | 0.15.0                 |
| 4.0              | 0.12.1                 |
| 3.0              | 0.10.1                 |

To learn more about the data lake frameworks that AWS Glue supports, see [Using data lake
frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

## Enabling Hudi

To enable Hudi for AWS Glue, complete the following tasks:

- Specify `hudi` as a value for the `--datalake-formats`
  job parameter. For more information, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").
- Create a key named `--conf` for your AWS Glue job, and set it to the
  following value. Alternatively, you can set the following configuration using
  `SparkConf` in your script. These settings help Apache Spark
  correctly handle Hudi tables.

```
spark.serializer=org.apache.spark.serializer.KryoSerializer
```

- Lake Formation permission support for Hudi is enabled by default for AWS Glue 4.0. No additional configuration is needed for reading/writing to Lake Formation-registered Hudi tables. To read a registered Hudi table, the AWS Glue job IAM role must have the SELECT permission. To write to a registered Hudi table, the AWS Glue job IAM role must have the SUPER permission. To learn more about managing Lake Formation permissions, see [Granting and revoking permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md").

**Using a different Hudi version**

To use a version of Hudi that AWS Glue doesn't support, specify your own Hudi JAR files
using the `--extra-jars` job parameter. Do not include `hudi` as a
value for the `--datalake-formats` job parameter. If you use AWS Glue 5.0, you must set `--user-jars-first true` job parameter.

## Example: Write a Hudi table

to Amazon S3 and register it in the AWS Glue Data Catalog

This example script demonstrates how to write a Hudi table to Amazon S3 and
register the table to the AWS Glue Data Catalog. The example uses the Hudi [Hive Sync tool](https://hudi.apache.org/docs/syncing_metastore/ "https://hudi.apache.org/docs/syncing_metastore/") to
register the table.

###### Note

This example requires you to set the `--enable-glue-datacatalog` job parameter in order to use the AWS Glue Data Catalog as an Apache Spark Hive metastore.
To learn more, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

Python

```
# Example: Create a Hudi table from a DataFrame
# and register the table to Glue Data Catalog

additional_options={
    "hoodie.table.name": "`<your_table_name>`",
    "hoodie.database.name": "`<your_database_name>`",
    "hoodie.datasource.write.storage.type": "COPY_ON_WRITE",
    "hoodie.datasource.write.operation": "upsert",
    "hoodie.datasource.write.recordkey.field": "`<your_recordkey_field>`",
    "hoodie.datasource.write.precombine.field": "`<your_precombine_field>`",
    "hoodie.datasource.write.partitionpath.field": "`<your_partitionkey_field>`",
    "hoodie.datasource.write.hive_style_partitioning": "true",
    "hoodie.datasource.hive_sync.enable": "true",
    "hoodie.datasource.hive_sync.database": "`<your_database_name>`",
    "hoodie.datasource.hive_sync.table": "`<your_table_name>`",
    "hoodie.datasource.hive_sync.partition_fields": "`<your_partitionkey_field>`",
    "hoodie.datasource.hive_sync.partition_extractor_class": "org.apache.hudi.hive.MultiPartKeysValueExtractor",
    "hoodie.datasource.hive_sync.use_jdbc": "false",
    "hoodie.datasource.hive_sync.mode": "hms",
    "path": "s3://`<s3Path/>`"
}

dataFrame.write.format("hudi") \
    .options(**additional_options) \
    .mode("overwrite") \
    .save()
```

Scala

```
// Example: Example: Create a Hudi table from a DataFrame
// and register the table to Glue Data Catalog

val additionalOptions = Map(
  "hoodie.table.name" -> "`<your_table_name>`",
  "hoodie.database.name" -> "`<your_database_name>`",
  "hoodie.datasource.write.storage.type" -> "COPY_ON_WRITE",
  "hoodie.datasource.write.operation" -> "upsert",
  "hoodie.datasource.write.recordkey.field" -> "`<your_recordkey_field>`",
  "hoodie.datasource.write.precombine.field" -> "`<your_precombine_field>`",
  "hoodie.datasource.write.partitionpath.field" -> "`<your_partitionkey_field>`",
  "hoodie.datasource.write.hive_style_partitioning" -> "true",
  "hoodie.datasource.hive_sync.enable" -> "true",
  "hoodie.datasource.hive_sync.database" -> "`<your_database_name>`",
  "hoodie.datasource.hive_sync.table" -> "`<your_table_name>`",
  "hoodie.datasource.hive_sync.partition_fields" -> "`<your_partitionkey_field>`",
  "hoodie.datasource.hive_sync.partition_extractor_class" -> "org.apache.hudi.hive.MultiPartKeysValueExtractor",
  "hoodie.datasource.hive_sync.use_jdbc" -> "false",
  "hoodie.datasource.hive_sync.mode" -> "hms",
  "path" -> "s3://`<s3Path/>`")

dataFrame.write.format("hudi")
  .options(additionalOptions)
  .mode("append")
  .save()
```

## Example: Read a Hudi table

from Amazon S3 using the AWS Glue Data Catalog

This example reads the Hudi table that you created in the [Example: Write a Hudi table
to Amazon S3 and register it in the AWS Glue Data Catalog](#aws-glue-programming-etl-format-hudi-write "#aws-glue-programming-etl-format-hudi-write") from
Amazon S3.

###### Note

This example requires you to set the `--enable-glue-datacatalog` job parameter in order to use the AWS Glue Data Catalog as an Apache Spark Hive metastore.
To learn more, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

Python
For this example, use the `GlueContext.create_data_frame.from_catalog()`
method.

```
# Example: Read a Hudi table from Glue Data Catalog

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

dataFrame = glueContext.create_data_frame.from_catalog(
    database = "`<your_database_name>`",
    table_name = "`<your_table_name>`"
)
```

Scala
For this example, use the [getCatalogSource](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSource "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSource") method.

```
// Example: Read a Hudi table from Glue Data Catalog

import com.amazonaws.services.glue.GlueContext
import org.apache.spark.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)

    val dataFrame = glueContext.getCatalogSource(
      database = "`<your_database_name>`",
      tableName = "`<your_table_name>`"
    ).getDataFrame()
  }
}
```

## Example: Update and

insert a `DataFrame` into a Hudi table in Amazon S3

This example uses the AWS Glue Data Catalog to insert a DataFrame into the Hudi table that you
created in [Example: Write a Hudi table
to Amazon S3 and register it in the AWS Glue Data Catalog](#aws-glue-programming-etl-format-hudi-write "#aws-glue-programming-etl-format-hudi-write").

###### Note

This example requires you to set the `--enable-glue-datacatalog` job parameter in order to use the AWS Glue Data Catalog as an Apache Spark Hive metastore.
To learn more, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

Python
For this example, use the `GlueContext.write_data_frame.from_catalog()`
method.

```
# Example: Upsert a Hudi table from Glue Data Catalog

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

glueContext.write_data_frame.from_catalog(
    frame = dataFrame,
    database = "`<your_database_name>`",
    table_name = "`<your_table_name>`",
    additional_options={
        "hoodie.table.name": "`<your_table_name>`",
        "hoodie.database.name": "`<your_database_name>`",
        "hoodie.datasource.write.storage.type": "COPY_ON_WRITE",
        "hoodie.datasource.write.operation": "upsert",
        "hoodie.datasource.write.recordkey.field": "`<your_recordkey_field>`",
        "hoodie.datasource.write.precombine.field": "`<your_precombine_field>`",
        "hoodie.datasource.write.partitionpath.field": "`<your_partitionkey_field>`",
        "hoodie.datasource.write.hive_style_partitioning": "true",
        "hoodie.datasource.hive_sync.enable": "true",
        "hoodie.datasource.hive_sync.database": "`<your_database_name>`",
        "hoodie.datasource.hive_sync.table": "`<your_table_name>`",
        "hoodie.datasource.hive_sync.partition_fields": "`<your_partitionkey_field>`",
        "hoodie.datasource.hive_sync.partition_extractor_class": "org.apache.hudi.hive.MultiPartKeysValueExtractor",
        "hoodie.datasource.hive_sync.use_jdbc": "false",
        "hoodie.datasource.hive_sync.mode": "hms"
    }
)
```

Scala
For this example, use the [getCatalogSink](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSink "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSink") method.

```
// Example: Upsert a Hudi table from Glue Data Catalog

import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.util.JsonOptions
import org.apacke.spark.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    glueContext.getCatalogSink("`<your_database_name>`", "`<your_table_name>`",
      additionalOptions = JsonOptions(Map(
        "hoodie.table.name" -> "`<your_table_name>`",
        "hoodie.database.name" -> "`<your_database_name>`",
        "hoodie.datasource.write.storage.type" -> "COPY_ON_WRITE",
        "hoodie.datasource.write.operation" -> "upsert",
        "hoodie.datasource.write.recordkey.field" -> "`<your_recordkey_field>`",
        "hoodie.datasource.write.precombine.field" -> "`<your_precombine_field>`",
        "hoodie.datasource.write.partitionpath.field" -> "`<your_partitionkey_field>`",
        "hoodie.datasource.write.hive_style_partitioning" -> "true",
        "hoodie.datasource.hive_sync.enable" -> "true",
        "hoodie.datasource.hive_sync.database" -> "`<your_database_name>`",
        "hoodie.datasource.hive_sync.table" -> "`<your_table_name>`",
        "hoodie.datasource.hive_sync.partition_fields" -> "`<your_partitionkey_field>`",
        "hoodie.datasource.hive_sync.partition_extractor_class" -> "org.apache.hudi.hive.MultiPartKeysValueExtractor",
        "hoodie.datasource.hive_sync.use_jdbc" -> "false",
        "hoodie.datasource.hive_sync.mode" -> "hms"
      )))
      .writeDataFrame(dataFrame, glueContext)
  }
}
```

## Example: Read a Hudi

table from Amazon S3 using Spark

This example reads a Hudi table from Amazon S3 using the Spark DataFrame
API.

Python

```
# Example: Read a Hudi table from S3 using a Spark DataFrame

dataFrame = spark.read.format("hudi").load("s3://`<s3path/>`")
```

Scala

```
// Example: Read a Hudi table from S3 using a Spark DataFrame

val dataFrame = spark.read.format("hudi").load("s3://`<s3path/>`")
```

## Example: Write a Hudi

table to Amazon S3 using Spark

This example writes a Hudi table to Amazon S3 using Spark.

Python

```
# Example: Write a Hudi table to S3 using a Spark DataFrame

dataFrame.write.format("hudi") \
    .options(**additional_options) \
    .mode("overwrite") \
    .save("s3://`<s3Path/>`)
```

Scala

```
// Example: Write a Hudi table to S3 using a Spark DataFrame

dataFrame.write.format("hudi")
  .options(additionalOptions)
  .mode("overwrite")
  .save("s3://`<s3path/>`")
```

## Example: Read and write Hudi table with Lake Formation permission control

This example reads and writes a Hudi table with Lake Formation permission control.

1. Create a Hudi table and register it in Lake Formation.
   1. To enable Lake Formation permission control, you’ll first need to register the table Amazon S3 path on Lake Formation. For more information, see [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md"). You can register it either from the Lake Formation console or by using the AWS CLI:

   ```
   aws lakeformation register-resource --resource-arn arn:aws:s3:::<s3-bucket>/<s3-folder> --use-service-linked-role --region <REGION>
   ```

   Once you register an Amazon S3 location, any AWS Glue table pointing to the location (or any of its child locations) will return the value for the `IsRegisteredWithLakeFormation` parameter as true in the `GetTable` call. 2. Create a Hudi table that points to the registered Amazon S3 path through the Spark dataframe API:

   ```
   hudi_options = {
       'hoodie.table.name': table_name,
       'hoodie.database.name': database_name,
       'hoodie.datasource.write.storage.type': 'COPY_ON_WRITE',
       'hoodie.datasource.write.recordkey.field': 'product_id',
       'hoodie.datasource.write.table.name': table_name,
       'hoodie.datasource.write.operation': 'upsert',
       'hoodie.datasource.write.precombine.field': 'updated_at',
       'hoodie.datasource.write.hive_style_partitioning': 'true',
       'hoodie.upsert.shuffle.parallelism': 2,
       'hoodie.insert.shuffle.parallelism': 2,
       'path': <S3_TABLE_LOCATION>,
       'hoodie.datasource.hive_sync.enable': 'true',
       'hoodie.datasource.hive_sync.database': database_name,
       'hoodie.datasource.hive_sync.table': table_name,
       'hoodie.datasource.hive_sync.use_jdbc': 'false',
       'hoodie.datasource.hive_sync.mode': 'hms'
   }

   df_products.write.format("hudi")  \
       .options(**hudi_options)  \
       .mode("overwrite")  \
       .save()
   ```

2. Grant Lake Formation permission to the AWS Glue job IAM role. You can either grant permissions from the Lake Formation console, or using the AWS CLI. For more information, see [Granting table permissions using the Lake Formation console and the named resource method](../../../lake-formation/latest/dg/granting-table-permissions.md "../../../lake-formation/latest/dg/granting-table-permissions.md")
3. Read the Hudi table registered in Lake Formation. The code is same as reading a non-registered Hudi table. Note that the AWS Glue job IAM role needs to have the SELECT permission for the read to succeed.

```
 val dataFrame = glueContext.getCatalogSource(
      database = "<your_database_name>",
      tableName = "<your_table_name>"
    ).getDataFrame()
```

4. Write to a Hudi table registered in Lake Formation. The code is same as writing to a non-registered Hudi table. Note that the AWS Glue job IAM role needs to have the SUPER permission for the write to succeed.

```
glueContext.getCatalogSink("<your_database_name>", "<your_table_name>",
      additionalOptions = JsonOptions(Map(
        "hoodie.table.name" -> "<your_table_name>",
        "hoodie.database.name" -> "<your_database_name>",
        "hoodie.datasource.write.storage.type" -> "COPY_ON_WRITE",
        "hoodie.datasource.write.operation" -> "<write_operation>",
        "hoodie.datasource.write.recordkey.field" -> "<your_recordkey_field>",
        "hoodie.datasource.write.precombine.field" -> "<your_precombine_field>",
        "hoodie.datasource.write.partitionpath.field" -> "<your_partitionkey_field>",
        "hoodie.datasource.write.hive_style_partitioning" -> "true",
        "hoodie.datasource.hive_sync.enable" -> "true",
        "hoodie.datasource.hive_sync.database" -> "<your_database_name>",
        "hoodie.datasource.hive_sync.table" -> "<your_table_name>",
        "hoodie.datasource.hive_sync.partition_fields" -> "<your_partitionkey_field>",
        "hoodie.datasource.hive_sync.partition_extractor_class" -> "org.apache.hudi.hive.MultiPartKeysValueExtractor",
        "hoodie.datasource.hive_sync.use_jdbc" -> "false",
        "hoodie.datasource.hive_sync.mode" -> "hms"
      )))
      .writeDataFrame(dataFrame, glueContext)
```

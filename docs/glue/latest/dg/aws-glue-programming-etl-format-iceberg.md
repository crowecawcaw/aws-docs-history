# Using the Iceberg framework in

AWS Glue

AWS Glue 3.0 and later supports the Apache Iceberg framework for data lakes. Iceberg provides
a high-performance table format that works just like a SQL table. This topic covers
available features for using your data in AWS Glue when you transport or store your data in an
Iceberg table. To learn more about Iceberg, see the official [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/ "https://iceberg.apache.org/docs/latest/").

You can use AWS Glue to perform read and write operations on Iceberg tables in Amazon S3, or work
with Iceberg tables using the AWS Glue Data Catalog. Additional operations including insert
and all [Spark
Queries](https://iceberg.apache.org/docs/latest/spark-queries/ "https://iceberg.apache.org/docs/latest/spark-queries/")
[Spark Writes](https://iceberg.apache.org/docs/latest/spark-writes/ "https://iceberg.apache.org/docs/latest/spark-writes/") are
also supported. Update is not supported for Iceberg tables.

###### Note

`ALTER TABLE … RENAME TO` is not available for Apache Iceberg 0.13.1 for
AWS Glue 3.0.

The following table lists the version of Iceberg included in each AWS Glue version.

| AWS Glue version | Supported Iceberg version |
| ---------------- | ------------------------- |
| 5.1              | 1.10.0                    |
| 5.0              | 1.7.1                     |
| 4.0              | 1.0.0                     |
| 3.0              | 0.13.1                    |

To learn more about the data lake frameworks that AWS Glue supports, see [Using data lake
frameworks with AWS Glue ETL jobs](aws-glue-programming-etl-datalake-native-frameworks.md "aws-glue-programming-etl-datalake-native-frameworks.md").

## Enabling the Iceberg

framework

To enable Iceberg for AWS Glue, complete the following tasks:

- Specify `iceberg` as a value for the
  `--datalake-formats` job parameter. For more information, see
  [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").
- Create a key named `--conf` for your AWS Glue job, and set it to the
  following value. Alternatively, you can set the following configuration using
  `SparkConf` in your script. These settings help Apache Spark
  correctly handle Iceberg tables.

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
--conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog
--conf spark.sql.catalog.glue_catalog.warehouse=s3://`<your-warehouse-dir`>/
--conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
--conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO
```

If you are reading or writing to Iceberg tables that are registered with Lake Formation, follow the guidance in [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md "security-lf-enable.md") in AWS Glue 5.0 and later. In AWS Glue 4.0, add the following configuration to enable Lake Formation support.

```
--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true
--conf spark.sql.catalog.glue_catalog.glue.id=<table-catalog-id>
```

If you use AWS Glue 3.0 with Iceberg 0.13.1, you must set the following
additional configurations to use Amazon DynamoDB lock manager to ensure atomic
transaction. AWS Glue 4.0 or later uses optimistic locking by default. For more information,
see [Iceberg AWS Integrations](https://iceberg.apache.org/docs/latest/aws/#dynamodb-lock-manager "https://iceberg.apache.org/docs/latest/aws/#dynamodb-lock-manager") in the official Apache Iceberg
documentation.

```
--conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager
--conf spark.sql.catalog.glue_catalog.lock.table=`<your-dynamodb-table-name>`
```

**Using a different Iceberg version**

To use a version of Iceberg that AWS Glue doesn't support, specify your own Iceberg JAR
files using the `--extra-jars` job parameter. Do not include
`iceberg` as a value for the `--datalake-formats`
parameter. If you use AWS Glue 5.0 or above, you must set `--user-jars-first true` job parameter.

**Enabling encryption for Iceberg tables**

###### Note

Iceberg tables have their own mechanisms to enable server-side encryption. You should enable this configuration in addition to AWS Glue's security configuration.

To enable server-side encryption on Iceberg tables, review the guidance from the [Iceberg documentation](https://iceberg.apache.org/docs/latest/aws/#s3-server-side-encryption "https://iceberg.apache.org/docs/latest/aws/#s3-server-side-encryption").

**Add Spark configuration for Iceberg cross region**

To add additional spark configuration for Iceberg cross-region table access with the AWS Glue Data Catalog and AWS Lake Formation, follow the steps below:

1. Create a [Multi-region access point](../../../AmazonS3/latest/userguide/multi-region-access-point-create-examples.md "../../../AmazonS3/latest/userguide/multi-region-access-point-create-examples.md").
2. Set the following Spark properties:

```
-----
    --conf spark.sql.catalog.my_catalog.s3.use-arn-region-enabled=true \
    --conf spark.sql.catalog.{CATALOG}.s3.access-points.bucket1", "arn:aws:s3::<account-id>:accesspoint/<mrap-id>.mrap \
    --conf spark.sql.catalog.{CATALOG}.s3.access-points.bucket2", "arn:aws:s3::<account-id>:accesspoint/<mrap-id>.mrap
-----
```

## Example: Write an

Iceberg table to Amazon S3 and register it to the AWS Glue Data Catalog

This example script demonstrates how to write an Iceberg table to Amazon S3.
The example uses [Iceberg AWS
Integrations](https://iceberg.apache.org/docs/latest/aws/ "https://iceberg.apache.org/docs/latest/aws/") to register the table to the AWS Glue Data Catalog.

Python

```
# Example: Create an Iceberg table from a DataFrame
# and register the table to Glue Data Catalog

dataFrame.createOrReplaceTempView("tmp_`<your_table_name>`")

query = f"""
CREATE TABLE glue_catalog.`<your_database_name>`.`<your_table_name>`
USING iceberg
TBLPROPERTIES ("format-version"="2")
AS SELECT * FROM tmp_`<your_table_name>`
"""
spark.sql(query)
```

Scala

```
// Example: Example: Create an Iceberg table from a DataFrame
// and register the table to Glue Data Catalog

dataFrame.createOrReplaceTempView("tmp_`<your_table_name>`")

val query = """CREATE TABLE glue_catalog.`<your_database_name>`.`<your_table_name>`
USING iceberg
TBLPROPERTIES ("format-version"="2")
AS SELECT * FROM tmp_`<your_table_name>`
"""
spark.sql(query)
```

Alternatively, you can write an Iceberg table to Amazon S3 and the Data Catalog using Spark methods.

Prerequisites: You will need to provision a catalog for the Iceberg library to use. When using the
AWS Glue Data Catalog, AWS Glue makes this straightforward. The AWS Glue Data Catalog is pre-configured for use by the Spark
libraries as `glue_catalog`. Data Catalog tables are identified by a
`databaseName` and a `tableName`. For more information
about the AWS Glue Data Catalog, see [Data discovery and cataloging in AWS Glue](catalog-and-crawler.md "catalog-and-crawler.md").

If you are not using the AWS Glue Data Catalog, you will need to provision a catalog through the Spark APIs. For more
information, see [Spark
Configuration](https://iceberg.apache.org/docs/latest/spark-configuration/ "https://iceberg.apache.org/docs/latest/spark-configuration/") in the Iceberg documentation.

This example writes an Iceberg table to Amazon S3 and the Data Catalog using Spark.

Python

```
# Example: Write an Iceberg table to S3 on the Glue Data Catalog

# Create (equivalent to CREATE TABLE AS SELECT)
dataFrame.writeTo("glue_catalog.`databaseName`.`tableName`") \
    .tableProperty("format-version", "2") \
    .create()

# Append (equivalent to INSERT INTO)
dataFrame.writeTo("glue_catalog.`databaseName`.`tableName`") \
    .tableProperty("format-version", "2") \
    .append()
```

Scala

```
// Example: Write an Iceberg table to S3 on the Glue Data Catalog

// Create (equivalent to CREATE TABLE AS SELECT)
dataFrame.writeTo("glue_catalog.`databaseName`.`tableName`")
    .tableProperty("format-version", "2")
    .create()

// Append (equivalent to INSERT INTO)
dataFrame.writeTo("glue_catalog.`databaseName`.`tableName`")
    .tableProperty("format-version", "2")
    .append()
```

## Example: Read an Iceberg

table from Amazon S3 using the AWS Glue Data Catalog

This example reads the Iceberg table that you created in [Example: Write an
Iceberg table to Amazon S3 and register it to the AWS Glue Data Catalog](#aws-glue-programming-etl-format-iceberg-write "#aws-glue-programming-etl-format-iceberg-write").

Python
For this example, use the `GlueContext.create_data_frame.from_catalog()`
method.

```
# Example: Read an Iceberg table from Glue Data Catalog

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

df = glueContext.create_data_frame.from_catalog(
    database="`<your_database_name>`",
    table_name="`<your_table_name>`",
    additional_options=additional_options
)
```

Scala
For this example, use the [getCatalogSource](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSource "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSource") method.

```
// Example: Read an Iceberg table from Glue Data Catalog

import com.amazonaws.services.glue.GlueContext
import org.apacke.spark.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    val df = glueContext.getCatalogSource("`<your_database_name>`", "`<your_table_name>`",
      additionalOptions = additionalOptions)
      .getDataFrame()
  }
}
```

## Example: Insert a

`DataFrame` into an Iceberg table in Amazon S3 using the
AWS Glue Data Catalog

This example inserts data into the Iceberg table that you created in [Example: Write an
Iceberg table to Amazon S3 and register it to the AWS Glue Data Catalog](#aws-glue-programming-etl-format-iceberg-write "#aws-glue-programming-etl-format-iceberg-write").

###### Note

This example requires you to set the `--enable-glue-datacatalog` job parameter in order to use the AWS Glue Data Catalog as an Apache Spark Hive metastore.
To learn more, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

Python
For this example, use the `GlueContext.write_data_frame.from_catalog()`
method.

```
# Example: Insert into an Iceberg table from Glue Data Catalog

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

glueContext.write_data_frame.from_catalog(
    frame=dataFrame,
    database="`<your_database_name>`",
    table_name="`<your_table_name>`",
    additional_options=additional_options
)
```

Scala
For this example, use the [getCatalogSink](glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSink "glue-etl-scala-apis-glue-gluecontext.md#glue-etl-scala-apis-glue-gluecontext-defs-getCatalogSink") method.

```
// Example: Insert into an Iceberg table from Glue Data Catalog

import com.amazonaws.services.glue.GlueContext
import org.apacke.spark.SparkContext

object GlueApp {
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    glueContext.getCatalogSink("`<your_database_name>`", "`<your_table_name>`",
      additionalOptions = additionalOptions)
      .writeDataFrame(dataFrame, glueContext)
  }
}
```

## Example: Read an

Iceberg table from Amazon S3 using Spark

Prerequisites: You will need to provision a catalog for the Iceberg library to use. When using the
AWS Glue Data Catalog, AWS Glue makes this straightforward. The AWS Glue Data Catalog is pre-configured for use by the Spark
libraries as `glue_catalog`. Data Catalog tables are identified by a
`databaseName` and a `tableName`. For more information
about the AWS Glue Data Catalog, see [Data discovery and cataloging in AWS Glue](catalog-and-crawler.md "catalog-and-crawler.md").

If you are not using the AWS Glue Data Catalog, you will need to provision a catalog through the Spark APIs. For more
information, see [Spark
Configuration](https://iceberg.apache.org/docs/latest/spark-configuration/ "https://iceberg.apache.org/docs/latest/spark-configuration/") in the Iceberg documentation.

This example reads an Iceberg table in Amazon S3 from the Data Catalog using Spark.

Python

```
# Example: Read an Iceberg table on S3 as a DataFrame from the Glue Data Catalog

dataFrame = spark.read.format("iceberg").load("glue_catalog.`databaseName`.`tableName`")
```

Scala

```
// Example: Read an Iceberg table on S3 as a DataFrame from the Glue Data Catalog

val dataFrame = spark.read.format("iceberg").load("glue_catalog.`databaseName`.`tableName`")
```

## Example: Read and write Iceberg table with Lake Formation permission control

This example reads and writes an Iceberg table with Lake Formation permission control.

###### Note

This example works only in AWS Glue 4.0. In AWS Glue 5.0 and later, follow the guidance in [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md "security-lf-enable.md").

1. Create an Iceberg table and register it in Lake Formation:
   1. To enable Lake Formation permission control, you’ll first need to register the table Amazon S3 path on Lake Formation. For more information, see [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md"). You can register it either from the Lake Formation console or by using the AWS CLI:

   ```
   aws lakeformation register-resource --resource-arn arn:aws:s3:::<s3-bucket>/<s3-folder> --use-service-linked-role --region <REGION>
   ```

   Once you register an Amazon S3 location, any AWS Glue table pointing to the location (or any of its child locations) will return the value for the `IsRegisteredWithLakeFormation` parameter as true in the `GetTable` call. 2. Create an Iceberg table that points to the registered path through Spark SQL:

   ###### Note

   The following are Python examples.

   ```
   dataFrame.createOrReplaceTempView("tmp_<your_table_name>")

   query = f"""
   CREATE TABLE glue_catalog.<your_database_name>.<your_table_name>
   USING iceberg
   AS SELECT * FROM tmp_<your_table_name>
   """
   spark.sql(query)
   ```

   You can also create the table manually through AWS Glue `CreateTable` API. For more information, see [Creating Apache Iceberg tables](../../../lake-formation/latest/dg/creating-iceberg-tables.md "../../../lake-formation/latest/dg/creating-iceberg-tables.md").

   ###### Note

   The `UpdateTable` API does not currently support Iceberg table format as an input to the operation.

2. Grant Lake Formation permission to the job IAM role. You can either grant permissions from the Lake Formation console, or using the AWS CLI. For more information, see: https://docs.aws.amazon.com/lake-formation/latest/dg/granting-table-permissions.html
3. Read an Iceberg table registered with Lake Formation. The code is same as reading a non-registered Iceberg table. Note that your AWS Glue job IAM role needs to have the SELECT permission for the read to succeed.

```
# Example: Read an Iceberg table from the AWS Glue Data Catalog
from awsglue.context import GlueContextfrom pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

df = glueContext.create_data_frame.from_catalog(
    database="<your_database_name>",
    table_name="<your_table_name>",
    additional_options=additional_options
)
```

4. Write to an Iceberg table registered with Lake Formation. The code is same as writing to a non-registered Iceberg table. Note that your AWS Glue job IAM role needs to have the SUPER permission for the write to succeed.

```
glueContext.write_data_frame.from_catalog(
    frame=dataFrame,
    database="<your_database_name>",
    table_name="<your_table_name>",
    additional_options=additional_options
)
```

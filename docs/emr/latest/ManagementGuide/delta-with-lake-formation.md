# Apache Delta Lake with fine-grained access control

Amazon EMR releases 6.15.0 and higher include support for fine-grained access control based
on AWS Lake Formation with Delta Lake when you read and write data with Spark SQL. Amazon EMR supports
table, row, column, and cell-level access control with Delta Lake. With this feature,
you can run snapshot queries on copy-on-write tables to query the latest snapshot of the
table at a given commit or compaction instant.

To use Delta Lake with Lake Formation, run the following command.

To use Delta Lake with Lake Formation on EMR 7.10 and higher, run the following command:

```
spark-sql \
   --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog
```

To use Delta Lake with Lake Formation on EMR 6.15 to 7.9, run the following

```
spark-sql \
  --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
  --conf spark.sql.catalog.spark_catalog.lf.managed=true
```

If you want Lake Formation to use record server to manage your Spark catalog,
set `spark.sql.catalog.<managed_catalog_name>.lf.managed` to true.

The following support matrix lists some core features of Delta Lake with Lake Formation:

|                                              | Copy on Write | Merge on Read |
| -------------------------------------------- | ------------- | ------------- |
| **Snapshot queries<br>• Spark<br>SQL**       | ✓             | ✓             |
| **Read-optimized queries<br>• Spark<br>SQL** | ✓             | ✓             |
| **Incremental queries**                      | Not supported | Not supported |
| **Time travel queries**                      | Not supported | Not supported |
| **Metadata tables**                          | ✓             | ✓             |
| **DML `INSERT`<br>commands**                 | ✓             | ✓             |
| **DDL commands**                             |               |               |
| **Spark datasource queries**                 |               |               |
| **Spark datasource writes**                  |               |               |

## Creating a Delta Lake table in AWS Glue Data Catalog

Amazon EMR with Lake Formation doesn't support DDL commands and Delta table creation. Follow these steps to create tables in the AWS Glue Data Catalog.

1. Use the following example to create a Delta table. Make sure that your S3 location exists.

```
spark-sql \
--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

> CREATE DATABASE if not exists `<DATABASE_NAME>` LOCATION 's3://`<S3_LOCATION>`/transactionaldata/native-delta/`<DATABASE_NAME>`/';
> CREATE TABLE `<TABLE_NAME>` (x INT, y STRING, z STRING) USING delta;
> INSERT INTO `<TABLE_NAME>` VALUES (1, 'a1', 'b1');
```

2. To see the details of your table, go to [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
3. In the left navigation, expand **Data Catalog**, choose **Tables**,
   then choose the table you created. Under **Schema**, you should see that the Delta table you created with Spark stores all columns in a data type of `array<string>` in AWS Glue.
4. To define column and cell-level filters in Lake Formation, remove the `col` column from your schema, and then
   add the columns that are in your table schema. In this example, add the columns `x`, `y`, and `z`.

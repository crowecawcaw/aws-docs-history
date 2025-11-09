# Apache Iceberg with fine-grained access control

Amazon EMR releases 6.15.0 and higher include support for fine-grained access control based
on AWS Lake Formation with Apache Iceberg when you read and write data with Spark SQL. Amazon EMR
supports table, row, column, and cell-level access control with Apache Iceberg. With
this feature, you can run snapshot queries on copy-on-write tables to query the latest
snapshot of the table at a given commit or compaction instant.

If you want to use Iceberg format, set the following configurations. Replace
`DB_LOCATION` with the Amazon S3 path where
your Iceberg tables are located, and replace the region and account ID placeholders with
your own values.

```
spark-sql \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
--conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog
--conf spark.sql.catalog.spark_catalog.warehouse=s3://`DB_LOCATION`
--conf spark.sql.catalog.spark_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
--conf spark.sql.catalog.spark_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO
--conf spark.sql.catalog.spark_catalog.glue.account-id=`ACCOUNT_ID`
--conf spark.sql.catalog.spark_catalog.glue.id=`ACCOUNT_ID`
--conf spark.sql.catalog.spark_catalog.client.region=`AWS_REGION`

```

If you want to use Iceberg format on earlier EMR versions, use the following command instead:

```
spark-sql \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension
--conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkCatalog
--conf spark.sql.catalog.spark_catalog.warehouse=s3://`DB_LOCATION`
--conf spark.sql.catalog.spark_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
--conf spark.sql.catalog.spark_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO
--conf spark.sql.catalog.spark_catalog.glue.account-id=`ACCOUNT_ID`
--conf spark.sql.catalog.spark_catalog.glue.id=`ACCOUNT_ID`
--conf spark.sql.catalog.spark_catalog.client.assume-role.region=`AWS_REGION`
--conf spark.sql.catalog.spark_catalog.lf.managed=true

```

The following support matrix lists some core features of Apache Iceberg with
Lake Formation:

|                                              | Copy on Write | Merge on Read |
| -------------------------------------------- | ------------- | ------------- |
| **Snapshot queries<br>• Spark<br>SQL**       | ✓             | ✓             |
| **Read-optimized queries<br>• Spark<br>SQL** | ✓             | ✓             |
| **Incremental queries**                      | ✓             | ✓             |
| **Time travel queries**                      | ✓             | ✓             |
| **Metadata tables**                          | ✓             | ✓             |
| **DML `INSERT`<br>commands**                 | ✓             | ✓             |
| **DDL commands**                             |               |               |
| **Spark datasource queries**                 |               |               |
| **Spark datasource writes**                  |               |               |

# Open-table format support

Amazon EMR releases 6.15.0 and higher include support for fine-grained access control
based on AWS Lake Formation with Hive tables, Apache Iceberg, Apache Hudi, and Delta Lake when
you read and write data with Spark SQL. Amazon EMR supports table, row, column, and
cell-level access control with Apache Hudi. Amazon EMR releases 6.15.0 and higher include
support for fine-grained access control at the row, column, or cell level based on
AWS Lake Formation. Starting with EMR 7.12, DML and DDL operations that modify table data
are supported for Apache Hive, Apache Iceberg, and Delta Lake tables using Lake
Formation vended credentials.

The topics in this section cover how you can access Lake Formation registered tables in open
table formats from EMR Spark jobs or interactive sessions with fine-grained access
control.

## Permission requirements

### Tables not registered in AWS Lake Formation

For tables not registered with AWS Lake Formation, the job runtime role accesses both
the AWS Glue Data Catalog and the underlying table data in Amazon S3. This requires the
job runtime role to have appropriate IAM permissions for both AWS Glue and Amazon
S3 operations.

### Tables registered in AWS Lake Formation

For tables registered with AWS Lake Formation, the job runtime role accesses the
AWS Glue Data Catalog metadata, while temporary credentials vended by Lake Formation
access the underlying table data in Amazon S3. The Lake Formation permissions
required to execute an operation depend on the AWS Glue Data Catalog and Amazon S3 API
calls that the Spark job initiates and can be summarized as follows:

- **DESCRIBE** permission allows the
  runtime role to read table or database metadata in the Data
  Catalog
- **ALTER** permission allows the runtime
  role to modify table or database metadata in the Data Catalog

- **DROP** permission allows the runtime
  role to delete table or database metadata from the Data Catalog
- **SELECT** permission allows the runtime
  role to read table data from Amazon S3
- **INSERT** permission allows the runtime
  role to write table data to Amazon S3
- **DELETE** permission allows the runtime
  role to delete table data from Amazon S3

###### Note

Lake Formation evaluates permissions lazily when a Spark job calls
AWS Glue to retrieve table metadata and Amazon S3 to retrieve table
data. Jobs that use a runtime role with insufficient permissions
will not fail until Spark makes an AWS Glue or Amazon S3 call that
requires the missing permission.

###### Note

In the following supported table matrix:

- Operations marked as **Supported**
  exclusively use Lake Formation credentials to access table data for
  tables registered with Lake Formation. If Lake Formation permissions are
  insufficient, the operation will not fall back to runtime role
  credentials. For tables not registered with Lake Formation, the job
  runtime role credentials access the table data.

- Operations marked as **Supported with IAM
  permissions on Amazon S3 location** do not use Lake
  Formation credentials to access underlying table data in Amazon S3. To
  run these operations, the job runtime role must have the necessary
  Amazon S3 IAM permissions to access the table data, regardless of
  whether the table is registered with Lake Formation.

Hive

| Operation                               | AWS Lake Formation permissions      | Support status                                                                                                                                                                                                                                                            |
| --------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SELECT                                  | SELECT                              | Supported                                                                                                                                                                                                                                                                 |
| CREATE TABLE                            | CREATE_TABLE                        | Supported                                                                                                                                                                                                                                                                 |
| CREATE TABLE LIKE                       | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                   |
| CREATE TABLE AS SELECT                  | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                   |
| DESCRIBE TABLE                          | DESCRIBE                            | Supported                                                                                                                                                                                                                                                                 |
| SHOW TBLPROPERTIES                      | DESCRIBE                            | Supported                                                                                                                                                                                                                                                                 |
| SHOW COLUMNS                            | DESCRIBE                            | Supported                                                                                                                                                                                                                                                                 |
| SHOW PARTITIONS                         | DESCRIBE                            | Supported                                                                                                                                                                                                                                                                 |
| SHOW CREATE TABLE                       | DESCRIBE                            | Supported                                                                                                                                                                                                                                                                 |
| ALTER TABLE<br>`tablename`              | SELECT and ALTER                    | Supported                                                                                                                                                                                                                                                                 |
| ALTER TABLE `tablename` SET<br>LOCATION | -                                   | Not supported                                                                                                                                                                                                                                                             |
| ALTER TABLE `tablename`ADD<br>PARTITION | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                 |
| REPAIR TABLE                            | SELECT and ALTER                    | Supported                                                                                                                                                                                                                                                                 |
| LOAD DATA                               |                                     | Not supported                                                                                                                                                                                                                                                             |
| INSERT                                  | INSERT and ALTER                    | Supported                                                                                                                                                                                                                                                                 |
| INSERT OVERWRITE                        | SELECT, INSERT, DELETE and ALTER    | Supported                                                                                                                                                                                                                                                                 |
| DROP TABLE                              | SELECT, DROP, DELETE and ALTER      | Supported                                                                                                                                                                                                                                                                 |
| TRUNCATE TABLE                          | SELECT, INSERT, DELETE and ALTER    | Supported                                                                                                                                                                                                                                                                 |
| Dataframe Writer V1                     | Same as corresponding SQL operation | Supported when appending data to an existing<br>table. Refer to [considerations and limitations](../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md "../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md") for more<br>information |
| Dataframe Writer V2                     | Same as corresponding SQL operation | Supported when appending data to an existing<br>table. Refer to [considerations and limitations](../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md "../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md") for more<br>information |

Iceberg

| Operation                           | AWS Lake Formation permissions      | Support status                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SELECT                              | SELECT                              | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| CREATE TABLE                        | CREATE_TABLE                        | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| CREATE TABLE LIKE                   | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| CREATE TABLE AS SELECT              | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| REPLACE TABLE AS SELECT             | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| DESCRIBE TABLE                      | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| SHOW TBLPROPERTIES                  | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| SHOW CREATE TABLE                   | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| ALTER TABLE                         | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| ALTER TABLE SET LOCATION            | SELECT, INSERT and ALTER            | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| ALTER TABLE WRITE ORDERED BY        | SELECT, INSERT and ALTER            | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| ALTER TABLE WRITE DISTRIBUTED<br>BY | SELECT, INSERT, and ALTER           | Supported with IAM permissions on<br>Amazon S3 location                                                                                                                                                                                                                                                                                                                                              |
| ALTER TABLE RENAME TABLE            | CREATE_TABLE, and DROP              | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| INSERT INTO                         | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| INSERT OVERWRITE                    | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| DELETE                              | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| UPDATE                              | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| MERGE INTO                          | SELECT, INSERT and ALTER            | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| DROP TABLE                          | SELECT, DELETE and DROP             | Supported                                                                                                                                                                                                                                                                                                                                                                                            |
| DataFrame Writer V1                 | -                                   | Not supported                                                                                                                                                                                                                                                                                                                                                                                        |
| DataFrame Writer V2                 | Same as corresponding SQL operation | Supported when appending data to an existing<br>table. Refer to [considerations and limitations](../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md "../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md") for more<br>information.                                                                                                                           |
| Metadata tables                     | SELECT                              | Supported. Certain tables are hidden.<br>Refer to [considerations and limitations](../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md "../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md") for more<br>information.                                                                                                                                         |
| Stored procedures                   | -                                   | Supported for tables that meet the<br>following conditions:<br>• Tables not registered in AWS Lake Formation<br>• Tables that do not use<br>`register_table` and<br>`migrate`<br>Refer to [considerations and limitations](../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md "../EMR-Serverless-UserGuide/emr-serverless-lf-enable-considerations.md") for more<br>information. |

**Spark configuration for Iceberg:** If
you want to use Iceberg format, set the following configurations.
Replace `DB_LOCATION` with the
Amazon S3 path where your Iceberg tables are located, and replace the region
and account ID placeholders with your own values.

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

If you want to use Iceberg format on earlier EMR versions, use the
following command instead:

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

**Examples:**

Here are some examples of working with Iceberg tables:

```
-- Create an Iceberg table
CREATE TABLE my_iceberg_table (
    id BIGINT,
    name STRING,
    created_at TIMESTAMP
) USING ICEBERG;

-- Insert data
INSERT INTO my_iceberg_table VALUES (1, 'Alice', current_timestamp());

-- Query the table
SELECT * FROM my_iceberg_table;
```

Hudi

| Operation                                 | AWS Lake Formation permissions      | Support status                                          |
| ----------------------------------------- | ----------------------------------- | ------------------------------------------------------- |
| SELECT                                    | SELECT                              | Supported                                               |
| CREATE TABLE                              | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location |
| CREATE TABLE LIKE                         | CREATE_TABLE                        | Supported with IAM permissions on<br>Amazon S3 location |
| CREATE TABLE AS SELECT                    | -                                   | Not supported                                           |
| DESCRIBE TABLE                            | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW TBLPROPERTIES                        | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW COLUMNS                              | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW CREATE TABLE                         | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| ALTER TABLE                               | SELECT                              | Supported with IAM permissions on<br>Amazon S3 location |
| INSERT INTO                               | SELECT and ALTER                    | Supported with IAM permissions on<br>Amazon S3 location |
| INSERT OVERWRITE                          | SELECT and ALTER                    | Supported with IAM permissions on<br>Amazon S3 location |
| DELETE                                    | -                                   | Not supported                                           |
| UPDATE                                    | -                                   | Not supported                                           |
| MERGE INTO                                | -                                   | Not supported                                           |
| DROP TABLE                                | SELECT and DROP                     | Supported with IAM permissions on<br>Amazon S3 location |
| DataFrame Writer V1                       | -                                   | Not supported                                           |
| DataFrame Writer V2                       | Same as corresponding SQL operation | Supported with IAM permissions on<br>Amazon S3 location |
| Metadata tables                           | -                                   | Not supported                                           |
| Table maintenance and utility<br>features | -                                   | Not supported                                           |

**Spark configuration for Hudi:**

To start the Spark shell on EMR 7.10 or higher versions, use the
following command:

```
spark-sql
--jars /usr/lib/hudi/hudi-spark-bundle.jar \
--conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog \
--conf spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension
```

To start the Spark shell on earlier EMR versions, use the below
command instead:

```
spark-sql
--jars /usr/lib/hudi/hudi-spark-bundle.jar \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
--conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog \
--conf spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension  \
--conf spark.sql.catalog.spark_catalog.lf.managed=true
```

**Examples:**

Here are some examples of working with Hudi tables:

```
-- Create a Hudi table
CREATE TABLE my_hudi_table (
    id BIGINT,
    name STRING,
    created_at TIMESTAMP
) USING HUDI
TBLPROPERTIES (
    'type' = 'cow',
    'primaryKey' = 'id'
);

-- Insert data
INSERT INTO my_hudi_table VALUES (1, 'Alice', current_timestamp());

-- Query the latest snapshot
SELECT * FROM my_hudi_table;
```

To query the latest snapshot of copy-on-write tables:

```
SELECT * FROM `my_hudi_cow_table`
```

```
spark.read.table("`my_hudi_cow_table`")
```

To query the latest compacted data of `MOR` tables, you can
query the read-optimized table that is suffixed with
`_ro`:

```
SELECT * FROM `my_hudi_mor_table`_ro
```

```
spark.read.table("`my_hudi_mor_table`_ro")
```

Delta Lake

| Operation                                  | AWS Lake Formation permissions      | Support status                                          |
| ------------------------------------------ | ----------------------------------- | ------------------------------------------------------- |
| SELECT                                     | SELECT                              | Supported                                               |
| CREATE TABLE                               | CREATE_TABLE                        | Supported                                               |
| CREATE TABLE LIKE                          | -                                   | Not supported                                           |
| CREATE TABLE AS SELECT                     | CREATE_TABLE                        | Supported                                               |
| REPLACE TABLE AS SELECT                    | SELECT, INSERT and ALTER            | Supported                                               |
| DESCRIBE TABLE                             | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW TBLPROPERTIES                         | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW COLUMNS                               | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| SHOW CREATE TABLE                          | DESCRIBE                            | Supported with IAM permissions on<br>Amazon S3 location |
| ALTER TABLE                                | SELECT and INSERT                   | Supported                                               |
| ALTER TABLE SET LOCATION                   | SELECT and INSERT                   | Supported with IAM permissions on<br>Amazon S3 location |
| ALTER TABLE `tablename`<br>CLUSTER BY      | SELECT and INSERT                   | Supported with IAM permissions on<br>Amazon S3 location |
| ALTER TABLE `tablename` ADD<br>CONSTRAINT  | SELECT and INSERT                   | Supported with IAM permissions on<br>Amazon S3 location |
| ALTER TABLE `tablename`<br>DROP CONSTRAINT | SELECT and INSERT                   | Supported with IAM permissions on<br>Amazon S3 location |
| INSERT INTO                                | SELECT and INSERT                   | Supported                                               |
| INSERT OVERWRITE                           | SELECT and INSERT                   | Supported                                               |
| DELETE                                     | SELECT and INSERT                   | Supported                                               |
| UPDATE                                     | SELECT and INSERT                   | Supported                                               |
| MERGE INTO                                 | SELECT and INSERT                   | Supported                                               |
| DROP TABLE                                 | SELECT, DELETE and DROP             | Supported                                               |
| DataFrame Writer V1                        | -                                   | Not supported                                           |
| DataFrame Writer V2                        | Same as corresponding SQL operation | Supported                                               |
| Table maintenance and utility<br>features  | -                                   | Not supported                                           |

**Spark configuration for Delta
Lake:**

To use Delta Lake with Lake Formation on EMR 7.10 and higher, run the
following command:

```
spark-sql \
   --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog
```

To use Delta Lake with Lake Formation on EMR 6.15 to 7.9, run the
following

```
spark-sql \
  --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
  --conf spark.sql.catalog.spark_catalog.lf.managed=true
```

If you want Lake Formation to use record server to manage your Spark catalog,
set
`spark.sql.catalog.<managed_catalog_name>.lf.managed`
to true.

**Examples:**

Here are some examples of working with Delta Lake tables:

```
-- Create a Delta Lake table
CREATE TABLE my_delta_table (
    id BIGINT,
    name STRING,
    created_at TIMESTAMP
) USING DELTA;

-- Insert data
INSERT INTO my_delta_table VALUES (1, 'Alice', current_timestamp());

-- Query the table
SELECT * FROM my_delta_table;

-- Update data
UPDATE my_delta_table SET name = 'Alice Smith' WHERE id = 1;

-- Merge data
MERGE INTO my_delta_table AS target
USING (SELECT 2 as id, 'Bob' as name, current_timestamp() as created_at) AS source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

**Creating a Delta Lake table in
AWS Glue Data Catalog**

Amazon EMR with Lake Formation doesn't support DDL commands and Delta table creation
in EMR releases earlier than 7.12. Follow these steps to create tables
in the AWS Glue Data Catalog.

1. Use the following example to create a Delta table. Make sure
   that your S3 location exists.

```
spark-sql \
--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

> CREATE DATABASE if not exists `<DATABASE_NAME>` LOCATION 's3://`<S3_LOCATION>`/transactionaldata/native-delta/`<DATABASE_NAME>`/';
> CREATE TABLE `<TABLE_NAME>` (x INT, y STRING, z STRING) USING delta;
> INSERT INTO `<TABLE_NAME>` VALUES (1, 'a1', 'b1');
```

2. To see the details of your table, go to
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
3. In the left navigation, expand **Data Catalog**,
   choose **Tables**, then choose the table you
   created. Under **Schema**, you should see that
   the Delta table you created with Spark stores all columns in a
   data type of `array<string>` in AWS Glue.
4. To define column and cell-level filters in Lake Formation, remove the
   `col` column from your schema, and then add the
   columns that are in your table schema. In this example, add the
   columns `x`, `y`, and
   `z`.

With this feature, you can run snapshot queries on copy-on-write tables to query
the latest snapshot of the table at a given commit or compaction instant. Currently,
a Lake Formation-enabled Amazon EMR cluster must retrieve Hudi's commit time column to perform
incremental queries and time travel queries. It doesn't support Spark's
`timestamp as of` syntax and the `Spark.read()` function.
The correct syntax is `select * from table where _hoodie_commit_time <=
 point_in_time`. For more information, see [Point in time Time-Travel queries on Hudi table](https://cwiki.apache.org/confluence/display/HUDI/RFC+-+07+%3A+Point+in+time+Time-Travel+queries+on+Hudi+table "https://cwiki.apache.org/confluence/display/HUDI/RFC+-+07+%3A+Point+in+time+Time-Travel+queries+on+Hudi+table").

###### Note

The performance of reads on Lake Formation clusters might be slower because of
optimizations that are not supported. These features include file listing based
on Hudi metadata, and data skipping. We recommend that you test your application
performance to ensure that it meets your requirements.

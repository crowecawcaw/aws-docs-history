# Accessing Amazon S3 tables with the Amazon S3 Tables Catalog for Apache Iceberg

You can access S3 tables from open source query engines like Apache Spark by using the
Amazon S3 Tables Catalog for Apache Iceberg client catalog. Amazon S3 Tables Catalog for Apache Iceberg is an open source library
hosted by AWS Labs. It works by translating Apache Iceberg operations in your query
engines (such as table discovery, metadata updates, and adding or removing tables) into
S3 Tables API operations.

Amazon S3 Tables Catalog for Apache Iceberg is distributed as a Maven JAR called
`s3-tables-catalog-for-iceberg.jar`. You can build the client catalog JAR from the [AWS Labs GitHub repository](https://github.com/awslabs/s3-tables-catalog "https://github.com/awslabs/s3-tables-catalog") or download it from [Maven](https://mvnrepository.com/artifact/software.amazon.s3tables/s3-tables-catalog-for-iceberg "https://mvnrepository.com/artifact/software.amazon.s3tables/s3-tables-catalog-for-iceberg"). When connecting to tables, the client catalog JAR is used as a dependency when you initialize a Spark session for Apache Iceberg.

## Using the Amazon S3 Tables Catalog for Apache Iceberg with Apache Spark

You can use the Amazon S3 Tables Catalog for Apache Iceberg client catalog to connect to tables from
open-source applications when you initialize a Spark session. In your session configuration you specify Iceberg and Amazon S3 dependencies, and create a custom catalog that uses your table bucket as the metadata warehouse.

###### **Prerequisites**

- An IAM identity with access to your table bucket and S3 Tables actions. For more information, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").

###### To initialize a Spark session using the Amazon S3 Tables Catalog for Apache Iceberg

- Initialize Spark using the following command. To use the command, replace the
  replace the Amazon S3 Tables Catalog for Apache Iceberg `version number` with the latest version from [AWS Labs GitHub repository](https://github.com/awslabs/s3-tables-catalog "https://github.com/awslabs/s3-tables-catalog"), and the `table bucket ARN` with your own table bucket
  ARN.

```
spark-shell \
--packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1,software.amazon.s3tables:s3-tables-catalog-for-iceberg-runtime:`0.1.4` \
--conf spark.sql.catalog.`s3tablesbucket`=org.apache.iceberg.spark.SparkCatalog \
--conf spark.sql.catalog.`s3tablesbucket`.catalog-impl=software.amazon.s3tables.iceberg.S3TablesCatalog \
--conf spark.sql.catalog.`s3tablesbucket`.warehouse=arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket` \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

### Querying S3 tables with Spark SQL

Using Spark, you can run DQL, DML, and DDL operations on S3 tables. When you query tables you use the fully qualified table name, including the session catalog name following this pattern:

``CatalogName`.`NamespaceName`.`TableName``

The following
example queries show some ways you can interact with S3 tables. To use these example queries in your
query engine, replace the `user input placeholder` values with your own.

###### To query tables with Spark

- Create a namespace

```
spark.sql(" CREATE NAMESPACE IF NOT EXISTS `s3tablesbucket`.`my_namespace`")
```

- Create a table

```
spark.sql(" CREATE TABLE IF NOT EXISTS `s3tablesbucket`.`my_namespace`.``my_table``
( id INT, name STRING, value INT ) USING iceberg ")
```

- Query a table

```
spark.sql(" SELECT * FROM `s3tablesbucket`.`my_namespace`.``my_table`` ").show()
```

- Insert data into a table

```
spark.sql(
"""
    INSERT INTO `s3tablesbucket`.`my_namespace`.`my_table`
    VALUES
        (1, 'ABC', 100),
        (2, 'XYZ', 200)
""")
```

- Load an existing data file into a table
  1.  Read the data into Spark.

  ```
  val data_file_location = "Path such as S3 URI to data file"
  val data_file = spark.read.parquet(`data_file_location`)
  ```

  2.  Write the data into an Iceberg table.

  ```
  data_file.writeTo("`s3tablesbucket`.`my_namespace`.`my_table`").using("Iceberg").tableProperty ("format-version", "2").createOrReplace()
  ```

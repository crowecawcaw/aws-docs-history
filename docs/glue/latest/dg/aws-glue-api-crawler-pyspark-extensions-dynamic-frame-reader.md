# DynamicFrameReader class

##  — methods —

- [\_\_init\_\_](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-__init__ "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-__init__")
- [from_rdd](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_rdd "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_rdd")
- [from_options](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_options "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_options")
- [from_catalog](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_catalog "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader-from_catalog")

## \_\_init\_\_

###### `__init__(glue_context)`

- `glue_context` – The [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") to use.

## from_rdd

###### `from_rdd(data, name, schema=None, sampleRatio=None)`

Reads a `DynamicFrame` from a Resilient Distributed Dataset (RDD).

- `data` – The dataset to read from.
- `name` – The name to read from.
- `schema` – The schema to read (optional).
- `sampleRatio` – The sample ratio (optional).

## from_options

###### `from_options(connection_type, connection_options={}, format=None,

format_options={}, transformation_ctx="")`

Reads a `DynamicFrame` using the specified connection and format.

- `connection_type` – The connection type.
  Valid values include `s3`, `mysql`, `postgresql`, `redshift`, `sqlserver`, `oracle`, `dynamodb`,
  and `snowflake`.
- `connection_options` – Connection options, such as path and database table
  (optional). For more information, see
  [Connection types and options for ETL in AWS Glue for Spark](aws-glue-programming-etl-connect.md "aws-glue-programming-etl-connect.md") .
  For a `connection_type` of `s3`, Amazon S3 paths are defined in an array.

```
connection_options = {"paths": [ "`s3://amzn-s3-demo-bucket/object_a`", "`s3://amzn-s3-demo-bucket/object_b`"]}
```

For JDBC connections, several properties must be defined. Note that the database name must be part of the URL. It can optionally be included in the connection options.

###### Warning

Storing passwords in your script is not recommended. Consider using `boto3` to retrieve them from AWS Secrets Manager or the AWS Glue Data Catalog.

```
connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`"}
```

For a JDBC connection that performs parallel reads, you can set the hashfield option. For example:

```
connection_options = {"url": "`jdbc-url/database`", "user": "`username`", "password": `passwordVariable`,"dbtable": "`table-name`", "redshiftTmpDir": "`s3-tempdir-path`" , "hashfield": "`month`"}
```

For more information, see [Reading from JDBC tables in parallel](run-jdbc-parallel-read-job.md "run-jdbc-parallel-read-job.md").

- `format` – A format specification (optional). This is used
  for an Amazon Simple Storage Service (Amazon S3) or an AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – The transformation context to use (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset. For more information, see [Pre-Filtering Using Pushdown Predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").

## from_catalog

###### `from_catalog(database, table_name, redshift_tmp_dir="", transformation_ctx="", push_down_predicate="", additional_options={})`

Reads a `DynamicFrame` using the specified catalog namespace and table
name.

- `database` – The database to read from.
- `table_name` – The name of the table to read from.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional if not
  reading data from Redshift).
- `transformation_ctx` – The transformation context to use (optional).
- `push_down_predicate` – Filters partitions without having to list and read all the files in your dataset.
  For more information, see [Pre-filtering using pushdown
  predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-pushdowns").
- `additional_options` – Additional options provided to AWS Glue.
  - To use a JDBC connection that performs parallel reads, you can set the
    `hashfield`, `hashexpression`, or `hashpartitions`
    options. For example:

  ```
  additional_options = {"hashfield": "`month`"}
  ```

  For more information, see [Reading from JDBC tables in parallel](run-jdbc-parallel-read-job.md "run-jdbc-parallel-read-job.md").
  - To pass a catalog expression to filter based on the index columns, you can see the
    `catalogPartitionPredicate` option.

  `catalogPartitionPredicate` — You can pass a catalog
  expression to filter based on the index columns. This pushes down the filtering to the
  server side. For more information, see [AWS Glue Partition Indexes](partition-indexes.md "partition-indexes.md"). Note that
  `push_down_predicate` and `catalogPartitionPredicate` use
  different syntaxes. The former one uses Spark SQL standard syntax and the later one
  uses JSQL parser.

  For more information, see [Managing partitions for ETL output in AWS Glue](aws-glue-programming-etl-partitions.md "aws-glue-programming-etl-partitions.md").

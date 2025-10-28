# DynamicFrameWriter class

##  methods

- [\_\_init\_\_](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-__init__ "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-__init__")
- [from_options](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_options "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_options")
- [from_catalog](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_catalog "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_catalog")
- [from_jdbc_conf](#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_jdbc_conf "#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_jdbc_conf")

## \_\_init\_\_

###### `__init__(glue_context)`

- `glue_context` – The [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") to use.

## from_options

###### `from_options(frame, connection_type, connection_options={},

format=None, format_options={}, transformation_ctx="")`

Writes a `DynamicFrame` using the specified connection and format.

- `frame` – The `DynamicFrame` to write.
- `connection_type` – The connection type.
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

- `format` – A format specification (optional). This is used
  for an Amazon Simple Storage Service (Amazon S3) or an AWS Glue connection that supports multiple formats. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `format_options` – Format options for the specified format. See [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md")
  for the formats that are supported.
- `transformation_ctx` – A transformation context to use (optional).

## from_catalog

###### `from_catalog(frame, name_space, table_name, redshift_tmp_dir="", transformation_ctx="")`

Writes a `DynamicFrame` using the specified catalog database and table
name.

- `frame` – The `DynamicFrame` to write.
- `name_space` – The database to use.
- `table_name` – The `table_name` to use.
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use
  (optional).
- `transformation_ctx` – A transformation context to use (optional).
- `additional_options` – Additional options provided to
  AWS Glue.

To write to Lake Formation governed tables, you can use these additional
options:

    + `transactionId` – (String) The transaction ID at which to do the
     write to the Governed table. This transaction can not be already committed or aborted,
     or the write will fail.
    + `callDeleteObjectsOnCancel`  – (Boolean, optional) If set to
     `true` (default), AWS Glue automatically calls the
     `DeleteObjectsOnCancel` API after the object is written to
     Amazon S3. For more information, see [DeleteObjectsOnCancel](../../../lake-formation/latest/dg/aws-lake-formation-api-transactions-api.md#aws-lake-formation-api-transactions-api-DeleteObjectsOnCancel "../../../lake-formation/latest/dg/aws-lake-formation-api-transactions-api.md#aws-lake-formation-api-transactions-api-DeleteObjectsOnCancel") in the
     *AWS Lake Formation Developer Guide*.

###### Example: Writing to a governed table in Lake Formation

```
txId = glueContext.start_transaction(read_only=False)
glueContext.write_dynamic_frame.from_catalog(
    frame=dyf,
    database = db,
    table_name = tbl,
    transformation_ctx = "datasource0",
    additional_options={"transactionId":txId})
...
glueContext.commit_transaction(txId)
```

## from_jdbc_conf

###### `from_jdbc_conf(frame, catalog_connection, connection_options={}, redshift_tmp_dir = "", transformation_ctx="")`

Writes a `DynamicFrame` using the specified JDBC connection
information.

- `frame` – The `DynamicFrame` to write.
- `catalog_connection` – A catalog connection to use.
- `connection_options` – Connection options, such as path and database table
  (optional).
- `redshift_tmp_dir` – An Amazon Redshift temporary directory to use (optional).
- `transformation_ctx` – A transformation context to use (optional).

## Example for write_dynamic_frame

This example writes the output locally using a `connection_type` of S3 with a
POSIX path argument in `connection_options`, which allows writing to local
storage.

```
glueContext.write_dynamic_frame.from_options(\
frame = dyf_splitFields,\
connection_options = {'path': '/home/glue/GlueLocalOutput/'},\
connection_type = 's3',\
format = 'json')
```

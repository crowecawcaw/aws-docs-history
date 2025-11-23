# Create tables in Athena

To create tables, you can run DDL statements in the Athena console, use the Athena [Create table
form](creating-tables-how-to.md#to-create-a-table-using-the-wizard "creating-tables-how-to.md#to-create-a-table-using-the-wizard"), or use a JDBC or an ODBC driver. Athena uses Apache Hive to define tables
and create databases, which are essentially a logical namespace of tables. Athena supports a
variety of serializer-deserializer (SerDe) libraries for creating tables for specific data
formats. For a list of supported SerDe libraries, see [Choose a SerDe for your data](supported-serdes.md "supported-serdes.md").

When you create a database and table in Athena, you are simply describing the schema and
the location where the table data are located in Amazon S3 for read-time querying. Athena does not
modify your data in Amazon S3. Database and table, therefore, have a slightly different meaning
than they do for traditional relational database systems because the data isn't stored along
with the schema definition for the database and table.

Athena stores the schema in the AWS Glue Data Catalog and uses it to read the data when you query the
table using SQL. This _schema-on-read_ approach, which projects a schema
onto your data when you run a query, eliminates the need for data loading or
transformation.

## Considerations and

limitations

Following are some important limitations and considerations for tables in
Athena.

### Amazon S3 considerations

When you create a table, you specify an Amazon S3 bucket location for the underlying
data using the `LOCATION` clause. Consider the following:

- Athena can only query the latest version of data on a versioned Amazon S3
  bucket, and cannot query previous versions of the data.
- You must have permissions to work with data in the Amazon S3 location. For more
  information, see [Control access to Amazon S3 from Athena](s3-permissions.md "s3-permissions.md").
- Athena supports querying objects that are stored with multiple storage
  classes in the same bucket specified by the `LOCATION` clause.
  For example, you can query data in objects that are stored in different
  Storage classes (Standard, Standard-IA and Intelligent-Tiering) in
  Amazon S3.
- Athena supports [Requester Pays buckets](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md"). For information how to enable Requester
  Pays for buckets with source data you intend to query in Athena, see [Create a workgroup](creating-workgroups.md "creating-workgroups.md").
- You can use Athena to query restored objects from the Amazon Glacier Flexible
  Retrieval (formerly Glacier) and Amazon Glacier Deep Archive [Amazon S3
  storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-glacier "../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-glacier") but you must enable the capability on a
  per-table basis. If you do not enable the feature on a table before you run
  a query, Athena skips all of the table's Amazon Glacier Flexible Retrieval and Amazon Glacier
  Deep Archive objects during query execution. For more information, see [Query restored Amazon Glacier objects](querying-glacier.md "querying-glacier.md").

For information about storage classes, see [Storage classes](../../../AmazonS3/latest/dev/storage-class-intro.md "../../../AmazonS3/latest/dev/storage-class-intro.md"), [Changing
the storage class of an object in amazon S3](../../../AmazonS3/latest/dev/ChgStoClsOfObj.md "../../../AmazonS3/latest/dev/ChgStoClsOfObj.md"), [Transitioning to the GLACIER storage class (object archival)](../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md#before-deciding-to-archive-objects "../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md#before-deciding-to-archive-objects"),
and [Requester Pays buckets](../../../AmazonS3/latest/dev/RequesterPaysBuckets.md "../../../AmazonS3/latest/dev/RequesterPaysBuckets.md") in the
_Amazon Simple Storage Service User Guide_.

- If you issue queries against Amazon S3 buckets with a large number of objects
  and the data is not partitioned, such queries may affect the Get request
  rate limits in Amazon S3 and lead to Amazon S3 exceptions. To prevent errors,
  partition your data. Additionally, consider tuning your Amazon S3 request rates.
  For more information, see [Request rate and performance considerations](../../../AmazonS3/latest/dev/request-rate-perf-considerations.md "../../../AmazonS3/latest/dev/request-rate-perf-considerations.md").

For more information about specifying a location for your data in Amazon S3, see [Specify a table location in Amazon S3](tables-location-format.md "tables-location-format.md").

### Other considerations

- Transactional data transformations not
  supported – Athena does not support transaction-based
  operations (such as the ones found in Hive or Presto) on table data. For a
  full list of keywords not supported, see [Unsupported DDL](unsupported-ddl.md "unsupported-ddl.md").
- Operations on tables are ACID – When
  you create, update, or delete tables, those operations are guaranteed
  ACID-compliant. For example, if multiple users or clients attempt to create
  or alter an existing table at the same time, only one will be
  successful.
- Tables are EXTERNAL – Except when
  creating [Iceberg](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md") tables,
  always use the `EXTERNAL` keyword. If you use `CREATE
TABLE` without the `EXTERNAL` keyword for non-Iceberg
  tables, Athena issues an error. When you drop a table in Athena, only the
  table metadata is removed; the data remains in Amazon S3.
- Maximum query string length – The
  maximum query string length is 256 KB.
- If you use the AWS Glue [CreateTable](../../../glue/latest/webapi/API_CreateTable.md "../../../glue/latest/webapi/API_CreateTable.md") API operation
  or the CloudFormation [`AWS::Glue::Table`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md") template to create a table for use in Athena without
  specifying the `TableType` property and then run a DDL query like
  `SHOW CREATE TABLE` or `MSCK REPAIR TABLE`, you can
  receive the error message **`FAILED: NullPointerException Name is
null`**.

To resolve the error, specify a value for the [TableInput](../../../glue/latest/webapi/API_TableInput.md "../../../glue/latest/webapi/API_TableInput.md")
`TableType` attribute as part of the AWS Glue `CreateTable` API
call or [CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md"). Possible values for `TableType` include
`EXTERNAL_TABLE` or `VIRTUAL_VIEW`.

This requirement applies only when you create a table using the AWS Glue
`CreateTable` API operation or the `AWS::Glue::Table`
template. If you create a table for Athena by using a DDL statement or an AWS Glue
crawler, the `TableType` property is defined for
you automatically.

###### Topics

- [Create tables using AWS Glue or the Athena
  console](creating-tables-how-to.md "creating-tables-how-to.md")
- [Specify a table location in Amazon S3](tables-location-format.md "tables-location-format.md")
- [Show table information after
  creation](creating-tables-showing-table-information.md "creating-tables-showing-table-information.md")

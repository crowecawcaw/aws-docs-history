# Exporting query data using the aws_s3.query_export_to_s3 function

Export your PostgreSQL data to Amazon S3 by calling the [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function.

###### Topics

- [Prerequisites](#postgresql-s3-export-examples-prerequisites "#postgresql-s3-export-examples-prerequisites")
- [Calling aws_s3.query_export_to_s3](#postgresql-s3-export-examples-basic "#postgresql-s3-export-examples-basic")
- [Exporting to a CSV file that uses a custom delimiter](#postgresql-s3-export-examples-custom-delimiter "#postgresql-s3-export-examples-custom-delimiter")
- [Exporting to a binary file with encoding](#postgresql-s3-export-examples-encoded "#postgresql-s3-export-examples-encoded")

## Prerequisites

Before you use the `aws_s3.query_export_to_s3` function, be sure to
complete the following prerequisites:

- Install the required PostgreSQL extensions as described in [Overview of exporting data to Amazon S3](postgresql-s3-export.md#postgresql-s3-export-overview "postgresql-s3-export.md#postgresql-s3-export-overview").
- Determine where to export your data to Amazon S3 as described in [Specifying the Amazon S3 file path to export to](postgresql-s3-export.md#postgresql-s3-export-file "postgresql-s3-export.md#postgresql-s3-export-file").
- Make sure that the DB cluster
  has export access to Amazon S3
  as described in [Setting up access to an Amazon S3 bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md").

The examples following use a database table called `sample_table`.
These examples export the data into a bucket called `amzn-s3-demo-bucket`. The
example table and data are created with the following SQL statements in psql.

```
psql=> CREATE TABLE sample_table (bid bigint PRIMARY KEY, name varchar(80));
psql=> INSERT INTO sample_table (bid,name) VALUES (1, 'Monday'), (2,'Tuesday'), (3, 'Wednesday');
```

## Calling aws_s3.query_export_to_s3

The following shows the basic ways of calling the [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function.

These examples use the variable `s3_uri_1` to identify a structure that
contains the information identifying the Amazon S3 file. Use the [aws_commons.create_s3_uri](postgresql-s3-export-functions.md#aws_commons.create_s3_uri "postgresql-s3-export-functions.md#aws_commons.create_s3_uri")
function to create the structure.

```
psql=> SELECT aws_commons.create_s3_uri(
   '`amzn-s3-demo-bucket`',
   'sample-filepath',
   'us-west-2'
) AS s3_uri_1 \gset
```

Although the parameters vary for the following two
`aws_s3.query_export_to_s3` function calls, the results are the same
for these examples. All rows of the `sample_table` table are exported
into a bucket called `amzn-s3-demo-bucket`.

```
psql=> SELECT * FROM aws_s3.query_export_to_s3('SELECT * FROM sample_table', :'s3_uri_1');

psql=> SELECT * FROM aws_s3.query_export_to_s3('SELECT * FROM sample_table', :'s3_uri_1', options :='format text');
```

The parameters are described as follows:

- `'SELECT * FROM sample_table'` – The first parameter is
  a required text string containing an SQL query. The PostgreSQL engine runs
  this query. The results of the query are copied to the S3 bucket identified
  in other parameters.
- `:'s3_uri_1'` – This parameter is a structure that
  identifies the Amazon S3 file. This example uses a variable to identify the
  previously created structure. You can instead create the structure by
  including the `aws_commons.create_s3_uri` function call inline
  within the `aws_s3.query_export_to_s3` function call as
  follows.

```
SELECT * from aws_s3.query_export_to_s3('select * from sample_table',
   aws_commons.create_s3_uri('`amzn-s3-demo-bucket`', 'sample-filepath', 'us-west-2')
);
```

- `options :='format text'` – The `options`
  parameter is an optional text string containing PostgreSQL `COPY`
  arguments. The copy process uses the arguments and format of the [PostgreSQL
  COPY](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html") command.

If the file specified doesn't exist in the Amazon S3 bucket, it's created. If the
file already exists, it's overwritten. The syntax for accessing the exported
data in Amazon S3 is the following.

```
s3-`region`://`bucket-name`[/`path-prefix`]/`file-prefix`
```

Larger exports are stored in multiple files, each with a maximum size of
approximately 6 GB. The additional file names have the same file prefix but with
`_part`XX`appended. The
`XX`` represents 2, then 3, and so on.
For example, suppose that you specify the path where you store data files as the
following.

```
s3-us-west-2://`amzn-s3-demo-bucket`/my-prefix
```

If the export has to create three data files, the Amazon S3 bucket contains the
following data files.

```
s3-us-west-2://`amzn-s3-demo-bucket`/my-prefix
s3-us-west-2://`amzn-s3-demo-bucket`/my-prefix_part2
s3-us-west-2://`amzn-s3-demo-bucket`/my-prefix_part3
```

For the full reference for this function and additional ways to call it, see [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3"). For more about accessing
files in Amazon S3, see [View an
object](../../../AmazonS3/latest/userguide/OpeningAnObject.md "../../../AmazonS3/latest/userguide/OpeningAnObject.md") in the _Amazon Simple Storage Service User Guide_.

## Exporting to a CSV file that uses a custom delimiter

The following example shows how to call the [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function to export data to a
file that uses a custom delimiter. The example uses arguments of the [PostgreSQL
COPY](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html") command to specify the comma-separated value (CSV) format and a
colon (:) delimiter.

```
SELECT * from aws_s3.query_export_to_s3('select * from basic_test', :'s3_uri_1', options :='format csv, delimiter $$:$$');
```

## Exporting to a binary file with encoding

The following example shows how to call the [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function to export data to a
binary file that has Windows-1253 encoding.

```
SELECT * from aws_s3.query_export_to_s3('select * from basic_test', :'s3_uri_1', options :='format binary, encoding WIN1253');
```

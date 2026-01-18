# Importing data from Amazon S3 to your RDS for PostgreSQL DB instance

You import data from your Amazon S3 bucket by using the `table_import_from_s3` function of the aws_s3
extension. For reference information, see
[aws_s3.table_import_from_s3](USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3 "USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3").

###### Note

The following examples use the IAM role method to allow access to the Amazon S3 bucket.
Thus, the `aws_s3.table_import_from_s3` function calls don't include
credential parameters.

The following shows a typical example.

```
`postgres=>` SELECT aws_s3.table_import_from_s3(
   't1',
   '',
   '(format csv)',
   :'s3_uri'
);
```

The parameters are the following:

- `t1` – The name for the table in the PostgreSQL DB instance to copy the data into.
- `''` – An optional list of columns in the database table.
  You can use this parameter to indicate which columns of the S3 data go in which
  table columns. If no columns are specified, all the columns are copied to the
  table. For an example of using a column list, see [Importing an
  Amazon S3 file that uses a custom delimiter](#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter "#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter").
- `(format csv)` – PostgreSQL COPY arguments. The copy process
  uses the arguments and format of the [PostgreSQL
  COPY](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html") command to import the data. Choices for format
  include comma-separated value (CSV) as shown in this example, text, and binary.
  The default is text.
- `s3_uri` – A structure that contains the information
  identifying the Amazon S3 file. For an example of using the [aws_commons.create_s3_uri](USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri "USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri") function to
  create an `s3_uri` structure, see [Overview of importing data from Amazon S3
  data](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md").
  For more information about this function, see [aws_s3.table_import_from_s3](USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3 "USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3").

The `aws_s3.table_import_from_s3` function returns text. To specify other kinds of files for import
from an Amazon S3 bucket, see one of the following examples.

###### Note

Importing 0 bytes file will cause an error.

###### Topics

- [Importing an
  Amazon S3 file that uses a custom delimiter](#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter "#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter")
- [Importing an Amazon S3
  compressed (gzip) file](#USER_PostgreSQL.S3Import.FileFormats.gzip "#USER_PostgreSQL.S3Import.FileFormats.gzip")
- [Importing an encoded
  Amazon S3 file](#USER_PostgreSQL.S3Import.FileFormats.Encoded "#USER_PostgreSQL.S3Import.FileFormats.Encoded")

## Importing an

Amazon S3 file that uses a custom delimiter

The following example shows how to import a file that uses a custom delimiter. It
also shows how to control where to put the data in the database table using the
`column_list` parameter of the [aws_s3.table_import_from_s3](USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3 "USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3") function.

For this example, assume that the following information is organized into
pipe-delimited columns in the Amazon S3 file.

```
1|foo1|bar1|elephant1
2|foo2|bar2|elephant2
3|foo3|bar3|elephant3
4|foo4|bar4|elephant4
...
```

###### To import a file that uses a custom delimiter

1. Create a table in the database for the imported data.

```
`postgres=>` CREATE TABLE test (a text, b text, c text, d text, e text);
```

2. Use the following form of the [aws_s3.table_import_from_s3](USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3 "USER_PostgreSQL.S3Import.md#aws_s3.table_import_from_s3") function to import
   data from the Amazon S3 file.

You can include the [aws_commons.create_s3_uri](USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri "USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri") function
call inline within the `aws_s3.table_import_from_s3` function
call to specify the file.

```
`postgres=>` SELECT aws_s3.table_import_from_s3(
   'test',
   'a,b,d,e',
   'DELIMITER ''|''',
   aws_commons.create_s3_uri('`amzn-s3-demo-bucket`', 'pipeDelimitedSampleFile', 'us-east-2')
);
```

The data is now in the table in the following columns.

```
`postgres=>` SELECT * FROM test;
`a | b | c | d | e
---+------+---+---+------+-----------
1 | foo1 | | bar1 | elephant1
2 | foo2 | | bar2 | elephant2
3 | foo3 | | bar3 | elephant3
4 | foo4 | | bar4 | elephant4`
```

## Importing an Amazon S3

compressed (gzip) file

The following example shows how to import a file from Amazon S3 that is compressed with
gzip. The file that you import needs to have the following Amazon S3 metadata:

- Key: `Content-Encoding`
- Value: `gzip`

If you upload the file using the AWS Management Console, the metadata is typically applied by the system. For information
about uploading files to Amazon S3 using the AWS Management Console, the AWS CLI, or the API, see
[Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the
_Amazon Simple Storage Service User Guide_.

For more information about Amazon S3 metadata and details about system-provided metadata, see [Editing object metadata in the Amazon S3
console](../../../AmazonS3/latest/userguide/add-object-metadata.md "../../../AmazonS3/latest/userguide/add-object-metadata.md") in the _Amazon Simple Storage Service User Guide_.

Import the gzip file into your RDS for PostgreSQL DB
instance as shown following.

```
`postgres=>` CREATE TABLE test_gzip(id int, a text, b text, c text, d text);
`postgres=>` SELECT aws_s3.table_import_from_s3(
 'test_gzip', '', '(format csv)',
 '`amzn-s3-demo-bucket`', 'test-data.gz', 'us-east-2'
);
```

## Importing an encoded

Amazon S3 file

The following example shows how to import a file from Amazon S3 that has Windows-1252
encoding.

```
`postgres=>` SELECT aws_s3.table_import_from_s3(
 'test_table', '', 'encoding ''WIN1252''',
 aws_commons.create_s3_uri('`amzn-s3-demo-bucket`', 'SampleFile', 'us-east-2')
);
```

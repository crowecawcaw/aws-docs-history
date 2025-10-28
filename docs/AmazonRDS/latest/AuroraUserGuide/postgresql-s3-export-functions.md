# Function reference

###### Functions

- [aws_s3.query_export_to_s3](#aws_s3.export_query_to_s3 "#aws_s3.export_query_to_s3")
- [aws_commons.create_s3_uri](#aws_commons.create_s3_uri "#aws_commons.create_s3_uri")

## aws_s3.query_export_to_s3

Exports a PostgreSQL query result to an Amazon S3 bucket. The `aws_s3`
extension provides the `aws_s3.query_export_to_s3` function.

The two required parameters are `query` and `s3_info`. These
define the query to be exported and identify the Amazon S3 bucket to export to. An
optional parameter called `options` provides for defining various export
parameters. For examples of using the `aws_s3.query_export_to_s3`
function, see [Exporting query data using the
aws_s3.query_export_to_s3 function](postgresql-s3-export-examples.md "postgresql-s3-export-examples.md").

**Syntax**

```
aws_s3.query_export_to_s3(
    query text,
    s3_info aws_commons._s3_uri_1,
    options text,
    kms_key text
)
```

###### Input parameters

_query_

A required text string containing an SQL query that the PostgreSQL
engine runs. The results of this query are copied to an S3 bucket
identified in the `s3_info` parameter.

_s3_info_

An `aws_commons._s3_uri_1` composite type containing the
following information about the S3 object:

- `bucket` – The name of the Amazon S3 bucket to
  contain the file.
- `file_path` – The Amazon S3 file name and
  path.
- `region` – The AWS Region that the bucket is
  in. For a listing of AWS Region names and associated values, see
  [Regions and
  Availability Zones](Concepts.md "Concepts.md").

Currently, this value must be the same AWS Region as that of
the exporting DB cluster
. The default
is the AWS Region of the exporting DB
cluster
.

To create an `aws_commons._s3_uri_1` composite structure,
see the [aws_commons.create_s3_uri](#aws_commons.create_s3_uri "#aws_commons.create_s3_uri") function.

_options_

An optional text string containing arguments for the PostgreSQL
`COPY` command. These arguments specify how the data is
to be copied when exported. For more details, see the [PostgreSQL COPY documentation](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html").

_kms_key text_

An optional text string containing the customer managed KMS key of the S3 bucket to export the data to.

### Alternate input

parameters

To help with testing, you can use an expanded set of parameters instead of the
`s3_info` parameter. Following are additional syntax variations
for the `aws_s3.query_export_to_s3` function.

Instead of using the `s3_info` parameter to identify an Amazon S3 file,
use the combination of the `bucket`, `file_path`, and
`region` parameters.

```
aws_s3.query_export_to_s3(
    query text,
    bucket text,
    file_path text,
    region text,
    options text,
    kms_key text
)
```

_query_

A required text string containing an SQL query that the PostgreSQL
engine runs. The results of this query are copied to an S3 bucket
identified in the `s3_info` parameter.

_bucket_

A required text string containing the name of the Amazon S3 bucket that
contains the file.

_file_path_

A required text string containing the Amazon S3 file name including the
path of the file.

_region_

An optional text string containing the AWS Region that the bucket
is in. For a listing of AWS Region names and associated values, see
[Regions and
Availability Zones](Concepts.md "Concepts.md").

Currently, this value must be the same AWS Region as that of the
exporting DB cluster
. The default is
the AWS Region of the exporting DB
cluster
.

_options_

An optional text string containing arguments for the PostgreSQL
`COPY` command. These arguments specify how the data
is to be copied when exported. For more details, see the [PostgreSQL COPY documentation](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html").

_kms_key text_

An optional text string containing the customer managed KMS key of the S3 bucket to export the data to.

### Output

parameters

```
aws_s3.query_export_to_s3(
    OUT rows_uploaded bigint,
    OUT files_uploaded bigint,
    OUT bytes_uploaded bigint
)
```

_rows_uploaded_

The number of table rows that were successfully uploaded to Amazon S3
for the given query.

_files_uploaded_

The number of files uploaded to Amazon S3. Files are created in sizes
of approximately 6 GB. Each additional file created has
`_part`XX`appended to
 the name. The`XX`` represents
2, then 3, and so on as needed.

_bytes_uploaded_

The total number of bytes uploaded to Amazon S3.

### Examples

```
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '`amzn-s3-demo-bucket`', 'sample-filepath');
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '`amzn-s3-demo-bucket`', 'sample-filepath','us-west-2');
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '`amzn-s3-demo-bucket`', 'sample-filepath','us-west-2','format text');
```

## aws_commons.create_s3_uri

Creates an `aws_commons._s3_uri_1` structure to hold Amazon S3 file
information. You use the results of the `aws_commons.create_s3_uri`
function in the `s3_info` parameter of the [aws_s3.query_export_to_s3](#aws_s3.export_query_to_s3 "#aws_s3.export_query_to_s3") function. For an example of
using the `aws_commons.create_s3_uri` function, see [Specifying the Amazon S3 file path to export
to](postgresql-s3-export.md#postgresql-s3-export-file "postgresql-s3-export.md#postgresql-s3-export-file").

**Syntax**

```
aws_commons.create_s3_uri(
   bucket text,
   file_path text,
   region text
)
```

###### Input parameters

_bucket_

A required text string containing the Amazon S3 bucket name for the
file.

_file_path_

A required text string containing the Amazon S3 file name including the
path of the file.

_region_

A required text string containing the AWS Region that the file is in.
For a listing of AWS Region names and associated values, see [Regions and
Availability Zones](Concepts.md "Concepts.md").

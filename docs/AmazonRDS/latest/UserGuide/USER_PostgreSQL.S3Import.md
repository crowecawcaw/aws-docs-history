# Function reference

###### Functions

- [aws_s3.table_import_from_s3](#aws_s3.table_import_from_s3 "#aws_s3.table_import_from_s3")
- [aws_commons.create_s3_uri](#USER_PostgreSQL.S3Import.create_s3_uri "#USER_PostgreSQL.S3Import.create_s3_uri")
- [aws_commons.create_aws_credentials](#USER_PostgreSQL.S3Import.create_aws_credentials "#USER_PostgreSQL.S3Import.create_aws_credentials")

## aws_s3.table_import_from_s3

Imports Amazon S3 data into an Amazon RDS table. The `aws_s3` extension provides the
`aws_s3.table_import_from_s3` function. The return value is text.

### Syntax

The required parameters are `table_name`, `column_list` and `options`.
These identify the database table and specify how the data is copied into the table.

You can also use the following parameters:

- The `s3_info` parameter specifies the Amazon S3 file to import.
  When you use this parameter, access to Amazon S3 is provided by an IAM role
  for the PostgreSQL DB instance.

```
aws_s3.table_import_from_s3 (
   table_name text,
   column_list text,
   options text,
   s3_info aws_commons._s3_uri_1
)
```

- The `credentials` parameter specifies the credentials to
  access Amazon S3. When you use this parameter, you don't use an IAM
  role.

```
aws_s3.table_import_from_s3 (
   table_name text,
   column_list text,
   options text,
   s3_info aws_commons._s3_uri_1,
   credentials aws_commons._aws_credentials_1
)
```

### Parameters

_table_name_

A required text string containing the name of the PostgreSQL
database table to import the data into.

_column_list_

A required text string containing an optional list of the
PostgreSQL database table columns in which to copy the data. If the
string is empty, all columns of the table are used. For an example,
see [Importing an
Amazon S3 file that uses a custom delimiter](USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter "USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.FileFormats.CustomDelimiter").

_options_

A required text string containing arguments for the PostgreSQL
`COPY` command. These arguments specify how the data
is to be copied into the PostgreSQL table. For more details, see the
[PostgreSQL COPY documentation](https://www.postgresql.org/docs/current/sql-copy.html "https://www.postgresql.org/docs/current/sql-copy.html").

_s3_info_

An `aws_commons._s3_uri_1` composite type containing
the following information about the S3 object:

- `bucket` – The name of the Amazon S3 bucket
  containing the file.
- `file_path` – The Amazon S3 file name
  including the path of the file.
- `region` – The AWS Region that the file
  is in. For a listing of AWS Region names and associated
  values, see [Regions, Availability Zones, and Local Zones](Concepts.md "Concepts.md").

_credentials_

An `aws_commons._aws_credentials_1` composite type
containing the following credentials to use for the import
operation:

- Access key
- Secret key
- Session token

For information about creating an
`aws_commons._aws_credentials_1` composite structure,
see [aws_commons.create_aws_credentials](#USER_PostgreSQL.S3Import.create_aws_credentials "#USER_PostgreSQL.S3Import.create_aws_credentials").

### Alternate

syntax

To help with testing, you can use an expanded set of parameters instead of the
`s3_info` and `credentials` parameters. Following are
additional syntax variations for the `aws_s3.table_import_from_s3`
function:

- Instead of using the `s3_info` parameter to identify an
  Amazon S3 file, use the combination of the `bucket`,
  `file_path`, and `region` parameters. With
  this form of the function, access to Amazon S3 is provided by an IAM role on
  the PostgreSQL DB instance.

```
aws_s3.table_import_from_s3 (
   table_name text,
   column_list text,
   options text,
   bucket text,
   file_path text,
   region text
)
```

- Instead of using the `credentials` parameter to specify
  Amazon S3 access, use the combination of the `access_key`,
  `session_key`, and `session_token`
  parameters.

```
aws_s3.table_import_from_s3 (
   table_name text,
   column_list text,
   options text,
   bucket text,
   file_path text,
   region text,
   access_key text,
   secret_key text,
   session_token text
)
```

### Alternate parameters

_bucket_

A text string containing the name of the Amazon S3 bucket that contains
the file.

_file_path_

A text string containing the Amazon S3 file name including the path of
the file.

_region_

A text string identifying the AWS Region location of the file.
For a listing of AWS Region names and associated values, see [Regions, Availability Zones, and Local Zones](Concepts.md "Concepts.md").

_access_key_

A text string containing the access key to use for the import
operation. The default is NULL.

_secret_key_

A text string containing the secret key to use for the import
operation. The default is NULL.

_session_token_

(Optional) A text string containing the session key to use for the
import operation. The default is NULL.

## aws_commons.create_s3_uri

Creates an `aws_commons._s3_uri_1` structure to hold Amazon S3 file
information. Use the results of the `aws_commons.create_s3_uri` function
in the `s3_info` parameter of the [aws_s3.table_import_from_s3](#aws_s3.table_import_from_s3 "#aws_s3.table_import_from_s3") function.

### Syntax

```
aws_commons.create_s3_uri(
   bucket text,
   file_path text,
   region text
)
```

### Parameters

_bucket_

A required text string containing the Amazon S3 bucket name for the
file.

_file_path_

A required text string containing the Amazon S3 file name including the
path of the file.

_region_

A required text string containing the AWS Region that the file is
in. For a listing of AWS Region names and associated values, see
[Regions, Availability Zones, and Local Zones](Concepts.md "Concepts.md").

## aws_commons.create_aws_credentials

Sets an access key and secret key in an `aws_commons._aws_credentials_1`
structure. Use the results of the `aws_commons.create_aws_credentials`
function in the `credentials` parameter of the [aws_s3.table_import_from_s3](#aws_s3.table_import_from_s3 "#aws_s3.table_import_from_s3") function.

### Syntax

```
aws_commons.create_aws_credentials(
   access_key text,
   secret_key text,
   session_token text
)
```

### Parameters

_access_key_

A required text string containing the access key to use for importing
an Amazon S3 file. The default is NULL.

_secret_key_

A required text string containing the secret key to use for importing
an Amazon S3 file. The default is NULL.

_session_token_

An optional text string containing the session token to use for
importing an Amazon S3 file. The default is NULL. If you provide an optional
`session_token`, you can use temporary
credentials.

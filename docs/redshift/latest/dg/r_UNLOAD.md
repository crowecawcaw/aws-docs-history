Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UNLOAD

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **_Client-side encryption for COPY and UNLOAD commands will<br>no longer be open to new customers starting April 30, 2025.<br>If you used client-side encryption with COPY and UNLOAD commands<br>in the 12 months before April 30, 2025, you can continue to use<br>client side encryption with COPY or UNLOAD commands until<br>April 30, 2026. After April 30, 2026, you won't be able to<br>use client-side encryption for COPY and UNLOAD.<br>We recommend that you switch to using server-side encryption<br>for COPY and UNLOAD as soon as possible. If you're already using<br>server-side encryption for COPY and UNLOAD, there's no change and<br>you can continue to use it without altering your queries.<br>For more information on encryption for COPY and UNLOAD,<br>see the ENCRYPTED parameter below._** |

Unloads the result of a query to one or more text, JSON, or Apache Parquet files on Amazon S3, using
Amazon S3 server-side encryption (SSE-S3). You can also specify server-side encryption with an
AWS Key Management Service key (SSE-KMS).

By default, the format of the unloaded file is pipe-delimited ( `|` ) text.

You can manage the size of files on Amazon S3, and by extension the number of files, by
setting the MAXFILESIZE parameter. Ensure that the S3 IP ranges are added to your allow list. To learn more about
the required S3 IP ranges, see [Network isolation](../mgmt/security-network-isolation.md#network-isolation "../mgmt/security-network-isolation.md#network-isolation").

You can unload the result of an Amazon Redshift query to your Amazon S3 data lake in Apache Parquet, an
efficient open columnar storage format for analytics. Parquet format is up to 2x faster to
unload and consumes up to 6x less storage in Amazon S3, compared with text formats. This enables
you to save data transformation and enrichment you have done in Amazon S3 into your Amazon S3 data
lake in an open format. You can then analyze your data with Redshift Spectrum and other AWS services
such as Amazon Athena, Amazon EMR, and Amazon SageMaker AI.

For more information and example scenarios about using the UNLOAD command, see
[Unloading data in Amazon Redshift](c_unloading_data.md "c_unloading_data.md").

## Required privileges and permissions

For the UNLOAD command to succeed, at least SELECT privilege on the data in the database is needed, along with permission to write to the Amazon S3 location.
For information about permissions to access AWS resources for the UNLOAD command, see [Permissions to access other AWS
Resources](copy-usage_notes-access-permissions.md "copy-usage_notes-access-permissions.md").

To apply least-privilege permissions, follow these recommendations to only grant permissions, as needed, to the user running the command.

- The user must have SELECT privilege on the data. For information about how to limit database privileges, see
  [GRANT](r_GRANT.md "r_GRANT.md").
- The user needs permission to assume the IAM role to write to the Amazon S3 bucket in your AWS account. To restrict access for a database user to assume a role, see
  [Restricting access to IAM roles](../mgmt/authorizing-redshift-service-database-users.md "../mgmt/authorizing-redshift-service-database-users.md") in the _Amazon Redshift Management Guide_.
- The user needs access to the Amazon S3 bucket. To restrict permission using an Amazon S3 bucket policy, see
  [Bucket policies for Amazon S3](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the _Amazon Simple Storage Service User Guide_.

## Syntax

```
UNLOAD ('*select-statement*')
TO '*s3://object-path/name-prefix*'
*authorization*
[ *option*, ...]

where *authorization* is
IAM_ROLE { default | 'arn:aws:iam::`<AWS account-id-1>`:role/`<role-name>`[,arn:aws:iam::`<AWS account-id-2>`:role/`<role-name>`][,...]' }

where *option* is
| [ FORMAT [ AS ] ] CSV | PARQUET | JSON
| PARTITION BY ( *column\_name* [, ... ] ) [ INCLUDE ]
| MANIFEST [ VERBOSE ]
| HEADER
| DELIMITER [ AS ] '*delimiter-char*'
| FIXEDWIDTH [ AS ] '*fixedwidth-spec*'
| ENCRYPTED [ AUTO ]
| BZIP2
| GZIP
| ZSTD
| ADDQUOTES
| NULL [ AS ] '*null-string*'
| ESCAPE
| ALLOWOVERWRITE
| CLEANPATH
| PARALLEL [ { ON | TRUE } | { OFF | FALSE } ]
| MAXFILESIZE [AS] *max-size* [ MB | GB ]
| ROWGROUPSIZE [AS] *size* [ MB | GB ]
| REGION [AS] '*aws-region*' }
| EXTENSION '*extension-name*'


```

## Parameters

('_select-statement_')

A SELECT query. The results of the query are unloaded. In most cases, it is
worthwhile to unload data in sorted order by specifying an ORDER BY clause in
the query. This approach saves the time required to sort the data when it is
reloaded.

The query must be enclosed in single quotation marks as shown following:

```
('select * from venue order by venueid')
```

###### Note

If your query contains quotation marks (for example to enclose literal
values), put the literal between two sets of single quotation
marks—you must also enclose the query between single quotation marks:

```
('select * from venue where venuestate=''NV''')
```

TO 's3://_object-path/name-prefix_'

The full path, including bucket name, to the location on Amazon S3 where Amazon Redshift
writes the output file objects, including the manifest file if MANIFEST is
specified. The object names are prefixed with _name-prefix_.
If you use `PARTITION BY`, a forward slash (/) is automatically
added to the end of the _name-prefix_ value if needed. For
added security, UNLOAD connects to Amazon S3 using an HTTPS connection. By default,
UNLOAD writes one or more files per slice. UNLOAD appends a slice number and
part number to the specified name prefix as follows:

``<object-path>`/`<name-prefix>``<slice-number>`_part_`<part-number>``.

If MANIFEST is specified, the manifest file is written as follows:

``<object_path>`/`<name_prefix>`manifest`.

If PARALLEL is specified OFF, the data files are written as follows:

``<object_path>`/`<name_prefix>``<part-number>``.

UNLOAD automatically creates encrypted files using Amazon S3 server-side
encryption (SSE), including the manifest file if MANIFEST is used. The COPY
command automatically reads server-side encrypted files during the load
operation. You can transparently download server-side encrypted files from your
bucket using either the Amazon S3 console or API. For more information, see [Protecting Data Using
Server-Side Encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").

###### Important

REGION is required when the Amazon S3 bucket isn't in the same AWS Region
as the Amazon Redshift database.

_authorization_

The UNLOAD command needs authorization to write data to Amazon S3. The
UNLOAD command uses the same parameters the COPY command uses for
authorization. For more information, see [Authorization parameters](copy-parameters-authorization.md "copy-parameters-authorization.md") in the COPY command syntax
reference.

IAM_ROLE { default | 'arn:aws:iam::`<AWS account-id-1>`:role/`<role-name>`'

Use the default keyword to have Amazon Redshift use the IAM role that is
set as default and associated with the cluster when the UNLOAD command
runs.

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses
for authentication and authorization. If you specify IAM_ROLE, you can't
use ACCESS_KEY_ID and SECRET_ACCESS_KEY, SESSION_TOKEN, or CREDENTIALS.
The IAM_ROLE can be chained. For more information, see
[Chaining IAM roles](../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-chaining-roles "../mgmt/authorizing-redshift-service.md#authorizing-redshift-service-chaining-roles") in the _Amazon Redshift Management Guide_.

[ FORMAT [AS] ] CSV | PARQUET | JSON

Keywords to specify the unload format to override the default format.

When CSV, unloads to a text file in CSV format using a comma ( , ) character
as the default delimiter. If a field contains delimiters, double quotation
marks, newline characters, or carriage returns, then the field in the unloaded
file is enclosed in double quotation marks. A double quotation mark within a
data field is escaped by an additional double quotation mark.
When zero rows are unloaded, Amazon Redshift might write empty Amazon S3 objects.

When PARQUET, unloads to a file in Apache Parquet version 1.0 format. By
default, each row group is compressed using SNAPPY compression. For more
information about Apache Parquet format, see [Parquet](https://parquet.apache.org/ "https://parquet.apache.org/").

When JSON, unloads to a JSON file with each line containing a JSON object, representing a full record in the query result.
Amazon Redshift supports writing nested JSON when the query result contains SUPER columns. To create a valid JSON object, the name of each column in the query must be unique.
In the JSON file, boolean values are unloaded as `t` or `f`, and NULL values are unloaded as `null`.
When zero rows are unloaded, Amazon Redshift does not write Amazon S3 objects.

The FORMAT and AS keywords are optional. You can't use CSV with
ESCAPE, FIXEDWIDTH, or ADDQUOTES.
You can't use PARQUET with DELIMITER, FIXEDWIDTH, ADDQUOTES, ESCAPE, NULL
AS, HEADER, GZIP, BZIP2, or ZSTD. PARQUET with ENCRYPTED is only supported with
server-side encryption with an AWS Key Management Service key (SSE-KMS). You can't use JSON with DELIMITER, HEADER, FIXEDWIDTH, ADDQUOTES, ESCAPE, or NULL AS.

PARTITION BY ( _column_name_ [, ... ] ) [INCLUDE]

Specifies the partition keys for the unload operation. UNLOAD automatically
partitions output files into partition folders based on the partition key
values, following the Apache Hive convention. For example, a Parquet file that
belongs to the partition year 2019 and the month September has the following
prefix:
`s3://amzn-s3-demo-bucket/my_prefix/year=2019/month=September/000.parquet`.

The value for _column_name_ must be a column in the query
results being unloaded.

If you specify PARTITION BY with the INCLUDE option, partition columns
aren't removed from the unloaded files.

Amazon Redshift doesn't support string literals in PARTITION BY clauses.

MANIFEST [ VERBOSE ]

Creates a manifest file that explicitly lists details for the data files
that are created by the UNLOAD process. The manifest is a text file in JSON
format that lists the URL of each file that was written to Amazon S3.

If MANIFEST is specified with the VERBOSE option, the manifest includes the
following details:

- The column names and data types, and for CHAR, VARCHAR, or NUMERIC
  data types, dimensions for each column. For CHAR and VARCHAR data types,
  the dimension is the length. For a DECIMAL or NUMERIC data type, the
  dimensions are precision and scale.
- The row count unloaded to each file. If the HEADER option is
  specified, the row count includes the header line.
- The total file size of all files unloaded and the total row count
  unloaded to all files. If the HEADER option is specified, the row count
  includes the header lines.
- The author. Author is always "Amazon Redshift".

You can specify VERBOSE only following MANIFEST.

The manifest file is written to the same Amazon S3 path prefix as the unload
files in the format `<object_path_prefix>manifest`. For
example, if UNLOAD specifies the Amazon S3 path prefix
'`s3://amzn-s3-demo-bucket/venue_`', the manifest file location is
'`s3://amzn-s3-demo-bucket/venue_manifest`'.

HEADER

Adds a header line containing column names at the top of each output file.
Text transformation options, such as CSV, DELIMITER, ADDQUOTES, and ESCAPE,
also apply to the header line. You can't use HEADER with
FIXEDWIDTH.

DELIMITER AS '_delimiter_character_'

Specifies a single ASCII character that is used to separate fields in the
output file, such as a pipe character ( | ), a comma ( , ), or a tab ( \t ).
The default delimiter for text files is a pipe character.
The default
delimiter for CSV files is a comma character. The AS keyword is optional. You
can't use DELIMITER with FIXEDWIDTH. If the data contains the delimiter
character, you need to specify the ESCAPE option to escape the delimiter, or
use ADDQUOTES to enclose the data in double quotation marks. Alternatively,
specify a delimiter that isn't contained in the data.

FIXEDWIDTH '_fixedwidth_spec_'

Unloads the data to a file where each column width is a fixed length, rather
than separated by a delimiter. The _fixedwidth_spec_ is a
string that specifies the number of columns and the width of the columns. The
AS keyword is optional. Because FIXEDWIDTH doesn't truncate data, the
specification for each column in the UNLOAD statement needs to be at least as
long as the length of the longest entry for that column. The format for
_fixedwidth_spec_ is shown below:

```
'*colID1:colWidth1,colID2:colWidth2, ...*'
```

You can't use FIXEDWIDTH with DELIMITER or HEADER.

ENCRYPTED [AUTO]

Specifies that the output files on Amazon S3 are encrypted using Amazon S3 server-side
encryption. If MANIFEST is specified, the manifest
file is also encrypted. For more information, see [Unloading encrypted data files](t_unloading_encrypted_files.md "t_unloading_encrypted_files.md"). If you don't specify the
ENCRYPTED parameter, UNLOAD automatically creates encrypted files using Amazon S3
server-side encryption with AWS-managed encryption keys (SSE-S3).

For ENCRYPTED, you might want to unload to Amazon S3 using server-side encryption
with an AWS KMS key (SSE-KMS). If so, use the [KMS_KEY_ID](#unload-parameters-kms-key-id "#unload-parameters-kms-key-id") parameter to provide the key ID.
You can't use the [Using the CREDENTIALS parameter](copy-parameters-authorization.md#copy-credentials "copy-parameters-authorization.md#copy-credentials") parameter with the
KMS_KEY_ID parameter. If you run an UNLOAD command for data using KMS_KEY_ID,
you can then do a COPY operation for the same data without specifying a key.

If ENCRYPTED AUTO is used, the UNLOAD command fetches the default AWS KMS
encryption key on the target Amazon S3 bucket property and encrypts the files written to
Amazon S3 with the AWS KMS key. If the bucket doesn't have the default AWS KMS
encryption key, UNLOAD automatically creates encrypted files using Amazon Redshift
server-side encryption with AWS-managed encryption keys (SSE-S3). You

can't use this option with KMS_KEY_ID, MASTER_SYMMETRIC_KEY, or
CREDENTIALS that contains master_symmetric_key.

KMS_KEY_ID '_key-id_'

Specifies the key ID for an AWS Key Management Service (AWS KMS) key to be used to encrypt data
files on Amazon S3. For more information, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
If you specify KMS_KEY_ID, you must specify the [ENCRYPTED](#unload-parameters-encrypted "#unload-parameters-encrypted") parameter also. If you specify
KMS_KEY_ID, you can't authenticate using the CREDENTIALS parameter.
Instead, use either [Using the IAM_ROLE parameter](copy-parameters-authorization.md#copy-iam-role "copy-parameters-authorization.md#copy-iam-role") or [Using the ACCESS_KEY_ID and SECRET_ACCESS_KEY parameters](copy-parameters-authorization.md#copy-access-key-id "copy-parameters-authorization.md#copy-access-key-id").

BZIP2

Unloads data to one or more bzip2-compressed files per slice. Each resulting
file is appended with a `.bz2` extension.

GZIP

Unloads data to one or more gzip-compressed files per slice. Each resulting
file is appended with a `.gz` extension.

ZSTD

Unloads data to one or more Zstandard-compressed files per slice. Each
resulting file is appended with a `.zst` extension.

ADDQUOTES

Places quotation marks around each unloaded data field, so that Amazon Redshift can
unload data values that contain the delimiter itself. For example, if the
delimiter is a comma, you could unload and reload the following data
successfully:

```
 "1","Hello, World"
```

Without the added quotation marks, the string `Hello, World`
would be parsed as two separate fields.

Some output formats do not support ADDQUOTES.

If you use ADDQUOTES, you must specify REMOVEQUOTES in the COPY if you
reload the data.

NULL AS '_null-string_'

Specifies a string that represents a null value in unload files. If this
option is used, all output files contain the specified string in place of any
null values found in the selected data. If this option isn't specified,
null values are unloaded as:

- Zero-length strings for delimited output
- Whitespace strings for fixed-width output

If a null string is specified for a fixed-width unload and the width of an
output column is less than the width of the null string, the following behavior
occurs:

- An empty field is output for non-character columns
- An error is reported for character columns

Unlike other data types where a user-defined string represents a null value, Amazon Redshift exports the SUPER data columns using the JSON format and represents it as null as determined by the JSON format. As a result, SUPER data columns ignore the NULL [AS] option used in UNLOAD commands.

ESCAPE

For CHAR and VARCHAR columns in delimited unload files, an escape character
(`\`) is placed before every occurrence of the following
characters:

- Linefeed: `\n`
- Carriage return: `\r`
- The delimiter character specified for the unloaded data.
- The escape character: `\`
- A quotation mark character: `"` or `'` (if both
  ESCAPE and ADDQUOTES are specified in the UNLOAD command).

###### Important

If you loaded your data using a COPY with the ESCAPE option, you must
also specify the ESCAPE option with your UNLOAD command to generate the
reciprocal output file. Similarly, if you UNLOAD using the ESCAPE option,
you need to use ESCAPE when you COPY the same data.

ALLOWOVERWRITE

By default, UNLOAD fails if it finds files that it would possibly overwrite.
If ALLOWOVERWRITE is specified, UNLOAD overwrites existing files, including the
manifest file.

CLEANPATH

The CLEANPATH option removes existing files located in the Amazon S3 path specified in the TO clause before unloading files to the specified location.

If you include the PARTITION BY clause, existing files are removed only from the partition folders to receive new files generated by the UNLOAD operation.

You must have the `s3:DeleteObject` permission on the Amazon S3 bucket.
For information, see
[Policies and Permissions in Amazon S3](../../../AmazonS3/latest/userguide/access-policy-language-overview.md "../../../AmazonS3/latest/userguide/access-policy-language-overview.md") in the _Amazon Simple Storage Service User Guide_.
Files that you remove by using the CLEANPATH option are permanently deleted and can't be recovered.

If the target Amazon S3 bucket has versioning enabled, UNLOAD with the CLEANPATH option does not remove previous versions of the files.

You can't specify the CLEANPATH option if you specify the ALLOWOVERWRITE option.

PARALLEL

By default, UNLOAD writes data in parallel to multiple files, according to
the number of slices in the cluster. The default option is ON or TRUE. If
PARALLEL is OFF or FALSE, UNLOAD writes to one or more data files serially,
sorted absolutely according to the ORDER BY clause, if one is used. The maximum
size for a data file is 6.2 GB. So, for example, if you unload 13.4 GB of data,
UNLOAD creates the following three files.

```
s3://amzn-s3-demo-bucket/key000    6.2 GB
s3://amzn-s3-demo-bucket/key001    6.2 GB
s3://amzn-s3-demo-bucket/key002    1.0 GB
```

###### Note

The UNLOAD command is designed to use parallel processing. We recommend
leaving PARALLEL enabled for most cases, especially if the files are used to
load tables using a COPY command.

MAXFILESIZE [AS] max-size [ MB | GB ]

Specifies the maximum size of files that UNLOAD creates in Amazon S3.
Specify a decimal value between 5 MB and 6.2 GB. The AS keyword is optional.
The default unit is MB. If MAXFILESIZE isn't specified, the default
maximum file size is 6.2 GB. The size of the manifest file, if one is used,
isn't affected by MAXFILESIZE.

ROWGROUPSIZE [AS] size [ MB | GB ]

Specifies the size of row groups. Choosing a larger size can reduce the number of row groups, reducing
the amount of network communication.
Specify an integer value between 32 MB and 128 MB. The AS keyword is optional.
The default unit is MB.

If ROWGROUPSIZE isn't specified, the default
size is 32 MB. To use this parameter, the storage format must be Parquet and the node type must be ra3.4xlarge, ra3.16xlarge,
or dc2.8xlarge.

REGION [AS] '_aws-region_'

Specifies the AWS Region where the target Amazon S3 bucket is located. REGION is
required for UNLOAD to an Amazon S3 bucket that isn't in the same AWS Region as
the Amazon Redshift database.

The value for _aws_region_ must match an AWS Region
listed in the [Amazon Redshift
regions and endpoints](../../../general/latest/gr/rande.md#redshift_region "../../../general/latest/gr/rande.md#redshift_region") table in the _AWS General Reference_.

By default, UNLOAD assumes that the target Amazon S3 bucket is located in the
same AWS Region as the Amazon Redshift database.

EXTENSION '_extension-name_'

Specifies the file extension to append to the names of the unloaded files. Amazon Redshift doesn't run any validation, so you must
verify that the specified file extension is correct. If you specify a compression method without providing
an extension, Amazon Redshift only adds the compression method's extension to the filename. If you don't
provide any extension and don't specify a compression method,
Amazon Redshift doesn't add anything to the filename.

## Usage notes

### Using ESCAPE for all delimited text UNLOAD

operations

When you UNLOAD using a delimiter, your data can include that delimiter or any of
the characters listed in the ESCAPE option description. In this case, you must use
the ESCAPE option with the UNLOAD statement. If you don't use the ESCAPE option
with the UNLOAD, subsequent COPY operations using the unloaded data might
fail.

###### Important

We strongly recommend that you always use ESCAPE with both UNLOAD and COPY
statements. The exception is if you are certain that your data doesn't
contain any delimiters or other characters that might need to be escaped.

### Loss of floating-point

precision

You might encounter loss of precision for floating-point data that is successively
unloaded and reloaded.

### Limit clause

The SELECT query can't use a LIMIT clause in the outer SELECT. For example,
the following UNLOAD statement fails.

```
unload ('select * from venue limit 10')
to 's3://amzn-s3-demo-bucket/venue_pipe_' iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

Instead, use a nested LIMIT clause, as in the following example.

```
unload ('select * from venue where venueid in
(select venueid from venue order by venueid desc limit 10)')
to 's3://amzn-s3-demo-bucket/venue_pipe_' iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

You can also populate a table using SELECT…INTO or CREATE TABLE AS using a LIMIT
clause, then unload from that table.

### Unloading a column of the GEOMETRY data

type

You can only unload GEOMETRY columns to text or CSV format. You can't unload
GEOMETRY data with the `FIXEDWIDTH` option. The data is unloaded in the
hexadecimal form of the extended well-known binary (EWKB) format. If the size of the
EWKB data is more than 4 MB, then a warning occurs because the data can't later
be loaded into a table.

### Unloading the HLLSKETCH data type

You can only unload HLLSKETCH columns to text or CSV format. You can't unload
HLLSKETCH data with the `FIXEDWIDTH` option. The data is unloaded in the
Base64 format for dense HyperLogLog sketches or in the JSON format for sparse
HyperLogLog sketches. For more information, see [HyperLogLog functions](hyperloglog-functions.md "hyperloglog-functions.md").

The following example exports a table containing HLLSKETCH columns into a
file.

```
CREATE TABLE a_table(an_int INT, b_int INT);
INSERT INTO a_table VALUES (1,1), (2,1), (3,1), (4,1), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2);

CREATE TABLE hll_table (sketch HLLSKETCH);
INSERT INTO hll_table select hll_create_sketch(an_int) from a_table group by b_int;

UNLOAD ('select * from hll_table') TO 's3://amzn-s3-demo-bucket/unload/'
IAM_ROLE 'arn:aws:iam::0123456789012:role/MyRedshiftRole' NULL AS 'null' ALLOWOVERWRITE CSV;
```

### Unloading a column of the VARBYTE data

type

You can only unload VARBYTE columns to text or CSV format.
The data is unloaded in the hexadecimal form.
You can't unload VARBYTE data with the `FIXEDWIDTH` option.
The `ADDQUOTES` option of UNLOAD to a CSV is not supported.
A VARBYTE column can't be a PARTITIONED BY column.

### FORMAT AS PARQUET clause

Be aware of these considerations when using FORMAT AS PARQUET:

- Unload to Parquet doesn't use file level compression. Each row group is
  compressed with SNAPPY.
- If MAXFILESIZE isn't specified, the default maximum file size is 6.2
  GB. You can use MAXFILESIZE to specify a file size of 5 MB–6.2 GB. The
  actual file size is approximated when the file is being written, so it might
  not be exactly equal to the number you specify.

To maximize scan performance, Amazon Redshift tries to create Parquet files that
contain equally sized 32-MB row groups. The MAXFILESIZE value that you specify
is automatically rounded down to the nearest multiple of 32 MB. For example, if
you specify MAXFILESIZE 200 MB, then each Parquet file unloaded is
approximately 192 MB (32 MB row group x 6 = 192 MB).

- If a column uses TIMESTAMPTZ data format, only the timestamp values are
  unloaded. The time zone information isn't unloaded.
- Don't specify file name prefixes that begin with underscore (\_) or
  period (.) characters. Redshift Spectrum treats files that begin with these characters as
  hidden files and ignores them.

### PARTITION BY clause

Be aware of these considerations when using PARTITION BY:

- Partition columns aren't included in the output file.
- Make sure to include partition columns in the SELECT query used in the
  UNLOAD statement. You can specify any number of partition columns in the UNLOAD
  command. However, there is a limitation that there should be at least one
  nonpartition column to be part of the file.
- If the partition key value is null, Amazon Redshift automatically unloads that data
  into a default partition called
  `partition_column=__HIVE_DEFAULT_PARTITION__`.
- The UNLOAD command doesn't make any calls to an external catalog. To
  register your new partitions to be part of your existing external table, use a
  separate ALTER TABLE ... ADD PARTITION ... command. Or you can run a CREATE
  EXTERNAL TABLE command to register the unloaded data as a new external table.
  You can also use an AWS Glue crawler to populate your Data Catalog. For more
  information, see [Defining Crawlers](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") in the
  _AWS Glue Developer Guide_.
- If you use the MANIFEST option, Amazon Redshift generates only one manifest file in the
  root Amazon S3 folder.
- The column data types that you can use as the partition key are SMALLINT,
  INTEGER, BIGINT, DECIMAL, REAL, BOOLEAN, CHAR, VARCHAR, DATE, and TIMESTAMP.

### Using the ASSUMEROLE privilege to

grant access to an IAM role for UNLOAD operations

To provide access for specific users and groups to an IAM role for UNLOAD operations, a superuser can grant the
ASSUMEROLE privilege on an IAM role to users and groups. For information, see [GRANT](r_GRANT.md "r_GRANT.md").

### UNLOAD doesn't support Amazon S3 access point aliases

You can't use Amazon S3 access point aliases with the UNLOAD command.

## Examples

For examples that show how to use the UNLOAD command, see [UNLOAD examples](r_UNLOAD_command_examples.md "r_UNLOAD_command_examples.md").

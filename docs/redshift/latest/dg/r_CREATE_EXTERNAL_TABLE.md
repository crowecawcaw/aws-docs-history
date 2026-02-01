Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE EXTERNAL TABLE

Creates a new external table in the specified schema. All external tables must be
created in an external schema. Search path isn't supported for external schemas and
external tables. For more information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

In addition to external tables created using the CREATE EXTERNAL TABLE command, Amazon Redshift can
reference external tables defined in an AWS Glue or AWS Lake Formation catalog or an Apache Hive
metastore. Use the [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") command to register an external database
defined in the external catalog and make the external tables available for use in Amazon Redshift. If
the external table exists in an AWS Glue or AWS Lake Formation catalog or Hive metastore, you don't
need to create the table using CREATE EXTERNAL TABLE. To view external tables, query the
[SVV_EXTERNAL_TABLES](r_SVV_EXTERNAL_TABLES.md "r_SVV_EXTERNAL_TABLES.md") system
view.

By running the CREATE EXTERNAL TABLE AS command, you can create an external table based
on the column definition from a query and write the results of that query into Amazon S3. The
results are in Apache Parquet or delimited text format. If the external table has a
partition key or keys, Amazon Redshift partitions new files according to those partition keys and
registers new partitions into the external catalog automatically. For more information
about CREATE EXTERNAL TABLE AS, see [Usage notes](r_CREATE_EXTERNAL_TABLE_usage.md "r_CREATE_EXTERNAL_TABLE_usage.md").

You can query an external table using the same SELECT syntax you use with other Amazon Redshift
tables. You can also use the INSERT syntax to write new files into the location of external
table on Amazon S3. For more information, see [INSERT (external table)](r_INSERT_external_table.md "r_INSERT_external_table.md").

To create a view with an external table, include the WITH NO SCHEMA BINDING clause in
the [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md") statement.

You can't run CREATE EXTERNAL TABLE inside a transaction (BEGIN … END). For more
information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

## Required privileges

To create external tables, you must be the owner of the external schema or a
superuser. To transfer ownership of an external schema, use ALTER SCHEMA to change the
owner. Access to external tables is controlled by access to the external schema. You
can't [GRANT](r_GRANT.md "r_GRANT.md") or [REVOKE](r_REVOKE.md "r_REVOKE.md") permissions on an external table. Instead, grant or revoke
USAGE on the external schema.

The [Usage notes](r_CREATE_EXTERNAL_TABLE_usage.md "r_CREATE_EXTERNAL_TABLE_usage.md") have additional information about
specific permissions for external tables.

## Syntax

```
CREATE EXTERNAL TABLE
*external\_schema.table\_name*
(*column\_name* *data\_type* [, …] )
[ PARTITIONED BY (*col\_name* *data\_type* [, … ] )]
[ { ROW FORMAT DELIMITED *row\_format* |
  ROW FORMAT SERDE '*serde\_name*'
  [ WITH SERDEPROPERTIES ( '*property\_name*' = '*property\_value*' [, ...] ) ] } ]
STORED AS *file\_format*
LOCATION { 's3://*bucket/folder*/' | 's3://*bucket/manifest\_file*' }
[ TABLE PROPERTIES ( '*property\_name*'='*property\_value*' [, ...] ) ]
```

The following is the syntax for CREATE EXTERNAL TABLE AS.

```
CREATE EXTERNAL TABLE
*external\_schema.table\_name*
[ PARTITIONED BY (*col\_name* [, … ] ) ]
[ ROW FORMAT DELIMITED *row\_format* ]
STORED AS *file\_format*
LOCATION { 's3://*bucket/folder*/' }
[ TABLE PROPERTIES ( '*property\_name*'='*property\_value*' [, ...] ) ]
 AS
 { select_statement }

```

## Parameters

_external_schema.table_name_

The name of the table to be created, qualified by an external schema name.
External tables must be created in an external schema. For more information,
see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

The maximum length for the table name is 127 bytes; longer names are
truncated to 127 bytes. You can use UTF-8 multibyte characters up to a maximum
of four bytes. Amazon Redshift enforces a limit of 9,900 tables per cluster, including
user-defined temporary tables and temporary tables created by Amazon Redshift during query
processing or system maintenance. Optionally, you can qualify the table name
with the database name. In the following example, the database name is
`spectrum_db`, the external schema name is
`spectrum_schema`, and the table name is
`test`.

```
create external table spectrum_db.spectrum_schema.test (c1 int)
stored as parquet
location 's3://amzn-s3-demo-bucket/myfolder/';
```

If the database or schema specified doesn't exist, the table isn't
created, and the statement returns an error. You can't create tables or
views in the system databases `template0`, `template1`,
`padb_harvest`, or `sys:internal`.

The table name must be a unique name for the specified schema.

For more information about valid names, see [Names and identifiers](r_names.md "r_names.md").

( _column_name_
_data_type_ )

The name and data type of each column being created.

The maximum length for the column name is 127 bytes; longer names are
truncated to 127 bytes. You can use UTF-8 multibyte characters up to a maximum
of four bytes. You can't specify column names `"$path"` or
`"$size"`. For more information about valid names, see [Names and identifiers](r_names.md "r_names.md").

By default, Amazon Redshift creates external tables with the pseudocolumns
`$path` and `$size`. You can disable creation of
pseudocolumns for a session by setting the
`spectrum_enable_pseudo_columns` configuration parameter to
`false`. For more information, see [Pseudocolumns](r_CREATE_EXTERNAL_TABLE_usage.md#r_CREATE_EXTERNAL_TABLE_usage-pseudocolumns "r_CREATE_EXTERNAL_TABLE_usage.md#r_CREATE_EXTERNAL_TABLE_usage-pseudocolumns") .

If pseudocolumns are enabled, the maximum number of columns you can define
in a single table is 1,598. If pseudocolumns aren't enabled, the maximum
number of columns you can define in a single table is 1,600.

If you are creating a "wide table," make sure that your list of columns
doesn't exceed row-width boundaries for intermediate results during loads
and query processing. For more information, see [Usage notes](r_CREATE_TABLE_NEW.md#r_CREATE_TABLE_usage "r_CREATE_TABLE_NEW.md#r_CREATE_TABLE_usage").

For a CREATE EXTERNAL TABLE AS command, a column list is not required,
because columns are derived from the query.

_data_type_

The following [Data types](c_Supported_data_types.md "c_Supported_data_types.md") are supported:

- SMALLINT (INT2)
- INTEGER (INT, INT4)
- BIGINT (INT8)
- DECIMAL (NUMERIC)
- REAL (FLOAT4)
- DOUBLE PRECISION (FLOAT8)
- BOOLEAN (BOOL)
- CHAR (CHARACTER)
- VARCHAR (CHARACTER VARYING)
- VARBYTE (CHARACTER VARYING) – can be used with Parquet and ORC
  data files, and only with non-partitioned tables.
- DATE – can be used only with text, Parquet, or ORC data files,
  or as a partition column.
- TIMESTAMP

For DATE, you can use the formats as described following. For month values
represented using digits, the following formats are supported:

- `mm-dd-yyyy` For example, `05-01-2017`. This is
  the default.
- `yyyy-mm-dd`, where the year is represented by more than 2
  digits. For example, `2017-05-01`.

For month values represented using the three letter abbreviation, the
following formats are supported:

- `mmm-dd-yyyy` For example, `may-01-2017`. This
  is the default.
- `dd-mmm-yyyy`, where the year is represented by more than 2
  digits. For example, `01-may-2017`.
- `yyyy-mmm-dd`, where the year is represented by more than 2
  digits. For example, `2017-may-01`.

For year values that are consistently less than 100, the year is calculated
in the following manner:

- If year is less than 70, the year is calculated as the year plus 2000.
  For example, the date 05-01-17 in the `mm-dd-yyyy` format is
  converted into `05-01-2017`.
- If year is less than 100 and greater than 69, the year is calculated
  as the year plus 1900. For example the date 05-01-89 in the
  `mm-dd-yyyy` format is converted into
  `05-01-1989`.
- For year values represented by two digits, add leading zeroes to
  represent the year in 4 digits.

Timestamp values in text files must be in the format `yyyy-mm-dd
 HH:mm:ss.SSSSSS`, as the following timestamp value shows:
`2017-05-01 11:30:59.000000`.

The length of a VARCHAR column is defined in bytes, not characters. For
example, a VARCHAR(12) column can contain 12 single-byte characters or 6
two-byte characters. When you query an external table, results are truncated to
fit the defined column size without returning an error. For more information,
see [Storage and
ranges](r_Character_types.md#r_Character_types-storage-and-ranges "r_Character_types.md#r_Character_types-storage-and-ranges").

For best performance, we recommend specifying the smallest column size that
fits your data. To find the maximum size in bytes for values in a column, use
the [OCTET_LENGTH](r_OCTET_LENGTH.md "r_OCTET_LENGTH.md") function. The following
example returns the maximum size of values in the email column.

```
`select max(octet_length(email)) from users;`

max
---
 62
```

PARTITIONED BY (_col_name_
_data_type_ [, … ] )

A clause that defines a partitioned table with one or more partition
columns. A separate data directory is used for each specified combination,
which can improve query performance in some circumstances. Partitioned columns
don't exist within the table data itself. If you use a value for
_col_name_ that is the same as a table column, you get an
error.

After creating a partitioned table, alter the table using an [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md") … ADD PARTITION
statement to register new partitions to the external catalog. When you add a
partition, you define the location of the subfolder on Amazon S3 that contains the
partition data.

For example, if the table `spectrum.lineitem_part` is defined
with `PARTITIONED BY (l_shipdate date)`, run the following ALTER
TABLE command to add a partition.

```
ALTER TABLE spectrum.lineitem_part ADD PARTITION (l_shipdate='1992-01-29')
LOCATION 's3://spectrum-public/lineitem_partition/l_shipdate=1992-01-29';
```

If you are using CREATE EXTERNAL TABLE AS, you don't need to run ALTER
TABLE...ADD PARTITION. Amazon Redshift automatically registers new partitions in the
external catalog. Amazon Redshift also automatically writes corresponding data to
partitions in Amazon S3 based on the partition key or keys defined in the
table.

To view partitions, query the [SVV_EXTERNAL_PARTITIONS](r_SVV_EXTERNAL_PARTITIONS.md "r_SVV_EXTERNAL_PARTITIONS.md") system view.

###### Note

For a CREATE EXTERNAL TABLE AS command, you don't need to specify
the data type of the partition column because this column is derived from
the query.

ROW FORMAT DELIMITED _rowformat_

A clause that specifies the format of the underlying data. Possible values
for _rowformat_ are as follows:

- LINES TERMINATED BY '_delimiter_'
- FIELDS TERMINATED BY '_delimiter_'

Specify a single ASCII character for '_delimiter_'. You
can specify non-printing ASCII characters using octal, in the format
`'\`_`ddd`_`'` where
_`d`_ is an octal digit (0–7) up to ‘\177’.
The following example specifies the BEL (bell) character using octal.

```
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\007'
```

If ROW FORMAT is omitted, the default format is DELIMITED FIELDS TERMINATED
BY '\A' (start of heading) and LINES TERMINATED BY '\n' (newline).

ROW FORMAT SERDE '_serde_name_'
[WITH SERDEPROPERTIES ( '_property_name_' =
'_property_value_' [, ...] ) ]

A clause that specifies the SERDE format for the underlying data.

'_serde_name_'

The name of the SerDe. You can specify the following
formats:

- org.apache.hadoop.hive.serde2.RegexSerDe
- com.amazonaws.glue.serde.GrokSerDe
- org.apache.hadoop.hive.serde2.OpenCSVSerde

This parameter supports the following SerDe property for
OpenCSVSerde:

```
'wholeFile' = 'true'
```

Set the `wholeFile` property to `true`
to properly parse new line characters (\n) within quoted strings
for OpenCSV requests.

- org.openx.data.jsonserde.JsonSerDe
  - The JSON SERDE also supports Ion files.
  - The JSON must be well-formed.
  - Timestamps in Ion and JSON must use ISO8601
    format.
  - This parameter supports the following SerDe property
    for JsonSerDe:

  ```
  'strip.outer.array'='true'
  ```

  Processes Ion/JSON files containing one very large
  array enclosed in outer brackets ( [ … ] ) as if it
  contains multiple JSON records within the array.

- com.amazon.ionhiveserde.IonHiveSerDe

The Amazon ION format provides text and binary formats, in
addition to data types. For an external table that references
data in ION format, you map each column in the external table to
the corresponding element in the ION format data. For more
information, see [Amazon Ion](https://amzn.github.io/ion-docs/ "https://amzn.github.io/ion-docs/"). You also need to specify the input and
output formats.

WITH SERDEPROPERTIES ( '_property_name_' =
'_property_value_' [, ...] ) ]

Optionally, specify property names and values, separated by
commas.

If ROW FORMAT is omitted, the default format is DELIMITED FIELDS TERMINATED
BY '\A' (start of heading) and LINES TERMINATED BY '\n' (newline).

STORED AS _file_format_

The file format for data files.

Valid formats are as follows:

- PARQUET
- RCFILE (for data using ColumnarSerDe only, not
  LazyBinaryColumnarSerDe)
- SEQUENCEFILE
- TEXTFILE (for text files, including JSON files).
- ORC
- AVRO
- INPUTFORMAT '_input_format_classname_' OUTPUTFORMAT
  '_output_format_classname_'

The CREATE EXTERNAL TABLE AS command only supports two file formats,
TEXTFILE and PARQUET.

For INPUTFORMAT and OUTPUTFORMAT, specify a class name, as the following
example shows.

```
'org.apache.hadoop.mapred.TextInputFormat'
```

LOCATION { 's3://_bucket/folder_/' |
's3://_bucket/manifest_file_'}

The path to the Amazon S3 bucket or folder that contains the data files or a
manifest file that contains a list of Amazon S3 object paths. The buckets must
be in the same AWS Region as the Amazon Redshift cluster. For a list of supported AWS
Regions, see [Amazon Redshift Spectrum limitations](c-spectrum-considerations.md "c-spectrum-considerations.md").

If the path specifies a bucket or folder, for example
`'s3://amzn-s3-demo-bucket/custdata/'`, Redshift Spectrum scans the files in
the specified bucket or folder and any subfolders. Redshift Spectrum ignores hidden files
and files that begin with a period or underscore.

If the path specifies a manifest file, the
`'s3://bucket/manifest_file'` argument must explicitly reference
a single file—for example,
`'s3://amzn-s3-demo-bucket/manifest.txt'`. It can't
reference a key prefix.

The manifest is a text file in JSON format that lists the URL of each file
that is to be loaded from Amazon S3 and the size of the file, in bytes. The URL
includes the bucket name and full object path for the file. The files that are
specified in the manifest can be in different buckets, but all the buckets must
be in the same AWS Region as the Amazon Redshift cluster. If a file is listed twice, the
file is loaded twice. The following example shows the JSON for a manifest that
loads three files.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket1/custdata.1", "meta": { "content_length": 5956875 } },
    {"url":"s3://amzn-s3-demo-bucket1/custdata.2", "meta": { "content_length": 5997091 } },
    {"url":"s3://amzn-s3-demo-bucket2/custdata.1", "meta": { "content_length": 5978675 } }
  ]
}
```

You can make the inclusion of a particular file mandatory. To do this,
include a `mandatory` option at the file level in the manifest. When
you query an external table with a mandatory file that is missing, the SELECT
statement fails. Ensure that all files included in the definition of the
external table are present. If they aren't all present, an error appears
showing the first mandatory file that isn't found. The following example
shows the JSON for a manifest with the `mandatory` option set to
`true`.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket1/custdata.1", "mandatory":true, "meta": { "content_length": 5956875 } },
    {"url":"s3://amzn-s3-demo-bucket1/custdata.2", "mandatory":false, "meta": { "content_length": 5997091 } },
    {"url":"s3://amzn-s3-demo-bucket2/custdata.1", "meta": { "content_length": 5978675 } }
  ]
}
```

To reference files created using UNLOAD, you can use the manifest created
using [UNLOAD](r_UNLOAD.md "r_UNLOAD.md") with the MANIFEST
parameter. The manifest file is compatible with a manifest file for [COPY from Amazon S3](copy-parameters-data-source-s3.md "copy-parameters-data-source-s3.md"), but uses different keys.
Keys that aren't used are ignored.

TABLE PROPERTIES (
'_property_name_'='_property_value_' [,
...] )

A clause that sets the table definition for table properties.

###### Note

Table properties are case-sensitive.

'compression_type'='_value_'

A property that sets the type of compression to use if the file
name doesn't contain an extension. If you set this property and
there is a file extension, the extension is ignored and the value set
by the property is used. Valid values for compression type are as
follows:

- bzip2
- gzip
- none
- snappy

'data_cleansing_enabled'='true / false’

This property sets whether data handling is on for the table. When
'data_cleansing_enabled' is set to true, data handling is on
for the table. When 'data_cleansing_enabled' is set to
false, data handling is off for the table. Following is a list of the
table–level data handling properties controlled by this
property:

- column_count_mismatch_handling
- invalid_char_handling
- numeric_overflow_handling
- replacement_char
- surplus_char_handling

For examples, see [Data handling
examples](r_CREATE_EXTERNAL_TABLE_examples.md#r_CREATE_EXTERNAL_TABLE_examples-data-handling "r_CREATE_EXTERNAL_TABLE_examples.md#r_CREATE_EXTERNAL_TABLE_examples-data-handling").

'invalid_char_handling'='_value_'

Specifies the action to perform when query results contain invalid
UTF-8 character values. You can specify the following actions:

DISABLED

Doesn't perform invalid character handling.

FAIL

Cancels queries that return data containing invalid UTF-8
values.

SET_TO_NULL

Replaces invalid UTF-8 values with null.

DROP_ROW

Replaces each value in the row with null.

REPLACE

Replaces the invalid character with the replacement
character you specify using
`replacement_char`.

'replacement_char'='_character_’

Specifies the replacement character to use when you set
`invalid_char_handling` to `REPLACE`.

'numeric_overflow_handling'='value’

Specifies the action to perform when ORC data contains an integer
(for example, BIGINT or int64) that is larger than the column
definition (for example, SMALLINT or int16). You can specify the
following actions:

DISABLED

Invalid character handling is turned off.

FAIL

Cancel the query when the data includes invalid
characters.

SET_TO_NULL

Set invalid characters to null.

DROP_ROW

Set each value in the row to null.

'surplus_bytes_handling'='_value_'

Specifies how to handle data being loaded that exceeds the length
of the data type defined for columns containing VARBYTE data. By
default, Redshift Spectrum sets the value to null for data that exceeds the width
of the column.

You can specify the following actions to perform when the query
returns data that exceeds the length of the data type:

SET_TO_NULL

Replaces data that exceeds the column width with
null.

DISABLED

Doesn't perform surplus byte handling.

FAIL

Cancels queries that return data exceeding the column
width.

DROP_ROW

Drop all rows that contain data exceeding column
width.

TRUNCATE

Removes the characters that exceed the maximum number of
characters defined for the column.

'surplus_char_handling'='_value_'

Specifies how to handle data being loaded that exceeds the length
of the data type defined for columns containing VARCHAR, CHAR, or
string data. By default, Redshift Spectrum sets the value to null for data that
exceeds the width of the column.

You can specify the following actions to perform when the query
returns data that exceeds the column width:

SET_TO_NULL

Replaces data that exceeds the column width with
null.

DISABLED

Doesn't perform surplus character handling.

FAIL

Cancels queries that return data exceeding the column
width.

DROP_ROW

Replaces each value in the row with null.

TRUNCATE

Removes the characters that exceed the maximum number of
characters defined for the column.

'column_count_mismatch_handling'='value’

Identifies if the file contains less or more values for a row than
the number of columns specified in the external table definition. This
property is only available for an uncompressed text file format. You
can specify the following actions:

DISABLED

Column count mismatch handling is turned off.

FAIL

Fail the query if the column count mismatch is
detected.

SET_TO_NULL

Fill missing values with NULL and ignore the additional
values in each row.

DROP_ROW

Drop all rows that contain column count mismatch error
from the scan.

'numRows'='_row_count_'

A property that sets the numRows value for the table definition. To
explicitly update an external table's statistics, set the numRows
property to indicate the size of the table. Amazon Redshift doesn't analyze
external tables to generate the table statistics that the query
optimizer uses to generate a query plan. If table statistics
aren't set for an external table, Amazon Redshift generates a query
execution plan based on an assumption that external tables are the
larger tables and local tables are the smaller tables.

'skip.header.line.count'='_line_count_'

A property that sets number of rows to skip at the beginning of
each source file.

'serialization.null.format'=' '

A property that specifies Spectrum should return a
`NULL` value when there is an exact match with the text
supplied in a field.

'orc.schema.resolution'='mapping_type'

A property that sets the column mapping type for tables that use
ORC data format. This property is ignored for other data
formats.

Valid values for column mapping type are as follows:

- name
- position

If the _orc.schema.resolution_ property is
omitted, columns are mapped by name by default. If
_orc.schema.resolution_ is set to any value
other than _'name'_ or
_'position'_, columns are mapped by position.
For more information about column mapping, see [Mapping external table columns to ORC
columns](c-spectrum-external-tables.md#c-spectrum-column-mapping-orc "c-spectrum-external-tables.md#c-spectrum-column-mapping-orc").

###### Note

The COPY command maps to ORC data files only by position. The
_orc.schema.resolution_ table property has no
effect on COPY command behavior.

'write.parallel'='on / off’

A property that sets whether CREATE EXTERNAL TABLE AS should write
data in parallel. By default, CREATE EXTERNAL TABLE AS writes data in
parallel to multiple files, according to the number of slices in the
cluster. The default option is on. When 'write.parallel' is
set to off, CREATE EXTERNAL TABLE AS writes to one or more data files
serially onto Amazon S3. This table property also applies to any subsequent
INSERT statement into the same external table.

‘write.maxfilesize.mb’=‘size’

A property that sets the maximum size (in MB) of each file written
to Amazon S3 by CREATE EXTERNAL TABLE AS. The size must be a valid integer
between 5 and 6200. The default maximum file size is 6,200 MB. This
table property also applies to any subsequent INSERT statement into
the same external table.

‘write.kms.key.id’=‘_value_’

You can specify an AWS Key Management Service key to enable Server–Side
Encryption (SSE) for Amazon S3 objects, where _value_ is
one of the following:

- `auto` to use the default AWS KMS key
  stored in the Amazon S3 bucket.
- _kms-key_ that you specify to encrypt
  data.

_select_statement_

A statement that inserts one or more rows into the external table
by defining any query. All rows that the query produces are written to
Amazon S3 in either text or Parquet format based on the table
definition.

## Examples

A collection of examples is available at [Examples](r_CREATE_EXTERNAL_TABLE_examples.md "r_CREATE_EXTERNAL_TABLE_examples.md").

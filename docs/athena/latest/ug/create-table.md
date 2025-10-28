# CREATE TABLE

Creates a table with the name and the parameters that you specify.

###### Note

This page contains summary reference information. For more information about creating
tables in Athena and an example `CREATE TABLE` statement, see [Create tables in Athena](creating-tables.md "creating-tables.md"). For an example of
creating a database, creating a table, and running a `SELECT` query on the
table in Athena, see [Get started](getting-started.md "getting-started.md").

## Synopsis

```
CREATE EXTERNAL TABLE [IF NOT EXISTS]
 [db_name.]table_name [(col_name data_type [COMMENT col_comment] [, ...] )]
 [COMMENT table_comment]
 [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
 [CLUSTERED BY (col_name, col_name, ...) INTO num_buckets BUCKETS]
 [ROW FORMAT row_format]
 [STORED AS file_format]
 [WITH SERDEPROPERTIES (...)]
 [LOCATION 's3://amzn-s3-demo-bucket/[folder]/']
 [TBLPROPERTIES ( ['has_encrypted_data'='true | false',] ['classification'='aws_glue_classification',] property_name=property_value [, ...] ) ]
```

## Parameters

**EXTERNAL**

Specifies that the table is based on an underlying data file that exists
in Amazon S3, in the `LOCATION` that you specify. Except when creating
[Iceberg](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md") tables,
always use the `EXTERNAL` keyword. If you use `CREATE
 TABLE` without the `EXTERNAL` keyword for non-Iceberg
tables, Athena issues an error. When you create an external table, the data
referenced must comply with the default format or the format that you
specify with the `ROW FORMAT`, `STORED AS`, and
`WITH SERDEPROPERTIES` clauses.

**[IF NOT EXISTS]**

This parameter checks if a table with the same name already exists. If it
does, the parameter returns `TRUE`, and Amazon Athena cancels the
`CREATE TABLE` action. Because cancellation occurs before
Athena calls the data catalog, it doesn't emit a AWS CloudTrail event.

**[db\_name.]table_name**

Specifies a name for the table to be created. The optional
`db_name` parameter specifies the database where the table
exists. If omitted, the current database is assumed. If the table name
includes numbers, enclose `table_name` in quotation marks, for
example `"table123"`. If `table_name` begins with an
underscore, use backticks, for example, `_mytable`. Special
characters (other than underscore) are not supported.

Athena table names are case-insensitive; however, if you work with Apache
Spark, Spark requires lowercase table names. For restrictions on table names
in Athena, see [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").

**[ ( col_name data_type [COMMENT col\_comment] [, ...] ) ]**

Specifies the name for each column to be created, along with the column's
data type. Column names do not allow special characters other than
underscore `(_)`. If `col_name` begins with an
underscore, enclose the column name in backticks, for example
`_mycolumn`. For restrictions on column names in Athena, see
[Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").

The `data_type` value can be any of the following:

- `boolean` – Values are `true` and
  `false`.
- `tinyint` – A 8-bit signed integer in two's
  complement format, with a minimum value of -2^7 and a maximum value
  of 2^7-1.
- `smallint` – A 16-bit signed integer in two's
  complement format, with a minimum value of -2^15 and a maximum value
  of 2^15-1.
- `int` – In Data Definition Language (DDL)
  queries like `CREATE TABLE`, use the `int`
  keyword to represent an integer. In other queries, use the keyword
  `integer`, where `integer` is represented
  as a 32-bit signed value in two's complement format, with a minimum
  value of-2^31 and a maximum value of 2^31-1. In the JDBC driver,
  `integer` is returned, to ensure compatibility with
  business analytics applications.
- `bigint` – A 64-bit signed integer in two's
  complement format, with a minimum value of -2^63 and a maximum value
  of 2^63-1.
- `double` – A 64-bit signed double-precision
  floating point number. The range is 4.94065645841246544e-324d to
  1.79769313486231570e+308d, positive or negative. `double`
  follows the IEEE Standard for Floating-Point Arithmetic (IEEE
  754).
- `float` – A 32-bit signed single-precision
  floating point number. The range is 1.40129846432481707e-45 to
  3.40282346638528860e+38, positive or negative. `float`
  follows the IEEE Standard for Floating-Point Arithmetic (IEEE 754).
  Equivalent to the `real` in Presto. In Athena, use
  `float` in DDL statements like `CREATE
TABLE` and `real` in SQL functions like
  `SELECT CAST`. The AWS Glue crawler returns values in
  `float`, and Athena translates `real` and
  `float` types internally (see the [June 5, 2018](release-notes.md#release-note-2018-06-05 "release-notes.md#release-note-2018-06-05") release notes).
- `decimal [ (`precision`,
`scale`) ]`, where
  `precision` is the
  total number of digits, and
  `scale` (optional) is the
  number of digits in fractional part, the default is 0. For example,
  use these type definitions: `decimal(11,5)`,
  `decimal(15)`. The maximum value for
  `precision` is 38, and the maximum
  value for `scale` is 38.

To specify decimal values as literals, such as when selecting rows
with a specific decimal value in a query DDL expression, specify the
`decimal` type definition, and list the decimal value
as a literal (in single quotes) in your query, as in this example:
`decimal_value = decimal '0.12'`.

- `char` – Fixed length character data, with a
  specified length between 1 and 255, such as `char(10)`.
  For more information, see [CHAR Hive data type](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-char "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-char").
- `varchar` – Variable length character data, with
  a specified length between 1 and 65535, such as
  `varchar(10)`. For more information, see [VARCHAR Hive data type](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-varchar "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-varchar").
- `string` – A string literal enclosed in single
  or double quotes.

###### Note

Non-string data types cannot be cast to `string` in
Athena; cast them to `varchar` instead.

- `binary` – (for data in Parquet)
- `date` – A date in ISO format, such as
  ``YYYY`-`MM`-`DD``.
  For example, `date '2008-09-15'`. An exception is the
  OpenCSVSerDe, which uses the number of days elapsed since January 1,

1970. For more information, see [Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md").

- `timestamp` – Date and time instant in a [`java.sql.Timestamp`](https://docs.oracle.com/javase/8/docs/api/java/sql/Timestamp.html "https://docs.oracle.com/javase/8/docs/api/java/sql/Timestamp.html") compatible format
  up to a maximum resolution of milliseconds, such as
  ``yyyy`-`MM`-`dd`
  `HH`:`mm`:`ss`[.f`...`]`.
 For example, `timestamp '2008-09-15 03:04:05.324'`. An
 exception is the OpenCSVSerDe, which uses `TIMESTAMP`  data in the UNIX numeric format (for example,
 `1579059880000`). For more information, see [Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md").
- `array` < data_type >
- `map` < primitive_type, data_type >
- `struct` < col_name : data_type [comment
  col\_comment] [, ...] >

**[COMMENT table\_comment]**

Creates the `comment` table property and populates it with the
`table_comment` you specify.

**[PARTITIONED BY (col_name data_type [ COMMENT col\_comment ], ... ) ]**

Creates a partitioned table with one or more partition columns that have
the `col_name`, `data_type` and
`col_comment` specified. A table can have one or more
partitions, which consist of a distinct column name and value combination. A
separate data directory is created for each specified combination, which can
improve query performance in some circumstances. Partitioned columns don't
exist within the table data itself. If you use a value for
`col_name` that is the same as a table column, you get an
error. For more information, see [Partitioning
Data](partitions.md "partitions.md").

###### Note

After you create a table with partitions, run a subsequent query that
consists of the [MSCK REPAIR
TABLE](msck-repair-table.md "msck-repair-table.md") clause to refresh partition metadata, for example,
`MSCK REPAIR TABLE cloudfront_logs;`. For partitions that
are not Hive compatible, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md") to load the partitions
so that you can query the data.

**[CLUSTERED BY (col\_name, col\_name, ...) INTO num\_buckets BUCKETS]**

Divides, with or without partitioning, the data in the specified
`col_name` columns into data subsets called _buckets_. The `num_buckets` parameter
specifies the number of buckets to create. Bucketing can improve the
performance of some queries on large data sets.

**[ROW FORMAT row\_format]**

Specifies the row format of the table and its underlying source data if
applicable. For `row_format`, you can specify one or more
delimiters with the `DELIMITED` clause or, alternatively, use the
`SERDE` clause as described below. If `ROW FORMAT`
is omitted or `ROW FORMAT DELIMITED` is specified, a native SerDe
is used.

- [DELIMITED FIELDS TERMINATED BY char [ESCAPED BY char]]
- [DELIMITED COLLECTION ITEMS TERMINATED BY char]
- [MAP KEYS TERMINATED BY char]
- [LINES TERMINATED BY char]
- [NULL DEFINED AS char]

Available only with Hive 0.13 and when the STORED AS file format
is `TEXTFILE`.

**--OR--**

- SERDE 'serde_name' [WITH SERDEPROPERTIES ("property_name" =
  "property_value", "property_name" = "property_value" [, ...]
  )]

The `serde_name` indicates the SerDe to use. The
`WITH SERDEPROPERTIES` clause allows you to provide
one or more custom properties allowed by the SerDe.

**[STORED AS file\_format]**

Specifies the file format for table data. If omitted,
`TEXTFILE` is the default. Options for
`file_format` are:

- SEQUENCEFILE
- TEXTFILE
- RCFILE
- ORC
- PARQUET
- AVRO
- ION
- INPUTFORMAT input_format_classname OUTPUTFORMAT
  output_format_classname

**[LOCATION 's3://amzn-s3-demo-bucket/[folder]/']**

Specifies the location of the underlying data in Amazon S3 from which the table
is created. The location path must be a bucket name or a bucket name and one
or more folders. If you are using partitions, specify the root of the
partitioned data. For more information about table location, see [Specify a table location in Amazon S3](tables-location-format.md "tables-location-format.md"). For information about data format and permissions, see [Amazon S3 considerations](creating-tables.md#s3-considerations "creating-tables.md#s3-considerations").

Use a trailing slash for your folder or bucket. Do not use file names or
glob characters.

**Use:**

`s3://amzn-s3-demo-bucket/`

`s3://amzn-s3-demo-bucket/`folder`/`

`s3://amzn-s3-demo-bucket/`folder`/`anotherfolder`/`

**Don't use:**

`s3://amzn-s3-demo-bucket`

`s3://amzn-s3-demo-bucket/*`

`s3://amzn-s3-demo-bucket/`mydatafile.dat``

**[TBLPROPERTIES ( ['has\_encrypted\_data'='true | false',]
['classification'='classification\_value',] property_name=property_value [, ...]
) ]**

Specifies custom metadata key-value pairs for the table definition in
addition to predefined table properties, such as
`"comment"`.

has_encrypted_data – Athena has a
built-in property, `has_encrypted_data`. Set this property to
`true` to indicate that the underlying dataset specified by
`LOCATION` is encrypted. If omitted and if the workgroup's
settings do not override client-side settings, `false` is
assumed. If omitted or set to `false` when underlying data is
encrypted, the query results in an error. For more information, see [Encryption at rest](encryption.md "encryption.md").

classification – Tables created for
Athena in the CloudTrail console add `cloudtrail` as a value for the
`classification` property. To run ETL jobs, AWS Glue requires
that you create a table with the `classification` property to
indicate the data type for AWS Glue as `csv`, `parquet`,
`orc`, `avro`, or `json`. For example,
`'classification'='csv'`. ETL jobs will fail if you do not
specify this property. You can subsequently specify it using the AWS Glue
console, API, or CLI. For more information, see [Create tables for ETL jobs](schema-classifier.md "schema-classifier.md") and
[Authoring Jobs in AWS Glue](../../../glue/latest/dg/author-job.md "../../../glue/latest/dg/author-job.md") in the
_AWS Glue Developer Guide_.

compression_level – The
`compression_level` property specifies the compression level
to use. This property applies only to ZSTD compression. Possible values are
from 1 to 22. The default value is 3. For more information, see [Use ZSTD compression levels](compression-support-zstd-levels.md "compression-support-zstd-levels.md").

For more information about other table properties, see [ALTER TABLE SET
TBLPROPERTIES](alter-table-set-tblproperties.md "alter-table-set-tblproperties.md").

## Examples

The following example `CREATE TABLE` statement creates a table based on
tab-separated planet data stored in Amazon S3.

```
CREATE EXTERNAL TABLE planet_data (
  planet_name string,
  order_from_sun int,
  au_to_sun float,
  mass float,
  gravity_earth float,
  orbit_years float,
  day_length float
  )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION 's3://amzn-s3-demo-bucket/tsv/'
```

Note the following points:

- The `ROW FORMAT DELIMITED` clause indicates that the data is
  delimited by a specific character.
- The `FIELDS TERMINATED BY '\t'` clause specifies that the fields in
  the TSV data are separated by the tab character ('\t').
- The `STORED AS TEXTFILE` clause indicates that the data is stored
  as plain text files in Amazon S3.

To query the data, you could use a simple `SELECT` statement like the
following:

```
SELECT * FROM planet_data
```

To use the example to create your own TSV table in Athena, replace the table and column
names with the names and data types of your own table and columns, and update the
`LOCATION` clause to point to the Amazon S3 path where your TSV files are
stored.

For more information about creating tables, see [Create tables in Athena](creating-tables.md "creating-tables.md").

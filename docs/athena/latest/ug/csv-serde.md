# Open CSV SerDe for processing CSV

Use the Open CSV SerDe to create Athena tables from comma-separated data (CSV) data.

## Serialization library name

The serialization library name for the Open CSV SerDe is
`org.apache.hadoop.hive.serde2.OpenCSVSerde`. For source code
information, see [CSV SerDe](https://cwiki.apache.org/confluence/display/Hive/CSV+Serde "https://cwiki.apache.org/confluence/display/Hive/CSV+Serde") in the Apache documentation.

## Using the Open CSV SerDe

To use this SerDe, specify its fully qualified class name after `ROW FORMAT
 SERDE`. Also specify the delimiters inside `SERDEPROPERTIES`, as in
the following example.

```
...
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar"     = "`",
  "escapeChar"    = "\\"
)
```

### Ignore headers

To ignore headers in your data when you define a table, you can use the
`skip.header.line.count` table property, as in the following
example.

```
TBLPROPERTIES ("skip.header.line.count"="1")
```

For examples, see the `CREATE TABLE` statements in [Query Amazon VPC flow logs](vpc-flow-logs.md "vpc-flow-logs.md") and [Query Amazon CloudFront logs](cloudfront-logs.md "cloudfront-logs.md").

### Using NULL for invalid

data

To use NULL values for data that fails to deserialize into the column’s defined
type, you can use the `use.null.for.invalid.data` table property, as
shown in the following example.

```
TBLPROPERTIES ("skip.header.line.count"="1")
```

###### Important

Setting `use.null.for.invalid.data` to `TRUE` can cause
incorrect or unexpected results because `NULL` values replace invalid
data in columns with schema mismatches. We recommend that you fix the data in your files or table
schema rather than enabling this property. When you enable this property,
queries will not fail on invalid data, which may prevent you from discovering
data quality issues.

### Considerations for

string data

The Open CSV SerDe has the following characteristics for string data:

- Uses double quotes (`"`) as the default quote character, and
  allows you to specify separator, quote, and escape characters, such as:

```
WITH SERDEPROPERTIES ("separatorChar" = ",", "quoteChar" = "`", "escapeChar" = "\\" )
```

- You cannot escape `\t` or `\n` directly. To escape
  them, use `"escapeChar" = "\\"`. For an example, see [Example: Escaping \t or \n](#csv-serde-opencsvserde-example-escaping-t-or-n "#csv-serde-opencsvserde-example-escaping-t-or-n").
- The Open CSV SerDe does not support embedded line breaks in CSV
  files.

### Considerations

for non-string data

For data types other than `STRING`, the Open CSV SerDe behaves as
follows:

- Recognizes `BOOLEAN`, `BIGINT`, `INT`,
  and `DOUBLE` data types.
- Does not recognize empty or null values in columns defined as a numeric
  data type, leaving them as `string`. One workaround is to create
  the column with the null values as `string` and then use
  `CAST` to convert the field in a query to a numeric data
  type, supplying a default value of `0` for nulls. For more
  information, see [When I query CSV data in Athena, I get the error HIVE_BAD_DATA: Error
  parsing field value](https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-error-csv/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-error-csv/") in the AWS Knowledge Center.
- For columns specified with the `timestamp` data type in your
  `CREATE TABLE` statement, recognizes `TIMESTAMP`
  data if it is specified in the UNIX numeric format in milliseconds, such as
  `1579059880000`. For an example, see [Example: Using the TIMESTAMP type and DATE type specified in the UNIX numeric format](#csv-serde-opencsvserde-example-timestamp-unix "#csv-serde-opencsvserde-example-timestamp-unix").
  - The Open CSV SerDe does not support `TIMESTAMP` in the
    JDBC-compliant `java.sql.Timestamp` format, such as
    `"YYYY-MM-DD HH:MM:SS.fffffffff"` (9 decimal place
    precision).

- For columns specified with the `DATE` data type in your
  `CREATE TABLE` statement, recognizes values as dates if the
  values represent the number of days that elapsed since January 1, 1970. For
  example, the value `18276` in a column with the `date`
  data type renders as `2020-01-15` when queried. In this UNIX
  format, each day is considered to have 86,400 seconds.
  - The Open CSV SerDe does not support `DATE` in any other
    format directly. To process timestamp data in other formats, you can
    define the column as `string` and then use time
    conversion functions to return the desired results in your
    `SELECT` query. For more information, see the article
    [When I query a table in Amazon Athena, the TIMESTAMP result is
    empty](https://aws.amazon.com/premiumsupport/knowledge-center/query-table-athena-timestamp-empty/ "https://aws.amazon.com/premiumsupport/knowledge-center/query-table-athena-timestamp-empty/") in the [AWS knowledge center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/").

- To further convert columns to the desired type in a table, you can [create a view](views.md "views.md") over the table and use
  `CAST` to convert to the desired type.

## Examples

###### Example: Querying simple CSV data

The following example assumes you have CSV data saved in the location
`s3://amzn-s3-demo-bucket/mycsv/` with the following contents:

```
"a1","a2","a3","a4"
"1","2","abc","def"
"a","a1","abc3","ab4"
```

Use a `CREATE TABLE` statement to create an Athena table based on the
data. Reference `OpenCSVSerde` (note the "d" in lower case) after
`ROW FORMAT SERDE` and specify the character separator, quote
character, and escape character in `WITH SERDEPROPERTIES`, as in the
following example.

```
CREATE EXTERNAL TABLE myopencsvtable (
   col1 string,
   col2 string,
   col3 string,
   col4 string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar' = '"',
   'escapeChar' = '\\'
   )
STORED AS TEXTFILE
LOCATION 's3://amzn-s3-demo-bucket/mycsv/';
```

Query all values in the table:

```
SELECT * FROM myopencsvtable;
```

The query returns the following values:

```
col1     col2    col3    col4
-----------------------------
a1       a2      a3      a4
1        2       abc     def
a        a1      abc3    ab4
```

###### Example: Using the TIMESTAMP type and DATE type specified in the UNIX numeric

format

Consider the following three columns of comma-separated data. The values in each
column are enclosed in double quotes.

```
"unixvalue creationdate 18276 creationdatetime 1579059880000","18276","1579059880000"
```

The following statement creates a table in Athena from the specified Amazon S3 bucket
location.

```
CREATE EXTERNAL TABLE IF NOT EXISTS testtimestamp1(
 `profile_id` string,
 `creationdate` date,
 `creationdatetime` timestamp
 )
 ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
 LOCATION 's3://amzn-s3-demo-bucket'
```

Next, run the following query:

```
SELECT * FROM testtimestamp1
```

The query returns the following result, showing the date and time data:

```
profile_id                                                        creationdate     creationdatetime
unixvalue creationdate 18276 creationdatetime 1579146280000       2020-01-15       2020-01-15 03:44:40.000
```

###### Example: Escaping \t or \n

Consider the following test data:

```
" \\t\\t\\n 123 \\t\\t\\n ",abc
" 456 ",xyz
```

The following statement creates a table in Athena, specifying that
`"escapeChar" = "\\"`.

```
CREATE EXTERNAL TABLE test1 (
f1 string,
s2 string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ("separatorChar" = ",", "escapeChar" = "\\")
LOCATION 's3://amzn-s3-demo-bucket/dataset/test1/'
```

Next, run the following query:

```
SELECT * FROM test1;
```

It returns this result, correctly escaping `\t` or
`\n`:

```
f1            s2
\t\t\n 123 \t\t\n            abc
456                          xyz
```

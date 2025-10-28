# Troubleshoot issues in Athena

The Athena team has gathered the following troubleshooting information from customer
issues. Although not comprehensive, it includes advice regarding some common performance,
timeout, and out of memory issues.

###### Topics

- [CREATE TABLE AS
  SELECT (CTAS)](#troubleshooting-athena-create-table-as-select-ctas "#troubleshooting-athena-create-table-as-select-ctas")
- [Data file issues](#troubleshooting-athena-data-file-issues "#troubleshooting-athena-data-file-issues")
- [Linux Foundation Delta Lake
  tables](#troubleshooting-athena-delta-lake-tables "#troubleshooting-athena-delta-lake-tables")
- [Federated queries](#troubleshooting-athena-federated-queries "#troubleshooting-athena-federated-queries")
- [JSON related errors](#troubleshooting-athena-json-related-errors "#troubleshooting-athena-json-related-errors")
- [MSCK REPAIR TABLE](#troubleshooting-athena-msck-repair-table "#troubleshooting-athena-msck-repair-table")
- [Output issues](#troubleshooting-athena-output-issues "#troubleshooting-athena-output-issues")
- [Parquet issues](#troubleshooting-athena-parquet-issues "#troubleshooting-athena-parquet-issues")
- [Partitioning issues](#troubleshooting-athena-partitioning-issues "#troubleshooting-athena-partitioning-issues")
- [Permissions](#troubleshooting-athena-permissions "#troubleshooting-athena-permissions")
- [Query syntax issues](#troubleshooting-athena-query-syntax-issues "#troubleshooting-athena-query-syntax-issues")
- [Query timeout
  issues](#troubleshooting-athena-query-timeout-issues "#troubleshooting-athena-query-timeout-issues")
- [Throttling issues](#troubleshooting-athena-throttling-issues "#troubleshooting-athena-throttling-issues")
- [Views](#troubleshooting-athena-views "#troubleshooting-athena-views")
- [Workgroups](#troubleshooting-athena-workgroups "#troubleshooting-athena-workgroups")
- [Additional
  resources](#troubleshooting-athena-additional-resources "#troubleshooting-athena-additional-resources")
- [Athena error catalog](error-reference.md "error-reference.md")

## CREATE TABLE AS

SELECT (CTAS)

### Duplicated data occurs with concurrent CTAS statements

Athena does not maintain concurrent validation for CTAS. Make sure that there is no
duplicate CTAS statement for the same location at the same time. Even if a CTAS or
INSERT INTO statement fails, orphaned data can be left in the data location
specified in the statement.

### HIVE_TOO_MANY_OPEN_PARTITIONS

When you use a CTAS statement to create a table with more than 100 partitions, you
may receive the error **`HIVE_TOO_MANY_OPEN_PARTITIONS: Exceeded limit of
 100 open writers for partitions/buckets`**. To work around this
limitation, you can use a CTAS statement and a series of `INSERT INTO`
statements that create or insert up to 100 partitions each. For more information,
see [Use CTAS and INSERT INTO to work around the 100 partition
limit](ctas-insert-into.md "ctas-insert-into.md").

## Data file issues

### Athena

cannot read hidden files

Athena treats sources files that start with an underscore (\_) or a dot (.) as
hidden. To work around this limitation, rename the files.

### Athena reads files that I excluded from the AWS Glue crawler

Athena does not recognize [exclude
patterns](../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude "../../../glue/latest/dg/define-crawler.md#crawler-data-stores-exclude") that you specify an AWS Glue crawler. For example, if you have an
Amazon S3 bucket that contains both `.csv` and
`.json` files and you exclude the `.json`
files from the crawler, Athena queries both groups of files. To avoid this, place the
files that you want to exclude in a different location.

### HIVE_BAD_DATA: Error parsing field value

This error can occur in the following scenarios:

- The data type defined in the table doesn't match the source data, or a
  single field contains different types of data. For suggested resolutions,
  see [My Amazon Athena query fails with the error "HIVE_BAD_DATA: Error parsing
  field value for field x: For input string: "12312845691""](https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-parsing-field-value/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-parsing-field-value/") in the
  AWS Knowledge Center.
- Null values are present in an integer field. One workaround is to create
  the column with the null values as `string` and then use
  `CAST` to convert the field in a query, supplying a default
  value of `0` for nulls. For more information, see [When I query CSV data in Athena, I get the error "HIVE_BAD_DATA: Error
  parsing field value '' for field x: For input string: """](https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-error-csv/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-hive-bad-data-error-csv/") in the
  AWS Knowledge Center.

### HIVE_CANNOT_OPEN_SPLIT: Error opening Hive split

s3://amzn-s3-demo-bucket

This error can occur when you query an Amazon S3 bucket prefix that has a large number
of objects. For more information, see [How do
I resolve the "HIVE_CANNOT_OPEN_SPLIT: Error opening Hive split
s3://amzn-s3-demo-bucket/: Slow down" error in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/hive-cannot-open-split-503-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/hive-cannot-open-split-503-athena/") in the AWS
Knowledge Center.

### HIVE_CURSOR_ERROR: com.amazonaws.services.s3.model.AmazonS3Exception: The

specified key does not exist

This error usually occurs when a file is removed when a query is running. Either
rerun the query, or check your workflow to see if another job or process is
modifying the files when the query is running.

### HIVE_CURSOR_ERROR: Unexpected end of input stream

This message indicates the file is either corrupted or empty. Check the integrity
of the file and rerun the query.

### HIVE_FILESYSTEM_ERROR: Incorrect fileSize `1234567`

for file

This message can occur when a file has changed between query planning and query
execution. It usually occurs when a file on Amazon S3 is replaced in-place (for example,
a `PUT` is performed on a key where an object already exists). Athena does
not support deleting or replacing the contents of a file when a query is running. To
avoid this error, schedule jobs that overwrite or delete files at times when queries
do not run, or only write data to new files or partitions.

### HIVE_UNKNOWN_ERROR: Unable to create input format

This error can be a result of issues like the following:

- The AWS Glue crawler wasn't able to classify the data format
- Certain AWS Glue table definition properties are empty
- Athena doesn't support the data format of the files in Amazon S3

For more information, see [How
do I resolve the error "unable to create input format" in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-unable-to-create-input-format/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-unable-to-create-input-format/") in the
AWS Knowledge Center or watch the Knowledge Center [video](https://www.youtube.com/watch?v=CGzXW3hRa8g "https://www.youtube.com/watch?v=CGzXW3hRa8g").

### The S3 location provided to save your query results is invalid.

Make sure that you have specified a valid S3 location for your query results. For
more information, see [Specify a query result location](query-results-specify-location.md "query-results-specify-location.md") in the [Work with query results and recent queries](querying.md "querying.md") topic.

## Linux Foundation Delta Lake

tables

### Delta

Lake table schema is out of sync

When you query a Delta Lake table that has a schema in AWS Glue that is outdated, you
can receive the following error message:

```
INVALID_GLUE_SCHEMA: Delta Lake table schema in Glue does not match the most recent schema of the
Delta Lake transaction log. Please ensure that you have the correct schema defined in Glue.
```

The schema can become outdated if it is modified in AWS Glue after it has been added
to Athena. To update the schema, perform one of the following steps:

- In AWS Glue, run the [AWS Glue crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md").
- In Athena, [drop the
  table](drop-table.md "drop-table.md") and [create](create-table.md "create-table.md") it again.
- Add missing columns manually, either by using the [ALTER TABLE ADD COLUMNS](alter-table-add-columns.md "alter-table-add-columns.md") statement in Athena, or by
  [editing
  the table schema in AWS Glue](../../../glue/latest/dg/console-tables.md#console-tables-details "../../../glue/latest/dg/console-tables.md#console-tables-details").

## Federated queries

### Timeout while calling ListTableMetadata

A call to the [ListTableMetadata](../APIReference/API_ListTableMetadata.md "../APIReference/API_ListTableMetadata.md") API can timeout if there are lot of tables in the
data source, if the data source is slow, or if the network is slow. To troubleshoot
this issue, try the following steps.

- Check the number of tables – If you
  have more than 1000 tables, try reducing the number of tables. For the
  fastest `ListTableMetadata` response, we recommend having fewer
  than 1000 tables per catalog.
- Check the Lambda configuration –
  Monitoring the Lambda function behavior is critical. When you use federated
  catalogs, be sure to examine the execution logs of the Lambda function. Based
  on the results, adjust the memory and timeout values accordingly. To
  identify any potential issues with timeouts, revisit your Lambda
  configuration. For more information, see [Configuring function timeout (console)](../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console "../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console") in the
  _AWS Lambda Developer Guide_.
- Check federated data source logs –
  Examine the logs and error messages from the federated data source to see if
  there are any issues or errors. The logs can provide valuable insights into
  the cause of the timeout.
- Use `StartQueryExecution` to fetch
  metadata – If you have more than 1000 tables, it can
  take longer than expected to retrieve metadata using your federated
  connector. Because the asynchronous nature of [StartQueryExecution](../APIReference/API_StartQueryExecution.md "../APIReference/API_StartQueryExecution.md") ensures that Athena runs the query in the
  most optimal way, consider using `StartQueryExecution` as an
  alternative to `ListTableMetadata`. The following AWS CLI examples
  show how `StartQueryExecution` can be used instead of
  `ListTableMetadata` to get all the metadata of tables in your
  data catalog.

First, run a query that gets all the tables, as in the following
example.

```
aws athena start-query-execution --region us-east-1 \
--query-string "SELECT table_name FROM information_schema.tables LIMIT 50" \
--work-group "`your-work-group-name`"
```

Next, retrieve the metadata of an individual table, as in the following
example.

```
aws athena start-query-execution --region us-east-1 \
--query-string "SELECT * FROM information_schema.columns \
WHERE table_name = '`your-table-name`' AND \
table_catalog = '`your-catalog-name`'" \
--work-group "`your-work-group-name`"
```

The time taken to get the results depends on the number of tables in your
catalog.

For more information about troubleshooting federated queries, see [Common_Problems](https://github.com/awslabs/aws-athena-query-federation/wiki/Common_Problems "https://github.com/awslabs/aws-athena-query-federation/wiki/Common_Problems") in the awslabs/aws-athena-query-federation section of
GitHub, or see the documentation for the individual [Athena data source connectors](connectors-available.md "connectors-available.md").

## JSON related errors

### NULL or incorrect data errors when trying to read JSON data

NULL or incorrect data errors when you try read JSON data
can be due to a number of causes. To identify lines that are causing errors when you
are using the OpenX SerDe, set `ignore.malformed.json` to
`true`. Malformed records will return as NULL. For more information,
see [I get errors when I try to read JSON data in Amazon Athena](https://aws.amazon.com/premiumsupport/knowledge-center/error-json-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/error-json-athena/") in the AWS
Knowledge Center or watch the Knowledge Center [video](https://youtu.be/ME7Pv1qPFLM "https://youtu.be/ME7Pv1qPFLM").

### HIVE_BAD_DATA: Error parsing field value for field 0: java.lang.String cannot

be cast to org.openx.data.jsonserde.json.JSONObject

The [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md") throws
this error when it fails to parse a column in an Athena query. This can happen if you
define a column as a `map` or `struct`, but the underlying
data is actually a `string`, `int`, or other primitive
type.

### HIVE_CURSOR_ERROR: Row is not a valid JSON object - JSONException: Duplicate

key

This error occurs when you use Athena to query AWS Config resources that have multiple
tags with the same name in different case. The solution is to run `CREATE
 TABLE` using `WITH SERDEPROPERTIES 'case.insensitive'='false'`
and map the names. For information about `case.insensitive` and mapping,
see [JSON SerDe libraries](json-serde.md "json-serde.md"). For more information,
see [How do I resolve "HIVE_CURSOR_ERROR: Row is not a valid JSON object -
JSONException: Duplicate key" when reading files from AWS Config in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/json-duplicate-key-error-athena-config/ "https://aws.amazon.com/premiumsupport/knowledge-center/json-duplicate-key-error-athena-config/") in
the AWS Knowledge Center.

### HIVE_CURSOR_ERROR messages with pretty-printed JSON

The [Hive JSON SerDe](hive-json-serde.md "hive-json-serde.md") and [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md") libraries expect
each JSON document to be on a single line of text with no line termination
characters separating the fields in the record. If the JSON text is in pretty print
format, you may receive an error message like **`HIVE_CURSOR_ERROR: Row is
 not a valid JSON Object`** or **`HIVE_CURSOR_ERROR:
 JsonParseException: Unexpected end-of-input: expected close marker for
 OBJECT`** when you attempt to query the table after you create it. For
more information, see [JSON data
files](https://github.com/rcongiu/Hive-JSON-Serde#json-data-files "https://github.com/rcongiu/Hive-JSON-Serde#json-data-files") in the OpenX SerDe documentation on GitHub.

### Multiple JSON records return a SELECT COUNT of 1

If you're using the [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md"), make sure that the records are separated by
a newline character. For more information, see [The SELECT COUNT query in Amazon Athena returns only one record even though the
input JSON file has multiple records](https://aws.amazon.com/premiumsupport/knowledge-center/select-count-query-athena-json-records/ "https://aws.amazon.com/premiumsupport/knowledge-center/select-count-query-athena-json-records/") in the AWS Knowledge
Center.

### Cannot query a table created by a AWS Glue crawler that uses a custom JSON

classifier

The Athena engine does not support [custom JSON
classifiers](../../../glue/latest/dg/custom-classifier.md#custom-classifier-json "../../../glue/latest/dg/custom-classifier.md#custom-classifier-json"). To work around this issue, create a new table without the
custom classifier. To transform the JSON, you can use CTAS or create a view. For
example, if you are working with arrays, you can use the UNNEST option to flatten
the JSON. Another option is to use a AWS Glue ETL job that supports the custom
classifier, convert the data to parquet in Amazon S3, and then query it in Athena.

## MSCK REPAIR TABLE

For information about MSCK REPAIR TABLE related issues, see the [Considerations and
limitations](msck-repair-table.md#msck-repair-table-considerations "msck-repair-table.md#msck-repair-table-considerations") and [Troubleshooting](msck-repair-table.md#msck-repair-table-troubleshooting "msck-repair-table.md#msck-repair-table-troubleshooting") sections of the [MSCK REPAIR TABLE](msck-repair-table.md "msck-repair-table.md") page.

## Output issues

### Unable

to verify/create output bucket

This error can occur if the specified query result location doesn't exist or if
the proper permissions are not present. For more information, see [How do I
resolve the "unable to verify/create output bucket" error in Amazon Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-output-bucket-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-output-bucket-error/")
in the AWS Knowledge Center.

### TIMESTAMP result

is empty

Athena requires the Java TIMESTAMP format. For more information, see [When I
query a table in Amazon Athena, the TIMESTAMP result is empty](https://aws.amazon.com/premiumsupport/knowledge-center/query-table-athena-timestamp-empty/ "https://aws.amazon.com/premiumsupport/knowledge-center/query-table-athena-timestamp-empty/") in the AWS
Knowledge Center.

### Store Athena query output in a format other than CSV

By default, Athena outputs files in CSV format only. To output the results of a
`SELECT` query in a different format, you can use the
`UNLOAD` statement. For more information, see [UNLOAD](unload.md "unload.md"). You can also use a CTAS query that uses the
`format`
[table
property](create-table-as.md#ctas-table-properties "create-table-as.md#ctas-table-properties") to configure the output format. Unlike `UNLOAD`, the
CTAS technique requires the creation of a table. For more information, see [How
can I store an Athena query output in a format other than CSV, such as a
compressed format?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-query-output-different-format/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-query-output-different-format/") in the AWS Knowledge Center.

### The S3 location provided to save your query results is invalid

You can receive this error message if your output bucket location is not in the
same Region as the Region in which you run your query. To avoid this, specify a
query results location in the Region in which you run the query. For steps, see
[Specify a query result location](query-results-specify-location.md "query-results-specify-location.md").

## Parquet issues

### org.apache.parquet.io.GroupColumnIO cannot be cast to

org.apache.parquet.io.PrimitiveColumnIO

This error is caused by a parquet schema mismatch. A column that has a
non-primitive type (for example, `array`) has been declared as a
primitive type (for example, `string`) in AWS Glue. To troubleshoot this
issue, check the data schema in the files and compare it with schema declared in
AWS Glue.

### Parquet

statistics issues

When you read Parquet data, you might receive error messages like the
following:

```
HIVE_CANNOT_OPEN_SPLIT: Index x out of bounds for length y
HIVE_CURSOR_ERROR: Failed to read x bytes
HIVE_CURSOR_ERROR: FailureException at Malformed input: offset=x
HIVE_CURSOR_ERROR: FailureException at java.io.IOException:
can not read class org.apache.parquet.format.PageHeader: Socket is closed by peer.
```

To workaround this issue, use the [CREATE TABLE](create-table.md "create-table.md") or [ALTER TABLE SET
TBLPROPERTIES](alter-table-set-tblproperties.md "alter-table-set-tblproperties.md") statement to set the Parquet
SerDe `parquet.ignore.statistics` property to `true`, as in
the following examples.

CREATE TABLE example

```
...
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES ('parquet.ignore.statistics'='true')
STORED AS PARQUET
...

```

ALTER TABLE example

```
ALTER TABLE ... SET TBLPROPERTIES ('parquet.ignore.statistics'='true')
```

For more information about the Parquet Hive SerDe, see [Parquet SerDe](parquet-serde.md "parquet-serde.md").

## Partitioning issues

### MSCK REPAIR TABLE does not remove stale partitions

If you delete a partition manually in Amazon S3 and then run MSCK REPAIR TABLE, you may
receive the error message **`Partitions missing from filesystem`**.
This occurs because MSCK REPAIR TABLE doesn't remove stale partitions from table
metadata. Use [ALTER TABLE DROP
PARTITION](alter-table-drop-partition.md "alter-table-drop-partition.md") to remove the stale partitions
manually. For more information, see the "Troubleshooting" section of the [MSCK REPAIR TABLE](msck-repair-table.md "msck-repair-table.md") topic.

### MSCK REPAIR TABLE

failure

When a large amount of partitions (for example, more than 100,000) are associated
with a particular table, `MSCK REPAIR TABLE` can fail due to memory
limitations. To work around this limit, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md")
instead.

### MSCK REPAIR TABLE detects partitions but doesn't add them to AWS Glue

This issue can occur if an Amazon S3 path is in camel case instead of lower case or an
IAM policy doesn't allow the `glue:BatchCreatePartition` action. For
more information, see [MSCK
REPAIR TABLE detects partitions in Athena but does not add them to the
AWS Glue Data Catalog](https://aws.amazon.com/premiumsupport/knowledge-center/athena-aws-glue-msck-repair-table/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-aws-glue-msck-repair-table/") in the AWS Knowledge Center.

### Partition projection ranges with the date format of dd-MM-yyyy-HH-mm-ss or

yyyy-MM-dd do not work

To work correctly, the date format must be set to `yyyy-MM-dd
 HH:00:00`. For more information, see the Stack Overflow post [Athena partition projection not working as expected](https://stackoverflow.com/questions/63943920/athena-partition-projection-not-working-as-expected "https://stackoverflow.com/questions/63943920/athena-partition-projection-not-working-as-expected").

### PARTITION BY doesn't support the BIGINT type

Convert the data type to `string` and retry.

### No

meaningful partitions available

This error message usually means the partition settings have been corrupted. To
resolve this issue, drop the table and create a table with new partitions.

### Partition projection does not work in conjunction with range partitions

Check that the time range unit [projection.<columnName>.interval.unit](partition-projection-supported-types.md#partition-projection-date-type "partition-projection-supported-types.md#partition-projection-date-type")
matches the delimiter for the partitions. For example, if partitions are delimited
by days, then a range unit of hours will not work.

### Partition projection error when range specified by hyphen

Specifying the `range` table property with a hyphen instead of a comma
produces an error like **`INVALID_TABLE_PROPERTY: For input string:
 "`number`-`number`"`**.
Ensure that the range values are separated by a comma, not a hyphen. For more
information, see [Integer type](partition-projection-supported-types.md#partition-projection-integer-type "partition-projection-supported-types.md#partition-projection-integer-type").

### HIVE_UNKNOWN_ERROR: Unable to create input format

One or more of the glue partitions are declared in a different format as each glue
partition has their own specific input format independently. Please check how your
partitions are defined in AWS Glue.

### HIVE_PARTITION_SCHEMA_MISMATCH

If the schema of a partition differs from the schema of the table, a query can
fail with the error message
**`HIVE_PARTITION_SCHEMA_MISMATCH`**.

For each table within the AWS Glue Data Catalog that has partition columns, the
schema is stored at the table level and for each individual partition within the
table. The schema for partitions are populated by an AWS Glue crawler based on the
sample of data that it reads within the partition.

When Athena runs a query, it validates the schema of the table and the schema of
any partitions necessary for the query. The validation compares the column data
types in order and makes sure that they match for the columns that overlap. This
prevents unexpected operations such as adding or removing columns from the middle of
a table. If Athena detects that the schema of a partition differs from the schema of
the table, Athena may not be able to process the query and fails with
`HIVE_PARTITION_SCHEMA_MISMATCH`.

There are a few ways to fix this issue. First, if the data was accidentally added,
you can remove the data files that cause the difference in schema, drop the
partition, and re-crawl the data. Second, you can drop the individual partition and
then run `MSCK REPAIR` within Athena to re-create the partition using the
table's schema. This second option works only if you are confident that the schema
applied will continue to read the data correctly.

### SemanticException table is not partitioned but partition spec exists

This error can occur when no partitions were defined in the `CREATE
 TABLE` statement. For more information, see [How
can I troubleshoot the error "FAILED: SemanticException table is not partitioned
but partition spec exists" in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-failed-semanticexception-table/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-failed-semanticexception-table/") in the AWS Knowledge
Center.

### Zero byte `_$folder$` files

If you run an `ALTER TABLE ADD PARTITION` statement and mistakenly
specify a partition that already exists and an incorrect Amazon S3 location, zero byte
placeholder files of the format
``partition_value`\_$folder$` are
created in Amazon S3. You must remove these files manually.

To prevent this from happening, use the `ADD IF NOT EXISTS` syntax in
your `ALTER TABLE ADD PARTITION` statement, like this:

```
ALTER TABLE table_name ADD IF NOT EXISTS PARTITIION […]
```

### Zero records returned from partitioned data

This issue can occur for a variety of reasons. For possible causes and
resolutions, see [I created a table in
Amazon Athena with defined partitions, but when I query the table, zero records are
returned](https://aws.amazon.com/premiumsupport/knowledge-center/athena-empty-results/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-empty-results/") in the AWS Knowledge Center.

See also [HIVE_TOO_MANY_OPEN_PARTITIONS](#troubleshooting-athena-ctas-hive-too-many-open-partitions "#troubleshooting-athena-ctas-hive-too-many-open-partitions").

## Permissions

### Access denied error when querying Amazon S3

This can occur when you don't have permission to read the data in the bucket,
permission to write to the results bucket, or the Amazon S3 path contains a Region
endpoint like `us-east-1.amazonaws.com`. For more information, see [When I run an Athena query, I get an "access denied" error](https://aws.amazon.com/premiumsupport/knowledge-center/access-denied-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/access-denied-athena/") in the AWS
Knowledge Center.

### Access denied with status code: 403 error when running DDL queries on encrypted

data in Amazon S3

When you may receive the error message **`Access Denied (Service: Amazon
 S3; Status Code: 403; Error Code: AccessDenied; Request ID:
 `<request_id>`)`** if the following
conditions are true:

1. You run a DDL query like `ALTER TABLE ADD PARTITION` or
   `MSCK REPAIR TABLE`.
2. You have a bucket that has [default
   encryption](../../../AmazonS3/latest/userguide/default-bucket-encryption.md "../../../AmazonS3/latest/userguide/default-bucket-encryption.md") configured to use `SSE-S3`.
3. The bucket also has a bucket policy like the following that forces
   `PutObject` requests to specify the `PUT` headers
   `"s3:x-amz-server-side-encryption": "true"` and
   `"s3:x-amz-server-side-encryption": "AES256"`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`<resource-name>`/*",
 "Condition": {
 "Null": {
 "s3:x-amz-server-side-encryption": "true"
 }
 }
 },
 {
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`<resource-name>`/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "AES256"
 }
 }
 }
 ]
}`

```

In a case like this, the recommended solution is to remove the bucket policy like
the one above given that the bucket's default encryption is already present.

### Access denied with status code: 403 when querying an Amazon S3 bucket in another

account

This error can occur when you try to query logs written
by another AWS service and the second account is the bucket owner but does not own
the objects in the bucket. For more information, see [I
get the Amazon S3 exception "access denied with status code: 403" in Amazon Athena when I
query a bucket in another account](https://aws.amazon.com/premiumsupport/knowledge-center/athena-access-denied-status-code-403/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-access-denied-status-code-403/") in the AWS Knowledge Center.

### Use IAM role credentials to connect to the Athena JDBC driver

You can retrieve a role's temporary credentials to authenticate the [JDBC connection to
Athena](connect-with-jdbc.md "connect-with-jdbc.md"). Temporary credentials have a maximum lifespan of 12 hours. For
more information, see [How can I use my
IAM role credentials or switch to another IAM role when connecting to Athena
using the JDBC driver?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-iam-jdbc-driver/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-iam-jdbc-driver/") in the AWS Knowledge Center.

### Required table

storage descriptor is not populated

This can occur when you try to query or view a table that you don’t have
permissions to. For this, the recommended solution is to grant `DESCRIBE`
and `SELECT` permissions on the resources through AWS Lake Formation. If your
resource is shared across accounts, where original resource exists in account A and
you want to query against a linked resource in account B. You must ensure that your
role has `DESCRIBE` permission on the original resource in account A, and
`SELECT` permission on the linked resource in account B.

## Query syntax issues

### FAILED:

NullPointerException name is null

If you use the AWS Glue [CreateTable](../../../glue/latest/webapi/API_CreateTable.md "../../../glue/latest/webapi/API_CreateTable.md") API operation
or the AWS CloudFormation [`AWS::Glue::Table`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.md") template to create a table for use in Athena without
specifying the `TableType` property and then run a DDL query like
`SHOW CREATE TABLE` or `MSCK REPAIR TABLE`, you can
receive the error message **`FAILED: NullPointerException Name is
 null`**.

To resolve the error, specify a value for the [TableInput](../../../glue/latest/webapi/API_TableInput.md "../../../glue/latest/webapi/API_TableInput.md")
`TableType` attribute as part of the AWS Glue `CreateTable` API
call or [AWS CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.md"). Possible values for `TableType` include
`EXTERNAL_TABLE` or `VIRTUAL_VIEW`.

This requirement applies only when you create a table using the AWS Glue
`CreateTable` API operation or the `AWS::Glue::Table`
template. If you create a table for Athena by using a DDL statement or an AWS Glue
crawler, the `TableType` property is defined for
you automatically.

### Function not

registered

This error occurs when you try to use a function that Athena doesn't support. For a
list of functions that Athena supports, see [Functions in Amazon Athena](functions.md "functions.md") or run the `SHOW FUNCTIONS` statement in
the Query Editor. You can also write your own [user defined function (UDF)](querying-udf.md "querying-udf.md"). For more
information, see [How
do I resolve the "function not registered" syntax error in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-syntax-function-not-registered/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-syntax-function-not-registered/") in the
AWS Knowledge Center.

### GENERIC_INTERNAL_ERROR exceptions

`GENERIC_INTERNAL_ERROR` exceptions can have a variety of causes,
including the following:

- GENERIC_INTERNAL_ERROR: Null – You
  might see this exception under either of the following conditions:
  - You have a schema mismatch between the data type of a column in
    table definition and the actual data type of the dataset.
  - You are running a `CREATE TABLE AS SELECT` (CTAS) query
    with inaccurate syntax.

- GENERIC_INTERNAL_ERROR: Parent builder is
  null – You might see this exception when you query a
  table with columns of data type `array`, and you are using the
  OpenCSVSerDe library. The OpenCSVSerde format doesn't support the
  `array` data type.
- GENERIC_INTERNAL_ERROR: Value exceeds
  MAX_INT – You might see this exception when the source
  data column is defined with the data type `INT` and has a numeric
  value greater than 2,147,483,647.
- GENERIC_INTERNAL_ERROR: Value exceeds
  MAX_BYTE – You might see this exception when the source
  data column has a numeric value exceeding the allowable size for the data
  type `BYTE`. The data type `BYTE` is equivalent to
  `TINYINT`. `TINYINT` is an 8-bit signed integer in
  two's complement format with a minimum value of -128 and a maximum value of

127.

- GENERIC_INTERNAL_ERROR: Number of partition values
  does not match number of filters – You might see this
  exception if you have inconsistent partitions on Amazon Simple Storage Service(Amazon S3) data. You
  might have inconsistent partitions under either of the following
  conditions:
  - Partitions on Amazon S3 have changed (example: new partitions were
    added).
  - The number of partition columns in the table do not match those in
    the partition metadata.

For more detailed information about each of these errors, see [How do I
resolve the error "GENERIC_INTERNAL_ERROR" when I query a table in
Amazon Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-generic-internal-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-generic-internal-error/") in the AWS Knowledge Center.

### Number of matching groups doesn't match the number of columns

This error occurs when you use the [Regex SerDe](regex-serde.md "regex-serde.md") in a CREATE TABLE statement and the number of
regex matching groups doesn't match the number of columns that you specified for the
table. For more information, see [How do I resolve the RegexSerDe error "number of matching groups doesn't match
the number of columns" in amazon Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/regexserde-error-athena-matching-groups/ "https://aws.amazon.com/premiumsupport/knowledge-center/regexserde-error-athena-matching-groups/") in the AWS Knowledge
Center.

### queryString failed to satisfy constraint: Member must have length less than or

equal to 262144

The maximum query string length in Athena (262,144 bytes) is not an adjustable
quota. AWS Support can't increase the quota for you, but you can work around the issue
by splitting long queries into smaller ones. For more information, see [How can I
increase the maximum query string length in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-query-string-length/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-query-string-length/") in the AWS
Knowledge Center.

### SYNTAX_ERROR: Column cannot be resolved

This error can occur when you query a table created by an AWS Glue crawler from a
UTF-8 encoded CSV file that has a byte order mark (BOM). AWS Glue doesn't recognize the
BOMs and changes them to question marks, which Amazon Athena doesn't recognize. The
solution is to remove the question mark in Athena or in AWS Glue.

### Too many arguments for

function call

In Athena engine version 3, functions cannot take more than 127 arguments. This limitation is by
design. If you use a function with more than 127 parameters, an error message like
the following occurs:

**`TOO_MANY_ARGUMENTS: line
 `nnn`:`nn`: Too many
 arguments for function call
 `function_name`()`**.

To resolve this issue, use fewer parameters per function call.

## Query timeout

issues

If you experience timeout errors with your Athena queries, check your CloudTrail logs.
Queries can time out due to throttling of AWS Glue or Lake Formation APIs. When these errors occur,
the corresponding error messages can indicate a query timeout issue rather than a
throttling issue. To troubleshoot the issue, you can check your CloudTrail logs before
contacting Support. For more information, see [Query AWS CloudTrail logs](cloudtrail-logs.md "cloudtrail-logs.md") and [Log Amazon Athena API calls with AWS CloudTrail](monitor-with-cloudtrail.md "monitor-with-cloudtrail.md").

For information about query timeout issues with federated queries when you call the
`ListTableMetadata` API, see [Timeout while calling ListTableMetadata](#troubleshooting-athena-federated-queries-list-table-metadata-timeout "#troubleshooting-athena-federated-queries-list-table-metadata-timeout").

## Throttling issues

If your queries exceed the limits of dependent services such as Amazon S3, AWS KMS, AWS Glue, or
AWS Lambda, the following messages can be expected. To resolve these issues, reduce the
number of concurrent calls that originate from the same account.

| Service    | Error message                                                                                   |
| ---------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Glue   | **`AWSGlueException: Rate exceeded.`**                                                          |
| AWS KMS    | **`You have exceeded the rate at which you may call KMS. Reduce the frequency of your calls.`** |
| AWS Lambda | **`Rate exceeded`** **`TooManyRequestsException`**                                              |
| Amazon S3  | **`AmazonS3Exception: Please reduce your request rate.`**                                       | For information about ways to prevent Amazon S3 throttling when you use Athena, see [Prevent Amazon S3 throttling](performance-tuning-s3-throttling.md "performance-tuning-s3-throttling.md"). ## Views ### Views created in Apache Hive shell do not work in Athena Because of their fundamentally different implementations, views created in Apache Hive shell are not compatible with Athena. To resolve this issue, re-create the views in Athena. ### View is stale; it must be re-created You can receive this error if the table that underlies a view has altered or dropped. The resolution is to recreate the view. For more information, see [How can I resolve the "view is stale; it must be re-created" error in Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/athena-view-is-stale-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/athena-view-is-stale-error/") in the AWS Knowledge Center. ## Workgroups For information about troubleshooting workgroup issues, see [Troubleshoot workgroup errors](workgroups-troubleshooting.md "workgroups-troubleshooting.md"). ## Additional resources The following pages provide additional information for troubleshooting issues with Amazon Athena. <br>• [Athena error catalog](error-reference.md "error-reference.md") <br>• [Service Quotas](service-limits.md "service-limits.md") <br>• [Considerations and limitations for SQL queries in Amazon Athena](other-notable-limitations.md "other-notable-limitations.md") <br>• [Unsupported DDL](unsupported-ddl.md "unsupported-ddl.md") <br>• [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md") <br>• [Data types in Amazon Athena](data-types.md "data-types.md") <br>• [Choose a SerDe for your data](supported-serdes.md "supported-serdes.md") <br>• [Use compression in Athena](compression-formats.md "compression-formats.md") <br>• [Escape reserved keywords in queries](reserved-words.md "reserved-words.md") <br>• [Troubleshoot workgroup errors](workgroups-troubleshooting.md "workgroups-troubleshooting.md") The following AWS resources can also be of help: <br>• [Athena topics in the AWS knowledge center](https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Athena "https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Athena") <br>• [Amazon Athena questions on AWS re:Post](https://repost.aws/tags/TA78iVOM7gR62_QqDe2-CmiA/amazon-athena "https://repost.aws/tags/TA78iVOM7gR62_QqDe2-CmiA/amazon-athena") <br>• [Athena posts in the AWS big data blog](https://aws.amazon.com/blogs/big-data/tag/amazon-athena/ "https://aws.amazon.com/blogs/big-data/tag/amazon-athena/") Troubleshooting often requires iterative query and discovery by an expert or from a community of helpers. If you continue to experience issues after trying the suggestions on this page, contact AWS Support (in the AWS Management Console, click **Support**, **Support Center**) or ask a question on [AWS re:Post](https://repost.aws/tags/TA78iVOM7gR62_QqDe2-CmiA/amazon-athena "https://repost.aws/tags/TA78iVOM7gR62_QqDe2-CmiA/amazon-athena") using the **Amazon Athena** tag. |

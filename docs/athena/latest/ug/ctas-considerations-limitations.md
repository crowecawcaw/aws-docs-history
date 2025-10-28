# Considerations and limitations for CTAS

queries

The following sections describe considerations and limitations to keep in mind when you
use `CREATE TABLE AS SELECT` (CTAS) queries in Athena.

## Learn the CTAS query

syntax

The CTAS query syntax differs from the syntax of `CREATE [EXTERNAL] TABLE`
used for creating tables. See [CREATE TABLE AS](create-table-as.md "create-table-as.md").

## The difference

between views and CTAS queries

CTAS queries write new data to a specified location in Amazon S3. Views do not write any
data.

## Specify a

location for your CTAS query results

If your workgroup [overrides the
client-side setting](workgroups-settings-override.md "workgroups-settings-override.md") for query results location, Athena creates your table in
the location
`s3://amzn-s3-demo-bucket/tables/`<query-id>`/`.
To see the query results location specified for the workgroup, [view the workgroup's details](viewing-details-workgroups.md "viewing-details-workgroups.md").

If your workgroup does not override the query results location, you can use the syntax
`WITH (external_location ='s3://amzn-s3-demo-bucket/')` in your CTAS
query to specify where your CTAS query results are stored.

###### Note

The `external_location` property must specify a location that is empty.
A CTAS query checks that the path location (prefix) in the bucket is empty and never
overwrites the data if the location already has data in it. To use the same location
again, delete the data in the key prefix location in the bucket.

If you omit the `external_location` syntax and are not using the workgroup
setting, Athena uses your [client-side setting](query-results-specify-location-console.md "query-results-specify-location-console.md")
for the query results location and creates your table in the location
`s3://amzn-s3-demo-bucket/`<Unsaved-or-query-name>`/`<year>/<month/<date>`/tables/`<query-id>`/`.

## Locate

orphaned files

If a `CTAS` or `INSERT INTO` statement fails, it is possible
that orphaned data files are left in the target data location for failed or cancelled
queries. Because Athena in some cases does not delete data from the target bucket for
your query, the partial data might be included in subsequent queries.

To locate orphaned files for inspection or deletion, you can use the data manifest
file that Athena provides to track the list of files to be written. In some rare cases
where an Athena query abruptly failed, the manifest file might not be present. You can
manually inspect the target S3 location to find the orphaned files. For more
information, see [Identify query output
files](querying-finding-output-files.md#querying-identifying-output-files "querying-finding-output-files.md#querying-identifying-output-files") and [DataManifestLocation](../APIReference/API_QueryExecutionStatistics.md#athena-Type-QueryExecutionStatistics-DataManifestLocation "../APIReference/API_QueryExecutionStatistics.md#athena-Type-QueryExecutionStatistics-DataManifestLocation").

We strongly recommend using Apache Iceberg to achieve atomic transactions of tables.
For more information, see [Query Apache Iceberg tables](querying-iceberg.md "querying-iceberg.md").

## Remember that ORDER

BY clauses are ignored

In a CTAS query, Athena ignores `ORDER BY` clauses in the
`SELECT` portion of the query.

According to the SQL specification (ISO 9075 Part 2), the ordering of the rows of a
table specified by a query expression is guaranteed only for the query expression that
immediately contains the `ORDER BY` clause. Tables in SQL are in any case
inherently unordered, and implementing the `ORDER BY` in sub query clauses
would both cause the query to perform poorly and not result in ordered output. Thus, in
Athena CTAS queries, there is no guarantee that the order specified by the `ORDER
 BY` clause will be preserved when the data is written.

## Choose a

format to store your query results

You can store CTAS results in `PARQUET`, `ORC`,
`AVRO`, `JSON`, and `TEXTFILE`. Multi-character
delimiters are not supported for the CTAS `TEXTFILE` format. If you don't
specify a data storage format, CTAS query results are stored in Parquet by default.

CTAS queries do not require specifying a SerDe to interpret format transformations.
See [Example: Writing query results to a different format](ctas-examples.md#ctas-example-format "ctas-examples.md#ctas-example-format").

## Consider

compression formats

`GZIP` compression is used for CTAS query results in JSON and TEXTFILE
formats. For Parquet, you can use `GZIP` or `SNAPPY`, and the
default is `GZIP`. For ORC, you can use `LZ4`,
`SNAPPY`, `ZLIB`, or `ZSTD`, and the default is
`ZLIB`. For CTAS examples that specify compression, see [Example: Specifying data storage and compression formats](ctas-examples.md#ctas-example-compression "ctas-examples.md#ctas-example-compression"). For more information about compression in
Athena, see [Use compression in Athena](compression-formats.md "compression-formats.md").

## Partition

and bucket your results

You can partition and bucket the results data of a CTAS query. To specify properties
of the destination table, include partitioning and bucketing predicates at the end of
the `WITH` clause. For more information, see [Use partitioning and bucketing](ctas-partitioning-and-bucketing.md "ctas-partitioning-and-bucketing.md") and [Example: Creating bucketed and partitioned tables](ctas-examples.md#ctas-example-bucketed "ctas-examples.md#ctas-example-bucketed").

When you use CTAS to create a partitioned table, Athena has a write limit of 100
partitions. For information about working around the 100-partition limitation, see [Use CTAS and INSERT INTO to work around the 100 partition
limit](ctas-insert-into.md "ctas-insert-into.md").

## Encrypt your

results

You can encrypt CTAS query results in Amazon S3, similar to the way you encrypt other query
results in Athena. For more information, see [Encrypt Athena query results
stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md").

## The expected

bucket owner setting does not apply to CTAS

For CTAS statements, the expected bucket owner setting does not apply to the
destination table location in Amazon S3. The expected bucket owner setting applies only to the Amazon S3
output location that you specify for Athena query results. For more information, see [Specify a query result
location using the Athena console](query-results-specify-location-console.md "query-results-specify-location-console.md").

## Column data types are

preserved

Column data types for a CTAS query are the same as specified for the original
query.

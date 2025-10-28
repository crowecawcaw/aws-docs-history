# CREATE TABLE AS

Creates a new table populated with the results of a [SELECT](select.md "select.md") query. To create an empty table, use [CREATE TABLE](create-table.md "create-table.md"). `CREATE TABLE AS`
combines a `CREATE TABLE` DDL statement with a `SELECT` DML statement
and therefore technically contains both DDL and DML. Note that although `CREATE TABLE
 AS` is grouped here with other DDL statements, CTAS queries in Athena are treated
as DML for Service Quotas purposes. For information about Service Quotas in Athena, see [Service Quotas](service-limits.md "service-limits.md").

###### Note

For CTAS statements, the expected bucket owner setting does not apply to the
destination table location in Amazon S3. The expected bucket owner setting applies only to the Amazon S3
output location that you specify for Athena query results. For more information, see [Specify a query result
location using the Athena console](query-results-specify-location-console.md "query-results-specify-location-console.md").

For additional information about `CREATE TABLE AS` that is beyond the scope of
this reference topic, see [Create a table from query results (CTAS)](ctas.md "ctas.md").

###### Topics

- [Synopsis](#synopsis "#synopsis")
- [CTAS table properties](#ctas-table-properties "#ctas-table-properties")
- [Examples](#ctas-table-examples "#ctas-table-examples")

## Synopsis

```
CREATE TABLE table_name
[ WITH ( property_name = expression [, ...] ) ]
AS query
[ WITH [ NO ] DATA ]
```

Where:

**WITH ( property_name = expression [, ...] )**

A list of optional CTAS table properties, some of which are specific to
the data storage format. See [CTAS table properties](#ctas-table-properties "#ctas-table-properties").

**query**

A [SELECT](select.md "select.md") query that is used to
create a new table.

###### Important

If you plan to create a query with partitions, specify the names of
partitioned columns last in the list of columns in the
`SELECT` statement.

**[ WITH [ NO ] DATA ]**

If `WITH NO DATA` is used, a new empty table with the same
schema as the original table is created.

###### Note

To include column headers in your query result output, you can use a simple
`SELECT` query instead of a CTAS query. You can retrieve the results
from your query results location or download the results directly using the Athena
console. For more information, see [Work with query results and recent queries](querying.md "querying.md").

## CTAS table properties

Each CTAS table in Athena has a list of optional CTAS table properties that you specify
using `WITH (property_name = expression [, ...] )`. For information about
using these parameters, see [Examples of CTAS queries](ctas-examples.md "ctas-examples.md").

**`WITH (property_name = expression [, ...], )`**

`table_type = ['HIVE', 'ICEBERG']`

Optional. The default is `HIVE`. Specifies the
table type of the resulting table

Example:

```
WITH (table_type ='ICEBERG')
```

`external_location = [location]`

###### Note

Because Iceberg tables are not external, this property
does not apply to Iceberg tables. To define the root
location of an Iceberg table in a CTAS statement, use the
`location` property described later in this
section.

Optional. The location where Athena saves your CTAS query in
Amazon S3.

Example:

```
 WITH (external_location ='s3://amzn-s3-demo-bucket/tables/parquet_table/')
```

Athena does not use the same path for query results twice. If
you specify the location manually, make sure that the Amazon S3
location that you specify has no data. Athena never attempts to
delete your data. If you want to use the same location again,
manually delete the data, or your CTAS query will fail.

If you run a CTAS query that specifies an
`external_location` in a workgroup that [enforces a query
results location](workgroups-settings-override.md "workgroups-settings-override.md"), the query fails with an error
message. To see the query results location specified for the
workgroup, [see the
workgroup's details](viewing-details-workgroups.md "viewing-details-workgroups.md").

If your workgroup overrides the client-side setting for query
results location, Athena creates your table in the following
location:

```
s3://amzn-s3-demo-bucket/tables/`query-id`/
```

If you do not use the `external_location` property
to specify a location and your workgroup does not override
client-side settings, Athena uses your [client-side setting](query-results-specify-location-console.md "query-results-specify-location-console.md") for the query results location
to create your table in the following location:

```
s3://amzn-s3-demo-bucket/`Unsaved-or-query-name`/`year`/`month`/`date`/tables/`query-id`/
```

`is_external = [boolean]`

Optional. Indicates if the table is an external table. The
default is true. For Iceberg tables, this must be set to
false.

Example:

```
WITH (is_external = false)
```

`location = [location]`

Required for Iceberg tables. Specifies the root location for
the Iceberg table to be created from the query results.

Example:

```
WITH (location ='s3://amzn-s3-demo-bucket/tables/`iceberg_table`/')
```

`field_delimiter = [delimiter]`

Optional and specific to text-based data storage formats. The
single-character field delimiter for files in CSV, TSV, and text
files. For example, `WITH (field_delimiter = ',')`.
Currently, multicharacter field delimiters are not supported for
CTAS queries. If you don't specify a field delimiter,
`\001` is used by default.

`format = [storage_format]`

The storage format for the CTAS query results, such as
`ORC`, `PARQUET`, `AVRO`,
`JSON`, `ION`, or
`TEXTFILE`. For Iceberg tables, the allowed
formats are `ORC`, `PARQUET`, and
`AVRO`. If omitted, `PARQUET` is used
by default. The name of this parameter, `format`,
must be listed in lowercase, or your CTAS query will fail.

Example:

```
WITH (format = 'PARQUET')
```

`bucketed_by = ARRAY[ column_name[,…], bucket_count = [int]
 ]`

###### Note

This property does not apply to Iceberg tables. For
Iceberg tables, use partitioning with bucket
transform.

An array list of buckets to bucket data. If omitted, Athena
does not bucket your data in this query.

`bucket_count = [int]`

###### Note

This property does not apply to Iceberg tables. For
Iceberg tables, use partitioning with bucket
transform.

The number of buckets for bucketing your data. If omitted,
Athena does not bucket your data. Example:

```
CREATE TABLE bucketed_table WITH (
  bucketed_by = ARRAY[`column_name`],
  bucket_count = 30, format = 'PARQUET',
  external_location ='s3://amzn-s3-demo-bucket/tables/parquet_table/'
) AS
SELECT
  *
FROM
  `table_name`
```

`partitioned_by = ARRAY[ col_name[,…] ]`

###### Note

This property does not apply to Iceberg tables. To use
partition transforms for Iceberg tables, use the
`partitioning` property described later in
this section.

Optional. An array list of columns by which the CTAS table
will be partitioned. Verify that the names of partitioned
columns are listed last in the list of columns in the
`SELECT` statement.

`partitioning = ARRAY[partition_transform, ...]`

Optional. Specifies the partitioning of the Iceberg table to
be created. Iceberg supports a wide variety of partition
transforms and partition evolution. Partition transforms are
summarized in the following table.

| Transform             | Description                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `year(ts)`            | Creates a partition for each year. The partition value is the integer difference in years between `ts` and January 1, 1970.                                |
| `month(ts)`           | Creates a partition for each month of each year. The partition value is the integer difference in months between `ts` and January 1, 1970.                 |
| `day(ts)`             | Creates a partition for each day of each year. The partition value is the integer difference in days between `ts` and January 1, 1970.                     |
| `hour(ts)`            | Creates a partition for each hour of each day. The partition value is a timestamp with the minutes and seconds set to zero.                                |
| `bucket(x, nbuckets)` | Hashes the data into the specified number of buckets. The partition value is an integer hash of `x`, with a value between 0 and `nbuckets - 1`, inclusive. |
| `truncate(s, nchars)` | Makes the partition value the first `nchars` characters of `s`.                                                                                            | Example: `WITH (partitioning = ARRAY['month(order_date)', 'bucket(account_number, 10)', 'country']))` `optimize_rewrite_min_data_file_size_bytes = [long]` Optional. Data optimization specific configuration. Files smaller than the specified value are included for optimization. The default is 0.75 times the value of `write_target_data_file_size_bytes`. This property applies only to Iceberg tables. For more information, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md"). Example: `WITH (optimize_rewrite_min_data_file_size_bytes = 402653184)` `optimize_rewrite_max_data_file_size_bytes = [long]` Optional. Data optimization specific configuration. Files larger than the specified value are included for optimization. The default is 1.8 times the value of `write_target_data_file_size_bytes`. This property applies only to Iceberg tables. For more information, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md"). Example: `WITH (optimize_rewrite_max_data_file_size_bytes = 966367641)` `optimize_rewrite_data_file_threshold = [int]` Optional. Data optimization specific configuration. If there are fewer data files that require optimization than the given threshold, the files are not rewritten. This allows the accumulation of more data files to produce files closer to the target size and skip unnecessary computation for cost savings. The default is 5. This property applies only to Iceberg tables. For more information, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md"). Example: `WITH (optimize_rewrite_data_file_threshold = 5)` `optimize_rewrite_delete_file_threshold = [int]` Optional. Data optimization specific configuration. If there are fewer delete files associated with a data file than the threshold, the data file is not rewritten. This allows the accumulation of more delete files for each data file for cost savings. The default is 2. This property applies only to Iceberg tables. For more information, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md"). Example: `WITH (optimize_rewrite_delete_file_threshold = 2)` `vacuum_min_snapshots_to_keep = [int]` Optional. Vacuum specific configuration. The minimum number of most recent snapshots to retain. The default is 1. This property applies only to Iceberg tables. For more information, see [VACUUM](vacuum-statement.md "vacuum-statement.md"). ###### Note The `vacuum_min_snapshots_to_keep` property requires Athena engine version 3. Example: `WITH (vacuum_min_snapshots_to_keep = 1)` `vacuum_max_snapshot_age_seconds = [long]` Optional. Vacuum specific configuration. A period in seconds that represents the age of the snapshots to retain. The default is 432000 (5 days). This property applies only to Iceberg tables. For more information, see [VACUUM](vacuum-statement.md "vacuum-statement.md"). ###### Note The `vacuum_max_snapshot_age_seconds` property requires Athena engine version 3. Example: `WITH (vacuum_max_snapshot_age_seconds = 432000)` `write_compression = [compression_format]` The compression type to use for any storage format that allows compression to be specified. The `compression_format` value specifies the compression to be used when the data is written to the table. You can specify compression for the `TEXTFILE`, `JSON`, `PARQUET`, and `ORC` file formats. For example, if the `format` property specifies `PARQUET` as the storage format, the value for `write_compression` specifies the compression format for Parquet. In this case, specifying a value for `write_compression` is equivalent to specifying a value for `parquet_compression`. Similarly, if the `format` property specifies `ORC` as the storage format, the value for `write_compression` specifies the compression format for ORC. In this case, specifying a value for `write_compression` is equivalent to specifying a value for `orc_compression`. Multiple compression format table properties cannot be specified in the same CTAS query. For example, you cannot specify both `write_compression` and `parquet_compression` in the same query. The same applies for `write_compression` and `orc_compression`. For information about the compression types that are supported for each file format, see [Use compression in Athena](compression-formats.md "compression-formats.md"). `orc_compression = [compression_format]` The compression type to use for the `ORC` file format when `ORC` data is written to the table. For example, `WITH (orc_compression = 'ZLIB')`. Chunks within the `ORC` file (except the `ORC` Postscript) are compressed using the compression that you specify. If omitted, ZLIB compression is used by default for `ORC`. ###### Note For consistency, we recommend that you use the `write_compression` property instead of `orc_compression`. Use the `format` property to specify the storage format as `ORC`, and then use the `write_compression` property to specify the compression format that `ORC` will use. `parquet_compression = [compression_format]` The compression type to use for the Parquet file format when Parquet data is written to the table. For example, `WITH (parquet_compression = 'SNAPPY')`. This compression is applied to column chunks within the Parquet files. If omitted, GZIP compression is used by default for Parquet. ###### Note For consistency, we recommend that you use the `write_compression` property instead of `parquet_compression`. Use the `format` property to specify the storage format as `PARQUET`, and then use the `write_compression` property to specify the compression format that `PARQUET` will use. `compression_level = [compression_level]` The compression level to use. This property applies only to ZSTD compression. Possible values are from 1 to 22. The default value is 3. For more information, see [Use ZSTD compression levels](compression-support-zstd-levels.md "compression-support-zstd-levels.md"). ## Examples For examples of CTAS queries, consult the following resources. <br>• [Examples of CTAS queries](ctas-examples.md "ctas-examples.md") <br>• [Use CTAS and INSERT INTO for ETL and data analysis](ctas-insert-into-etl.md "ctas-insert-into-etl.md") <br>• [Use CTAS statements with Amazon Athena to reduce cost and improve performance](https://aws.amazon.com/blogs/big-data/using-ctas-statements-with-amazon-athena-to-reduce-cost-and-improve-performance/ "https://aws.amazon.com/blogs/big-data/using-ctas-statements-with-amazon-athena-to-reduce-cost-and-improve-performance/") <br>• [Use CTAS and INSERT INTO to work around the 100 partition limit](ctas-insert-into.md "ctas-insert-into.md") |

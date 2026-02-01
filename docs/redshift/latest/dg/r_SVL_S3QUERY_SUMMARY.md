Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_S3QUERY_SUMMARY

Use the SVL_S3QUERY_SUMMARY view to get a summary of all Amazon Redshift Spectrum queries (S3
queries) that have been run on the system. SVL_S3QUERY_SUMMARY aggregates detail from
SVL_S3QUERY at the segment level.

SVL_S3QUERY_SUMMARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

For SVCS_S3QUERY_SUMMARY, see [SVCS_S3QUERY_SUMMARY](r_SVCS_S3QUERY_SUMMARY.md "r_SVCS_S3QUERY_SUMMARY.md").

## Table columns

| Column name             | Data type        | Description                                                                                                                                                                                                                                                                                 |
| ----------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                  | integer          | The ID of the user that generated the given<br>entry.                                                                                                                                                                                                                                       |
| query                   | integer          | The query ID. You can use this value to join<br>various other system tables and views.                                                                                                                                                                                                      |
| xid                     | bigint           | The transaction ID.                                                                                                                                                                                                                                                                         |
| pid                     | integer          | The process ID.                                                                                                                                                                                                                                                                             |
| segment                 | integer          | The segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps.                                                                                                                                                                               |
| step                    | integer          | The query step that ran.                                                                                                                                                                                                                                                                    |
| starttime               | timestamp        | Time in UTC that the query started<br>executing.                                                                                                                                                                                                                                            |
| endtime                 | timestamp        | Time in UTC that the query completed.                                                                                                                                                                                                                                                       |
| elapsed                 | integer          | The length of time that it took the query to<br>run (in microseconds).                                                                                                                                                                                                                      |
| aborted                 | integer          | If a query was stopped by the system or canceled<br>by the user, this column contains `1`. If the<br>query ran to completion, this column contains<br>`0`.                                                                                                                                  |
| external_table_name     | char(136)        | The internal format of name of the external name<br>of the table for the external table scan.                                                                                                                                                                                               |
| file_format             | character(16)    | The file format of the external table data.                                                                                                                                                                                                                                                 |
| is_partitioned          | char(1)          | If true (`t`), this column<br>value indicates that the external table is partitioned.                                                                                                                                                                                                       |
| is_rrscan               | char(1)          | If true (`t`), this column<br>value indicates that a range-restricted scan was applied.                                                                                                                                                                                                     |
| is_nested               | char(1)          | If true (`t`), this column<br>value indicates that the nested column data type is accessed.                                                                                                                                                                                                 |
| s3_scanned_rows         | bigint           | The number of rows scanned from Amazon S3 and sent to<br>the Redshift Spectrum layer.                                                                                                                                                                                                       |
| s3_scanned_bytes        | bigint           | The number of bytes scanned from Amazon S3 and sent to<br>the Redshift Spectrum layer, based on compressed data.                                                                                                                                                                            |
| s3query_returned_rows   | bigint           | The number of rows returned from the Redshift<br>Spectrum layer to the cluster.                                                                                                                                                                                                             |
| s3query_returned_bytes  | bigint           | The number of bytes returned from the Redshift<br>Spectrum layer to the cluster. A large amount of data returned to<br>Amazon Redshift might affect system performance.                                                                                                                     |
| files                   | integer          | The number of files that were processed for this<br>Redshift Spectrum query. A small number of files limits the benefits<br>of parallel processing.                                                                                                                                         |
| files_max               | integer          | The maximum number of files processed on one<br>slice.                                                                                                                                                                                                                                      |
| files_avg               | integer          | The average number of files processed on one<br>slice.                                                                                                                                                                                                                                      |
| splits                  | int              | The number of splits processed for this segment.<br>The number of splits processed on this slice. With large splitable<br>data files, for example, data files larger than about 512 MB,<br>Redshift Spectrum tries to split the files into multiple S3 requests<br>for parallel processing. |
| splits_max              | int              | The maximum number of splits processed on this<br>slice.                                                                                                                                                                                                                                    |
| splits_avg              | int              | The average number of splits processed on this<br>slice.                                                                                                                                                                                                                                    |
| total_split_size        | bigint           | The total size of all splits processed.                                                                                                                                                                                                                                                     |
| max_split_size          | bigint           | The maximum split size processed, in<br>bytes.                                                                                                                                                                                                                                              |
| avg_split_size          | bigint           | The average split size processed, in<br>bytes.                                                                                                                                                                                                                                              |
| total_retries           | integer          | The total number of retries for one individual<br>processed file.                                                                                                                                                                                                                           |
| max_retries             | integer          | The maximum number of retries for any of<br>processed files.                                                                                                                                                                                                                                |
| max_request_duration    | integer          | The maximum duration of an individual file<br>request (in microseconds). Long running queries might indicate a<br>bottleneck.                                                                                                                                                               |
| avg_request_duration    | double precision | The average duration of the file requests (in<br>microseconds).                                                                                                                                                                                                                             |
| max_request_parallelism | integer          | The maximum number of parallel requests at one<br>slice for this Redshift Spectrum query.                                                                                                                                                                                                   |
| avg_request_parallelism | double precision | The average number of parallel requests at one slice for this Redshift Spectrum query.                                                                                                                                                                                                      |
| total_slowdown_count    | bigint           | The total number of Amazon S3 requests with a slow down error that occurred during the external table scan.                                                                                                                                                                                 |
| max_slowdown_count      | integer          | The maximum number of Amazon S3 requests with a slow down error that occurred during the external table scan on one slice.                                                                                                                                                                  |

## Sample query

The following example gets the scan step details for the last query
completed.

```
select query, segment, elapsed, s3_scanned_rows, s3_scanned_bytes, s3query_returned_rows, s3query_returned_bytes, files
from svl_s3query_summary
where query = pg_last_query_id()
order by query,segment;
```

```
query | segment | elapsed | s3_scanned_rows | s3_scanned_bytes | s3query_returned_rows | s3query_returned_bytes | files
------+---------+---------+-----------------+------------------+-----------------------+------------------------+------
 4587 |       2 |   67811 |               0 |                0 |                     0 |                      0 |     0
 4587 |       2 |  591568 |          172462 |         11260097 |                  8513 |                 170260 |     1
 4587 |       2 |  216849 |               0 |                0 |                     0 |                      0 |     0
 4587 |       2 |  216671 |               0 |                0 |                     0 |                      0 |     0
```



 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_S3QUERY\_SUMMARY
<a name="r_SVL_S3QUERY_SUMMARY"></a>

Use the SVL\_S3QUERY\_SUMMARY view to get a summary of all data lake queries that have been run on the system. SVL\_S3QUERY\_SUMMARY aggregates detail from SVL\_S3QUERY at the segment level.

SVL\_S3QUERY\_SUMMARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

For SVCS\_S3QUERY\_SUMMARY, see [SVCS\_S3QUERY\_SUMMARY](r_SVCS_S3QUERY_SUMMARY.md).

## Table columns
<a name="r_SVL_S3QUERY_SUMMARY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of the user that generated the given entry. | 
| query | integer | The query ID. You can use this value to join various other system tables and views.  | 
| xid | bigint | The transaction ID. | 
| pid | integer | The process ID. | 
| segment | integer | The segment number. A query consists of multiple segments, and each segment consists of one or more steps.  | 
| step | integer | The query step that ran.  | 
| starttime | timestamp | Time in UTC that the query started executing. | 
| endtime | timestamp | Time in UTC that the query completed. | 
| elapsed | integer | The length of time that it took the query to run (in microseconds). | 
| aborted | integer | If a query was stopped by the system or canceled by the user, this column contains 1. If the query ran to completion, this column contains 0. | 
| external\_table\_name | char(136) | The internal format of name of the external name of the table for the external table scan. | 
| file\_format | character(16) | The file format of the external table data. | 
| is\_partitioned | char(1) | If true (t), this column value indicates that the external table is partitioned. | 
| is\_rrscan | char(1) | If true (t), this column value indicates that a range-restricted scan was applied. | 
| is\_nested | char(1) | If true (t), this column value indicates that the nested column data type is accessed. | 
| s3\_scanned\_rows | bigint | The number of rows scanned from Amazon S3 and sent to the Redshift Spectrum layer. On RG provisioned clusters, this is the total number of rows scanned directly from Amazon S3 by the cluster's native reader across all slices, before filter pushdown. | 
| s3\_scanned\_bytes | bigint | The number of bytes scanned from Amazon S3 and sent to the Redshift Spectrum layer, based on compressed data. On RG provisioned clusters, this is the total number of bytes scanned directly from Amazon S3 by the cluster's native reader across all slices, before filter pushdown. | 
| s3query\_returned\_rows | bigint | The number of rows returned from the Redshift Spectrum layer to the cluster. On RG provisioned clusters, this is the total number of rows returned by the cluster's native reader across all slices, after filter pushdown. | 
| s3query\_returned\_bytes | bigint | The number of bytes returned from the Redshift Spectrum layer to the cluster. A large amount of data returned to Amazon Redshift might affect system performance. On RG provisioned clusters, this is the total number of bytes returned by the cluster's native reader across all slices, after filter pushdown. | 
| files | integer | The number of files that were processed for this data lake query. A small number of files limits the benefits of parallel processing.  | 
| files\_max | integer | The maximum number of files processed on one slice. | 
| files\_avg | integer | The average number of files processed on one slice. | 
| splits | int | The number of splits processed for this segment. The number of splits processed on this slice. With large splitable data files, for example, data files larger than about 512 MB, Redshift Spectrum tries to split the files into multiple S3 requests for parallel processing. | 
| splits\_max | int | The maximum number of splits processed on this slice.  | 
| splits\_avg | int | The average number of splits processed on this slice. | 
| total\_split\_size | bigint | The total size of all splits processed. | 
| max\_split\_size | bigint | The maximum split size processed, in bytes. | 
| avg\_split\_size | bigint | The average split size processed, in bytes. | 
| total\_retries | integer | The total number of retries for one individual processed file. On RG node type clusters, this column is deprecated and contains -1. For Amazon S3 client retries on RG, see STL\_S3CLIENT. | 
| max\_retries | integer | The maximum number of retries for any of processed files. On RG node type clusters, this column is deprecated and contains -1. For Amazon S3 client retries on RG, see STL\_S3CLIENT. | 
| max\_request\_duration | integer | The maximum duration of an individual file request (in microseconds). Long running queries might indicate a bottleneck. On RG node type clusters, this column is deprecated and contains -1. | 
| avg\_request\_duration | double precision | The average duration of the file requests (in microseconds). On RG node type clusters, this column is deprecated and contains -1. | 
| max\_request\_parallelism | integer | The maximum number of parallel requests at one slice for this Redshift Spectrum query. On RG node type clusters, this column is deprecated and contains -1. | 
| avg\_request\_parallelism | double precision | The average number of parallel requests at one slice for this Redshift Spectrum query. On RG node type clusters, this column is deprecated and contains -1.  | 
| total\_slowdown\_count | bigint | The total number of Amazon S3 requests with a slow down error that occurred during the external table scan. On RG node type clusters, this column is deprecated and contains -1. | 
| max\_slowdown\_count | integer | The maximum number of Amazon S3 requests with a slow down error that occurred during the external table scan on one slice. On RG node type clusters, this column is deprecated and contains -1. | 

## Sample query
<a name="r_SVL_S3QUERY_SUMMARY-sample-query"></a>

The following example gets the scan step details for the last query completed.

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
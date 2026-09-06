

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_S3QUERY
<a name="r_SVL_S3QUERY"></a>

Use the SVL\_S3QUERY view to get details about data lake queries at the segment and node slice level.

SVL\_S3QUERY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
SVL\_S3QUERY only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_SVL_S3QUERY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of user who generated a given entry. | 
| query | integer | The query ID. | 
| segment | integer | A segment number. A query consists of multiple segments, and each segment consists of one or more steps. | 
| step | integer | The query step that ran.  | 
| node | integer | The node number. | 
| slice | integer | The data slice that a particular segment ran against. | 
| starttime | timestamp | Time in UTC that the query started executing. | 
| endtime | timestamp | Time in UTC that the query execution completed | 
| elapsed | integer | Elapsed time (in microseconds). | 
| external\_table\_name | char(136) | Internal format of external table name for the s3 scan step. | 
| is\_partitioned | char(1) | If true (t), this column value indicates that the external table is partitioned. | 
| is\_rrscan | char(1) | If true (t), this column value indicates that a range-restricted scan was applied. | 
| s3\_scanned\_rows | bigint | The number of rows scanned from Amazon S3 and sent to the Redshift Spectrum layer. On RG provisioned clusters, this is the number of rows read directly from Amazon S3 by the cluster's native reader, before filter pushdown. | 
| s3\_scanned\_bytes | bigint | The number of bytes scanned from Amazon S3 and sent to the Redshift Spectrum layer. On RG provisioned clusters, this is the total scan-range size in bytes processed by the cluster's native reader. | 
| s3query\_returned\_rows | bigint | The number of rows returned from the Redshift Spectrum layer to the cluster. On RG provisioned clusters, this is the number of rows produced by the external table scan after filter pushdown. | 
| s3query\_returned\_bytes | bigint | The number of bytes returned from the Redshift Spectrum layer to the cluster. On RG provisioned clusters, this is the number of bytes produced by the external table scan after filter pushdown. | 
| files | integer | The number of files that were processed for this S3 scan step on this slice. | 
| splits | int | The number of splits processed on this slice. With large splitable data files, for example, data files larger than about 512 MB, Redshift Spectrum tries to split the files into multiple S3 requests for parallel processing. On RG provisioned clusters, this is the number of scan ranges consumed by the cluster's native reader. | 
| total\_split\_size | bigint | The total size of all splits processed on this slice, in bytes. On RG provisioned clusters, this is the total size of all scan ranges consumed, in bytes. | 
| max\_split\_size | bigint | The maximum split size processed for this slice, in bytes. On RG provisioned clusters, this is the size of the largest scan range consumed, in bytes. | 
| total\_retries | integer | The total number of retries for the processed files. On RG node type clusters, this column is deprecated and contains -1. For Amazon S3 client retries on RG, see STL\_S3CLIENT. | 
| max\_retries | integer | The maximum number of retries for an individual processed file. On RG node type clusters, this column is deprecated and contains -1. For Amazon S3 client retries on RG, see STL\_S3CLIENT. | 
| max\_request\_duration | integer | The maximum duration of an individual Redshift Spectrum request (in microseconds). On RG node type clusters, this column is deprecated and contains -1. | 
| avg\_request\_duration | double precision | The average duration of the Redshift Spectrum requests (in microseconds). On RG node type clusters, this column is deprecated and contains -1. | 
| max\_request\_parallelism | integer | The maximum number of outstanding Redshift Spectrum on this slice for this S3 scan step. On RG node type clusters, this column is deprecated and contains -1. | 
| avg\_request\_parallelism | double precision | The average number of parallel Redshift Spectrum requests on this slice for this S3 scan step. On RG node type clusters, this column is deprecated and contains -1. | 

## Sample query
<a name="r_SVL_S3QUERY-sample-query"></a>

The following example gets the scan step details for the last query completed.

```
select query, segment, slice, elapsed, s3_scanned_rows, s3_scanned_bytes, s3query_returned_rows, s3query_returned_bytes, files 
from svl_s3query 
where query = pg_last_query_id() 
order by query,segment,slice;
```

```
query | segment | slice | elapsed | s3_scanned_rows | s3_scanned_bytes | s3query_returned_rows | s3query_returned_bytes | files
------+---------+-------+---------+-----------------+------------------+-----------------------+------------------------+------
 4587 |       2 |     0 |   67811 |               0 |                0 |                     0 |                      0 |     0
 4587 |       2 |     1 |  591568 |          172462 |         11260097 |                  8513 |                 170260 |     1
 4587 |       2 |     2 |  216849 |               0 |                0 |                     0 |                      0 |     0
 4587 |       2 |     3 |  216671 |               0 |                0 |                     0 |                      0 |     0
```
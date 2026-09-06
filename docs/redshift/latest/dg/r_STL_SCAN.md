

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_SCAN
<a name="r_STL_SCAN"></a>

Analyzes table scan steps for queries. The step number for rows in this table is always 0 because a scan is the first step in a segment.

STL\_SCAN is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
STL\_SCAN only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_STL_SCAN-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| query | integer | Query ID. The query column can be used to join other system tables and views. | 
| slice | integer | Number that identifies the slice where the query was running. | 
| segment | integer | Number that identifies the query segment. | 
| step | integer | Query step that ran. | 
| starttime | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: 2009-06-12 11:29:19.131358. | 
| endtime | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: 2009-06-12 11:29:19.131358. | 
| tasknum | integer | Number of the query task process that was assigned to run the step. | 
| rows | bigint | Total number of rows that were processed. | 
| bytes | bigint | Size, in bytes, of all the output rows for the step. | 
| fetches | bigint | This information is for internal use only. | 
| type | integer | ID of the scan type. For a list of valid values, see the following table. | 
| tbl | integer | Table ID. | 
| is\_rrscan | character(1) | If true (t), indicates that range-restricted scan was used on the step. | 
| is\_delayed\_scan | character(1) | This information is for internal use only. | 
| rows\_pre\_filter | bigint | For scans of permanent tables, the total number of rows emitted before filtering rows marked for deletion (ghost rows) and before applying user-defined query filters. | 
| rows\_pre\_user\_filter | bigint | For scans of permanent tables, the number of rows processed after filtering rows marked for deletion (ghost rows) but before applying user-defined query filters. | 
| perm\_table\_name | character(136) | For scans of permanent tables, the name of the table scanned. | 
| is\_rlf\_scan | character(1) | If true (t), indicates that row-level filtering was used on the step. | 
| is\_rlf\_scan\_reason | integer | This information is for internal use only. | 
| num\_em\_blocks | integer | This information is for internal use only. | 
| checksum | bigint | This information is for internal use only. | 
| runtime\_filtering | character(1) | If true (t), indicates that runtime filters are applied. | 
| scan\_region | integer | This information is for internal use only. | 
| num\_sortkey\_as\_predicate | integer | This information is for internal use only. | 
| row\_fetcher\_state | integer | This information is for internal use only. | 
| consumed\_scan\_ranges | bigint | This information is for internal use only. | 
| work\_stealing\_reason | bigint | This information is for internal use only. | 
| is\_vectorized\_scan | character(1) | This information is for internal use only. | 
|  is\_vectorized\_scan\_reason | integer | This information is for internal use only. | 
| row\_fetcher\_reason | bigint | This information is for internal use only. | 
| topology\_signature | bigint | This information is for internal use only. | 
| use\_tpm\_partition | character(1) | This information is for internal use only. | 
| is\_rrscan\_expr | character(1) | This information is for internal use only. | 
| scanned\_mega\_value | character(1) | This information is for internal use only. This information shows whether the given scan step has scanned a large value. A large value will be stored in multiple blocks. Block size is 1 MB by default, a large value is greater than 1 MB in a default setting. | 

## Scan types
<a name="r_STL_SCAN-scan-types"></a>


| Type ID | Description | 
| --- | --- | 
| 1 | Data from the network. | 
| 2 | Permanent user tables in compressed shared memory. | 
| 3 | Transient row-wise tables. | 
| 21 | Load files from Amazon S3. | 
| 22 | Load tables from Amazon DynamoDB. | 
| 23 | Load data from a remote SSH connection. | 
| 24 | Load data from remote cluster (sorted region). This is used for resizing. | 
| 25 | Load data from remote cluster(unsorted region). This is used for resizing. | 
| 28 | Read data from a time series view with UNION ALL on multiple tables. | 
| 29 |  Read data from Amazon S3 external tables. | 
| 30 | Read partition information of an Amazon S3 external table. | 
| 33 | Read data from a remote Postgres table. | 
| 36 | Read data from a remote MySQL table. | 
| 37 | Read data from a remote Kinesis stream. | 

## Usage notes
<a name="w2aac59c29b9d101c15"></a>

Ideally `rows` should be relatively close to `rows_pre_filter`. A large difference between `rows` and `rows_pre_filter` is an indication that the execution engine is scanning rows that are later discarded, which is inefficient. The difference between `rows_pre_filter` and `rows_pre_user_filter` is the number of ghost rows in the scan. Run a VACUUM to remove rows marked for deletion. The difference between `rows` and `rows_pre_user_filter` is the number of rows filtered by the query. If a lot of rows are discarded by the user filter, review your choice of sort column or, if this is due to a large unsorted region, run a vacuum.

## Sample queries
<a name="r_STL_SCAN-sample-queries"></a>

The following example shows that `rows_pre_filter` is larger than `rows_pre_user_filter` because the table has deleted rows that have not been vacuumed (ghost rows). 

```
SELECT query, slice, segment,step,rows, rows_pre_filter, rows_pre_user_filter 
from stl_scan where query = pg_last_query_id();

 query |  slice | segment | step | rows  | rows_pre_filter | rows_pre_user_filter
-------+--------+---------+------+-------+-----------------+----------------------
 42915 |      0 |       0 |    0 | 43159 |           86318 |                43159
 42915 |      0 |       1 |    0 |     1 |               0 |                    0
 42915 |      1 |       0 |    0 | 43091 |           86182 |                43091
 42915 |      1 |       1 |    0 |     1 |               0 |                    0
 42915 |      2 |       0 |    0 | 42778 |           85556 |                42778
 42915 |      2 |       1 |    0 |     1 |               0 |                    0
 42915 |      3 |       0 |    0 | 43428 |           86856 |                43428
 42915 |      3 |       1 |    0 |     1 |               0 |                    0
 42915 |  10000 |       2 |    0 |     4 |               0 |                    0
(9 rows)
```
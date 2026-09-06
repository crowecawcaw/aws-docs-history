

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_S3PARTITION
<a name="r_SVL_S3PARTITION"></a>

Use the SVL\_S3PARTITION view to get details about data lake partitions at the segment and node slice level.

SVL\_S3PARTITION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
SVL\_S3PARTITION only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_SVL_S3PARTITION-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| query | integer | The query ID. | 
| segment | integer | A segment number. A query consists of multiple segments, and each segment consists of one or more steps. | 
| node | integer | The node number. | 
| slice | integer | The data slice that a particular segment ran against. | 
| starttime | timestamp without time zone | Time in UTC that the partition pruning started executing. | 
| endtime | timestamp without time zone | Time in UTC that the partition pruning completed. | 
| duration | bigint | Elapsed time (in microseconds). | 
| total\_partitions | integer | Number of total partitions. | 
| qualified\_partitions | integer | Number of qualified partitions. | 
| assigned\_partitions | integer | Number of assigned partitions on the slice. | 
| assignment | character | Type of assignment. | 

## Sample query
<a name="r_SVL_S3PARTITION-sample-query"></a>

The following example gets the partition details for the last query completed.

```
SELECT query, segment,
       MIN(starttime) AS starttime,
       MAX(endtime) AS endtime,
       datediff(ms,MIN(starttime),MAX(endtime)) AS dur_ms,
       MAX(total_partitions) AS total_partitions,
       MAX(qualified_partitions) AS qualified_partitions,
       MAX(assignment) as assignment_type
FROM svl_s3partition
WHERE query=pg_last_query_id()
GROUP BY query, segment
```

```
query | segment |           starttime           |           endtime           | dur_ms| total_partitions | qualified_partitions | assignment_type
------+---------+-------------------------------+-----------------------------+-------+------------------+----------------------+----------------
99232 |       0 | 2018-04-17 22:43:50.201515    | 2018-04-17 22:43:54.674595  |  4473 |       2526       |        334           | p
```
Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_S3PARTITION

Use the SVL_S3PARTITION view to get details about Amazon Redshift Spectrum partitions at the
segment and node slice level.

SVL_S3PARTITION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

SVL_S3PARTITION only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name          | Data type                   | Description                                                                                                 |
| -------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| query                | integer                     | The query ID.                                                                                               |
| segment              | integer                     | A segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps. |
| node                 | integer                     | The node number.                                                                                            |
| slice                | integer                     | The data slice that a particular segment ran<br>against.                                                    |
| starttime            | timestamp without time zone | Time in UTC that the partition pruning started<br>executing.                                                |
| endtime              | timestamp without time zone | Time in UTC that the partition pruning<br>completed.                                                        |
| duration             | bigint                      | Elapsed time (in microseconds).                                                                             |
| total_partitions     | integer                     | Number of total partitions.                                                                                 |
| qualified_partitions | integer                     | Number of qualified partitions.                                                                             |
| assigned_partitions  | integer                     | Number of assigned partitions on the<br>slice.                                                              |
| assignment           | character                   | Type of assignment.                                                                                         |

## Sample query

The following example gets the partition details for the last query
completed.

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

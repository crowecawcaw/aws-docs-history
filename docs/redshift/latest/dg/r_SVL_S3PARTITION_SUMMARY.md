Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_S3PARTITION_SUMMARY

Use the SVL_S3PARTITION_SUMMARY view to get a summary of Redshift Spectrum queries partition processing at the segment level.

SVL_S3PARTITION_SUMMARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about SVCS_S3PARTITION, see [SVCS_S3PARTITION_SUMMARY](r_SVCS_S3PARTITION_SUMMARY.md "r_SVCS_S3PARTITION_SUMMARY.md").

## Table columns

| Column name             | Data type | Description                                                                            |
| ----------------------- | --------- | -------------------------------------------------------------------------------------- |
| query                   | integer   | The query ID. You can use this value to join<br>various other system tables and views. |
| segment                 | integer   | The segment number. A query consists of multiple<br>segments.                          |
| assignment              | char(1)   | The type of partition assignment across nodes.                                         |
| min_starttime           | timestamp | The time in UTC that the partition processing started.                                 |
| max_endtime             | timestamp | The time in UTC that the partition processing completed.                               |
| min_duration            | bigint    | The minimum partition processing time used by a node for this query (in microseconds). |
| max_duration            | bigint    | The maximum partition processing time used by a node for this query (in microseconds). |
| avg_duration            | bigint    | The average partition processing time used by a node for this query (in microseconds). |
| total_partitions        | integer   | The total number of partitions in an external table.                                   |
| qualified_partitions    | integer   | The total number of qualified partitions.                                              |
| min_assigned_partitions | integer   | The minimum number of partitions assigned on one node.                                 |
| max_assigned_partitions | integer   | The maximum number of partitions assigned on one node.                                 |
| avg_assigned_partitions | bigint    | The average number of partitions assigned on one node.                                 |

## Sample query

The following example gets the partition scan details for the last query
completed.

```
select query, segment, assignment, min_starttime, max_endtime, min_duration, avg_duration
from svl_s3partition_summary
where query = pg_last_query_id()
order by query,segment;
```

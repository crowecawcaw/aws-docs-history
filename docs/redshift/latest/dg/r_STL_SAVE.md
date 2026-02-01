Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_SAVE

Contains details for _save_ steps in queries. A save
step saves the input stream to a transient table. A transient table is a temporary table
that stores intermediate results during query execution.

A query consists of multiple segments, and each segment consists of one or more steps.
For more information, see [Query processing](c-query-processing.md "c-query-processing.md").

STL_SAVE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_SAVE only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name  | Data type    | Description                                                                                                                                                                   |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid       | integer      | ID of the user who generated the entry.                                                                                                                                       |
| query        | integer      | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice        | integer      | Number that identifies the slice where the query was running.                                                                                                                 |
| segment      | integer      | Number that identifies the query segment.                                                                                                                                     |
| step         | integer      | Query step that ran.                                                                                                                                                          |
| starttime    | timestamp    | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime      | timestamp    | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum      | integer      | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows         | bigint       | Total number of rows that were processed.                                                                                                                                     |
| bytes        | bigint       | Size, in bytes, of all the output rows for the<br>step.                                                                                                                       |
| tbl          | integer      | ID of the materialized transient table.                                                                                                                                       |
| is_diskbased | character(1) | Whether this step of the query was performed as a<br>disk-based operation: true (`t`) or false<br>(`f`).                                                                      |
| workmem      | bigint       | Number of bytes of working memory assigned to the<br>step.                                                                                                                    |

## Sample queries

The following query shows which save steps in the most recent query were performed
on each slice.

```
select query, slice, segment, step, tasknum, rows,  tbl
from stl_save where query = pg_last_query_id();

 query | slice | segment | step | tasknum | rows | tbl
-------+-------+---------+------+---------+------+-----
 52236 |     3 |       0 |    2 |      21 |    0 | 239
 52236 |     2 |       0 |    2 |      20 |    0 | 239
 52236 |     2 |       2 |    2 |      20 |    0 | 239
 52236 |     3 |       2 |    2 |      21 |    0 | 239
 52236 |     1 |       0 |    2 |      21 |    0 | 239
 52236 |     0 |       0 |    2 |      20 |    0 | 239
 52236 |     0 |       2 |    2 |      20 |    0 | 239
 52236 |     1 |       2 |    2 |      21 |    0 | 239
(8 rows)
```

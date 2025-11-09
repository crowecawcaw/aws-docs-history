Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_RETURN

Contains details for _return_ steps in queries. A
return step returns the results of queries completed on the compute nodes to the leader
node. The leader node then merges the data and returns the results to the requesting
client. For queries completed on the leader node, a return step returns results to the
client.

A query consists of multiple segments, and each segment consists of one or more steps.
For more information, see [Query processing](c-query-processing.md "c-query-processing.md").

STL_RETURN is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_RETURN only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type | Description                                                                                                                                                                   |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer   | ID of the user who generated the entry.                                                                                                                                       |
| query       | integer   | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice       | integer   | Number that identifies the slice where the query was running.                                                                                                                 |
| segment     | integer   | Number that identifies the query segment.                                                                                                                                     |
| step        | integer   | Query step that ran.                                                                                                                                                          |
| starttime   | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime     | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum     | integer   | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows        | bigint    | Total number of rows that were processed.                                                                                                                                     |
| bytes       | bigint    | Size, in bytes, of all the output rows for the<br>step.                                                                                                                       |
| packets     | integer   | Total number of packets sent over the<br>network.                                                                                                                             |
| checksum    | bigint    | This information is for internal use only.                                                                                                                                    |

## Sample queries

The following query shows which steps in the most recent query were performed on
each slice.

```
SELECT query, slice, segment, step, endtime, rows, packets
from stl_return where query = pg_last_query_id();

 query |  slice | segment | step |          endtime           | rows | packets
-------+--------+---------+------+----------------------------+------+---------
     4 |      2 |       3 |    2 | 2013-12-27 01:43:21.469043 |    3 |       0
     4 |      3 |       3 |    2 | 2013-12-27 01:43:21.473321 |    0 |       0
     4 |      0 |       3 |    2 | 2013-12-27 01:43:21.469118 |    2 |       0
     4 |      1 |       3 |    2 | 2013-12-27 01:43:21.474196 |    0 |       0
     4 |      4 |       3 |    2 | 2013-12-27 01:43:21.47704  |    2 |       0
     4 |      5 |       3 |    2 | 2013-12-27 01:43:21.478593 |    0 |       0
     4 |   12811|       4 |    1 | 2013-12-27 01:43:21.480755 |    0 |       0
(7 rows)
```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVCS\_STREAM\_SEGS

Lists the relationship between streams and concurrent segments.

###### Note

System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.
The views are similar to the tables with the prefix STL except that the STL tables provide information only for queries run on the main cluster.

SVCS\_STREAM\_SEGS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type | Description                                                                   |
| ----------- | --------- | ----------------------------------------------------------------------------- |
| userid      | integer   | ID of the user who generated the entry.                                       |
| query       | integer   | Query ID. The query column can be used to join other system tables and views. |
| stream      | integer   | The set of concurrent segments of a query.                                    |
| segment     | integer   | Number that identifies the query segment.                                     |

## Sample queries

To view the relationship between streams and concurrent segments for the most
recent query, type the following query:

```
select *
from svcs_stream_segs
where query = pg_last_query_id();

 query | stream | segment
-------+--------+---------
    10 |      1 |       2
    10 |      0 |       0
    10 |      2 |       4
    10 |      1 |       3
    10 |      0 |       1
(5 rows)
```

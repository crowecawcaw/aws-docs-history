Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STL\_STREAM\_SEGS

Lists the relationship between streams and concurrent segments.

Streams in this context are Amazon Redshift streams. This system view doesn't pertain to [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

STL\_STREAM\_SEGS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL\_STREAM\_SEGS only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

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
from stl_stream_segs
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

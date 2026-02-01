Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_UNIQUE

Analyzes execution steps that occur when a DISTINCT function is used in the SELECT
list or when duplicates are removed in a UNION or INTERSECT query.

STL_UNIQUE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_UNIQUE only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name             | Data type    | Description                                                                                                                                                                                                                                                          |
| ----------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                  | integer      | ID of the user who generated the entry.                                                                                                                                                                                                                              |
| query                   | integer      | Query ID. The query column can be used to join other system tables and views.                                                                                                                                                                                        |
| slice                   | integer      | Number that identifies the slice where the query was running.                                                                                                                                                                                                        |
| segment                 | integer      | Number that identifies the query segment.                                                                                                                                                                                                                            |
| step                    | integer      | Query step that ran.                                                                                                                                                                                                                                                 |
| starttime               | timestamp    | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                         |
| endtime                 | timestamp    | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                        |
| tasknum                 | integer      | Number of the query task process that was assigned to run the step.                                                                                                                                                                                                  |
| rows                    | bigint       | Total number of rows that were processed.                                                                                                                                                                                                                            |
| `type`                  | character(6) | The type of step. Valid values are:<br>• HASHED. Indicates that the step used grouped, unsorted<br>aggregation.<br>• PLAIN. Indicates that the step used ungrouped, scalar<br>aggregation.<br>• SORTED. Indicates that the step used grouped, sorted<br>aggregation. |
| is_diskbased            | character(1) | If true (t), the query was performed as a<br>disk-based operation. If false (f), the query was performed in<br>memory.                                                                                                                                               |
| slots                   | integer      | Total number of hash buckets.                                                                                                                                                                                                                                        |
| workmem                 | bigint       | Total number of bytes in working memory that were<br>assigned to the step.                                                                                                                                                                                           |
| max_buffers_used        | bigint       | Maximum number of buffers used in the hash table<br>before going to disk.                                                                                                                                                                                            |
| resizes                 | integer      | This information is for internal use only.                                                                                                                                                                                                                           |
| occupied                | integer      | This information is for internal use only.                                                                                                                                                                                                                           |
| flushable               | integer      | This information is for internal use only.                                                                                                                                                                                                                           |
| used_unique_prefetching | character(1) | This information is for internal use only.                                                                                                                                                                                                                           |
| bytes                   | biginit      | The number of bytes of all the output rows for the step.                                                                                                                                                                                                             |

## Sample queries

Suppose you run the following query:

```
select distinct eventname
from event order by 1;
```

Assuming the ID for the previous query is 6313, the following example shows the
number of rows produced by the unique step for each slice in segments 0 and 1.

```
select query, slice, segment, step, datediff(msec, starttime, endtime) as msec, tasknum, rows
from stl_unique where query = 6313
order by query desc, slice, segment, step;
```

```
 query | slice | segment | step | msec | tasknum | rows
-------+-------+---------+------+------+---------+------
  6313 |     0 |       0 |    2 |    0 |      22 |  550
  6313 |     0 |       1 |    1 |  256 |      20 |  145
  6313 |     1 |       0 |    2 |    1 |      23 |  540
  6313 |     1 |       1 |    1 |   42 |      21 |  127
  6313 |     2 |       0 |    2 |    1 |      22 |  540
  6313 |     2 |       1 |    1 |  255 |      20 |  158
  6313 |     3 |       0 |    2 |    1 |      23 |  542
  6313 |     3 |       1 |    1 |   38 |      21 |  146
(8 rows)
```

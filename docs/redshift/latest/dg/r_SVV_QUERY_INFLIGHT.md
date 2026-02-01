Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_QUERY_INFLIGHT

Use the SVV_QUERY_INFLIGHT view to determine what queries are currently running on the
database. This view joins [STV_INFLIGHT](r_STV_INFLIGHT.md "r_STV_INFLIGHT.md") to [STL_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md").
SVV_QUERY_INFLIGHT does not show leader-node only queries. For more information, see
[Leader node–only
functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md").

SVV_QUERY_INFLIGHT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name | Data type      | Description                                                                                                                                                                                                                                                     |
| ----------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer        | ID of user who generated entry.                                                                                                                                                                                                                                 |
| slice       | integer        | Slice where the query is running.                                                                                                                                                                                                                               |
| query       | integer        | Query ID. Can be used to join various other system<br>tables and views.                                                                                                                                                                                         |
| pid         | integer        | Process ID. All of the queries in a session are<br>run in the same process, so this value remains constant if you run a<br>series of queries in the same session. You can use this column to<br>join to the [STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md") table. |
| starttime   | timestamp      | Time that the query started.                                                                                                                                                                                                                                    |
| suspended   | integer        | Whether the query is suspended:<br>`0` = false; `1` =<br>true.                                                                                                                                                                                                  |
| text        | character(200) | Query text, in 200-character increments.                                                                                                                                                                                                                        |
| sequence    | integer        | Sequence number for segments of query statements.                                                                                                                                                                                                               |

## Sample queries

The sample output below shows two queries currently running, the
SVV_QUERY_INFLIGHT query itself and query 428, which is split into three rows in the
table. (The starttime and statement columns are truncated in this sample output.)

```
select slice, query, pid, starttime, suspended, trim(text) as statement, sequence
from svv_query_inflight
order by query, sequence;

slice|query| pid  |      starttime       |suspended| statement | sequence
-----+-----+------+----------------------+---------+-----------+---------
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | select ...|    0
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | enueid ...|    1
1012 | 428 | 1658 | 2012-04-10 13:53:... |       0 | atname,...|    2
1012 | 429 | 1608 | 2012-04-10 13:53:... |       0 | select ...|    0
(4 rows)
```

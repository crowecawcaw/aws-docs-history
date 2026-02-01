Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_QUERY_REPORT

Amazon Redshift creates the SVL_QUERY_REPORT view from a UNION of a number of Amazon Redshift STL
system tables to provide information about completed query steps.

This view breaks down the information about completed queries by slice and by step,
which can help with troubleshooting node and slice issues in the Amazon Redshift
cluster.

SVL_QUERY_REPORT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name     | Data type    | Description                                                                                                                                                                                                                                                                                                                     |
| --------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid          | integer      | ID of user who generated entry.                                                                                                                                                                                                                                                                                                 |
| query           | integer      | Query ID. Can be used to join various other system<br>tables and views.                                                                                                                                                                                                                                                         |
| slice           | integer      | Data slice where the step ran.                                                                                                                                                                                                                                                                                                  |
| segment         | integer      | Segment number.<br>A query consists of multiple segments, and each segment<br>consists of one or more steps. Query segments can run in<br>parallel. Each segment runs in a single process.                                                                                                                                      |
| step            | integer      | Query step that completed.                                                                                                                                                                                                                                                                                                      |
| start_time      | timestamp    | Exact time in UTC when the segment started<br>executing, with 6 digits of precision for fractional seconds. For<br>example: `2012-12-12 11:29:19.131358`                                                                                                                                                                        |
| end_time        | timestamp    | Exact time in UTC when the segment finished<br>executing, with 6 digits of precision for fractional seconds. For<br>example: `2012-12-12 11:29:19.131467`                                                                                                                                                                       |
| elapsed_time    | bigint       | Time (in microseconds) that it took the segment to<br>run.                                                                                                                                                                                                                                                                      |
| rows            | bigint       | Number of rows produced by the step (per slice).<br>This number represents the number of rows for the slice that result<br>from the execution of the step, not the number of rows received or<br>processed by the step. In other words, this is the number of rows<br>that survive the step and are passed on to the next step. |
| bytes           | bigint       | Number of bytes produced by the step (per<br>slice).                                                                                                                                                                                                                                                                            |
| label           | char(256)    | Step label, which consists of a query step name<br>and, when applicable, table ID and table name (for example,<br>`scan tbl=100448 name =user`). Three-digit table IDs<br>usually refer to scans of transient tables. When you see`tbl=0`, it usually refers to a scan of a constant<br>value.                                  |
| is_diskbased    | character(1) | Whether this step of the query was performed as a<br>disk-based operation: true (`t`) or false<br>(`f`). Only certain steps, such as hash,<br>sort, and aggregate steps, can go to disk. Many types of steps are<br>always performed in memory.                                                                                 |
| workmem         | bigint       | Amount of working memory (in bytes) assigned to<br>the query step. This value is the query_working_mem threshold<br>allocated for use during execution, not the amount of memory that<br>was actually used                                                                                                                      |
| is_rrscan       | character(1) | If true (`t`), indicates that<br>range-restricted scan was used on the step.                                                                                                                                                                                                                                                    |
| is_delayed_scan | character(1) | If true (`t`), indicates that<br>delayed scan was used on the step.                                                                                                                                                                                                                                                             |
| rows_pre_filter | bigint       | For scans of permanent tables, the total number of<br>rows emitted before filtering rows marked for deletion (ghost rows)<br>and before applying user-defined query filters.                                                                                                                                                    |

## Sample queries

The following query demonstrates the data skew of the returned rows for the query
with query ID 279. Use this query to determine if database data is evenly
distributed over the slices in the data warehouse cluster:

```
select query, segment, step, max(rows), min(rows),
case when sum(rows) > 0
then ((cast(max(rows) -min(rows) as float)*count(rows))/sum(rows))
else 0 end
from svl_query_report
where query = 279
group by query, segment, step
order by segment, step;
```

This query should return data similar to the following sample output:

```
query | segment | step |   max    |   min    |         case
------+---------+------+----------+----------+----------------------
279 |       0 |    0 | 19721687 | 19721687 |                    0
279 |       0 |    1 | 19721687 | 19721687 |                    0
279 |       1 |    0 |   986085 |   986084 | 1.01411202804304e-06
279 |       1 |    1 |   986085 |   986084 | 1.01411202804304e-06
279 |       1 |    4 |   986085 |   986084 | 1.01411202804304e-06
279 |       2 |    0 |  1775517 |   788460 |     1.00098637606408
279 |       2 |    2 |  1775517 |   788460 |     1.00098637606408
279 |       3 |    0 |  1775517 |   788460 |     1.00098637606408
279 |       3 |    2 |  1775517 |   788460 |     1.00098637606408
279 |       3 |    3 |  1775517 |   788460 |     1.00098637606408
279 |       4 |    0 |  1775517 |   788460 |     1.00098637606408
279 |       4 |    1 |  1775517 |   788460 |     1.00098637606408
279 |       4 |    2 |        1 |        1 |                    0
279 |       5 |    0 |        1 |        1 |                    0
279 |       5 |    1 |        1 |        1 |                    0
279 |       6 |    0 |       20 |       20 |                    0
279 |       6 |    1 |        1 |        1 |                    0
279 |       7 |    0 |        1 |        1 |                    0
279 |       7 |    1 |        0 |        0 |                    0
(19 rows)
```

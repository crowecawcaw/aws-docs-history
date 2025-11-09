Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVCS_QUERY_SUMMARY

Use the SVCS_QUERY_SUMMARY view to find general information about the execution of a
query.

Note that the information in SVCS_QUERY_SUMMARY is aggregated from all nodes.

###### Note

The SVCS_QUERY_SUMMARY view only contains information about queries completed by
Amazon Redshift, not other utility and DDL commands. For a complete listing and information
on all statements completed by Amazon Redshift, including DDL and utility commands, you can
query the SVL_STATEMENTTEXT view.

System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.
The views are similar to the views with the prefix SVL except that the SVL views provide information only for queries run on the main cluster.

SVCS_QUERY_SUMMARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

For information about SVL_QUERY_SUMMARY, see [SVL_QUERY_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md").

## Table columns

| Column name     | Data type        | Description                                                                                                                                                                                                                                                                                   |
| --------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid          | integer          | ID of user who generated entry.                                                                                                                                                                                                                                                               |
| query           | integer          | Query ID. Can be used to join various other system<br>tables and views.                                                                                                                                                                                                                       |
| stm             | integer          | Stream: A set of concurrent segments in a query. A<br>query has one or more streams.                                                                                                                                                                                                          |
| seg             | integer          | Segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps. Query<br>segments can run in parallel. Each segment runs in a single process.                                                                                                       |
| step            | integer          | Query step that ran.                                                                                                                                                                                                                                                                          |
| maxtime         | bigint           | Maximum amount of time for the step to run (in<br>microseconds).                                                                                                                                                                                                                              |
| avgtime         | bigint           | Average time for the step to run (in<br>microseconds).                                                                                                                                                                                                                                        |
| rows            | bigint           | Number of data rows involved in the query step.                                                                                                                                                                                                                                               |
| bytes           | bigint           | Number of data bytes involved in the query step.                                                                                                                                                                                                                                              |
| rate_row        | double precision | Query execution rate per row.                                                                                                                                                                                                                                                                 |
| rate_byte       | double precision | Query execution rate per byte.                                                                                                                                                                                                                                                                |
| label           | text             | Step label, which consists of a query step name<br>and, when applicable, table ID and table name (for example, scan<br>tbl=100448 name =user). Three-digit table IDs usually refer to scans<br>of transient tables. When you see `tbl=0`, it usually<br>refers to a scan of a constant value. |
| is_diskbased    | character(1)     | Whether this step of the query was performed as a<br>disk-based operation on any node in the cluster: true<br>(`t`) or false (`f`).<br>Only certain steps, such as hash, sort, and aggregate steps, can go<br>to disk. Many types of steps are always run in memory.                          |
| workmem         | bigint           | Amount of working memory (in bytes) assigned to<br>the query step.                                                                                                                                                                                                                            |
| is_rrscan       | character(1)     | If true (`t`), indicates that<br>range-restricted scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                                       |
| is_delayed_scan | character(1)     | If true (`t`), indicates that<br>delayed scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                                                |
| rows_pre_filter | bigint           | For scans of permanent tables, the total number of<br>rows emitted before filtering rows marked for deletion (ghost<br>rows).                                                                                                                                                                 |

## Sample queries

**Viewing processing information for a query step**

The following query shows basic processing information for each step of query 87:

```
select query, stm, seg, step, rows, bytes
from svcs_query_summary
where query = 87
order by query, seg, step;
```

This query retrieves the processing information about query 87, as shown in the
following sample output:

```
 query | stm | seg | step |  rows  |  bytes
-------+-----+-----+------+--------+---------
87     |   0 |   0 |    0 |     90 |    1890
87     |   0 |   0 |    2 |     90 |     360
87     |   0 |   1 |    0 |     90 |     360
87     |   0 |   1 |    2 |     90 |    1440
87     |   1 |   2 |    0 | 210494 | 4209880
87     |   1 |   2 |    3 |  89500 |       0
87     |   1 |   2 |    6 |      4 |      96
87     |   2 |   3 |    0 |      4 |      96
87     |   2 |   3 |    1 |      4 |      96
87     |   2 |   4 |    0 |      4 |      96
87     |   2 |   4 |    1 |      1 |      24
87     |   3 |   5 |    0 |      1 |      24
87     |   3 |   5 |    4 |      0 |       0
(13 rows)
```

**Determining whether query steps spilled to disk**

The following query shows whether or not any of the steps for the query with query
ID 1025 (see the [SVL_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md") view to
learn how to obtain the query ID for a query) spilled to disk or if the query ran
entirely in-memory:

```
select query, step, rows, workmem, label, is_diskbased
from svcs_query_summary
where query = 1025
order by workmem desc;
```

This query returns the following sample output:

```
query| step|  rows  |  workmem   |  label        | is_diskbased
-----+-----+--------+-----------+---------------+--------------
1025 |  0  |16000000|  141557760 |scan tbl=9     | f
1025 |  2  |16000000|  135266304 |hash tbl=142   | t
1025 |  0  |16000000|  128974848 |scan tbl=116536| f
1025 |  2  |16000000|  122683392 |dist           | f
(4 rows)
```

By scanning the values for IS_DISKBASED, you can see which query steps went to
disk. For query 1025, the hash step ran on disk. Steps might run on disk include
hash, aggr, and sort steps. To view only disk-based query steps, add `and
 is_diskbased = 't'` clause to the SQL statement in the above
example.

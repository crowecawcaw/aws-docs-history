Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STL\_INSERT

Analyzes insert execution steps for queries.

STL\_INSERT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL\_INSERT only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name           | Data type    | Description                                                                                                                                                                                                                                                          |
| --------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                | integer      | ID of the user who generated the entry.                                                                                                                                                                                                                              |
| query                 | integer      | Query ID. The query column can be used to join other system tables and views.                                                                                                                                                                                        |
| slice                 | integer      | Number that identifies the slice where the query was running.                                                                                                                                                                                                        |
| segment               | integer      | Number that identifies the query segment.                                                                                                                                                                                                                            |
| step                  | integer      | Query step that ran.                                                                                                                                                                                                                                                 |
| starttime             | timestamp    | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                         |
| endtime               | timestamp    | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.                                                                                        |
| tasknum               | integer      | Number of the query task process that was assigned to run the step.                                                                                                                                                                                                  |
| rows                  | bigint       | Total number of rows that were processed.                                                                                                                                                                                                                            |
| tbl                   | integer      | Table ID.                                                                                                                                                                                                                                                            |
| inserted\_mega\_value | character(1) | This information is for internal use only. This information shows whether the given insert step has inserted a large value. A large value will be stored in multiple blocks. Block size is 1 MB by default, a large value is greater than 1 MB in a default setting. |

## Sample queries

The following example returns insert execution steps for the most recent query.

```
select slice, segment, step, tasknum, rows, tbl
from stl_insert
where query=pg_last_query_id();
```

```
 slice | segment | step | tasknum | rows  |  tbl
-------+---------+------+---------+-------+--------
     0 |       2 |    2 |      15 | 24958 | 100548
     1 |       2 |    2 |      15 | 25032 | 100548
(2 rows)
```

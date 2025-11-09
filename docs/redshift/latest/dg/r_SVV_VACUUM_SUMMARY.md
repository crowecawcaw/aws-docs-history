Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_VACUUM_SUMMARY

The SVV_VACUUM_SUMMARY view joins the STL_VACUUM, STL_QUERY, and STV_TBL_PERM tables
to summarize information about vacuum operations logged by the system. The view returns
one row per table per vacuum transaction. The view records the elapsed time of the
operation, the number of sort partitions created, the number of merge increments
required, and deltas in row and block counts before and after the operation was
performed.

SVV_VACUUM_SUMMARY is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_VACUUM_HISTORY](SYS_VACUUM_HISTORY.md "SYS_VACUUM_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

For information about SVV_VACUUM_PROGRESS, see [SVV_VACUUM_PROGRESS](r_SVV_VACUUM_PROGRESS.md "r_SVV_VACUUM_PROGRESS.md").

For information about SVL_VACUUM_PERCENTAGE, see [SVL_VACUUM_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md "r_SVL_VACUUM_PERCENTAGE.md").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name          | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| table_name           | text      | Name of the vacuumed table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| xid                  | bigint    | Transaction ID of the VACUUM operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| sort_partitions      | bigint    | Number of sorted partitions created during the<br>sort phase of the vacuum operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| merge_increments     | bigint    | Number of merge increments required to complete<br>the merge phase of the vacuum operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| elapsed_time         | bigint    | Elapsed runtime of the vacuum operation (in<br>microseconds).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| row_delta            | bigint    | Difference in the total number of table rows<br>before and after the vacuum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| sortedrow_delta      | bigint    | Difference in the number of sorted table rows<br>before and after the vacuum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| block_delta          | integer   | Difference in block count for the table before and<br>after the vacuum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| max_merge_partitions | integer   | This column is used for performance analysis and<br>represents the maximum number of partitions that vacuum can process<br>for the table per merge phase iteration. (Vacuum sorts the unsorted<br>region into one or more sorted partitions. Depending on the number<br>of columns in the table and the current Amazon Redshift configuration, the<br>merge phase can process a maximum number of partitions in a single<br>merge iteration. The merge phase will still work if the number of<br>sorted partitions exceeds the maximum number of merge partitions,<br>but more merge iterations will be required.) |

## Sample query

The following query returns statistics for vacuum operations on three different
tables. The SALES table was vacuumed twice.

```

select table_name, xid, sort_partitions as parts, merge_increments as merges,
elapsed_time, row_delta, sortedrow_delta as sorted_delta, block_delta
from svv_vacuum_summary
order by xid;

table_  | xid  |parts|merges| elapsed_ | row_    | sorted_ | block_
name    |      |     |      | time     | delta   | delta   | delta
--------+------+-----+------+----------+---------+---------+--------
users   | 2985 |   1 |    1 | 61919653 |       0 |   49990 |      20
category| 3982 |   1 |    1 | 24136484 |       0 |      11 |       0
sales   | 3992 |   2 |    1 | 71736163 |       0 | 1207192 |      32
sales   | 4000 |   1 |    1 | 15363010 | -851648 | -851648 |    -140
(4 rows)
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Vacuuming tables

Amazon Redshift can automatically sort and perform a VACUUM DELETE operation on tables in the
background. To clean up tables after a load or a series of incremental updates, you can
also run the [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md") command,
either against the entire database or against individual tables.

###### Note

Only users with the necessary table permissions can effectively vacuum a table.
If VACUUM is run
without the necessary table permissions, the operation completes successfully but has no
effect. For a list of valid table permissions to effectively run VACUUM, see
[VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

For this reason, we recommend vacuuming individual tables as needed. We also
recommend this approach because vacuuming the entire database is potentially an
expensive operation.

## Automatic table sort

Amazon Redshift automatically sorts data in the background to maintain table data in the order of
its sort key. Amazon Redshift keeps track of your scan queries to determine which sections of the
table will benefit from sorting.

Depending on the load on the system, Amazon Redshift automatically initiates the sort. This
automatic sort lessens the need to run the VACUUM command to keep data in sort key
order. If you need data fully sorted in sort key order, for example after a large data load, then you
can still manually run the VACUUM command. To determine whether your table will benefit by
running VACUUM SORT, monitor the `vacuum_sort_benefit` column in [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md").

Amazon Redshift tracks scan queries that use the sort key on each table. Amazon Redshift estimates
the maximum percentage of improvement in scanning and filtering of data for each table
(if the table was fully sorted). This estimate is visible in the
`vacuum_sort_benefit` column in [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md"). You can use this column, along with the
`unsorted` column, to determine when queries can benefit from manually
running VACUUM SORT on a table.
The `unsorted` column reflects the physical sort order of a table.

The `vacuum_sort_benefit` column specifies the impact of sorting a table by manually running VACUUM SORT.

For example, consider the following query:

```
select "table", unsorted,vacuum_sort_benefit from svv_table_info order by 1;
```

```

 table | unsorted | vacuum_sort_benefit
-------+----------+---------------------
 sales |    85.71 |                5.00
 event |    45.24 |               67.00

```

For the table “sales”, even though the table is ~86% physically unsorted, the query performance impact from the table being 86% unsorted is only 5%.
This might be either because only a small portion of the table is accessed by queries, or very few queries accessed the table.
For the table “event”, the table is ~45% physically unsorted. But the query performance impact of 67% indicates that either a larger portion of the table was accessed by queries,
or the number of queries accessing the table was large. The table "event" can potentially benefit from running VACUUM SORT.

## Automatic vacuum delete

When you perform a delete, the rows are marked for deletion, but not removed. Amazon Redshift
automatically runs a VACUUM DELETE operation in the background based on the number of
deleted rows in database tables. Amazon Redshift schedules the VACUUM DELETE to run during periods of
reduced load and pauses the operation during periods of high load.

###### Topics

- [VACUUM frequency](#vacuum-frequency "#vacuum-frequency")
- [Sort stage and merge stage](#vacuum-stages "#vacuum-stages")
- [Vacuum threshold](#vacuum-sort-threshold "#vacuum-sort-threshold")
- [Vacuum types](#vacuum-types "#vacuum-types")
- [Minimizing vacuum times](vacuum-managing-vacuum-times.md "vacuum-managing-vacuum-times.md")

## VACUUM frequency

You should vacuum as often as necessary to maintain consistent query performance.
Consider these factors when determining how often to run your VACUUM command:

- Run VACUUM during time periods when you expect minimal activity on the cluster,
  such as evenings or during designated database administration windows.
- Run VACUUM commands outside of maintenance windows. For more information,
  see [Schedule around maintenance windows](c_best-practices-avoid-maintenance.md "c_best-practices-avoid-maintenance.md").
- A large unsorted region results in longer vacuum times. If you delay vacuuming,
  the vacuum will take longer because more data has to be reorganized.
- VACUUM is an I/O intensive operation, so the longer it takes for your vacuum to
  complete, the more impact it will have on concurrent queries and other database
  operations running on your cluster.
- VACUUM takes longer for tables that use interleaved sorting. To evaluate
  whether interleaved tables must be re-sorted, query the [SVV_INTERLEAVED_COLUMNS](r_SVV_INTERLEAVED_COLUMNS.md "r_SVV_INTERLEAVED_COLUMNS.md")
  view.

## Sort stage and merge stage

Amazon Redshift performs a vacuum operation in two stages: first, it sorts the rows in the
unsorted region, then, if necessary, it merges the newly sorted rows at the end of the
table with the existing rows. When vacuuming a large table, the vacuum operation
proceeds in a series of steps consisting of incremental sorts followed by merges. If the
operation fails or if Amazon Redshift goes offline during the vacuum, the partially vacuumed
table or database will be in a consistent state, but you must manually restart the
vacuum operation. Incremental sorts are lost, but merged rows that were committed before
the failure do not need to be vacuumed again. If the unsorted region is large, the lost
time might be significant. For more information about the sort and merge stages, see
[Reduce the volume of merged rows](vacuum-managing-vacuum-times.md#vacuum-managing-volume-of-unmerged-rows "vacuum-managing-vacuum-times.md#vacuum-managing-volume-of-unmerged-rows").

Users can access tables while they are being vacuumed. You can perform queries and
write operations while a table is being vacuumed, but when DML and a vacuum run
concurrently, both might take longer. If you run UPDATE and DELETE statements during
a vacuum, system performance might be reduced. Incremental merges temporarily block
concurrent UPDATE and DELETE operations, and UPDATE and DELETE operations in turn
temporarily block incremental merge steps on the affected tables. DDL operations, such
as ALTER TABLE, are blocked until the vacuum operation finishes with the table.

###### Note

Various modifiers to VACUUM control the way that it works. You can use them to tailor the
vacuum operation for the current need. For example, using VACUUM RECLUSTER shortens
the vacuum operation by not performing a full merge operation. For more information,
see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

## Vacuum threshold

By default, VACUUM skips the sort phase for any table where more than 95 percent of
the table's rows are already sorted. Skipping the sort phase can significantly improve
VACUUM performance. To change the default sort threshold for a single table, include the
table name and the TO _threshold_ PERCENT parameter when you run the
VACUUM command.

## Vacuum types

For information about different vacuum types, see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Compound sort key

A compound key is made up of all of the columns listed in the sort key
definition, in the order they are listed. A compound sort key is most useful when a
query's filter applies conditions, such as filters and joins, that use a prefix of
the sort keys. The performance benefits of compound sorting decrease when queries
depend only on secondary sort columns, without referencing the primary columns.
COMPOUND is the default sort type.

Compound sort keys might speed up joins, GROUP BY and ORDER BY operations, and
window functions that use PARTITION BY and ORDER BY. For example, a merge join,
which is often faster than a hash join, is feasible when the data is distributed and
presorted on the joining columns. Compound sort keys also help improve compression.

As you add rows to a sorted table that already contains data, the unsorted region
grows, which has a significant effect on performance. The effect is greater when the
table uses interleaved sorting, especially when the sort columns include data that
increases monotonically, such as date or timestamp columns. Run a VACUUM operation
regularly, especially after large data loads, to re-sort and re-analyze the data.
For more information, see [Reduce the size of the unsorted region](vacuum-managing-vacuum-times.md#r_vacuum_diskspacereqs "vacuum-managing-vacuum-times.md#r_vacuum_diskspacereqs"). After vacuuming to resort the data,
it's a good practice to run an ANALYZE command to update the statistical
metadata for the query planner. For more information, see [Analyzing tables](t_Analyzing_tables.md "t_Analyzing_tables.md").

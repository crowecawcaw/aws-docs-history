# Collect and Utilize table statistics

Collecting table statistics allows Trino’s cost-based optimizer to make informed decisions about join orders, filter pushdown,
and partition pruning, resulting in better performance.

You can use the `ANALYZE` command to collect statistics for Hive or Iceberg tables:

```
ANALYZE sales;
```

Collecting statistics on wide tables can be taxing on resources. We recommend specifying a subset of columns that are used in
joins, in filters, or in grouping operations.

This is another helpful command. It displays current statistics for a table to verify if statistics are up to date.

```
show stats for table_name;
```

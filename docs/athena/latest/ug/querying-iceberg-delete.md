# DELETE

Athena Iceberg `DELETE` writes Iceberg position delete files to a table.
This is known as a _merge-on-read_ delete. In contrast to a
_copy-on-write_ delete, a merge-on-read delete is more
efficient because it does not rewrite file data. When Athena reads Iceberg data, it
merges the Iceberg position delete files with data files to produce the latest view
of a table. To remove these position delete files, you can run the [REWRITE
DATA compaction action](querying-iceberg-data-optimization.md#querying-iceberg-data-optimization-rewrite-data-action "querying-iceberg-data-optimization.md#querying-iceberg-data-optimization-rewrite-data-action"). `DELETE` operations are charged by the
amount of data scanned. For syntax, see [DELETE](delete-statement.md "delete-statement.md").

The following example deletes rows from `iceberg_table` that have
`c3` as the value for `category`.

```
DELETE FROM iceberg_table WHERE category='c3'
```

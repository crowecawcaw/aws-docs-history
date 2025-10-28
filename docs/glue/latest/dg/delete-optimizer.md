# Deleting an optimizer

You can delete an optimizer and associated metadata for the table using AWS CLI or AWS API operation.

Run the following AWS CLI command to delete optimization history for a table. You need to
specify the optimizer `type` along with the catalog ID, database name and table
name. The acceptable values are: `compaction`, `retention`, and
`orphan_file_deletion`.

```
aws glue delete-table-optimizer \
  --catalog-id `123456789012` \
  --database-name `iceberg_db` \
  --table-name `iceberg_table` \
  --type `compaction`
```

Use `DeleteTableOptimizer` operation to delete an optimizer for a table.

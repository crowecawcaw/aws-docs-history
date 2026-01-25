# Canceling data loading

To cancel a data loading job, call the `rds_aurora.limitless_data_load_cancel` stored procedure, with the job ID as the input
parameter. You call this stored procedure from the same database in the DB shard group where the specific data loading job was started. For
example:

```
CALL rds_aurora.limitless_data_load_cancel(12345);

INFO: limitless data load job with id 12345 is canceling without rollback.
```

You can't cancel a data loading job that doesn't exist or isn't running in the same DB shard group.

The Aurora PostgreSQL Limitless Database data loading utility leaves loaded data in the destination tables without rollback, as the response shows. If you don’t want to
keep the loaded data, we recommend truncating the destination tables.

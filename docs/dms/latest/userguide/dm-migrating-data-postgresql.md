# Migrating data from PostgreSQL databases

with homogeneous data migrations in AWS DMS

You can use [Homogeneous data migrations](data-migrations.md "data-migrations.md") to migrate a self-managed PostgreSQL database to RDS for PostgreSQL or Aurora PostgreSQL.
AWS DMS creates a serverless environment for your data migration. For different types of data migrations,
AWS DMS uses different native PostgreSQL database tools.

For homogeneous data migrations of the **Full load** type, AWS DMS uses pg_dump to read data from
your source database and store it on the disk attached to the serverless environment. After AWS DMS reads
all your source data, it uses pg_restore in the target database to restore your data.

For homogeneous data migrations of the **Full load and change data capture (CDC)** type, AWS DMS uses
`pg_dump` to read schema objects without table data from your source database and store them on the disk attached to the serverless
environment. It then uses `pg_restore` in the target database to restore your schema objects.
After AWS DMS completes the `pg_restore` process, it automatically switches to a publisher and
subscriber model for logical replication with the `Initial Data Synchronization` option to copy
initial table data directly from the source database to the target database, and then initiates ongoing replication.
In this model, one or more subscribers subscribe to one or more publications
on a publisher node.

For homogeneous data migrations of the **Change data capture (CDC)** type, AWS DMS requires the native start
point to start the replication. If you provide the native start point, then AWS DMS captures changes from
that point. Alternatively, choose **Immediately** in the data migration settings to
automatically capture the start point for the replication when the actual data migration starts.

###### Note

For a CDC-only migration to work properly, all source database schemas and objects must already be present
on the target database. The target may have objects that are not present on the source, however.

You can use the following code example to get the native start point in your PostgreSQL
database.

```
select confirmed_flush_lsn from pg_replication_slots where slot_name=‘migrate_to_target';
```

This query uses the `pg_replication_slots` view in your PostgreSQL database
to capture the log sequence number (LSN) value.

After AWS DMS sets the status of your PostgreSQL homogeneous data migration to **Stopped**,
**Failed**, or **Deleted**, the publisher and replication aren't removed.
If you don't want to resume the migration, then delete the replication slot and the publisher by using the
following command.

```
SELECT pg_drop_replication_slot('migration_subscriber_{ARN}');
            DROP PUBLICATION publication_{ARN};
```

The following diagram shows the process of using homogeneous data migrations in AWS DMS to migrate a PostgreSQL database
to RDS for PostgreSQL or Aurora PostgreSQL.

![An architecture diagram of the PostgreSQL data migration with DMS Homogeneous Data Migrations.](images/data-migrations-postgresql.png)

## Best practices for using a PostgreSQL database as a

source for homogeneous data migrations

- To speed up initial data syncing on the subscriber side for FLCDC task, you must adjust
  `max_logical_replication_workers` and `max_sync_workers_per_subscription`. Increasing
  these values enhances table synchronization speed.
  - **max_logical_replication_workers** –
    Specifies maximum number of logical replication workers. This includes both the apply workers on the
    subscriber side and the table synchronization workers.
  - **max_sync_workers_per_subscription** –
    Increasing `max_sync_workers_per_subscription` only affects the number of tables
    that are synchronized in parallel, not the number of workers per table.

###### Note

`max_logical_replication_workers` should not exceed `max_worker_processes`,
and `max_sync_workers_per_subscription` should be less than or equal to
`max_logical_replication_workers`.

- For migrating large tables, consider dividing them into separate tasks using selection rules.
  For example, you can divide large tables into separate individual tasks and small tables into another single task.
- Monitor disk and CPU usage on the subscriber side to maintain optimal performance.

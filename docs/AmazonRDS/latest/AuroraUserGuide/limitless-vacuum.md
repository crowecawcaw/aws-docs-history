# Reclaiming storage space by vacuuming

PostgreSQL Multiversion Concurrency Control (MVCC) helps to preserve data integrity by saving an internal copy of updated or
deleted rows until a transaction is either committed or rolled back. These copies, also called _tuples_, can cause table bloat if they aren't cleaned up regularly. PostgreSQL instances order transactions by
their transaction IDs, and PostgreSQL uses transaction ID–based MVCC to control tuple visibility and provide transaction
isolation. Each transaction establishes a snapshot of data, and each tuple has a version. Both the snapshot and version are
transaction ID–based.

To clean up data, the `VACUUM` utility performs four key functions in PostgreSQL:

- `VACUUM` – Removes expired row versions, making the space available for reuse.
- `VACUUM FULL` – Provides complete defragmentation by removing dead row versions and compacting the
  tables, reducing the size and increasing efficiency.
- `VACUUM FREEZE` – Protects against transaction ID wraparound issues by marking older row versions as
  frozen.
- `VACUUM ANALYZE` – Removes dead row versions and updates the database's query planning statistics.
  It's a combination of the `VACUUM` and `ANALYZE` functions. For more information on how
  `ANALYZE` works in Aurora PostgreSQL Limitless Database, see [ANALYZE](limitless-reference.md#limitless-reference.DML-limitations.ANALYZE "limitless-reference.md#limitless-reference.DML-limitations.ANALYZE").
  As with MVCC, vacuuming in Aurora PostgreSQL is transaction ID–based. If there's an ongoing transaction when vacuuming starts, rows that are
  still visible to that transaction aren't removed.

For more information on the `VACUUM` utility, see [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html")
in the PostgreSQL documentation. For more information about `VACUUM` support in Aurora PostgreSQL Limitless Database, see [VACUUM](limitless-reference.md#limitless-reference.DML-limitations.VACUUM "limitless-reference.md#limitless-reference.DML-limitations.VACUUM").

###### Topics

- [AUTOVACUUM](#limitless-autovacuum "#limitless-autovacuum")
- [Time-based vacuuming in Aurora PostgreSQL Limitless Database](#limitless-vacuum.time-based "#limitless-vacuum.time-based")
- [Using database statistics for vacuuming](#limitless-vacuum.stats "#limitless-vacuum.stats")
- [Differences in vacuuming behavior between Aurora PostgreSQL and Aurora PostgreSQL Limitless Database](#limitless-vacuum-limitations "#limitless-vacuum-limitations")

## AUTOVACUUM

Aurora PostgreSQL uses the `VACUUM` and `AUTOVACUUM` utilities to remove unneeded tuples. The underlying mechanism for
`AUTOVACUUM` and manual `VACUUM` is the same; the only difference is the automation.

`AUTOVACUUM` in Aurora PostgreSQL and Aurora PostgreSQL Limitless Database is a combination of the `VACUUM` and `ANALYZE` utilities.
`AUTOVACUUM` determines which databases and tables to clean up, according to a predefined rule, such as the percentage of dead
tuples and the number of inserts.

For example, `AUTOVACUUM` "wakes up" periodically to perform cleanup. The interval is controlled by the
`autovacuum_naptime` parameter. The default value is 1 minute. The default values for `AUTOVACUUM` and
`VACUUM` configuration parameters are the same for Aurora PostgreSQL Limitless Database as for Aurora PostgreSQL.

The `AUTOVACUUM` daemon, if enabled, automatically issues `ANALYZE` commands whenever the content of a table has changed
sufficiently. In Aurora PostgreSQL Limitless Database, `AUTOVACUUM` issues `ANALYZE` on both routers and shards.

For more information about the `AUTOVACUUM` daemon and table storage parameters associated with `AUTOVACUUM`, see [The autovacuum daemon](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM "https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM ") and [Storage parameters](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html "https://www.postgresql.org/docs/current/runtime-config-autovacuum.html") in the PostgreSQL
documentation.

## Time-based vacuuming in Aurora PostgreSQL Limitless Database

Aurora PostgreSQL Limitless Database is a distributed system, meaning that multiple instances can be involved in a transaction. Therefore, transaction
ID–based visibility doesn't apply. Instead, Aurora PostgreSQL Limitless Database uses _time-based_ visibility, because
transaction IDs aren't “unified” across instances, but time can be “unified” across instances. Each transaction snapshot and
each tuple version obeys the time instead of the transaction ID. To be more specific, a transaction snapshot has a snapshot
start time, and a tuple has a creation time (when an `INSERT` or `UPDATE` happens) and a deletion time
(when a `DELETE` happens).

To maintain data consistency across the instances in the DB shard group, Aurora PostgreSQL Limitless Database has to make sure that vacuuming doesn't
remove any tuples that are still visible to any active transaction in the DB shard group. Therefore, vacuuming in Aurora PostgreSQL Limitless Database
is also time-based. Other aspects of `VACUUM` remain the same, including that to run `VACUUM` on a
particular table, a user must have access to that table.

###### Note

We strongly recommend that you don't leave transactions open for long periods of time.

Time-based vacuuming consumes more memory than transaction ID–based vacuuming.

The following example illustrates how time-based vacuuming works.

1. A customer table is distributed across four shards.
2. Transaction 1 starts with a repeatable read, and targets only one shard (shard 1). This transaction remains
   open.

Transaction 1 is older than any other transaction started after it. 3. Transaction 2 starts later, and deletes all tuples from a table, then commits. 4. If `AUTOVACUUM` or manual `VACUUM` tries to clean up dead tuples (dead due to transaction
2), it doesn't remove anything.

This is true not only for shard 1, but also for shards 2–4, because transaction 1 might still need to
access these tuples. They're still visible to transaction 1 because of MVCC.

The last step is achieved through synchronization, so that all shards are aware
of transaction 1, even though transaction 1 doesn't touch all of them.

## Using database statistics for vacuuming

To get information on tuples that you might need to clean up, use the [limitless_stat_all_tables](limitless-monitoring-views.md#limitless_stat_all_tables "limitless-monitoring-views.md#limitless_stat_all_tables") view, which works similarly to [pg_stat_all_tables](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW"). The following example queries the view.

```
SELECT * FROM rds_aurora.limitless_stat_all_tables WHERE relname LIKE '%customer%';
```

Similarly, for database statistics use [limitless_stat_database](limitless-monitoring-views.md#limitless_stat_database "limitless-monitoring-views.md#limitless_stat_database") instead of
[pg_stat_database](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW"), and [limitless_stat_activity](limitless-monitoring-views.md#limitless_stat_activity "limitless-monitoring-views.md#limitless_stat_activity") instead of [pg_stat_activity](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW").

To check table disk usage, use the [limitless_stat_relation_sizes](limitless-monitoring-functions.md#limitless_stat_relation_sizes "limitless-monitoring-functions.md#limitless_stat_relation_sizes")
function, which works similarly to [pg_relation_size](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-DBOBJECT "https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-DBOBJECT").
The following example queries the function.

```
SELECT * FROM rds_aurora.limitless_stat_relation_sizes('public','customer');
```

To track the progress of a `VACUUM` operation on Aurora PostgreSQL Limitless Database, use the [limitless_stat_progress_vacuum](limitless-monitoring-views.md#limitless_stat_progress_vacuum "limitless-monitoring-views.md#limitless_stat_progress_vacuum") view instead of [pg_stat_progress_vacuum](https://www.postgresql.org/docs/15/progress-reporting.html#VACUUM-PROGRESS-REPORTING "https://www.postgresql.org/docs/15/progress-reporting.html#VACUUM-PROGRESS-REPORTING"). The following example queries the view.

```
SELECT * FROM rds_aurora.limitless_stat_progress_vacuum;
```

For more information, see [Aurora PostgreSQL Limitless Database views](limitless-monitoring-views.md "limitless-monitoring-views.md") and
[Aurora PostgreSQL Limitless Database functions](limitless-monitoring-functions.md "limitless-monitoring-functions.md").

## Differences in vacuuming behavior between Aurora PostgreSQL and Aurora PostgreSQL Limitless Database

Some other differences between Aurora PostgreSQL and Aurora PostgreSQL Limitless Database in how vacuuming works are the following:

- Aurora PostgreSQL performs `VACUUM` operations on transaction IDs up to the oldest ongoing transaction. If
  there's no ongoing transaction in the database, `VACUUM` performs the operation until the last
  transaction.
- Aurora PostgreSQL Limitless Database synchronizes the oldest time snapshot every 10 seconds. Therefore, `VACUUM` might not perform
  the operation on any transactions that were run within the last 10 seconds.

For information on support for `VACUUM` in Aurora PostgreSQL Limitless Database, see
[VACUUM](limitless-reference.md#limitless-reference.DML-limitations.VACUUM "limitless-reference.md#limitless-reference.DML-limitations.VACUUM") in the
[Aurora PostgreSQL Limitless Database reference](limitless-reference.md "limitless-reference.md").

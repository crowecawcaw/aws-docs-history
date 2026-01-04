# Monitoring the

write-through cache and logical slots for Aurora PostgreSQL logical replication

Monitor the logical replication write-through cache and manage logical slots to
improve performance for your Aurora PostgreSQL DB cluster. Following, find more information about
the write-through cache and logical slots.

###### Topics

- [Monitoring the Aurora PostgreSQL logical replication write-through cache](#AuroraPostgreSQL.Replication.Logical-write-through-cache "#AuroraPostgreSQL.Replication.Logical-write-through-cache")
- [Managing logical slots for Aurora PostgreSQL](#AuroraPostgreSQL.Replication.Logical.Configure.managing-logical-slots "#AuroraPostgreSQL.Replication.Logical.Configure.managing-logical-slots")

## Monitoring the Aurora PostgreSQL logical replication write-through cache

By default, Aurora PostgreSQL versions 14.5, 13.8, 12.12, and 11.17 and higher use a
write-through cache to improve the performance for logical replication. Without the
write-through cache, Aurora PostgreSQL uses the Aurora storage layer in its
implementation of the native PostgreSQL logical replication process. It does so by
writing WAL data to storage and then reading the data back from storage to decode it
and send (replicate) to its targets (subscribers). This can result in bottlenecks
during logical replication for Aurora PostgreSQL DB clusters.

The write-through cache minimizes reliance on the Aurora storage layer. Instead of
consistently writing to and reading from this layer, Aurora PostgreSQL uses a buffer to
cache the logical WAL stream for use during the replication process, reducing the
need to access disk. This buffer is the native PostgreSQL cache used in logical
replication and is identified in Aurora PostgreSQL DB cluster parameters as
`rds.logical_wal_cache`.

When you use logical replication with your Aurora PostgreSQL DB cluster (for the
versions that support the write-through cache), you can monitor the cache hit ratio
to see how well it's working for your use case. To do so, connect to your
Aurora PostgreSQL DB cluster's write instance using `psql` and then use
the Aurora function, `aurora_stat_logical_wal_cache`, as shown in the
following example.

```
SELECT * FROM aurora_stat_logical_wal_cache();
```

The function returns output such as the following.

```
name       | active_pid | cache_hit | cache_miss | blks_read | hit_rate | last_reset_timestamp
-----------+------------+-----------+------------+-----------+----------+--------------
test_slot1 | 79183      | 24        | 0          | 24        | 100.00%  | 2022-08-05 17:39...
test_slot2 |            | 1         | 0          |  1        | 100.00%  | 2022-08-05 17:34...
(2 rows)
```

The `last_reset_timestamp` values have been shortened for readability.
For more information about this function, see [aurora_stat_logical_wal_cache](aurora_stat_logical_wal_cache.md "aurora_stat_logical_wal_cache.md").

Aurora PostgreSQL provides the following two functions for monitoring the
write-through cache.

- The `aurora_stat_logical_wal_cache` function – For
  reference documentation, see [aurora_stat_logical_wal_cache](aurora_stat_logical_wal_cache.md "aurora_stat_logical_wal_cache.md").
- The `aurora_stat_reset_wal_cache` function – For
  reference documentation, see [aurora_stat_reset_wal_cache](aurora_stat_reset_wal_cache.md "aurora_stat_reset_wal_cache.md").

If you find that the automatically adjusted WAL cache size isn't sufficient
for your workloads, you can change the the value of the
`rds.logical_wal_cache` manually. Consider the following:

- When the `rds.logical_replication` parameter is disabled,
  `rds.logical_wal_cache` is set to zero (0).
- When the `rds.logical_replication` parameter is enabled,
  `rds.logical_wal_cache` has a default value of 16 MB.
- The `rds.logical_wal_cache` parameter is static and requires a
  database instance reboot for changes to take effect. This parameter is
  defined in terms of 8 Kb blocks. Note that any positive value less than 32
  Kb is treated as 32 Kb. For more information about `wal_buffers`
  see [Write Ahead Log](https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-SETTINGS "https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-SETTINGS") in the PostgreSQL documentation.

## Managing logical slots for Aurora PostgreSQL

Streaming activity is captured in the `pg_replication_origin_status`
view. To see the contents of this view, you can use the
`pg_show_replication_origin_status()` function, as shown
following:

```
SELECT * FROM pg_show_replication_origin_status();
```

You can get a list of your logical slots by using the following SQL query.

```
SELECT * FROM pg_replication_slots;
```

To drop a logical slot, use the `pg_drop_replication_slot` with the
name of the slot, as shown in the following command.

```
SELECT pg_drop_replication_slot('test_slot');
```

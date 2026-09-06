

# Avoiding performance issues with REPLICA IDENTITY FULL in RDS for PostgreSQL
<a name="PostgreSQL.ReplicaIdentityFull"></a>

PostgreSQL logical replication requires each published table to have a *replica identity* so that the subscriber can locate the correct row to update or delete. By default, the primary key serves as the replica identity. When a table has no primary key or suitable unique index, you can set the replica identity to `FULL`, which causes PostgreSQL to use the entire row as the key.

While `REPLICA IDENTITY FULL` solves the immediate problem of replicating tables without primary keys, it can introduce serious performance issues on both the publisher and subscriber. Understanding these impacts is important for anyone using logical replication with RDS for PostgreSQL, including features that rely on logical replication internally, such as blue/green deployments.

## Why REPLICA IDENTITY FULL causes problems
<a name="PostgreSQL.ReplicaIdentityFull.WhyProblems"></a>

### Increased WAL volume on the publisher
<a name="PostgreSQL.ReplicaIdentityFull.WALVolume"></a>

The `REPLICA IDENTITY` setting controls what information PostgreSQL writes to the write-ahead log (WAL) to identify rows that are updated or deleted. With the default replica identity (primary key), only the key columns are logged as the old row identity. With `FULL`, PostgreSQL records the old values of *every* column for each `UPDATE` and `DELETE`. This has several consequences:
+ **WAL size increases significantly.** For updates, the size of each WAL record roughly doubles because both old and new values for every column are recorded. If the table contains large values stored using [TOAST](https://www.postgresql.org/docs/current/storage-toast.html), the increase can be much larger because TOASTed values must be fetched and written to the WAL even if they were not modified by the update.
+ **Higher I/O and CPU usage on the publisher.** The additional WAL writes consume more disk I/O bandwidth and CPU cycles, especially for write-heavy workloads.
+ **More data sent to subscribers.** The publisher must transmit larger WAL records over the network to each subscriber, increasing bandwidth consumption.

### Slow row lookups on the subscriber
<a name="PostgreSQL.ReplicaIdentityFull.SlowLookups"></a>

When the subscriber receives an `UPDATE` or `DELETE` log record, it must find the matching row in its local copy of the table. With `REPLICA IDENTITY FULL`, the subscriber searches for a row that matches *all* column values from the old row image.

How PostgreSQL performs this search differs by PostgreSQL major version:
+ **Before PostgreSQL 16:** If the table has no primary key and no explicitly configured replica identity index, the subscriber performs a sequential scan of the entire table for every single `UPDATE` or `DELETE` operation. On large tables, this makes apply performance extremely slow.
+ **PostgreSQL 16 and later:** The subscriber can use a btree or hash index for row lookups, even if that index is not explicitly set as the replica identity. However, the subscriber does not evaluate which index is most efficient. [Beginning in version 16](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=89e46da5e), PostgreSQL selects the [first suitable index](https://www.postgresql.org/docs/18/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION-REPLICA-IDENTITY) it finds, and the user has no control over this choice. If the selected index has low selectivity (for example, an index on a boolean or status column), the row lookup can be nearly as slow as a sequential scan. For this reason, relying on implicit index selection with `REPLICA IDENTITY FULL` is unreliable and should be considered a fallback, not a recommended configuration.

### How REPLICA IDENTITY FULL causes replication lag
<a name="PostgreSQL.ReplicaIdentityFull.ReplicationLag"></a>

The two problems described above — larger WAL on the publisher and slower row lookups on the subscriber — combine to cause replication lag.

By default, PostgreSQL logical replication uses a single *apply worker* process per subscription to receive changes from the publisher and apply them to the subscriber's tables. The apply worker processes changes serially, one row at a time, in commit order. This means the subscriber's throughput is limited by how fast it can apply each individual change.

When `REPLICA IDENTITY FULL` is set on a table without an appropriate index, every `UPDATE` and `DELETE` requires a sequential scan of the entire table to find the matching row. If the table has millions of rows, each of these operations can take seconds or longer. The result is a cascading problem:

1. **The publisher generates changes faster than the subscriber can apply them.** The publisher's write workload continues at normal speed, but the subscriber's apply worker is bottlenecked on sequential scans or poorly selective indexes for each row lookup.

1. **WAL accumulates on the publisher and can exhaust storage.** PostgreSQL cannot reclaim WAL segments until the subscriber confirms it has applied them. As the subscriber falls further behind, the publisher accumulates WAL on disk. On RDS for PostgreSQL, this appears as growing `OldestReplicationSlotLag` in CloudWatch. In severe cases, this can consume all available storage and cause the publisher to stop accepting writes.

1. **The lag is self-reinforcing.** As the subscriber falls behind, the table on the subscriber continues to grow from replicated inserts, making each sequential scan even slower. Without intervention, the lag grows without bound.

This problem is especially severe for tables that receive frequent `UPDATE` or `DELETE` operations. `INSERT` operations are not affected because they don't require a row lookup on the subscriber.

**Note**  
Starting with PostgreSQL 16, the apply worker can use parallel apply for large streaming transactions, which can help with throughput. However, the fundamental row-lookup bottleneck for `REPLICA IDENTITY FULL` without indexes remains, because each individual row still requires a scan to locate.

### Impact on blue/green deployments
<a name="PostgreSQL.ReplicaIdentityFull.BlueGreen"></a>

Blue/green deployments in Amazon RDS use logical replication internally to keep the green environment synchronized with the blue environment by setting up a single subscription per database. The logical replication apply process in the green environment is *single-threaded*. A single apply worker process receives all changes from the blue environment and applies them one at a time, in commit order. There is no parallel apply in the blue/green replication path.

This single-threaded design means the green environment's ability to keep up with the blue environment depends entirely on how fast that one apply worker can process each individual change. When tables use `REPLICA IDENTITY FULL` without a primary key or suitable index, the impact on the apply worker depends on the PostgreSQL version. In versions prior to 16, every `UPDATE` and `DELETE` on those tables forces the apply worker to perform a sequential scan of the entire table to find the matching row. In versions 16 and later, PostgreSQL will use a [suitable index](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=89e46da5e) if one is available, but if no qualifying index exists, the apply worker still falls back to a sequential scan. While the apply worker is scanning a large table for one row, all other pending changes across all tables queue up and wait.

The consequences for blue/green deployments are significant:
+ **Replication lag grows continuously.** If the blue environment generates write traffic faster than the single apply worker can process it, the green environment falls further and further behind. Because the apply worker is single-threaded, there is no way to parallelize the catch-up.
+ **Switchover can be blocked.** A blue/green switchover requires the green environment to be fully synchronized with the blue environment. If replication lag is too high, the switchover cannot complete within the timeout period.
+ **The green environment might never catch up.** For write-heavy workloads with large tables using `REPLICA IDENTITY FULL` and no indexes, the apply rate can be so slow that the green environment falls permanently behind, making switchover impossible without first resolving the replica identity configuration.
+ **WAL accumulates on the blue environment.** While the green environment is behind, the blue environment retains WAL segments for the replication slot. This increases storage usage on the blue (production) environment and can affect production performance.

To avoid these problems, ensure that all tables have a primary key or a suitable unique index explicitly configured as the replica identity using `ALTER TABLE ... REPLICA IDENTITY USING INDEX` *before* creating a blue/green deployment. Don't rely on `REPLICA IDENTITY FULL` with implicit index selection in PostgreSQL 16\+, because the subscriber might choose a poorly selective index or fall back to sequential scans. Test the deployment with a representative write workload to confirm the green environment can keep up.

For more information about blue/green deployment limitations, see [Limitations and considerations for Amazon RDS blue/green deployments](blue-green-deployments-considerations.md). For best practices, see [RDS for PostgreSQL best practices for blue/green deployments](blue-green-deployments-best-practices.md#blue-green-deployments-best-practices-postgres).

## How to identify tables using REPLICA IDENTITY FULL
<a name="PostgreSQL.ReplicaIdentityFull.Identify"></a>

Run the following query to find all tables with `REPLICA IDENTITY FULL`:

```
SELECT n.nspname AS schema, c.relname AS table_name, c.relreplident
FROM pg_catalog.pg_class c
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r'
  AND c.relreplident = 'f'
  AND n.nspname NOT IN ('pg_catalog', 'information_schema')
ORDER BY n.nspname, c.relname;
```

The `relreplident` column values are:
+ `d` — default (primary key)
+ `n` — nothing
+ `f` — full (entire row)
+ `i` — a specific index

## Workarounds and best practices
<a name="PostgreSQL.ReplicaIdentityFull.Workarounds"></a>

### Add a primary key wherever possible
<a name="PostgreSQL.ReplicaIdentityFull.AddPrimaryKey"></a>

The most effective solution is to add a primary key to tables that lack one. When a primary key exists, PostgreSQL uses it as the default replica identity, which provides efficient row lookups on the subscriber and minimizes WAL overhead on the publisher.

```
ALTER TABLE my_table ADD COLUMN id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY;
```

**Important**  
This statement acquires an `ACCESS EXCLUSIVE` lock and rewrites the entire table, because the default value expression uses `nextval()` which is volatile. All reads and writes to the table are blocked for the duration of the rewrite. On large tables, this can cause significant downtime. Plan this change during a maintenance window or consider alternative approaches such as creating the column as nullable first, then backfilling and adding the constraint in separate steps.

If adding a primary key is not feasible due to application constraints, consider adding a unique index on a set of `NOT NULL` columns and setting it as the replica identity:

```
CREATE UNIQUE INDEX my_table_replica_idx ON my_table (col1, col2);
ALTER TABLE my_table REPLICA IDENTITY USING INDEX my_table_replica_idx;
```

**Note**  
To avoid blocking writes while the index is built, use the [`CONCURRENTLY`](https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) clause: `CREATE UNIQUE INDEX CONCURRENTLY my_table_replica_idx ON my_table (col1, col2);`

**Note**  
The index used for replica identity must be unique, must not be partial, must not be deferrable, and must include only columns with `NOT NULL` constraints.

### Don't rely on implicit index selection (PostgreSQL 16\+)
<a name="PostgreSQL.ReplicaIdentityFull.SubscriberIndexes"></a>

Starting with PostgreSQL 16, the subscriber's apply worker can use btree or hash indexes for row lookups when the replica identity is set to `FULL`, even if those indexes are not explicitly configured as the replica identity. While this prevents sequential scans in some cases, relying on this implicit behavior is an anti-pattern for the following reasons:
+ **You don't control which index is chosen.** PostgreSQL selects the first qualifying index it finds in catalog order, not the most selective or efficient one. If the table has multiple qualifying indexes, the one chosen might have low selectivity, leading to poor lookup performance.
+ **The behavior is fragile.** Adding, dropping, or rebuilding indexes can change which index the apply worker uses, potentially causing unexpected performance regressions in replication.
+ **It masks the underlying problem.** Tables without a primary key or explicit replica identity are inherently risky for logical replication. Relying on implicit index selection defers the problem rather than solving it.

Instead, explicitly configure the replica identity for every replicated table:
+ **Best option:** Add a primary key. This is the most reliable and efficient replica identity.
+ **Alternative:** Use `ALTER TABLE ... REPLICA IDENTITY USING INDEX` to designate a specific unique, non-partial, non-deferrable index with only `NOT NULL` columns. This gives you explicit control over which columns are used for row identification.

Reserve `REPLICA IDENTITY FULL` only for tables where neither option is feasible, and understand that performance depends on factors outside your direct control.

### Monitor replication lag
<a name="PostgreSQL.ReplicaIdentityFull.MonitorLag"></a>

When using `REPLICA IDENTITY FULL`, monitor replication lag closely to detect subscriber apply slowdowns before they become critical.

**On the publisher**, check the lag between the current WAL position and what the subscriber has confirmed:

```
SELECT slot_name, confirmed_flush_lsn, pg_current_wal_lsn(),
       (pg_current_wal_lsn() - confirmed_flush_lsn) AS lag_bytes
FROM pg_replication_slots
WHERE slot_type = 'logical';
```

A steadily growing `lag_bytes` value indicates the subscriber is falling behind. The `pg_stat_replication_slots` view provides additional statistics about each replication slot's usage.

**On the subscriber**, the `pg_stat_subscription` view shows the state of each apply worker, including the last WAL location received and reported:

```
SELECT subname, received_lsn, latest_end_lsn,
       last_msg_send_time, last_msg_receipt_time
FROM pg_stat_subscription;
```

**Note**  
On PostgreSQL 16 and later, you can also select `worker_type` to distinguish between the main apply worker and parallel apply workers.

A large gap between `received_lsn` and `latest_end_lsn`, or stale timestamps in `last_msg_send_time`, can indicate the apply worker is struggling to keep up. The `pg_stat_subscription_stats` view also tracks apply errors and conflicts that might contribute to lag.

**For RDS for PostgreSQL**, you can also monitor the `OldestReplicationSlotLag` CloudWatch metric, which tracks the lag in bytes of the most behind replication slot. A rising value is an early warning sign of replication lag.

**Checking which tables might be using a sub-optimal index during apply**

On the subscriber, you can identify tables where the apply worker is performing excessive heap reads, which can indicate that the table doesn't have an efficient index for row lookups during apply. Run the following query on the subscriber:

```
SELECT relname, heap_blks_read, heap_blks_hit,
       idx_blks_read, idx_blks_hit,
       heap_blks_read + heap_blks_hit AS total_heap_access
FROM pg_statio_user_tables
WHERE heap_blks_read > 0
ORDER BY heap_blks_read DESC
LIMIT 10;
```

A table with a high `heap_blks_read` value relative to `idx_blks_read` can indicate that the apply worker is not using an efficient index to locate rows for `UPDATE` and `DELETE` operations. This is a common source of replication lag when `REPLICA IDENTITY FULL` is in use.

**Note**  
This query requires the [`track_counts`](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-COUNTS) parameter to be enabled on the subscriber. This parameter is on by default.

### Evaluate whether REPLICA IDENTITY FULL is necessary
<a name="PostgreSQL.ReplicaIdentityFull.Evaluate"></a>

Before setting `REPLICA IDENTITY FULL`, consider whether you truly need it. Common reasons for using it include:
+ The table has no primary key or unique index.
+ You need the full before-image of rows for change data capture (CDC) consumers.
+ You need TOASTed column values included in replication events for updates that don't modify those columns.

If your only reason is the lack of a primary key, adding one is almost always the better path. If you need full before-images for CDC, consider whether your CDC consumer can reconstruct full rows by maintaining state externally, which avoids the WAL and subscriber overhead of `REPLICA IDENTITY FULL`.

## Summary of recommendations
<a name="PostgreSQL.ReplicaIdentityFull.Summary"></a>


| Scenario | Recommendation | 
| --- | --- | 
| Table has a primary key | Use the default replica identity (no action needed) | 
| Table has a unique NOT NULL index | Set that index as the replica identity with ALTER TABLE ... REPLICA IDENTITY USING INDEX | 
| Table has no suitable key (PostgreSQL 16\+) | Add a primary key or unique index. Using REPLICA IDENTITY FULL with implicit index selection is unreliable and should be a last resort | 
| Table has no suitable key (before PostgreSQL 16) | Add a primary key or unique index; avoid REPLICA IDENTITY FULL if possible | 
| Write-heavy workload with large/TOASTed columns | Avoid REPLICA IDENTITY FULL due to WAL volume amplification | 
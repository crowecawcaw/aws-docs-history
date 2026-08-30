# Troubleshooting binary log replication lag for Aurora MySQL

This section provides guidance on binary log replication lag for Aurora MySQL configured as a binary log
replica. It covers replication architecture, parallel replication, dependency tracking, monitoring, and
configuration best practices.

Binary log replication replicates data between MySQL-compatible databases. The binary log replication covered
in this section is asynchronous: the source does not wait for replicas to confirm application of changes before
committing transactions. This does not apply to semi-synchronous replication. In semi-synchronous replication,
the source waits for at least one replica to acknowledge receipt of the transaction before committing. For
example, Multi-AZ DB clusters for Amazon RDS for MySQL use semi-synchronous replication, which is out of scope for
this section. The replica
maintains a persistent connection to the source via the I/O thread to continuously stream binary log events.
This section applies to all binlog replication topologies where Aurora MySQL is the replica. The source can be
another Aurora MySQL cluster, Amazon RDS for MySQL, on-premises MySQL, or MySQL on Amazon EC2. This section also
applies when Aurora MySQL is the source replicating to any MySQL-compatible target.

###### Note

For cross-region replication use cases, consider using [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md") as an alternative to binary log-based replication. Aurora Global Database
uses dedicated infrastructure for replication, providing lower latency and requiring less operational management
than binary log replication across regions.

**Experiencing a lag spike right now?** Skip the background material and start
with [Identifying the replication lag bottleneck](#aurora-mysql-replication-lag-identifying "#aurora-mysql-replication-lag-identifying") to determine whether the I/O thread or the
SQL thread is the bottleneck, then follow the link for that scenario:
[Troubleshooting I/O thread lag](#aurora-mysql-replication-lag-io-thread "#aurora-mysql-replication-lag-io-thread") or
[Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread").

###### Topics

- [MySQL replication architecture](#aurora-mysql-binlog-replication-lag-overview "#aurora-mysql-binlog-replication-lag-overview")
- [Identifying the replication lag bottleneck](#aurora-mysql-replication-lag-identifying "#aurora-mysql-replication-lag-identifying")
- [Troubleshooting I/O thread lag](#aurora-mysql-replication-lag-io-thread "#aurora-mysql-replication-lag-io-thread")
- [Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread")
- [Multi-threaded replication (MTR)](#aurora-mysql-replication-lag-mtr "#aurora-mysql-replication-lag-mtr")
- [Aurora-specific replication optimizations](#aurora-mysql-replication-lag-aurora-optimizations "#aurora-mysql-replication-lag-aurora-optimizations")
- [Monitoring parallel replication](#aurora-mysql-replication-lag-monitoring "#aurora-mysql-replication-lag-monitoring")
- [Best practices for minimizing replication lag](#aurora-mysql-replication-lag-best-practices "#aurora-mysql-replication-lag-best-practices")

## MySQL replication architecture

MySQL replication is implemented through specialized threads:

- **Binary log dump thread (source)** – Created when a replica connects.
  Sends binary log contents to the replica. Visible in `SHOW PROCESSLIST` as the "Binlog Dump" thread.
- **Replication I/O thread (replica)** – Connects to the source and requests
  binary log updates. Writes them to the replica's relay log. Always a single thread per replication channel
  regardless of multi-threaded replication (MTR) configuration.
- **Replication SQL thread (replica)** – Reads relay log and applies
  transactions. The applier always consists of one coordinator thread that reads transactions from the
  relay log, plus N worker threads that apply them, where N is the value of
  `replica_parallel_workers`. With `replica_parallel_workers=1`, the single worker
  applies transactions sequentially. With `replica_parallel_workers >= 2`, the coordinator
  assigns independent transactions to multiple worker threads for parallel apply.

###### Note

Setting `replica_parallel_workers=0` is deprecated as of MySQL 8.0.30 and is subject to
removal in a future MySQL release. Use `replica_parallel_workers=1` for single-threaded
apply instead.

The replication process works as follows:

1. The source executes DML, DCL, or DDL statements.
2. On commit, the source writes the data to the binary log.
3. The I/O thread on the replica fetches events and writes them to the relay log.
4. The SQL thread applies changes from the relay log (single-threaded or multi-threaded).

## Identifying the replication lag bottleneck

Replication lag can occur in two areas: the I/O thread or the SQL thread. The first step is to determine which
component is lagging.

###### Note

The `Seconds_Behind_Source` field in `SHOW REPLICA STATUS` measures the delay
between when an event was logged on the source and when the SQL thread applies it. This metric does not
indicate I/O thread lag specifically. To identify I/O thread lag, you must compare binary log positions
as described in the following steps.

###### Note

Some MySQL commands and internal strings shown in this section, such as `SHOW MASTER STATUS`,
use legacy terminology. This documentation uses the preferred terms "source" and "replica" throughout.

###### To determine which replication thread is lagging

1. On the replica, run `SHOW REPLICA STATUS` and compare
   `Source_Log_File` / `Read_Source_Log_Pos` (I/O thread position) with `File` /
   `Position` from `SHOW MASTER STATUS` on the source. If these differ significantly
   (>50 MB or >1 binlog file apart), the I/O thread is lagging.
2. Compare the I/O thread position with the SQL thread position
   (`Relay_Source_Log_File` / `Exec_Source_Log_Pos`). If the I/O thread is caught up but the
   SQL thread is behind (>50 MB apart), the SQL thread is the bottleneck.

###### Quick initial assessment using replica-only data

You can perform an initial assessment using only replica-side data. Run `SHOW REPLICA STATUS`
twice, 1–2 minutes apart, and observe the following:

- If `Read_Source_Log_Pos` is advancing but `Exec_Source_Log_Pos` is
  stalled or advancing much more slowly, the SQL thread is the bottleneck (Scenario B). Proceed to
  [Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread").
- If both `Read_Source_Log_Pos` and `Exec_Source_Log_Pos` are stalled
  while `Seconds_Behind_Source` is growing, the I/O thread is likely behind.
  Before making configuration changes, confirm by comparing the replica positions against the source
  using `SHOW MASTER STATUS` as described in step 1 of the preceding procedure.

| Scenario | I/O thread vs Source | SQL thread vs I/O thread | Bottleneck            |
| -------- | -------------------- | ------------------------ | --------------------- |
| A        | Far behind (>50 MB)  | Close (<10 MB)           | I/O thread            |
| B        | Close (<10 MB)       | Far behind (>50 MB)      | SQL thread            |
| C        | Far behind           | Far behind               | Both (start with I/O) |

###### Example Interpreting binary log positions

The following example shows how to compare binary log positions to determine the bottleneck.

On the replica, `SHOW REPLICA STATUS` returns:

```
Source_Log_File:       mysql-bin.000045
Read_Source_Log_Pos:   524288000
Relay_Source_Log_File: mysql-bin.000045
Exec_Source_Log_Pos:   524200000
```

On the source, `SHOW MASTER STATUS` returns:

```
File:     mysql-bin.000045
Position: 1073741824
```

To determine the I/O thread lag, subtract the I/O thread position from the source position:

(1073741824 − 524288000) / 1048576 = **524 MB** – The I/O thread is
far behind the source (Scenario A).

To determine the SQL thread lag, subtract the SQL thread position from the I/O thread position:

(524288000 − 524200000) / 1048576 = **0.08 MB** – The SQL thread is
keeping up with the I/O thread.

In this case, focus troubleshooting on the I/O thread. For more information, see
[Troubleshooting I/O thread lag](#aurora-mysql-replication-lag-io-thread "#aurora-mysql-replication-lag-io-thread").

###### Anatomy of a replication lag spike

A common pattern is a sudden spike in `Seconds_Behind_Source` followed by a rapid return to near-zero.
This occurs when a long-running DML on the source (such as an UPDATE scanning millions of rows but modifying only a few)
takes minutes to execute. With ROW-based binary logging, only the modified rows are written to the binary log.
When the SQL thread picks up this event, it calculates lag based on the transaction's start time on the source.
This produces a large initial value. However, because only a few rows need to be applied, the replica catches up quickly.
This is expected behavior and does not indicate a sustained replication problem.

## Troubleshooting I/O thread lag

The I/O thread is responsible for fetching binary log events from the source and writing them to the relay log.
Common causes and resolutions:

| Cause                                         | How to identify                                                                              | Resolution                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network bandwidth limitations                 | Check CloudWatch `NetworkReceiveThroughput` / `NetworkTransmitThroughput`                    | Use instances with higher network capacity; ensure similar instance classes on source and replica                                                                                                                                                                                                                                                                     |
| Network latency (cross-region or on-premises) | Geographic distance between source and replica; high round-trip time                         | For on-premises sources, use for dedicated, low-latency connectivity                                                                                                                                                                                                                                                                                                  |
| Resource constraints on source                | High CPU (`CPUUtilization`), memory pressure (`FreeableMemory`)                              | Scale up source instance. Each connected replica creates a binlog dump thread on the source –<br>reduce the number of connected replicas if the source is resource-constrained.                                                                                                                                                                                       |
| Large transactions with BLOB/TEXT data        | Monitor binary log event sizes via `SumBinaryLogSize` CloudWatch metric                      | Set `binlog_row_image=noblob`; enable binary log transaction compression<br>(`binlog_transaction_compression=ON`). Test in non-production first – compression<br>increases CPU utilization on both source and replica.                                                                                                                                                |
| Relay log space limit reached                 | `Replica_IO_State` shows "Waiting for the replica SQL thread to free enough relay log space" | This indicates the SQL thread is the root cause, not the I/O thread. Address SQL thread lag first.<br>In Aurora MySQL, the default `relay_log_space_limit` is approximately 953 MiB. This message<br>is part of normal operation when the SQL thread cannot apply changes fast enough. This message<br>does not necessarily indicate an I/O thread performance issue. |

### Optimization strategies for I/O thread lag

1. **Use at least the same instance class as the source** –
   This approach provides sufficient CPU, memory, I/O capacity, and network bandwidth.
2. **Ensure sufficient network bandwidth** –
   Use instances with high network capacity. For on-premises sources, consider for dedicated bandwidth
   and a more consistent network experience.
3. **Check source-side resources, especially with many replicas** –
   Monitor the source's CPU, memory, network, and binlog I/O. Each connected replica adds a binlog dump
   thread on the source, so a source serving many replicas can itself become the bottleneck.
   We recommend confirming the source is not saturated before scaling up the replica. If the source
   is resource-constrained, consider reducing the number of connected replicas.
4. **Verify the Aurora binlog I/O cache is active** –
   The binlog I/O cache reduces disk I/O on the source for serving binary log events. It is enabled
   automatically in Aurora MySQL version 2.10 and higher – no configuration is required. If the
   source is an Aurora cluster, verify the cache is being used with
   `SHOW GLOBAL STATUS LIKE 'aurora_binlog_io_cache%'`.
   For more information, see [Optimizing binlog replication](binlog-optimization.md#binlog-optimization-binlog-io-cache "binlog-optimization.md#binlog-optimization-binlog-io-cache").
5. **Enable binary log transaction compression** –
   Set `binlog_transaction_compression=ON` in the parameter group. Reduces bandwidth requirements.
   This setting has the following considerations:

   - Compression increases CPU utilization on both source and replica.
   - Test in a non-production environment first to find the optimal balance between
     compression and resource utilization.
   - Optionally, adjust the compression level using
     `binlog_transaction_compression_level_zstd` (default: 3, range: 1–22).

6. **Minimize writes to binary logs** –
   Set `binlog_row_image=noblob` to eliminate BLOB/TEXT data from binary logs.
   Do not use if the replica has triggers that reference BLOB columns. For more information, see
   [binlog\_row\_image](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_image "https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_image") on the MySQL website.
7. **Implement replication filters on the source** –
   Use `binlog-do-db` or `binlog-ignore-db` to exclude unnecessary databases.
   These are static parameters requiring a reboot.

###### Important

Source-side filters affect what is written to binary logs entirely. Excluded databases are not
replicated to any downstream replica. If the source is a self-managed MySQL instance (on-premises
or on Amazon EC2), excluded databases are also not available for binary log-based point-in-time
recovery. Amazon RDS for MySQL does not support source-side binlog filtering
(`binlog-do-db`/`binlog-ignore-db` are not configurable); use replica-side
replication filters instead. Aurora uses the cluster volume for PITR and is not affected by binary
log filters for backup purposes.

## Troubleshooting SQL thread lag

The SQL thread is the bottleneck when the I/O thread is caught up with the source but
`Seconds_Behind_Source` is growing. To quantify the lag, monitor over a 15-minute window.
Compare the binlog generation rate on the source (the `Position` delta from
`SHOW MASTER STATUS`) with the SQL thread apply rate on the replica (the
`Exec_Source_Log_Pos` delta).

Common causes and resolutions:

| Cause                                         | How to identify                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single-threaded replication                   | `SELECT @@global.replica_parallel_workers;` returns 0 or 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Enable multi-threaded replication (MTR) with WRITESET dependency tracking. MTR alone does not<br>resolve lag if clock conflicts are high. See<br>[Dependency tracking on the source](#aurora-mysql-replication-lag-mtr-dependency "#aurora-mysql-replication-lag-mtr-dependency") for tuning dependency tracking and<br>[Error log multi-threaded replica statistics](#aurora-mysql-replication-lag-monitoring-error-log "#aurora-mysql-replication-lag-monitoring-error-log") for identifying clock conflicts.                                                                                |
| Lack of primary keys                          | Without a primary key (or unique key with NOT NULL), the replica performs a full table scan for each<br>modified row in UPDATE and DELETE operations. Use the following query to identify tables without primary keys:<br>`<br>SELECT t.table_schema, t.table_name<br>FROM information_schema.tables t<br>LEFT JOIN information_schema.table_constraints tc<br>ON t.table_schema = tc.table_schema<br>AND t.table_name = tc.table_name<br>AND tc.constraint_type = 'PRIMARY KEY'<br>WHERE tc.constraint_type IS NULL<br>AND t.table_type = 'BASE TABLE'<br>AND t.table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')<br>ORDER BY 1;<br>`                                                                                                                | Add primary keys to all replicated tables. If adding explicit primary keys is not immediately<br>feasible, consider enabling Generated Invisible Primary Keys (GIPK) by setting the<br>`sql_generate_invisible_primary_key` parameter to `ON` (available in Aurora<br>MySQL 3 versions based on MySQL 8.0.30 and later).<br>For more information about Generated Invisible Primary Keys, see<br>[Generated Invisible<br>Primary Keys](https://dev.mysql.com/doc/refman/8.0/en/create-table-gipks.html "https://dev.mysql.com/doc/refman/8.0/en/create-table-gipks.html") on the MySQL website. |
| Large write transactions on source            | A transaction that modifies many rows (for example, a bulk UPDATE or DELETE) replicates<br>as a single unit that only one worker thread can apply, regardless of MTR configuration.<br>On the source, identify active long-running write transactions with:<br>`<br>SELECT trx_id, trx_started, trx_rows_modified, trx_query<br>FROM information_schema.innodb_trx<br>WHERE trx_rows_modified > 10000<br>ORDER BY trx_started;<br>`<br>On the replica, one worker stays busy on the same statement in `SHOW PROCESSLIST`<br>while the others sit idle. Long-running idle transactions or transactions waiting on locks<br>on the source do not by themselves cause replication lag – only the committed write<br>volume matters, because events reach the binary log at commit time. | Break bulk operations into smaller transactions (for example, a few thousand rows per<br>commit) so the replica can apply them in parallel. For a worked example, see<br>[Example 4: A single large transaction cannot be parallelized](#aurora-mysql-replication-lag-monitoring-example4 "#aurora-mysql-replication-lag-monitoring-example4").                                                                                                                                                                                                                                                |
| DDL operations                                | DDL blocks other replication events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use an online schema change tool, or use Blue/Green deployments. Schedule DDL during<br>low-traffic periods. For `pt-online-schema-change`, see<br>[Percona Toolkit](https://docs.percona.com/percona-toolkit/ "https://docs.percona.com/percona-toolkit/") on the Percona website.<br>For `gh-ost`, see<br>[gh-ost](https://github.com/github/gh-ost "https://github.com/github/gh-ost") on the GitHub website.                                                                                                                                                                               |
| Suboptimal parallel replication configuration | Low worker utilization; high clock conflicts in coordinator stats. Check the<br>"Waited at clock conflicts" field in the multi-threaded replica statistics error log entry<br>(see [Error log multi-threaded replica statistics](#aurora-mysql-replication-lag-monitoring-error-log "#aurora-mysql-replication-lag-monitoring-error-log")). High values<br>relative to "seconds elapsed" indicate transactions are frequently blocked by dependencies.                                                                                                                                                                                                                                                                                                                               | Tune dependency tracking (WRITESET) and worker count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Resource contention from analytical workloads | Complex OLAP queries competing with SQL thread for resources (CPU, memory)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Separate analytical workloads to dedicated replicas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Outdated table statistics                     | Suboptimal query plans on replica. Use the following query to identify tables with stale statistics (older than 7 days):<br>`<br>SELECT database_name, table_name,<br>MIN(last_update) AS oldest_stat_update,<br>DATEDIFF(NOW(), MIN(last_update)) AS stats_age_in_days<br>FROM mysql.innodb_index_stats<br>WHERE database_name NOT IN ('mysql', 'sys')<br>GROUP BY database_name, table_name<br>HAVING stats_age_in_days > 7<br>ORDER BY stats_age_in_days DESC;<br>`                                                                                                                                                                                                                                                                                                               | Run `ANALYZE TABLE` periodically on tables with stale statistics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Reduce apply workload with replica-side replication filters

Aurora MySQL version 3.01.0 and higher supports replica-side replication filters. Use these to skip
irrelevant databases or tables during apply, reducing SQL thread workload. Replica-side filters are applied
by the SQL thread – the I/O thread still fetches all binary log events from the source, so these
filters reduce apply work only, not network transfer. Unlike source-side filters (which operate at the
database level only), replica-side filters support table-level granularity using
`replicate-do-table` and `replicate-ignore-table`. For more information, see
[Configuring replication filters with Aurora MySQL](AuroraMySQL.Replication.Filters.md "AuroraMySQL.Replication.Filters.md").

## Multi-threaded replication (MTR)

With MTR, the replica applies independent transactions in parallel. It cannot split a single large
transaction into parallel parts. The degree of parallelism is limited by the dependency information written by the source.

When MTR is enabled (`replica_parallel_workers >= 2`), the SQL applier is split into a
**coordinator thread** and multiple **worker threads**.
The coordinator reads transactions from the relay log. It examines the logical timestamps
(`last_committed` and `sequence_number`) that the source embeds in each transaction.
It then assigns independent transactions to available worker threads for parallel execution. Two transactions
are independent if they do not share data dependencies – that is, if they modify different rows.
The source determines these dependencies at commit time using the configured dependency tracking method and
records them in the binary log. The replica cannot increase parallelism beyond what the source permits.

### MTR is the recommended default

We recommend running replicas with MTR enabled. MTR is enabled by default
(`replica_parallel_workers=4`) in MySQL 8.0.27 and higher, including the Aurora MySQL 3 versions
based on those releases. On earlier versions (Aurora MySQL 2.12.1 and higher, or versions based on MySQL
releases before 8.0.27), enable it explicitly by setting `replica_parallel_workers` to a value
of 2 or more. Keeping MTR enabled costs little when parallelism is unavailable and lets the replica take
advantage of it whenever the workload allows.

MTR does not reduce lag in the following cases:

- The bottleneck is the I/O thread (network/bandwidth issue).
- Lag is caused by a single long-running transaction.
- The replica is CPU-saturated (more threads makes it worse).
- Tables lack primary keys (forces full table scans, negating parallelism).

### Dependency tracking on the source

The source determines which transactions can be applied in parallel using the
`binlog_transaction_dependency_tracking` parameter. Recommended value: `WRITESET`.

- **COMMIT\_ORDER** – Tracks dependencies based on commit timing.
  Works best with high concurrency and large group commits. Limited parallelism in low-concurrency environments.
- **WRITESET (recommended)** – Tracks actual row-level data dependencies.
  Performance is always at least as good as COMMIT\_ORDER. Significantly better with low-concurrency workloads.
  Requires tables to have primary keys.

WRITESET dependency tracking produces empty or partial writesets (limiting parallelism) in the following cases:

    + Tables without primary or unique keys
    + DDL statements (CREATE TABLE, ALTER TABLE, and so on)
    + Transactions that modify parent tables in foreign key relationships

Additionally, the dependency history is cleared when the binary log rotates or when the
`binlog_transaction_dependency_history_size` limit is reached, temporarily reducing parallelism.

- **WRITESET\_SESSION** – Same as WRITESET with an additional constraint
  that transactions from the same session cannot be parallelized.

###### Note

MySQL 8.4 has removed `binlog_transaction_dependency_tracking` and defaults to WRITESET (not configurable).
Earlier versions default to COMMIT\_ORDER.

### Parallel type (`replica_parallel_type`)

The `replica_parallel_type` parameter determines how transactions are distributed among worker threads.
There are two options:

- **LOGICAL\_CLOCK (recommended)** – Uses logical timestamps to determine which
  transactions can be executed in parallel, even within the same database. This approach results in higher
  replication throughput and lower latency for most workloads. Use it unless you have a specific
  multi-database workload that does not benefit from it.
- **DATABASE** – Assigns transactions to worker threads based on the database
  they affect. Consider it only when your application uses multiple databases with clearly separated
  workloads and transactions rarely cross database boundaries. When using DATABASE, the
  `binlog_transaction_dependency_tracking` setting on the source is not used – parallelism
  is determined solely by which database a transaction targets.

###### Note

In MySQL versions 8.0.26 and earlier, `replica_parallel_type` defaults to `DATABASE`.
From MySQL 8.0.27 onwards, it defaults to `LOGICAL_CLOCK`. If you are using an older version,
explicitly set this parameter to `LOGICAL_CLOCK` to take advantage of finer-grained dependency tracking.

### MTR configuration

Source-side parameters| Parameter | Recommended value | Notes |
| --- | --- | --- |
| `binlog_transaction_dependency_tracking` | WRITESET | Cluster parameter group. Dynamic. Not needed for MySQL 8.4. |
| `binlog_transaction_dependency_history_size` | 25000 (default) | Cluster parameter group. Dynamic. Controls how many row hashes the source keeps for<br>WRITESET dependency tracking; when the history fills up or the binary log rotates, it is<br>cleared and parallelism temporarily drops. Consider doubling the value (for example, to<br>50000) on write-heavy sources if the replica shows periodic spikes in the "waited at clock<br>conflicts" error log statistic (see<br>[Error log multi-threaded replica statistics](#aurora-mysql-replication-lag-monitoring-error-log "#aurora-mysql-replication-lag-monitoring-error-log")) that align with binary<br>log rotation. Larger values consume more memory on the source. |
| `binlog_format` | ROW | Cluster parameter group. Static (requires reboot). |
| `binlog_group_commit_sync_delay` | 0 (default) | Microseconds to delay group commit. Increasing this value groups more transactions together,<br>improving parallelism on the replica at the cost of slight commit latency increase on the source.<br>Only beneficial when using COMMIT\_ORDER dependency tracking – WRITESET already tracks<br>actual row-level dependencies regardless of commit timing. Dynamic. |
| `binlog_group_commit_sync_no_delay_count` | 0 (default) | Maximum number of transactions to wait for before committing. Use with<br>`binlog_group_commit_sync_delay` to cap the delay once enough transactions<br>are batched. Only relevant for COMMIT\_ORDER dependency tracking. Dynamic. |

Replica-side parameters| Parameter | Recommended value | Notes |
| --- | --- | --- |
| `replica_parallel_workers` | Start at the vCPU count, up to twice the vCPU count | Instance parameter group. Dynamic but requires replication restart. The community default<br>is 4 as of MySQL 8.0.27 (and Aurora MySQL 3 versions based on it); earlier versions default to<br>0, which is deprecated as of MySQL 8.0.30. We recommend<br>starting at the vCPU count, then monitoring CPU utilization and the<br>"Waited (count) when Workers occupied" error log statistic (see<br>[Error log multi-threaded replica statistics](#aurora-mysql-replication-lag-monitoring-error-log "#aurora-mysql-replication-lag-monitoring-error-log")).<br>Increase only when "Waited (count) when Workers occupied" is consistently high and CPU<br>utilization remains below 80%. |
| `replica_parallel_type` | LOGICAL\_CLOCK | Cluster parameter group. Dynamic but requires replication restart. |
| `replica_pending_jobs_size_max` | >= `max_allowed_packet` on source | Instance parameter group. Dynamic. |
| `replica_preserve_commit_order` | ON | Cluster parameter group. Dynamic but requires replication restart. |
| `binlog_format` | OFF | Cluster parameter group. Static. Aurora-specific extension to disable binary logging. |

After changing parallel worker settings, restart replication:

```
CALL mysql.rds_stop_replication;
CALL mysql.rds_start_replication;
```

## Aurora-specific replication optimizations

Aurora MySQL provides the following features to improve binary log replication performance. The following table
summarizes the availability, default state, and how to enable each feature.

| Feature                              | Version                    | Default                                                     | How to enable / verify                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | -------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **In-memory relay log**              | Aurora MySQL 3.10+         | ON (for Aurora-managed replication when conditions are met) | Automatically enabled for Aurora-managed replication (blue/green deployments,<br>Aurora-to-Aurora, and cross-region replicas) when the replica uses single-threaded replication<br>(`replica_parallel_workers=0`), multi-threaded replication with GTID mode and<br>auto-positioning enabled, or file-based replication with<br>`replica_preserve_commit_order=ON`. Controlled by the dynamic<br>`aurora_in_memory_relaylog` parameter (DB cluster or instance level): stop replication,<br>set it to `ON` or `OFF` in the parameter group, then restart replication<br>– no instance reboot required. Not available on Aurora Serverless. Verify the current status<br>with `SHOW GLOBAL STATUS LIKE 'Aurora_in_memory_relaylog_status'`. For more<br>information, see [In-memory relay log](binlog-optimization.md#binlog-optimization-in-memory-relay-log "binlog-optimization.md#binlog-optimization-in-memory-relay-log"). |
| **Parallel secondary index changes** | Aurora MySQL 3.06+         | OFF (`0`)                                                   | Set `aurora_binlog_replication_sec_index_parallel_workers` to the desired<br>thread count. Stop replication, set the parameter, then start replication. No instance<br>restart required. For more information, see<br>[Multithreaded binary log replication](binlog-optimization.md#binlog-optimization-multithreading "binlog-optimization.md#binlog-optimization-multithreading").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Binlog I/O cache**                 | Aurora MySQL 2.10+ and 3.x | ON (automatic)                                              | Automatically enabled. Reduces disk I/O on the source when serving binary log events<br>to replicas. No configuration needed. For more information, see<br>[Optimizing binlog replication](binlog-optimization.md#binlog-optimization-binlog-io-cache "binlog-optimization.md#binlog-optimization-binlog-io-cache").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Monitoring parallel replication

Use the following methods to monitor replication performance and identify bottlenecks in parallel apply:

### Performance Schema

Key tables for monitoring MTR:

- `performance_schema.replication_applier_status_by_worker` – Shows details of
  transactions handled by each worker thread, including apply timestamps and errors.
- `performance_schema.replication_applier_status_by_coordinator` – Shows information
  about the coordinator thread's buffering activity.

To evaluate how evenly work is distributed across worker threads, use the following query:

```
SELECT
  a.channel_name,
  rw1.thread_id AS replica_worker_thread_id,
  ts1.count_star AS number_of_trx_executed,
  ROUND((ts1.count_star / sum_count_star) * 100, 2) AS percent_of_trx_executed_by_worker
FROM (
  SELECT rw.channel_name, SUM(ts.count_star) AS sum_count_star
  FROM performance_schema.events_transactions_summary_by_thread_by_event_name AS ts
    JOIN performance_schema.replication_applier_status_by_worker AS rw
      ON ts.thread_id = rw.thread_id
  GROUP BY rw.channel_name
) AS a
JOIN performance_schema.replication_applier_status_by_worker AS rw1
  ON a.channel_name = rw1.channel_name
JOIN performance_schema.events_transactions_summary_by_thread_by_event_name AS ts1
  ON rw1.thread_id = ts1.thread_id;
```

If one or two workers handle the majority of transactions, it indicates high transaction dependencies
limiting parallelism. Consider switching to WRITESET dependency tracking on the source.

If the I/O thread and SQL thread positions are close to each other but `Seconds_Behind_Source` is
still growing, the coordinator thread itself might be the bottleneck. Check
`performance_schema.replication_applier_status_by_coordinator` for buffering delays. A coordinator
bottleneck typically indicates heavy transaction dependencies or an overloaded single coordinator thread that
cannot distribute events fast enough.

### Error log multi-threaded replica statistics

When `log_error_verbosity=3` (the default), Aurora MySQL writes multi-threaded replica statistics
to the MySQL error log periodically. You can view these entries by:

- In the RDS console, in the **Logs & events** section, view the error log.
- Downloading via AWS CLI: `aws rds download-db-log-file-portion --db-instance-identifier <instance-id> --log-file-name error/mysql-error-running.log`
- If CloudWatch Logs export is enabled for the error log, searching in the exported log group.

To locate the multi-threaded replica statistics entries in the error log, search for the string shown in
the following example. The MySQL error log uses legacy terminology in this internal string; this
documentation uses the preferred term "replica" throughout.

The following is an example error log entry:

```
2026-05-10 14:54:28.045308 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 120; events assigned = 7215200; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 1203644200 waited (count) when Workers occupied = 1022462 waited when Workers occupied = 62349203500
```

Key fields to analyze:

| Field                                   | Description                                                                                                                                                                                                          | Action                                                                                                                                                                                                                               |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| seconds elapsed                         | Time in seconds since the last statistics output. Aurora MySQL does not write statistics at regular intervals –<br>it writes them based on the number of events executed plus time elapsed.                          | Use to calculate throughput: events assigned / seconds elapsed = average events per interval.                                                                                                                                        |
| events assigned                         | Number of events assigned by the coordinator thread to worker threads since the last output.                                                                                                                         | Monitor for changes in replication throughput over time.                                                                                                                                                                             |
| Worker queues filled over overrun level | Number of events queued to worker threads in excess of the overrun level (90% of maximum queue length of 16384 events).<br>If zero, no workers are operating at upper capacity.                                      | Indicates workers cannot keep up with the coordinator. Check for long-running transactions or missing indexes.                                                                                                                       |
| Waited due a Worker queue full          | Number of times the coordinator had to wait because a worker thread's queue was full (reached 100% capacity).                                                                                                        | Check for long-running transactions, missing indexes, or lock contention on worker threads.                                                                                                                                          |
| Waited due the total size               | Number of times the coordinator waited because the `replica_pending_jobs_size_max` limit was reached.<br>If an unusually large event exceeds this size, the transaction is held until all workers have empty queues. | Increase `replica_pending_jobs_size_max`. Check for large transactions on the source.                                                                                                                                                |
| Waited at clock conflicts               | Number of nanoseconds the coordinator waited because a transaction depended on another transaction that<br>had not yet been committed. This quantifies the time events could not be assigned due to dependencies.    | Switch to WRITESET dependency tracking on the source. Ensure tables have primary keys.<br>Some clock conflict waiting is expected – focus on reducing the ratio relative to other waits.                                             |
| Waited (count) when Workers occupied    | Number of times the coordinator needed to assign the first event of a transaction but all worker queues were<br>non-empty. The coordinator sleeps until a queue becomes empty.                                       | This indicates `replica_parallel_workers` is underprovisioned. Dependencies are not the<br>bottleneck – you could have executed more events in parallel but lacked available worker threads.<br>Increase `replica_parallel_workers`. |
| Waited when Workers occupied            | Total nanoseconds the coordinator slept while waiting for an empty worker queue.                                                                                                                                     | High values confirm worker capacity is the bottleneck. Increase `replica_parallel_workers`.                                                                                                                                          |

### Worked examples: diagnosing parallel apply bottlenecks

The following examples show how to use the preceding monitoring sources to diagnose common parallel
apply bottlenecks. Each example starts from the same symptom – `Seconds_Behind_Source`
is steadily growing and you have already confirmed the SQL thread is the bottleneck (see
[Identifying the replication lag bottleneck](#aurora-mysql-replication-lag-identifying "#aurora-mysql-replication-lag-identifying")) – and uses the multi-threaded
replica statistics and Performance Schema to determine the corrective action.

#### Example 1: Workers are underprovisioned

In CloudWatch, the `ReplicaLag` metric climbs steadily from near zero to approximately
400 seconds over 30 minutes. CPU utilization on the replica stays around 55%, so the replica is not
CPU-bound.

To confirm where the lag is, run `SHOW REPLICA STATUS` twice, 60 seconds apart.
`Read_Source_Log_Pos` advances by approximately 1.2 GB while `Exec_Source_Log_Pos`
advances by only approximately 300 MB. The I/O thread is keeping up with the source, but the SQL thread
is falling behind – the SQL thread is the bottleneck.

MTR is enabled with `replica_parallel_workers=4`. Retrieve the most recent multi-threaded
replica statistics from the error log (see
[Error log multi-threaded replica statistics](#aurora-mysql-replication-lag-monitoring-error-log "#aurora-mysql-replication-lag-monitoring-error-log")):

```
2026-05-10 14:54:28.045308 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 123; events assigned = 9876544; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 8455000 waited (count) when Workers occupied = 2456789 waited when Workers occupied = 110293847000
```

Interpret the key fields:

- **waited when Workers occupied = 110293847000** nanoseconds,
  or approximately 110 seconds. Out of the 123 seconds in this interval, the coordinator spent roughly
  90% of its time waiting for a worker thread to become free.
- **waited at clock conflicts = 8455000** nanoseconds, or
  approximately 0.008 seconds, which is negligible. Transaction dependencies are not the limiting
  factor.

**Diagnosis:** the coordinator consistently has more independent
transactions ready to apply than it has workers to run them. Because clock-conflict waiting is
negligible, parallelism is limited by worker count, not by dependencies.

**Action:** increase `replica_parallel_workers` to the
replica's vCPU count (for example, 16 on a `db.r6g.4xlarge`) and restart replication:

```
CALL mysql.rds_stop_replication;
CALL mysql.rds_start_replication;
```

**Verification:** a later statistics line shows the wait has nearly
disappeared, and `ReplicaLag` returns to under 5 seconds:

```
2026-05-10 15:02:14.882201 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 120; events assigned = 31840552; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 9120000 waited (count) when Workers occupied = 41233 waited when Workers occupied = 5980411000
```

"waited when Workers occupied" dropped from approximately 110 seconds to approximately 6 seconds, and
throughput (events assigned) more than tripled. Stop increasing workers once CPU utilization approaches
80% or the wait stops decreasing.

#### Example 2: COMMIT\_ORDER dependency tracking serializes a low-concurrency workload

The source is an Amazon RDS for MySQL instance running an OLTP workload with only 4–8 concurrently
committing application threads. The replica is a `db.r6g.4xlarge` with
`replica_parallel_workers=16` and `replica_parallel_type=LOGICAL_CLOCK`. Despite
16 workers, `ReplicaLag` holds steady around 600 seconds and replica CPU utilization is only
about 20% – the workers look idle.

First, check how evenly transactions are distributed across workers using the worker-distribution
query from [Performance Schema](#aurora-mysql-replication-lag-monitoring-perf-schema "#aurora-mysql-replication-lag-monitoring-perf-schema"):

```
+--------------+--------------------------+------------------------+-----------------------------------+
| channel_name | replica_worker_thread_id | number_of_trx_executed | percent_of_trx_executed_by_worker |
+--------------+--------------------------+------------------------+-----------------------------------+
|              |                       45 |                1903556 |                             96.41 |
|              |                       46 |                  23104 |                              1.17 |
|              |                       47 |                  18995 |                              0.96 |
|              |                       48 |                  16720 |                              0.85 |
.
.
+--------------+--------------------------+------------------------+-----------------------------------+
```

The preceding output shows the first 4 of the 16 worker threads. One worker is applying over 96% of
transactions while the other 15 are nearly idle (each of the remaining workers executed less than 0.05%).
Apply is effectively serial.

Next, confirm this with the multi-threaded replica statistics in the error log:

```
2026-05-10 15:22:11.110432 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 120; events assigned = 2014500; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 98712340000 waited (count) when Workers occupied = 50122 waited when Workers occupied = 1209847000
```

- **waited at clock conflicts = 98712340000** nanoseconds, or
  approximately 99 of the 120 seconds. The coordinator spent about 82% of the interval unable to
  dispatch the next transaction because it depended on one still being applied.
- **waited when Workers occupied = 1209847000** nanoseconds, or
  approximately 1.2 seconds. Workers were almost always free, so more workers do not
  help.

This points to a dependency problem, not a capacity problem. Check the dependency tracking method on
the **source**:

```
SELECT @@global.binlog_transaction_dependency_tracking;
```

```
+-------------------------------------------------+
| @@global.binlog_transaction_dependency_tracking |
+-------------------------------------------------+
| COMMIT_ORDER                                    |
+-------------------------------------------------+
```

**Root cause:** with `COMMIT_ORDER`, the source decides which
transactions can run in parallel based on which transactions committed together in the same binary log
group commit. In this low-concurrency workload only a handful of threads commit at a time, so group
commits are tiny. As a result, the source stamps nearly every transaction with a
`last_committed` value equal to the previous transaction's `sequence_number`,
marking it as dependent on the one before it. The replica must then apply them one after another –
even though they modify completely unrelated rows – which is why 15 of the 16 workers sit
idle.

**Action:** switch the source to row-level dependency tracking, which is
independent of commit timing. Set it dynamically and persist it in the cluster (or DB) parameter
group:

```
SET GLOBAL binlog_transaction_dependency_tracking = WRITESET;
```

`WRITESET` computes a hash of the rows each transaction modifies, so transactions touching
different rows receive independent timestamps and can be applied in parallel regardless of when they
committed. Ensure all tables have primary keys, because WRITESET produces empty writesets for tables
without them (see [Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread")). On MySQL 8.4, WRITESET is the default
and this parameter no longer exists.

**Verification:** after the change, the worker-distribution query shows
work spread evenly across all workers (showing the first 4 of 16; each worker now handles roughly 6% of
transactions):

```
+--------------+--------------------------+------------------------+-----------------------------------+
| channel_name | replica_worker_thread_id | number_of_trx_executed | percent_of_trx_executed_by_worker |
+--------------+--------------------------+------------------------+-----------------------------------+
|              |                       45 |                 132540 |                              6.30 |
|              |                       46 |                 125610 |                              5.97 |
|              |                       47 |                 129774 |                              6.17 |
|              |                       48 |                 122901 |                              5.84 |
.
.
+--------------+--------------------------+------------------------+-----------------------------------+
```

and the error-log statistics show clock conflicts collapsing while `ReplicaLag` falls to
near zero:

```
2026-05-10 15:41:55.204713 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 120; events assigned = 19874100; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 412300000 waited (count) when Workers occupied = 88122 waited when Workers occupied = 7019847000
```

"waited at clock conflicts" dropped from approximately 99 seconds to approximately 0.4 seconds,
throughput rose roughly tenfold, and the bottleneck shifted from dependencies to worker capacity –
at which point you can tune worker count as in Example 1.

#### Example 3: A missing primary key forces full table scans on the replica

`ReplicaLag` spikes during a nightly batch job that runs large `UPDATE` and
`DELETE` statements, then recovers afterward. During the spike, replica CPU is moderate but
one worker appears stuck.

On the replica, run `SHOW PROCESSLIST` and look at the replication worker threads. One
worker stays in the `Updating` state on the same statement for many seconds at a
time:

```
+----+-------------+------+---------+----------+------+
| Id | User        | db   | Command | State    | Time |
+----+-------------+------+---------+----------+------+
| 12 | system user | app  | Connect | Updating |   38 |
+----+-------------+------+---------+----------+------+
```

Check which replicated tables lack a primary key using the detection query from
[Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread"):

```
+--------------+----------------+
| table_schema | table_name     |
+--------------+----------------+
| app          | events_archive |
+--------------+----------------+
```

**Root cause:** with ROW-based binary logging, each row in an
`UPDATE` or `DELETE` event must be located on the replica before it can be applied.
If the table has no primary key or unique NOT NULL key, the replica performs a full table scan for
**every** affected row. On a multi-million-row table, a batch operation
turns into millions of full scans, and the worker applying it stalls – blocking apply progress
and driving up lag.

**Action:** add a primary key to the table. If you cannot define an
explicit key immediately, enable Generated Invisible Primary Keys (GIPK) by setting the
`sql_generate_invisible_primary_key` parameter to `ON` (available in Aurora MySQL 3
versions based on MySQL 8.0.30 and later), so new tables receive an automatic primary key (see
[Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread")).

**Verification:** after adding the primary key, the worker no longer
lingers in `Updating`, the SQL thread apply rate recovers, and `ReplicaLag`
returns to baseline during the next batch window.

#### Example 4: A single large transaction cannot be parallelized

`ReplicaLag` jumps sharply at a predictable time each day, holds for several minutes, then
drops back to near zero. WRITESET dependency tracking is enabled,
`replica_parallel_workers=16`, and all tables have primary keys, so the earlier examples do
not apply.

During the spike, the worker-distribution query shows one worker busy and the rest idle, but unlike
Example 2 the error log shows neither high clock conflicts nor worker-occupied waits:

```
2026-05-10 02:13:40.551922 [Note] [MY-010559] [Repl] Multi-threaded slave statistics for channel '': seconds elapsed = 95; events assigned = 4120000; worker queues filled over overrun level = 0; waited due a Worker queue full = 0; waited due the total size = 0; waited at clock conflicts = 1530000 waited (count) when Workers occupied = 980 waited when Workers occupied = 210440000
```

Both dependency waits and worker-occupied waits are low, yet only one worker is active. This rules out
both the dependency bottleneck (Example 2) and the worker-capacity bottleneck (Example 1).

Inspect the busy worker in
`performance_schema.replication_applier_status_by_worker`, or run
`SHOW PROCESSLIST`. A single worker is applying one transaction for the entire duration of
the spike. On the source, an application job runs one large statement – for example,
`DELETE FROM orders WHERE created_at < '2025-01-01'` affecting several million rows
– as a single transaction.

**Root cause:** MTR parallelizes **across**
independent transactions; it cannot split a single transaction across workers. A large transaction is
applied by exactly one worker, so adding workers, switching to WRITESET, or adding primary keys does not
help. For more information, see [Multi-threaded replication (MTR)](#aurora-mysql-replication-lag-mtr "#aurora-mysql-replication-lag-mtr").

**Action:** break the large operation into smaller batches on the source
(for example, delete in chunks of a few thousand rows per transaction, with a brief pause between
batches). Smaller transactions commit independently, so the replica can spread them across workers.
Schedule bulk jobs during low-traffic windows where possible.

**Verification:** after batching the job, the daily
`ReplicaLag` spike flattens, and the worker-distribution query shows the batch spread across
multiple workers instead of one.

### Monitoring best practices

1. Configure CloudWatch alarms on the `ReplicaLag` metric with appropriate thresholds.
2. Use heartbeat tables for more accurate lag measurement than
   `Seconds_Behind_Source`. For example, use `pt-heartbeat`, which requires
   separate installation (see [Percona
   Toolkit](https://docs.percona.com/percona-toolkit/ "https://docs.percona.com/percona-toolkit/") on the Percona website).
3. Monitor `SumBinaryLogSize` CloudWatch metric on the source to track binary log generation rate.
4. Enable CloudWatch Logs log exports for the error log to retain multi-threaded replica statistics.
5. Use Enhanced Monitoring for CPU, memory, and I/O utilization on both source and replica.
6. Use Amazon CloudWatch Database Insights to identify top wait events and queries causing resource
   contention. Performance Insights reaches end of life on July 31, 2026; after that date the Performance Insights console redirects to
   CloudWatch Database Insights. Choose the Database Insights mode that fits your needs – Standard mode
   preserves the core monitoring experience and pricing, while Advanced mode adds fleet-level monitoring,
   lock diagnostics, and execution plan capture. For more information, see
   [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

## Best practices for minimizing replication lag

The following recommendations summarize the key actions for minimizing replication lag. For detailed
guidance on each topic, follow the cross-reference links.

1. **Ensure all tables have primary keys** –
   Without primary keys, the replica performs full table scans for each modified row in UPDATE and DELETE
   operations. For more information, see
   [Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread").
2. **Enable multi-threaded replication with WRITESET** –
   Parallelizes SQL apply for independent transactions. For configuration details, see
   [Multi-threaded replication (MTR)](#aurora-mysql-replication-lag-mtr "#aurora-mysql-replication-lag-mtr").
3. **Use at least the same instance class as the source** –
   Provides sufficient CPU, memory, and network resources for replication. For more information, see
   [Optimization strategies for I/O thread lag](#aurora-mysql-replication-lag-io-optimization "#aurora-mysql-replication-lag-io-optimization").
4. **Keep transaction sizes small** –
   Large transactions reduce parallelism and increase History List Length. For more information, see
   [Troubleshooting SQL thread lag](#aurora-mysql-replication-lag-sql-thread "#aurora-mysql-replication-lag-sql-thread").
5. **Disable binary logging on replicas** –
   Set `binlog_format=OFF` unless downstream replication is needed. For parameter details, see
   [MTR configuration](#aurora-mysql-replication-lag-mtr-config "#aurora-mysql-replication-lag-mtr-config").
6. **Avoid long-running transactions and queries on replicas** –
   Long-running read transactions prevent history list purging, which can degrade replication performance.
7. **Enable GTID-based replication** –
   Provides automatic position tracking and enables the Aurora in-memory relay log (Aurora MySQL 3.10+). For more information, see
   [Aurora-specific replication optimizations](#aurora-mysql-replication-lag-aurora-optimizations "#aurora-mysql-replication-lag-aurora-optimizations").

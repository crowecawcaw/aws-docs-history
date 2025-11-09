# Optimizing binary log replication for Aurora MySQL

Following, you can learn how to optimize binary log replication performance and troubleshoot related issues in
Aurora MySQL.

###### Tip

This discussion presumes that you are familiar with the MySQL binary log replication mechanism and how it works. For
background information, see [Replication Implementation](https://dev.mysql.com/doc/refman/8.0/en/replication-implementation.html "https://dev.mysql.com/doc/refman/8.0/en/replication-implementation.html") in the MySQL documentation.

## Multithreaded binary log

replication

With multithreaded binary log replication, a SQL thread reads events from the relay log and queues them up for SQL
worker threads to apply. The SQL worker threads are managed by the coordinator thread. The binary log events are applied
in parallel when possible. The level of parallelism depends on factors including version, parameters, schema design, and workload characteristics.

Multithreaded binary log replication is supported in Aurora MySQL version 3, and
in Aurora MySQL version 2.12.1 and higher. For a multithreaded replica to efficiently process binlog events in parallel,
you must configure the source for multithreaded binary log replication, and the source must use a version that includes
the parallelism information on its binary log files.

When an Aurora MySQL DB instance is configured to use binary log replication, by
default the replica instance uses single-threaded replication for Aurora MySQL
versions lower than 3.04. To enable multithreaded replication, you update the
`replica_parallel_workers` parameter to a value greater than `1`
in your custom parameter group.

For Aurora MySQL version 3.04 and higher, replication is multithreaded by default, with
`replica_parallel_workers` set to `4`. You can modify this parameter in your custom parameter
group.

To increase the resilience of your database against unexpected halts, we recommend that you enable GTID replication on the source
and allow GTIDs on the replica. To allow GTID replication, set `gtid_mode` to `ON_PERMISSIVE` on both the source
and replica. For more information about GTID-based replication, see
[Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

The following configuration options help you to fine-tune multithreaded
replication. For usage information, see [Replication and Binary Logging Options and Variables](https://dev.mysql.com/doc/refman/8.0/en/replication-options.html "https://dev.mysql.com/doc/refman/8.0/en/replication-options.html") in the
_MySQL Reference Manual_. For more information about
multithreaded replication, see the MySQL Blog [_Improving the Parallel Applier with
Writeset-based Dependency Tracking_](https://dev.mysql.com/blog-archive/improving-the-parallel-applier-with-writeset-based-dependency-tracking/ "https://dev.mysql.com/blog-archive/improving-the-parallel-applier-with-writeset-based-dependency-tracking/").

Optimal parameter values depend on several factors. For example, performance for binary log replication is influenced by
your database workload characteristics and the DB instance class the replica is running on. Thus, we recommend that you
thoroughly test all changes to these configuration parameters before applying new parameter settings to a production
instance:

- `binlog_format recommended value` – set to `ROW`
- `binlog_group_commit_sync_delay`
- `binlog_group_commit_sync_no_delay_count`
- `binlog_transaction_dependency_history_size`
- `binlog_transaction_dependency_tracking` – recommended value is `WRITESET`
- `replica_preserve_commit_order`
- `replica_parallel_type` – recommended value is `LOGICAL_CLOCK`
- `replica_parallel_workers`
- `replica_pending_jobs_size_max`
- `transaction_write_set_extraction` – recommended value is `XXHASH64`

Your schema and workload characteristics are factors that affect replication in parallel. The most common factors are the following.

- Absence of primary keys – RDS can't establish writeset dependency for tables without primary keys.
  With `ROW` format, a single multi-row statement can be accomplished with a single full table scan on the source, but results
  in one full table scan per row modified on the replica. The absence of primary keys significantly decreases replication throughput.
- Presence of foreign keys – If foreign keys are present, Amazon RDS can't use writeset dependency for parallelism
  of the tables with the FK relationship.
- Size of transactions – If a single transaction spans dozens or hundreds of megabytes or gigabytes, the coordinator thread and
  one of the worker threads might spend a long time processing only that transaction. During that time, all other worker threads might remain
  idle after they conclude processing their previous transactions.

In Aurora MySQL version 3.06 and higher, you can improve performance for binary log replicas when replicating
transactions for large tables with more than one secondary index. This feature introduces a thread pool to apply
secondary index changes in parallel on a binlog replica. The feature is controlled by the `aurora_binlog_replication_sec_index_parallel_workers` DB cluster parameter, which controls the total number
of parallel threads available to apply the secondary index changes. The parameter is set to `0` (disabled) by
default. Enabling this feature doesn't require an instance restart. To enable this feature, stop ongoing replication,
set the desired number of parallel worker threads, and then start replication again.

## Optimizing binlog replication

In Aurora MySQL 2.10 and higher, Aurora automatically applies an optimization known as the binlog I/O cache to binary
log replication. By caching the most recently committed binlog events, this optimization is designed to improve binlog
dump thread performance while limiting the impact to foreground transactions on the binlog source instance.

###### Note

This memory used for this feature is independent of the MySQL `binlog_cache` setting.

This feature doesn't apply to Aurora DB instances that use the `db.t2` and `db.t3`
instance classes.

You don't need to adjust any configuration parameters to turn on this optimization. In particular, if you had adjusted the
configuration parameter `aurora_binlog_replication_max_yield_seconds` to a nonzero value in earlier Aurora MySQL versions, set it
back to zero for currently available versions.

The status variables `aurora_binlog_io_cache_reads` and `aurora_binlog_io_cache_read_requests` help you to monitor
how often the data is read from the binlog I/O cache.

- `aurora_binlog_io_cache_read_requests` shows the number of binlog I/O read requests from the cache.
- `aurora_binlog_io_cache_reads` shows the number of binlog I/O reads that retrieve information from
  the cache.

The following SQL query computes the percentage of binlog read requests that take advantage of the cached
information. In this case, the closer the ratio is to 100, the better it is.

```
mysql> SELECT
  (SELECT VARIABLE_VALUE FROM INFORMATION_SCHEMA.GLOBAL_STATUS
    WHERE VARIABLE_NAME='aurora_binlog_io_cache_reads')
  / (SELECT VARIABLE_VALUE FROM INFORMATION_SCHEMA.GLOBAL_STATUS
    WHERE VARIABLE_NAME='aurora_binlog_io_cache_read_requests')
  * 100
  as binlog_io_cache_hit_ratio;
+---------------------------+
| binlog_io_cache_hit_ratio |
+---------------------------+
|         99.99847949080622 |
+---------------------------+

```

The binlog I/O cache feature also includes new metrics related to the binlog dump threads. _Dump threads_ are the threads that are created when new binlog replicas are connected to the binlog
source instance.

The dump thread metrics are printed to the database log every 60 seconds with the prefix `[Dump thread
 metrics]`. The metrics include information for each binlog replica such as `Secondary_id`,
`Secondary_uuid`, binlog file name, and the position that each replica is reading. The metrics also
include `Bytes_behind_primary` representing the distance in bytes between replication source and replica.
This metric measures the lag of the replica I/O thread. That figure is different from the lag of the replica SQL applier
thread, which is represented by the `seconds_behind_master` metric on the binlog replica. You can determine
whether binlog replicas are catching up to the source or falling behind by checking whether the distance decreases or
increases.

## In-memory relay log

In Aurora MySQL version 3.10 and higher, Aurora introduces an optimization known as in-memory relay log to improve replication throughput. This optimization enhances relay log I/O performance by caching all intermediate relay log content in memory. As a result, it reduces commit latency by minimizing storage I/O operations since the relay log content remains readily accessible in memory.

By default, the in-memory relay log feature is automatically enabled for Aurora-managed replication scenarios (including blue-green deployments, Aurora-Aurora replication, and cross-region replicas) when the replica meets any of these configurations:

- Single-threaded replication mode (replica_parallel_workers = 0)
- Multi-threaded replication with GTID mode enabled:
  - Auto-position enabled
  - GTID mode set to ON on the replica

- File-based replication with replica_preserve_commit_order = ON

The in-memory relay log feature is supported on instance classes larger than t3.large, but is not available on Aurora Serverless instances. The relay log circular buffer has a fixed size of 128 MB. To monitor the memory consumption of this feature, you can run the following query:

```
SELECT event_name, current_alloc FROM sys.memory_global_by_current_bytes WHERE event_name = 'memory/sql/relaylog_io_cache';
```

The in-memory relay log feature is controlled by the aurora_in_memory_relaylog parameter, which can be set at either the DB cluster or instance level. You can enable or disable this feature dynamically without restarting your instance:

1. Stop the ongoing replication
2. Set aurora_in_memory_relaylog to ON (to enable) or OFF (to disable) in parameter group
3. Restart replication

Example:

```
CALL mysql.rds_stop_replication;
set aurora_in_memory_relaylog to ON to enable or OFF to disable in cluster parameter group
CALL mysql.rds_start_replication;
```

Even when aurora_in_memory_relaylog is set to ON, the in-memory relay log feature might still be disabled under certain conditions. To verify the feature's current status, you can use the following command:

```
SHOW GLOBAL STATUS LIKE 'Aurora_in_memory_relaylog_status';
```

If the feature is unexpectedly disabled, you can identify the reason by running:

```
SHOW GLOBAL STATUS LIKE 'Aurora_in_memory_relaylog_disabled_reason';
```

This command returns a message explaining why the feature is currently disabled.



# IO:WALSync



**Topics**
+ [Supported engine versions](#wait-event.iowalsync.context.supported)
+ [Context](#wait-event.iowalsync.context)
+ [Likely causes of increased waits](#wait-event.iowalsync.causes)
+ [Actions](#wait-event.iowalsync.actions)

## Supported engine versions
<a name="wait-event.iowalsync.context.supported"></a>

This wait event information is supported for all versions of RDS for PostgreSQL 10 and higher.

## Context
<a name="wait-event.iowalsync.context"></a>

To make a transaction durable, PostgreSQL writes the WAL buffers to the WAL file and then flushes the WAL file to durable storage. A process reports the wait event `IO:WALWrite` while it writes the WAL buffers to the WAL file, and `IO:WALSync` while it waits for the flush to complete. For more information about `IO:WALWrite`, see [IO:WALWrite](wait-event.iowalwrite.md).

The process that performs the flush can be a backend that commits a transaction or a background process such as the WAL writer. Only one process flushes the WAL at a time. Other sessions that wait for the same flush to complete report the wait event `LWLock:WALWrite`. For this reason, `IO:WALSync` often appears together with `LWLock:WALWrite` in Performance Insights.

When the `synchronous_commit` parameter is set to `on` (the default), a COMMIT doesn't return to the client until the WAL for the transaction is flushed. As a result, the time spent in `IO:WALSync` adds directly to the commit latency.

## Likely causes of increased waits
<a name="wait-event.iowalsync.causes"></a>

If this wait event occurs often, look for the following causes.

**High commit rate**  
Each commit of a transaction that changes data requires a WAL flush. Workloads that run many small transactions, such as single row inserts or updates with autocommit, cause frequent flushes. To check the commit rate, monitor the `xact_commit` counter metric. For more information, see [Detailed Database Metrics for Amazon RDS for PostgreSQL](USER_PerfInsights_Counters.md#USER_PerfInsights_Counters.PostgreSQL).

**Storage write latency**  
The time to flush the WAL file depends on the write latency of the storage volume. When the storage volume reaches its IOPS or throughput limit, or when other write activity such as checkpoints competes with the WAL writes, the flush takes longer. To check the storage write latency, monitor the `WriteLatency`, `WriteIOPS`, and `WriteThroughput` metrics in CloudWatch. For more information, see [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md).

**Multi-AZ DB instance deployment**  
In a Multi-AZ DB instance deployment, writes to the primary DB instance are synchronously replicated to the standby replica. A Multi-AZ DB instance deployment can have increased write and commit latency compared to a Single-AZ deployment. For more information, see [Multi-AZ DB instance deployments for Amazon RDS](Concepts.MultiAZSingleStandby.md).

## Actions
<a name="wait-event.iowalsync.actions"></a>

To reduce this wait event, take the following actions.

**Topics**
+ [Reduce the number of commits](#wait-event.iowalsync.actions.commits)
+ [Consider asynchronous commit for transactions that can tolerate data loss](#wait-event.iowalsync.actions.sync-commit)
+ [Monitor the WAL flush time](#wait-event.iowalsync.actions.monitor)
+ [Improve storage write performance](#wait-event.iowalsync.actions.storage)

### Reduce the number of commits
<a name="wait-event.iowalsync.actions.commits"></a>

To reduce the number of WAL flushes, combine statements into transaction blocks instead of committing each statement. For bulk data loads, use multirow INSERT statements or the COPY command. Use Performance Insights to find the queries that run most often.

### Consider asynchronous commit for transactions that can tolerate data loss
<a name="wait-event.iowalsync.actions.sync-commit"></a>

When `synchronous_commit` is set to `off`, a COMMIT returns before the WAL for the transaction is flushed, so the session doesn't wait on `IO:WALSync`. If the database crashes, the most recent transactions that were reported as committed can be lost, but the database stays consistent. You can set this parameter for a specific session or transaction instead of for the whole DB instance. For more information, see [Asynchronous Commit](https://www.postgresql.org/docs/current/wal-async-commit.html) in the PostgreSQL documentation.

### Monitor the WAL flush time
<a name="wait-event.iowalsync.actions.monitor"></a>

When the `track_wal_io_timing` parameter is turned on, PostgreSQL records the number of WAL flushes and the time spent on them. In RDS for PostgreSQL 15 and higher, this parameter is turned on by default. You can check these values in the following views:
+ RDS for PostgreSQL 14 to 17: the `wal_sync` and `wal_sync_time` columns of the `pg_stat_wal` view
+ RDS for PostgreSQL 18 and higher: the `fsyncs` and `fsync_time` columns of the `pg_stat_io` view for rows where `object` is `wal`

Divide the flush time by the number of flushes to get the average time for one flush. For more information, see [The Cumulative Statistics System](https://www.postgresql.org/docs/current/monitoring-stats.html) in the PostgreSQL documentation.

### Improve storage write performance
<a name="wait-event.iowalsync.actions.storage"></a>

If the storage write latency is high, consider increasing the Provisioned IOPS or throughput of the storage volume, or moving to Provisioned IOPS storage. Before you scale the storage, tune your workload first.

For a DB instance that uses Provisioned IOPS storage, you can also use a dedicated log volume (DLV). A DLV moves PostgreSQL database transaction logs to a storage volume that's separate from the volume containing the database tables. For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv).
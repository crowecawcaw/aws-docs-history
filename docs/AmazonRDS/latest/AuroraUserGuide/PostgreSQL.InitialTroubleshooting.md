

# Initial troubleshooting for common PostgreSQL performance issues in Aurora PostgreSQL
<a name="PostgreSQL.InitialTroubleshooting"></a>

This guide covers the four most common performance issues that affect Aurora PostgreSQL databases: table and index bloat, parallel query resource exhaustion, high connection and authentication pressure, and autovacuum tuning. Use this guide as a first-pass diagnostic checklist when you experience performance degradation, before you begin deeper investigation.

Each section describes the symptoms you might observe, provides diagnostic queries to confirm the root cause, and recommends specific remediation steps.

**Understanding "nothing changed" performance regressions**  
PostgreSQL workloads often run without issues for weeks or months, then experience sudden performance degradation even though the application code and query patterns appear unchanged. This happens because the database environment is never truly static — several invisible factors shift over time and can trigger plan changes or resource contention:  
**Bloat accumulation is a workload change.** PostgreSQL's multiversion concurrency control (MVCC) retains old row versions until autovacuum reclaims them. When dead tuples accumulate faster than autovacuum can process them, tables and indexes grow physically larger. The query planner may then switch from efficient index scans to sequential scans because the cost estimates shift as the table size increases. Your SQL hasn't changed, but the data the planner sees has.
**New parameter values are a workload change.** A parameterized query that performs well for one range of values can perform poorly when the application begins using a different range. PostgreSQL may reuse a generic execution plan that doesn't account for data skew in the new range, or the planner's statistics may not accurately reflect the distribution for those values. When bloat is also present, the impact compounds — a suboptimal plan now scans significantly more dead data.
**Statistics can be stale even when autovacuum runs.** Autovacuum triggers `ANALYZE` based on the number of rows inserted or updated, not on whether the data distribution has meaningfully changed. If your application shifts to querying a different value range or time window, the planner's cost estimates may be inaccurate even though autovacuum has run recently.
**Overall database growth is a workload change.** As tables grow over time, the volume of data pages that queries must scan increases. Queries that performed well on smaller tables may develop latency as the table size grows, even when the query logic and indexes remain unchanged. Monitor `VolumeBytesUsed` to track storage growth trends.
When you investigate performance regressions where "nothing changed," treat bloat accumulation, new parameter value ranges, overall database growth, and stale statistics as the most likely root causes. Use the diagnostic steps in this guide to confirm which factor applies.  
For more information, see the following:  
[Maintenance activities for PostgreSQL databases in Amazon RDS and Amazon Aurora](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/introduction.html) (AWS Prescriptive Guidance)
[Optimizing PostgreSQL query performance](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/introduction.html) (AWS Prescriptive Guidance)
[Managing query execution plans for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.html)
[Monitoring Amazon Aurora metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) (monitor `VolumeBytesUsed` for storage growth trends)

## Quick diagnostic checklist
<a name="PostgreSQL.InitialTroubleshooting.Checklist"></a>

Use the following ordered triage steps when you first investigate a performance issue:

1. **Check `pg_stat_activity`.** Look at connection count, idle-in-transaction sessions, and long-running queries. For more information, see [Essential concepts for Aurora PostgreSQL tuning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.concepts.html).

1. **Check for bloat.** Look for high `n_dead_tup` in `pg_stat_user_tables` and consider using `pgstattuple` for precise measurement. For more information, see [Diagnosing table and index bloat](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.diag-table-ind-bloat.html).

1. **Check `pg_stat_user_tables`.** Look for high `n_dead_tup` values and stale `last_autovacuum` timestamps. For more information, see [Working with PostgreSQL autovacuum on Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html).

1. **Review `EXPLAIN ANALYZE` on slow queries.** Look for parallel plans and sequential scans on large tables. For more information, see [Best practices for parallel queries in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ParallelQueries.html).

1. **Check CloudWatch and Performance Insights metrics.** Review CPU utilization, connection count, IOPS, and freeable memory. For more information, see [Monitoring Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MonitoringAurora.html). For common wait events and corrective actions, see [Aurora PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.concepts.summary.html).

1. **Review your DB parameter group.** Check `max_parallel_workers_per_gather` and autovacuum settings. For more information, see [Tuning PostgreSQL parameters in Amazon RDS and Amazon Aurora](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-postgresql-parameters/introduction.html).

## Table and index bloat
<a name="PostgreSQL.InitialTroubleshooting.Bloat"></a>

Table and index bloat occurs when dead tuples accumulate in your tables faster than autovacuum can reclaim them. Over time, this causes gradual query performance degradation, increased storage usage, and suboptimal query plans.

### Symptoms
<a name="PostgreSQL.InitialTroubleshooting.Bloat.Symptoms"></a>
+ Gradual query performance degradation over weeks or months
+ Storage usage growing despite stable data volume
+ The query planner chooses sequential scans over index scans due to stale statistics
+ High `dead_tuple_count` in table statistics

### Diagnosis
<a name="PostgreSQL.InitialTroubleshooting.Bloat.Diagnosis"></a>

You can estimate bloat across all tables by querying the system catalog. This approach does not require any extensions:

```
SELECT schemaname, relname,
       n_dead_tup,
       n_live_tup,
       ROUND(n_dead_tup::numeric / GREATEST(n_live_tup, 1) * 100, 2) AS dead_pct,
       last_autovacuum,
       last_autoanalyze
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC
LIMIT 20;
```

To address bloat, you can use the `pg_repack` extension to reorganize tables and indexes with minimal locking. For more information, see [Removing bloat from tables with pg\_repack](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pg_repack.html) and [Remove bloat from Amazon Aurora and RDS for PostgreSQL with pg\_repack](https://aws.amazon.com/blogs/database/remove-bloat-from-amazon-aurora-and-rds-for-postgresql-with-pg_repack/).

**Important**  
Rather than relying on manual maintenance, ensure that autovacuum is enabled and properly tuned for your workload. See [Autovacuum tuning](#PostgreSQL.InitialTroubleshooting.Autovacuum) for tuning recommendations.

## Parallel query resource exhaustion
<a name="PostgreSQL.InitialTroubleshooting.ParallelQuery"></a>

PostgreSQL can execute queries in parallel to improve performance for large sequential scans and aggregations. However, each parallel worker is a full backend process that counts against `max_worker_processes` (and the sub-limit `max_parallel_workers`) and allocates its own `work_mem`. A single query with 4 parallel workers can consume hundreds of megabytes of memory and significant CPU. Under high concurrency, excessive parallelism can exhaust CPU and memory rapidly.

Common symptoms include sudden CPU spikes, high memory usage per query, and elevated `DatabaseConnections` in CloudWatch without application changes. You may also observe wait events such as `IPC:BgWorkerStartup`, `IPC:ExecuteGather`, and `IPC:ParallelFinish`. For more information about these wait events, see [IPC:parallel wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-ipc-parallel.html).

For most OLTP and high-concurrency production workloads, disable automatic parallelism by setting `max_parallel_workers_per_gather = 0` in your DB parameter group. You can then selectively enable parallelism for specific analytics or reporting sessions by setting the parameter per session or per role.

For detailed guidance on diagnosing and controlling parallel query behavior, see [Best practices for parallel queries in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ParallelQueries.html).

## High connection and authentication pressure
<a name="PostgreSQL.InitialTroubleshooting.ConnectionPressure"></a>

Connection churn — frequent opening and closing of database connections without pooling — creates authentication overhead and can exhaust available connection slots. Idle connections that remain open also consume slots without performing useful work.

### Symptoms
<a name="PostgreSQL.InitialTroubleshooting.ConnectionPressure.Symptoms"></a>
+ Elevated `total_auth_attempts` in Performance Insights monitoring. For more information, see [Non-native counters for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.Aurora_PostgreSQL.NonNative).
+ Slow connection establishment times
+ `FATAL: too many connections for role` or `remaining connection slots are reserved` errors
+ CPU spikes correlated with connection churn

### Diagnosis
<a name="PostgreSQL.InitialTroubleshooting.ConnectionPressure.Diagnosis"></a>

Run the following query to check your current connection state:

```
SELECT
  setting::int AS max_connections,
  (SELECT count(*) FROM pg_stat_activity) AS current_connections,
  (SELECT count(*) FROM pg_stat_activity WHERE state = 'idle') AS idle_connections,
  (SELECT count(*) FROM pg_stat_activity WHERE state = 'idle in transaction') AS idle_in_txn
FROM pg_settings
WHERE name = 'max_connections';
```

A high number of `idle` or `idle in transaction` connections relative to `max_connections` indicates that connections are not being released properly. Idle-in-transaction connections are especially problematic because they hold locks and prevent autovacuum from reclaiming dead tuples.

### Remediation
<a name="PostgreSQL.InitialTroubleshooting.ConnectionPressure.Remediation"></a>
+ **Deploy connection pooling.** Use PgBouncer or Amazon RDS Proxy to reduce the number of direct connections to your database. Connection pooling reuses existing connections rather than creating new ones for each request.
+ **Set `idle_in_transaction_session_timeout`.** This parameter automatically terminates sessions that remain idle in a transaction beyond the specified duration. This prevents long-running idle transactions from holding locks and blocking autovacuum.
+ **Review application connection handling.** Ensure your application closes connections promptly and does not hold transactions open longer than necessary.

**Note**  
Parallel query workers consume CPU and memory. If you observe resource exhaustion alongside parallel query activity, see [Parallel query resource exhaustion](#PostgreSQL.InitialTroubleshooting.ParallelQuery) for guidance on controlling parallel worker usage.

## Using Performance Insights wait events for troubleshooting
<a name="PostgreSQL.InitialTroubleshooting.WaitEvents"></a>

Performance Insights captures wait events that show where your database is spending time. When you investigate performance issues, wait events help you identify whether the bottleneck is CPU, I/O, locking, network, or inter-process communication. Common wait event categories that appear during the issues described in this guide include:
+ **CPU** — The session is active on CPU or waiting for CPU. High CPU wait events often correlate with excessive parallelism or inefficient query plans scanning bloated tables.
+ **IPC (inter-process communication)** — Wait events such as `IPC:BgWorkerStartup`, `IPC:ExecuteGather`, and `IPC:ParallelFinish` indicate parallel query coordination overhead.
+ **IO** — Wait events such as `IO:DataFileRead` indicate that queries are reading data from storage because the required pages are not in shared memory. This is common when bloated tables exceed the buffer cache.
+ **Lock** — Wait events such as `Lock:transactionid` and `Lock:tuple` indicate contention between sessions. Idle-in-transaction connections can hold locks that block other queries and autovacuum.
+ **Client** — Wait events such as `Client:ClientRead` indicate the database is waiting for the application to send data. High client wait events can indicate connection churn or network latency.

For a complete reference of wait events that commonly indicate performance problems and their recommended corrective actions, see [Aurora PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.concepts.summary.html).

## Autovacuum tuning
<a name="PostgreSQL.InitialTroubleshooting.Autovacuum"></a>

Autovacuum is the background process that reclaims dead tuples, prevents table and index bloat, updates planner statistics, and protects against transaction ID wraparound. The default autovacuum settings are conservative and designed for small databases. High-write production workloads almost always require tuning.

When autovacuum cannot keep up with your write workload, bloat accumulates, planner statistics become stale, and the risk of transaction ID wraparound increases. If `age(relfrozenxid)` approaches 2 billion, the database shuts down to prevent data corruption.

For detailed guidance on tuning autovacuum parameters, monitoring vacuum activity, and configuring per-table overrides, see [Working with PostgreSQL autovacuum on Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html).

## Related information
<a name="PostgreSQL.InitialTroubleshooting.RelatedInfo"></a>
+ [Best practices for parallel queries in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ParallelQueries.html)
+ [Managing Aurora PostgreSQL connection churn with pooling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.connection_pooling.html)
+ [Managing autovacuum with large indexes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.html)
+ [Diagnosing table and index bloat](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.diag-table-ind-bloat.html)
+ [IPC:Parallel wait events reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-ipc-parallel.html)
+ [Best practices with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.html)
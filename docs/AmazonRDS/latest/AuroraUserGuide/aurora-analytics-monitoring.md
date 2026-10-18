

# Monitoring
<a name="aurora-analytics-monitoring"></a>

This topic describes the metrics, wait events, and diagnostic queries you use to monitor your analytics workload, and how to build dashboards from them. For specific symptoms, see [Troubleshooting](aurora-analytics-troubleshooting.md).

Aurora PostgreSQL reports its analytics activity through four channels. Each channel answers a different question, and most investigations use more than one.
+ **Amazon CloudWatch metrics**: Instance-level time series for memory, cache, spill, Amazon S3 requests, and worker threads, alongside the standard Aurora metrics. Use them for dashboards, alarms, and trends over hours to weeks. This channel is the only one that supports alarms.
+ **SQL diagnostic functions**: Per-query and per-backend counters read live from the instance. Use them when you need exact bytes, spill, or thread counts for one query or one process ID, which Amazon CloudWatch cannot attribute.
+ **Database Insights**: Sampled session activity rather than published metrics. Use it to see which queries dominate the instance and what they are waiting on.
+ **Logging**: Engine messages in the PostgreSQL error log. Use it as a last resort for problems that leave no trail in the other three channels.

## Amazon CloudWatch metrics
<a name="aurora-analytics-cloudwatch-metrics"></a>

The following Amazon CloudWatch metrics are published for Aurora Analytics.


**Aurora Analytics Amazon CloudWatch metrics**  

| Metric name | Description | Unit | 
| --- | --- | --- | 
| AuroraAnalyticsActiveThreads | Total number of actively executing analytics worker threads. | Count | 
| AuroraAnalyticsMemoryUsage | Memory consumed by all sessions running foreign table queries. | Bytes | 
| AuroraAnalyticsCacheHit | Data served from the cache. | Bytes | 
| AuroraAnalyticsCacheHitRatio | Ratio of cache hits to total data accesses (0.0 to 1.0, where 1.0 means all reads served from cache). To express as a percentage, multiply by 100. | Ratio | 
| AuroraAnalyticsCacheSize | Size of the on-disk cache. | Bytes | 
| AuroraAnalyticsDiskSpillSize | Temporary disk space used by query spills. | Bytes | 
| AuroraAnalyticsRemoteRead | Data read from Amazon S3 (remote reads). | Bytes | 
| AuroraAnalyticsS3GetRequest | Number of Amazon S3 GetObject requests. | Count | 
| AuroraAnalyticsS3HeadRequest | Number of Amazon S3 HeadObject requests. | Count | 

**Note**  
The `AuroraAnalyticsActiveThreads` metric shows the total active worker threads, including both query execution threads and Amazon S3 I/O threads. A value much higher than your session count is normal, because each query can use many threads. For example, 8 concurrent sessions can produce several hundred active threads. For more information, see [Interpreting the active thread count](#aurora-analytics-active-thread-count).

### Monitoring local storage performance
<a name="aurora-analytics-local-storage-metrics"></a>

Aurora PostgreSQL uses local storage for the on-disk read cache and for query spill files, such as sorts and hash tables that exceed `query_mem`. Which metrics report that I/O depends on how local storage is attached to the instance class, so check your class first and then use the matching set of metrics below.

#### Instances with Amazon EBS storage only
<a name="aurora-analytics-ebs-storage-metrics"></a>

Classes such as `db.r8g`, `db.r7g`, and `db.r7i` have no instance store, so the read cache and spill files share the Amazon EBS-backed volume with the rest of the database. Analytical I/O therefore competes with normal PostgreSQL I/O, and it is reported by the general storage metrics rather than by a set of metrics specific to Analytics.


**Storage metrics for Amazon EBS-only classes**  

| Metric name | Relevance to analytics | Unit | 
| --- | --- | --- | 
| ReadIOPS / WriteIOPS | Amazon EBS read and write IOPS for the cache and spill files. Because these counters also include PostgreSQL I/O, compare them against a period with no analytical queries running to see the analytical share. | Count/Second | 
| ReadLatency / WriteLatency | Amazon EBS read and write latency. Higher values indicate an I/O-bound workload, where an NVMe instance class would help. | Seconds | 
| ReadThroughput / WriteThroughput | Amazon EBS read and write throughput for the cache and spill files. | Bytes/Second | 
| DiskQueueDepth | Outstanding I/O requests to the Amazon EBS volume. Sustained high values indicate the volume is saturated and that queries are waiting on storage. | Count | 
| FreeLocalStorage | Available local storage. A dropping value means the cache and spill files are filling the volume. | Bytes | 

**Note**  
On Amazon EBS-only classes, watch `ReadLatency` and `DiskQueueDepth` together. Rising latency with a rising queue depth means the volume is at its limit, and the fix is a larger instance or an NVMe class rather than a query change.

#### Instances with local NVMe storage
<a name="aurora-analytics-nvme-storage-metrics"></a>

Classes such as `db.r8gd` and `db.r6gd` include an NVMe instance store, and Aurora PostgreSQL places the read cache and spill files there instead of on the Amazon EBS volume. This keeps analytical I/O off the database volume and gives the cache much lower read latency. The NVMe device reports through its own set of ephemeral storage metrics, so `ReadIOPS`, `ReadLatency`, and `DiskQueueDepth` no longer reflect analytical I/O on these classes.


**Storage metrics for NVMe classes**  

| Metric name | Relevance to analytics | Unit | 
| --- | --- | --- | 
| ReadIOPSEphemeralStorage / WriteIOPSEphemeralStorage | NVMe read and write IOPS. High read values indicate active cache reads. High write values indicate cache population or spill activity. | Count/Second | 
| ReadLatencyEphemeralStorage / WriteLatencyEphemeralStorage | NVMe read and write latency. Increasing values might indicate storage contention between concurrent queries. | Seconds | 
| ReadThroughputEphemeralStorage / WriteThroughputEphemeralStorage | NVMe read and write throughput. | Bytes/Second | 
| FreeEphemeralStorage | Available ephemeral NVMe storage. A dropping value means the cache and spill files are filling the instance store. | Bytes | 

**Note**  
The on-disk read cache does not survive an instance restart, replacement, or failover. On NVMe classes the instance store is ephemeral and is wiped; on Amazon EBS-only classes the Amazon EBS volume persists, but the cache is still invalidated. In both cases the cache starts empty afterward, so the first queries against a table read from Amazon S3 again. Expect higher latency and a lower `AuroraAnalyticsCacheHitRatio` until the cache is warm.

### Standard Aurora metrics relevant to Analytics
<a name="aurora-analytics-standard-metrics"></a>

Beyond the metrics specific to analytics, the following standard Aurora metrics are useful for monitoring an analytical workload.


**Standard Aurora metrics relevant to Analytics**  

| Metric name | Relevance to analytics | Unit | 
| --- | --- | --- | 
| FreeLocalStorage | Available local storage for the read cache and for query spill files. A dropping value means the cache and spill files are filling the volume. On NVMe classes, use FreeEphemeralStorage instead, because the cache and spill files are on the instance store. | Bytes | 
| FreeableMemory | Overall instance memory pressure. Low values indicate too many concurrent sessions. | Bytes | 
| CPUUtilization | High CPU during analytical queries is expected. Sustained 100% might indicate thread contention. | Percent | 
| DatabaseConnections | Tracks concurrent connections including analytical sessions. | Count | 

## SQL-based diagnostic functions
<a name="aurora-analytics-diagnostic-functions"></a>

Aurora PostgreSQL provides SQL-callable functions that report counters Amazon CloudWatch cannot attribute: exact bytes, spill, and thread counts for one query or one backend. Start with the following table to choose a function, then see the SQL functions reference for its columns.


**SQL diagnostic functions**  

| Function | Scope | What it answers | 
| --- | --- | --- | 
| aurora\_analytics\_stat\_statements() | Per normalized query, cumulative | Which queries read from Amazon S3 rather than the cache, spill to disk, or spend the most CPU in the engine. | 
| aurora\_analytics\_stat\_resource\_usage() | Per backend, live | Which backend is consuming memory, worker threads, and spill space right now. | 
| aurora\_analytics\_instance\_metrics() | Whole instance, cumulative since engine start | How much Amazon S3 request and cache activity the instance has done, and whether the engine restarted. | 
| aurora\_analytics\_cache\_size() | Whole instance, current | How large the on-disk read cache has grown. | 

All byte columns report raw bytes, so wrap them in `pg_size_pretty()` for readable output. For the syntax, permissions, and worked examples of each function, see [SQL functions reference](aurora-analytics-sql-functions-reference.md).

### Sample queries and output
<a name="aurora-analytics-sample-queries"></a>

To find queries reading from Amazon S3 instead of the cache, run the following query.

```
-- Optional: enable the detailed columns, such as CPU time
SET aurora_analytics.track_detailed_metrics = true;

-- Run your queries, then check statistics
SELECT SUBSTR(query, 1, 45) AS query,
       calls,
       pg_size_pretty(analytics_cache_hit_bytes) AS cache_hits,
       pg_size_pretty(analytics_remote_read_bytes) AS s3_reads,
       pg_size_pretty(analytics_total_disk_spill) AS spill,
       round(analytics_total_cpu_time::numeric, 2) AS cpu_ms
FROM aurora_analytics_stat_statements()
WHERE analytics_cache_hit_bytes > 0 OR analytics_remote_read_bytes > 0
ORDER BY analytics_remote_read_bytes DESC;
```

Interpret the results as follows.
+ `analytics_cache_hit_bytes` much greater than `analytics_remote_read_bytes`: cache is warm and most reads are served locally.
+ `analytics_remote_read_bytes` much greater than `analytics_cache_hit_bytes`: cache is cold or the working set is too large.
+ `analytics_total_disk_spill` greater than 0: query is spilling to disk due to memory pressure.

To attribute memory, threads, and spill to a backend, run the following query.

```
SELECT pid,
       pg_size_pretty(current_memory_usage) AS mem_used,
       active_threads,
       pg_size_pretty(disk_spill_size) AS spill
FROM aurora_analytics_stat_resource_usage()
WHERE current_memory_usage > 0
ORDER BY current_memory_usage DESC;
```

Join the `pid` column to `pg_stat_activity` to see which query each backend is running. Use this when `AuroraAnalyticsMemoryUsage` is high and you need to know which session is responsible.

To view instance-wide Amazon S3 and cache activity, run the following query.

```
SELECT s3_head_request_count,
       s3_get_request_count,
       pg_size_pretty(s3_cache_hit_bytes) AS cache_hit,
       pg_size_pretty(s3_remote_read_bytes) AS s3_read
FROM aurora_analytics_instance_metrics();
```

To check cache size, run the following query.

```
SELECT pg_size_pretty(aurora_analytics_cache_size()) AS cache_size;
```

To find active analytical queries, run the following query.

```
WITH analytics_tables AS (
    SELECT c.relname
    FROM pg_foreign_table ft
    JOIN pg_class c ON c.oid = ft.ftrelid
    JOIN pg_foreign_server fs ON fs.oid = ft.ftserver
    WHERE fs.srvname = 'aurora_analytics_server'
)
SELECT a.pid, a.usename, a.datname,
       NOW() - a.query_start AS runtime, a.state,
       LEFT(a.query, 100) AS query_preview
FROM pg_stat_activity a
WHERE a.state = 'active'
  AND EXISTS (SELECT 1 FROM analytics_tables t WHERE a.query ILIKE '%' || t.relname || '%')
ORDER BY a.query_start;
```

## Interpreting the active thread count
<a name="aurora-analytics-active-thread-count"></a>

The `AuroraAnalyticsActiveThreads` Amazon CloudWatch metric and the `active_threads` column of `aurora_analytics_stat_resource_usage()` report the number of analytics worker threads that are actively executing at the moment of measurement. This count is often much higher than your number of concurrent sessions, which is expected. The active thread count includes two kinds of worker threads.
+ **Query execution threads**: Threads that run the query plan (scan, filter, aggregate, join, sort). Aurora manages the number of these threads automatically, scaled from the query's memory budget. For more information, see [Worker threads](aurora-analytics-resource-management.md#aurora-analytics-worker-threads).
+ **Amazon S3 I/O threads**: Threads from a pool that downloads data blocks from Amazon S3 in parallel on cache misses. These threads are active only while data is being fetched from Amazon S3. On a cold cache, or when the working set exceeds the cache, many of these threads can be active at once.

Only threads that are actively doing work are counted. A thread that is idle and waiting for work is not included, so the count rises and falls continuously as a query runs.

Because both kinds of threads are counted together, the total can be much higher than the number of concurrent queries. A handful of concurrent queries reading from Amazon S3 on cache misses can produce several hundred active threads. This is normal. A persistently high count driven by Amazon S3 I/O threads indicates a low cache hit ratio, so consider warming or scaling the cache.

These worker threads are internal to the analytics engine and do not appear in `pg_stat_activity`, which shows only your PostgreSQL sessions. This is why a small number of sessions can drive high CPU usage: a single session can run dozens or hundreds of active threads.

The active thread count answers "why is CPU high with only a few sessions?", while the `Extension:AuroraAnalyticsExecute` wait event tells you how many sessions are waiting on the analytics engine. For more information, see [Interpreting the AuroraAnalyticsExecute wait event](#aurora-analytics-wait-event).

## Monitoring xmin horizon on reader instances
<a name="aurora-analytics-xmin-horizon"></a>

Long-running analytical queries on reader instances hold an xmin snapshot open, which can prevent autovacuum on the writer from reclaiming dead tuples. Running analytical workloads on a dedicated reader isolates this impact; for more information, see [Using a dedicated reader instance for analytics](aurora-analytics-dedicated-reader.md).

Set `statement_timeout` to bound how long a single query can run. Like other PostgreSQL settings, you can set it at the session, role, database, or cluster parameter group level; use the lowest level that fits. Set it per session for a single connection.

```
SET statement_timeout = 'XX';
```

Or set it as a default for the analytics role.

```
ALTER ROLE analytics_user SET statement_timeout = 'XX';
```

## Database Insights
<a name="aurora-analytics-performance-insights"></a>

Where Amazon CloudWatch tells you that the instance is under pressure, Database Insights tells you which sessions and which SQL are responsible. Foreign table queries appear there like any other PostgreSQL query, so you use the same average active sessions (AAS) chart, the same Top SQL list, and the same wait event breakdown.

Aurora PostgreSQL adds one wait event for foreign table queries.


**Analytics wait event**  

| Wait event | Type | Meaning | 
| --- | --- | --- | 
| Extension:AuroraAnalyticsExecute | Extension | The backend is executing a query in the analytics engine, including time spent reading data from Amazon S3. This is the primary wait event for foreign table queries. | 

To identify top analytical queries, do the following.

1. Navigate to the Top SQL tab.

1. Sort by Total time or Calls.

1. Look for queries referencing foreign tables (typically prefixed with `ft_`).

### Interpreting the AuroraAnalyticsExecute wait event
<a name="aurora-analytics-wait-event"></a>

When a query references a foreign table, the PostgreSQL backend hands execution to the embedded analytics engine and blocks until the engine returns results. During this time, the backend reports the `Extension:AuroraAnalyticsExecute` wait event. In Database Insights, this appears in the average active sessions (AAS) chart as `Extension:AuroraAnalyticsExecute`. Keep the following in mind.
+ **It is reported per session, not per thread.** Each PostgreSQL backend running an analytical query contributes at most one unit of average active sessions to `Extension:AuroraAnalyticsExecute`, in the same way as any other PostgreSQL wait event. If you run 8 concurrent analytical queries, the contribution of this wait event to AAS is bounded by 8, regardless of how many worker threads the engine uses internally.
+ **It covers both compute and Amazon S3 reads.** A single query spends time on columnar computation (aggregation, joins, sorting) and, on cache misses, on fetching data from Amazon S3. Both are counted under this one wait event. The engine does not currently emit a separate wait event for Amazon S3 reads.
+ **It is distinct from the active thread count.** The number of internal worker threads that the engine uses to process a query is reported separately, by the `AuroraAnalyticsActiveThreads` Amazon CloudWatch metric and the `aurora_analytics_stat_resource_usage()` function. A single session showing one unit of `Extension:AuroraAnalyticsExecute` in Database Insights can correspond to dozens or hundreds of active worker threads. For more information, see [Interpreting the active thread count](#aurora-analytics-active-thread-count).

### Tracking query duration trends
<a name="aurora-analytics-query-duration-trends"></a>

Use Database Insights to track whether average query time is stable or degrading over time. A sudden increase might indicate the following.
+ The cache was cleared (restart, failover).
+ Data volume increased.
+ Concurrency increased beyond stable limits.

## Logging
<a name="aurora-analytics-logging"></a>

Aurora PostgreSQL can write analytics engine messages to the PostgreSQL error log. Logging is a diagnostic tool rather than a monitoring channel: it produces detail about individual operations, not time series you can trend or alarm on. Two parameters control it. Set them in a DB cluster parameter group to cover the whole workload, or with `SET` in a single session to scope the output to one investigation. The session-scoped `SET` requires the `rds_superuser` role.

`aurora_analytics.enable_logging`  
Turns engine logging on or off. On by default.

`aurora_analytics.logging_level`  
Controls verbosity. `DEBUG1` is the level that produces useful diagnostic detail.

Messages go to the PostgreSQL error log. Retrieve it in one of three ways.
+ **Amazon RDS console**: Choose your DB instance, choose **Logs and events**, then choose the log in the **Logs** section.
+ **Amazon CloudWatch Logs**: Available when log export is configured for the DB cluster, which also gives you retention and querying.
+ **AWS CLI**: Run the following command.

  ```
  aws rds download-db-log-file-portion \
    --db-instance-identifier <instance-id> \
    --log-file-name error/postgresql.log \
    --starting-token 0
  ```

**Note**  
PostgreSQL's own `log_temp_files` parameter does not capture analytics spill, because the engine does not write PostgreSQL temp files. Use `AuroraAnalyticsDiskSpillSize` to see spill instead.

## Key metrics reference
<a name="aurora-analytics-key-metrics"></a>

The following table provides a quick reference for analytics health. Two rows depend on your instance class, so check which storage the class uses before you build alarms from this table. On NVMe classes, `FreeLocalStorage` does not track the volume that holds the read cache and spill files, so an alarm on it will stay quiet while the instance store fills.


**Key metrics reference**  

| What to check | Metric | Healthy | Warning | Critical | 
| --- | --- | --- | --- | --- | 
| Analytics memory | AuroraAnalyticsMemoryUsage | Within the 30% of instance memory budget | 30 to 50% of instance memory | Above 50%, or queries failing with out of memory errors | 
| Instance memory headroom | FreeableMemory | Stable and well above zero under load | Falling steadily as concurrency rises | Near zero, the instance is at restart risk | 
| Cache effectiveness | AuroraAnalyticsCacheHitRatio | Greater than 0.7 | 0.3 to 0.7 | Less than 0.3 after warm-up | 
| Spill volume | AuroraAnalyticsDiskSpillSize | Zero or low | Above your workload baseline | Large and sustained | 
| Free local storage, Amazon EBS-only classes | FreeLocalStorage | Greater than 30% free | 10 to 30% free | Less than 10% free | 
| Free local storage, NVMe classes | FreeEphemeralStorage | Greater than 30% free | 10 to 30% free | Less than 10% free | 
| Storage read latency | ReadLatency on Amazon EBS-only classes, ReadLatencyEphemeralStorage on NVMe classes | Flat as concurrency rises | Rising with query concurrency | Rising with DiskQueueDepth high as well, on Amazon EBS-only classes | 
| Remote reads | AuroraAnalyticsRemoteRead | Low, the cache is serving | Increasing | Consistently high after warm-up | 
| Instance CPU | CPUUtilization | Less than 80% | 80 to 95% | Greater than 95% sustained | 


# Monitoring and troubleshooting
<a name="aurora-analytics-monitoring-troubleshooting"></a>

Aurora PostgreSQL reports foreign table query activity through Amazon CloudWatch, SQL diagnostic functions, Database Insights, and the PostgreSQL log, the same tools you already use for Aurora PostgreSQL. Monitoring covers the metrics, wait events, and diagnostic queries for watching a workload; Troubleshooting covers common symptoms and how to resolve them.

**Topics**
+ [Monitoring](#aurora-analytics-monitoring)
+ [Troubleshooting](#aurora-analytics-troubleshooting)
+ [Execution plan](aurora-analytics-execution-plan.md)

## Monitoring
<a name="aurora-analytics-monitoring"></a>

This section describes the metrics, wait events, and diagnostic queries you use to monitor your analytics workload, and how to build dashboards from them. For specific symptoms, see [Troubleshooting](#aurora-analytics-troubleshooting).

Aurora PostgreSQL reports its analytics activity through four channels. Each channel answers a different question, and most investigations use more than one.
+ **Amazon CloudWatch metrics**: Instance-level time series for memory, cache, spill, Amazon S3 requests, and worker threads, alongside the standard Aurora metrics. Use them for dashboards, alarms, and trends over hours to weeks. This channel is the only one that supports alarms.
+ **SQL diagnostic functions**: Per-query and per-backend counters read live from the instance. Use them when you need exact bytes, spill, or thread counts for one query or one process ID, which Amazon CloudWatch cannot attribute.
+ **Database Insights**: Sampled session activity rather than published metrics. Use it to see which queries dominate the instance and what they are waiting on.
+ **Logging**: Engine messages in the PostgreSQL error log. Use it as a last resort for problems that leave no trail in the other three channels.

### Amazon CloudWatch metrics
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

#### Monitoring local storage performance
<a name="aurora-analytics-local-storage-metrics"></a>

Aurora PostgreSQL uses local storage for the on-disk read cache and for query spill files, such as sorts and hash tables that exceed `query_mem`. Which metrics report that I/O depends on how local storage is attached to the instance class, so check your class first and then use the matching set of metrics below.

##### Instances with Amazon EBS storage only
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

##### Instances with local NVMe storage
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

#### Standard Aurora metrics relevant to Analytics
<a name="aurora-analytics-standard-metrics"></a>

Beyond the metrics specific to analytics, the following standard Aurora metrics are useful for monitoring an analytical workload.


**Standard Aurora metrics relevant to Analytics**  

| Metric name | Relevance to analytics | Unit | 
| --- | --- | --- | 
| FreeLocalStorage | Available local storage for the read cache and for query spill files. A dropping value means the cache and spill files are filling the volume. On NVMe classes, use FreeEphemeralStorage instead, because the cache and spill files are on the instance store. | Bytes | 
| FreeableMemory | Overall instance memory pressure. Low values indicate too many concurrent sessions. | Bytes | 
| CPUUtilization | High CPU during analytical queries is expected. Sustained 100% might indicate thread contention. | Percent | 
| DatabaseConnections | Tracks concurrent connections including analytical sessions. | Count | 

### SQL-based diagnostic functions
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

#### Sample queries and output
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

### Interpreting the active thread count
<a name="aurora-analytics-active-thread-count"></a>

The `AuroraAnalyticsActiveThreads` Amazon CloudWatch metric and the `active_threads` column of `aurora_analytics_stat_resource_usage()` report the number of analytics worker threads that are actively executing at the moment of measurement. This count is often much higher than your number of concurrent sessions, which is expected. The active thread count includes two kinds of worker threads.
+ **Query execution threads**: Threads that run the query plan (scan, filter, aggregate, join, sort). Aurora manages the number of these threads automatically, scaled from the query's memory budget. For more information, see [Worker threads](aurora-analytics-resource-management.md#aurora-analytics-worker-threads).
+ **Amazon S3 I/O threads**: Threads from a pool that downloads data blocks from Amazon S3 in parallel on cache misses. These threads are active only while data is being fetched from Amazon S3. On a cold cache, or when the working set exceeds the cache, many of these threads can be active at once.

Only threads that are actively doing work are counted. A thread that is idle and waiting for work is not included, so the count rises and falls continuously as a query runs.

Because both kinds of threads are counted together, the total can be much higher than the number of concurrent queries. A handful of concurrent queries reading from Amazon S3 on cache misses can produce several hundred active threads. This is normal. A persistently high count driven by Amazon S3 I/O threads indicates a low cache hit ratio, so consider warming or scaling the cache.

These worker threads are internal to the analytics engine and do not appear in `pg_stat_activity`, which shows only your PostgreSQL sessions. This is why a small number of sessions can drive high CPU usage: a single session can run dozens or hundreds of active threads.

The active thread count answers "why is CPU high with only a few sessions?", while the `Extension:AuroraAnalyticsExecute` wait event tells you how many sessions are waiting on the analytics engine. For more information, see [Interpreting the AuroraAnalyticsExecute wait event](#aurora-analytics-wait-event).

### Monitoring xmin horizon on reader instances
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

### Database Insights
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

#### Interpreting the AuroraAnalyticsExecute wait event
<a name="aurora-analytics-wait-event"></a>

When a query references a foreign table, the PostgreSQL backend hands execution to the embedded analytics engine and blocks until the engine returns results. During this time, the backend reports the `Extension:AuroraAnalyticsExecute` wait event. In Database Insights, this appears in the average active sessions (AAS) chart as `Extension:AuroraAnalyticsExecute`. Keep the following in mind.
+ **It is reported per session, not per thread.** Each PostgreSQL backend running an analytical query contributes at most one unit of average active sessions to `Extension:AuroraAnalyticsExecute`, in the same way as any other PostgreSQL wait event. If you run 8 concurrent analytical queries, the contribution of this wait event to AAS is bounded by 8, regardless of how many worker threads the engine uses internally.
+ **It covers both compute and Amazon S3 reads.** A single query spends time on columnar computation (aggregation, joins, sorting) and, on cache misses, on fetching data from Amazon S3. Both are counted under this one wait event. The engine does not currently emit a separate wait event for Amazon S3 reads.
+ **It is distinct from the active thread count.** The number of internal worker threads that the engine uses to process a query is reported separately, by the `AuroraAnalyticsActiveThreads` Amazon CloudWatch metric and the `aurora_analytics_stat_resource_usage()` function. A single session showing one unit of `Extension:AuroraAnalyticsExecute` in Database Insights can correspond to dozens or hundreds of active worker threads. For more information, see [Interpreting the active thread count](#aurora-analytics-active-thread-count).

#### Tracking query duration trends
<a name="aurora-analytics-query-duration-trends"></a>

Use Database Insights to track whether average query time is stable or degrading over time. A sudden increase might indicate the following.
+ The cache was cleared (restart, failover).
+ Data volume increased.
+ Concurrency increased beyond stable limits.

### Logging
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

### Key metrics reference
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

## Troubleshooting
<a name="aurora-analytics-troubleshooting"></a>

This section describes specific symptoms, their causes, and how to resolve them. For the metrics, wait events, and diagnostic queries used to watch a workload, see [Monitoring](#aurora-analytics-monitoring).

### Setup and configuration issues
<a name="aurora-analytics-ts-setup"></a>

The following are common setup and configuration issues.

#### Extension not available
<a name="aurora-analytics-ts-extension-not-available"></a>

**Symptom**: `CREATE EXTENSION aurora_analytics` fails with the following error.

```
ERROR:  extension "aurora_analytics" is not available
```

**Causes and solutions**: This error means you are running a version of Aurora PostgreSQL that does not support the `aurora_analytics` extension. To use this feature, upgrade to Aurora PostgreSQL 17.11 or higher, or 18.6 or higher. Use the following table to identify the cause and resolve it.


**Extension not available: causes and solutions**  

| Cause | Solution | 
| --- | --- | 
| Engine version does not support the analytics feature. | Verify your DB cluster is running a supported Aurora PostgreSQL version (17.11 or higher, or 18.6 or higher). Upgrade if needed. | 
| Connected to the wrong endpoint. | Verify that you are connected to the correct Aurora DB cluster endpoint. | 

To diagnose, run the following queries. The second returns no rows on an unsupported version.

```
SELECT version();

SELECT * FROM pg_available_extensions WHERE name = 'aurora_analytics';
```

#### Feature not enabled
<a name="aurora-analytics-ts-feature-not-enabled"></a>

**Symptom**: A query against a foreign table fails with the following error. This is distinct from the extension-not-available error: the extension is installed successfully, but queries are rejected because the feature is turned off at the DB cluster level.

```
ERROR:  aurora_analytics is not enabled
HINT:  Set aurora_analytics.enabled to true in the parameter group and retry the query.
```

**Cause**: `aurora_analytics.enabled` is set to `off`.

**Solution**: Set `aurora_analytics.enabled` to `on` in your DB cluster parameter group. As a dynamic parameter, the change is applied immediately without a reboot.

To diagnose, run the following query.

```
SHOW aurora_analytics.enabled;
```

#### Permission denied to create extension
<a name="aurora-analytics-ts-permission-denied"></a>

**Symptom**: Creating the extension fails with the following error.

```
ERROR:  permission denied to create extension "aurora_analytics"
```

**Solution**: To create the extension, you must have the `rds_superuser` role, or be a user that has been granted the `rds_extension` role and delegated this extension. Being the database owner is not sufficient. Grant the `rds_superuser` role and retry.

```
GRANT rds_superuser TO your_user;
CREATE EXTENSION aurora_analytics;
```

Alternatively, to allow a non-superuser to create the extension, grant the `rds_extension` role and delegate this specific extension. Run the following as `rds_superuser`.

```
GRANT rds_extension TO your_user;
ALTER USER your_user SET rds.allowed_delegated_extensions = 'aurora_analytics';
```

The `rds_extension` grant alone is not sufficient. Without `aurora_analytics` in `rds.allowed_delegated_extensions`, `CREATE EXTENSION` fails with "This extension is not specified in \\"rds.allowed\_delegated\_extensions\\"". For more information, see *Using Amazon RDS delegated extension support for PostgreSQL*.

#### IAM role not active
<a name="aurora-analytics-ts-iam-role-not-active"></a>

**Symptom**: Foreign table queries fail with access denied errors, or the role status shows `Pending` instead of `Active`.

**Diagnostic**: Run the following command to check the role association status.

```
aws rds describe-db-clusters \
  --db-cluster-identifier <cluster-id> \
  --query "DBClusters[0].AssociatedRoles"
```

**Solution**: Use the following table to act on the status.


**IAM role status and action**  

| Status | Action | 
| --- | --- | 
| PENDING | Wait a few minutes. Role association is asynchronous. | 
| ACTIVE | Role is attached correctly. The issue is likely in the IAM policy. See the Amazon S3 and AWS Glue errors in the following sections. | 
| Not listed | Attach the role using add-role-to-db-cluster. | 

### Amazon S3 and data access errors
<a name="aurora-analytics-ts-data-access"></a>

The following are common Amazon S3 and data access errors.

#### Access denied reading Amazon S3
<a name="aurora-analytics-ts-s3-access-denied"></a>

**Symptom**: A foreign table query fails with the following error.

```
ERROR:  [Aurora Analytics] HTTP 403 Forbidden
```

**Causes and solutions**: Check the following.
+ IAM policy is missing `s3:GetObject`: add the permission for the specific Amazon S3 prefix.
+ IAM policy is missing `s3:ListBucket`: required when the location points to a folder rather than a single file.
+ Wrong Amazon S3 bucket or prefix in policy: verify that the ARN matches your foreign table location exactly.
+ Amazon S3 bucket in a different account: add a cross-account bucket policy that grants access to your Aurora role.
+ Amazon S3 VPC endpoint not configured: create an Amazon S3 gateway endpoint and associate it with Aurora's route tables.

**Diagnostic**: Run the following query to inspect the foreign table options.

```
SELECT ft.ftrelid::regclass, ftoptions
FROM pg_foreign_table ft
WHERE ft.ftrelid::regclass::text = 'ft_orders';
```

#### AWS Glue timeout or connection error
<a name="aurora-analytics-ts-glue-timeout"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: curlCode: 28, Timeout was reached; Connection timed out after 301 milliseconds
```

**Cause**: No AWS Glue VPC interface endpoint exists, or a security group is blocking TCP port 443.

**To resolve this issue**: Do the following.

1. Create an AWS Glue VPC interface endpoint in the same VPC as your Aurora DB cluster.

   ```
   aws ec2 create-vpc-endpoint \
     --vpc-id <vpc-id> \
     --vpc-endpoint-type Interface \
     --service-name com.amazonaws.<region>.glue \
     --subnet-ids <subnet-ids> \
     --security-group-ids <sg-id> \
     --private-dns-enabled
   ```

1. Make sure that the security group allows inbound TCP 443 from your VPC CIDR.

   ```
   aws ec2 authorize-security-group-ingress \
     --group-id <sg-id> \
     --protocol tcp \
     --port 443 \
     --cidr <vpc-cidr>
   ```

1. Verify that DNS resolution resolves to private IPs, not public AWS IPs.

   ```
   nslookup glue.<region>.amazonaws.com
   ```

#### AWS Glue table not found
<a name="aurora-analytics-ts-glue-not-found"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: EntityNotFoundException: Database not found: <name>

-- or

ERROR:  [Aurora Analytics] Glue GetTable API failed: EntityNotFoundException: Table not found: <name>
```

**Causes and solutions**: Use the following table to identify the cause and resolve it.


**AWS Glue table not found: causes and solutions**  

| Cause | Solution | 
| --- | --- | 
| Error in the database or table name. | Verify that names match exactly (case-sensitive). | 
| AWS Glue resource in a different AWS Region. | Make sure the AWS Glue ARN Region matches your VPC endpoint Region. | 
| IAM policy does not grant access to this database or table. | Add the specific AWS Glue ARN to your IAM policy. | 
| Table was deleted from AWS Glue. | Re-register the table in the AWS Glue Data Catalog. | 

**Diagnostic**: Run the following command.

```
aws glue get-table \
  --database-name <db> \
  --name <table> \
  --region <region>
```

#### Wrong format specified
<a name="aurora-analytics-ts-wrong-format"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] failed to fetch column information...
HINT:  If the S3 location contains Parquet files, verify the foreign table was created with format 'parquet' instead of 'iceberg'.
```

**Solution**: Recreate the foreign table with the correct format.

```
DROP FOREIGN TABLE ft_my_table;

CREATE FOREIGN TABLE ft_my_table ()
SERVER aurora_analytics_server
OPTIONS (
    location 's3://my-bucket/data/',
    format 'parquet',
    region 'us-east-1'
);
```

#### DNS resolution failure
<a name="aurora-analytics-ts-dns-failure"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: curlCode: 6, Could not resolve host: glue.<region>.amazonaws.com
```

**Cause**: Wrong Region in the AWS Glue ARN, or the VPC endpoint is not available in that Region.

**Solution**: Do the following.
+ Verify that the Region in your AWS Glue ARN matches the Region where your VPC endpoint is deployed.
+ Verify that the VPC endpoint has Private DNS enabled.

### Query performance issues
<a name="aurora-analytics-ts-performance"></a>

The following are common query performance issues.

#### Queries are slow
<a name="aurora-analytics-ts-slow-queries"></a>

**Symptom**: Queries take longer than expected.

**Causes and solutions**: Use the following table to identify why queries are slow and how to respond.


**Why queries are slow**  

| Cause | Signal that identifies it | Source | Action | 
| --- | --- | --- | --- | 
| Cold cache after a restart, failover, or first access. | AuroraAnalyticsCacheHitRatio low then recovering on an identical rerun, or pg\_postmaster\_start\_time() recent. | Amazon CloudWatch | Warm the cache by running typical queries. Subsequent runs are faster. | 
| Reads served from Amazon S3 instead of the cache. | AuroraAnalyticsCacheHitRatio stays low after warm-up, or analytics\_remote\_read\_bytes high versus analytics\_cache\_hit\_bytes. | Amazon CloudWatch, aurora\_analytics\_cache\_size(), aurora\_analytics\_stat\_statements() | Add filters so queries scan less data; if the working set exceeds the cache, scale to a larger instance for more cache. | 
| Query spilling to disk because query\_mem is too low. | analytics\_total\_disk\_spill greater than 0, AuroraAnalyticsDiskSpillSize rising. | Amazon CloudWatch, aurora\_analytics\_stat\_statements() | Reduce intermediate data first; raise query\_mem within headroom. | 
| Too many concurrent analytical sessions. | AuroraAnalyticsActiveThreads rising alongside DatabaseConnections. | Amazon CloudWatch | Reduce concurrency, or scale up. | 
| Foreign table queries consuming the instance CPU. | CPUUtilization sustained high, Extension:AuroraAnalyticsExecute dominating AAS. | Amazon CloudWatch, Database Insights | Reduce concurrency, or scale to more vCPUs. | 
| Many small or uncompressed objects in Amazon S3. |  | Amazon CloudWatch | Consolidate into larger files and use Snappy or ZSTD. See [Optimizing data layout in Amazon S3](aurora-analytics-data-layout.md). | 
| Query reading columns it does not need (SELECT \* on a wide table). | analytics\_remote\_read\_bytes far exceeding analytics\_total\_result\_size. | aurora\_analytics\_stat\_statements() | Select only the columns you need. | 
| Cross-Region Amazon S3 access after a Global Database switchover. | AuroraAnalyticsRemoteRead and AuroraAnalyticsS3GetRequest both elevated. | Amazon CloudWatch | Repoint foreign tables at a replica bucket in the local Region. See [Cross-Region Amazon S3 latency after switchover](#aurora-analytics-cross-region-latency). | 

**Useful queries**: To check whether queries are served from the cache or from Amazon S3, and whether they spill, run the following query.

```
SET aurora_analytics.track_detailed_metrics = true;
-- Run your query, then check per-query stats
SELECT query, analytics_cache_hit_bytes, analytics_remote_read_bytes, analytics_total_disk_spill
FROM aurora_analytics_stat_statements()
ORDER BY analytics_remote_read_bytes DESC;
```

If `analytics_remote_read_bytes` is high relative to `analytics_cache_hit_bytes`, the cache is cold or the working set exceeds cache capacity.

To check how many analytical sessions are active, run the following query.

```
SELECT COUNT(*) FROM pg_stat_activity a
WHERE a.state = 'active'
  AND EXISTS (
      SELECT 1 FROM pg_foreign_table ft
      JOIN pg_class c ON c.oid = ft.ftrelid
      JOIN pg_foreign_server fs ON fs.oid = ft.ftserver
      WHERE fs.srvname = 'aurora_analytics_server'
        AND a.query ILIKE '%' || c.relname || '%'
  );
```

#### Out of memory errors
<a name="aurora-analytics-ts-out-of-memory"></a>

**Symptom**: Two errors share the same `ERROR` line but differ in the `HINT` or `DETAIL`. In the first, the query needs more memory.

```
ERROR:  [Aurora Analytics] Out of Memory Error: Failed to allocate memory for query execution.
HINT:  Possible solution: Increasing the query mem (SET aurora_analytics.query_mem='...GB')
```

In the second, the DB instance is under instance-wide memory pressure.

```
ERROR:  [Aurora Analytics] Out of Memory Error: Failed to allocate memory for query execution.
DETAIL:  Transaction cancelled due to insufficient memory
```

**Cause**: Distinguish the two cases by the accompanying line.
+ `HINT` present, query memory too low. The query's working set exceeds its per-query `query_mem` budget. This is specific to the query, and retrying without changing anything does not help. The query fails the same way each time until you give it more memory or reduce the data it processes.
+ `DETAIL` present, instance memory pressure. The DB instance is under overall memory pressure, often from too many concurrent sessions, and Aurora's improved memory management cancelled the transaction to keep the instance stable. This is often transient, and a retry frequently succeeds once pressure clears.

**Confirm the cause with metrics**: Check the following.
+ `AuroraAnalyticsMemoryUsage` high relative to instance size, at the time of the error: analytics sessions are consuming the memory. Reduce concurrency or `query_mem` per session.
+ `FreeableMemory` low at the time of the error: the whole instance is under memory pressure, not just analytics, which is the `DETAIL` case.
+ `DatabaseConnections` spiking alongside the error: too many concurrent sessions are competing for memory.

**To resolve this issue**: Choose the path that matches the message. If the error carries a `HINT` (query memory too low), do the following.
+ Increase memory for the session, then rerun.

  ```
  SET aurora_analytics.query_mem = '16GB';
  -- Rerun your query
  ```
+ Optimize the query to reduce its working set. Add filters to reduce data volume before JOINs, break complex queries into stages using CTEs or temp tables, or reduce ORDER BY scope with LIMIT.
+ Scale up the instance if the workload legitimately requires more memory than the instance can budget per query.
+ Retrying the same query unchanged does not resolve this case.

If the error carries a `DETAIL` (instance memory pressure), do the following.
+ Retry the query. If the cause was transient instance-wide memory pressure, the query often succeeds after pressure is relieved.
+ Reduce concurrency. If many sessions are active, some may need to wait.
+ Scale up the instance to provide more memory for the same workload.

**Note**  
Aurora PostgreSQL improved memory management cancels transactions when the DB instance is under critical memory pressure, which prevents workload-induced DB instance restarts. This protection is enabled by default. For more information, see *Improved memory management in Aurora PostgreSQL* in the *Amazon Aurora User Guide*.

#### Out of storage due to query spills
<a name="aurora-analytics-ts-out-of-storage"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] could not write to temporary file: No space left on device
```

**Cause**: When a query's intermediate results exceed `query_mem`, the engine spills data to temporary local storage. If multiple concurrent queries are spilling simultaneously, or a single query spills a very large volume of data, local storage can be exhausted. `query_mem` is a per-query budget rather than an instance-wide pool, which means each concurrent query can spill its own overflow, and spill files share local storage with the read cache. Together these are why concurrency, rather than any single large query, is the usual trigger for exhaustion.

**Diagnostic**: Watch `AuroraAnalyticsDiskSpillSize` in Amazon CloudWatch for instance-wide spill volume, then attribute it to a backend.

```
SELECT pid,
       pg_size_pretty(disk_spill_size) AS spill,
       pg_size_pretty(current_memory_usage) AS mem_used,
       active_threads
FROM aurora_analytics_stat_resource_usage()
WHERE disk_spill_size > 0
ORDER BY disk_spill_size DESC;
```

**To resolve this issue**: Do the following.
+ Reduce concurrency. Fewer concurrent spilling sessions means less total disk pressure. This addresses the usual cause, takes effect on the next run, and needs no elevated privileges.
+ Optimize the query to reduce intermediate data volume. Add `LIMIT` to ORDER BY queries, add filters before joins to reduce cardinality, or pre-aggregate in subqueries before joining.
+ Check whether the read cache, rather than spill, is consuming local storage, and clear it only if it is (requires the `rds_superuser` role, and make sure no queries are running).

  ```
  -- Compare the cache size against the instance's local storage first
  SELECT aurora_analytics_cache_size();
  SELECT aurora_analytics_clear_cache();
  ```
+ Scale up the instance. Larger instances, especially `db.r8gd` variants, have more local NVMe storage for both cache and spills.

### Foreign table issues
<a name="aurora-analytics-ts-foreign-tables"></a>

The following are common foreign table issues.

#### Schema mismatch
<a name="aurora-analytics-ts-schema-mismatch"></a>

**Symptom**: A query fails with the following error, or returns incorrect data types.

```
ERROR:  column "column_name" does not exist
```

**Causes**: The column definitions do not match the actual Parquet or Iceberg schema, or the source schema changed after the foreign table was created.

**To resolve this issue**: If the foreign table already exists and only its column definitions have drifted from the source, refresh it in place with `aurora_analytics_refresh_foreign_table`, which reconciles the column definitions without dropping and recreating the table (preserving grants and dependent objects). For the full syntax and permissions, see [SQL functions reference](aurora-analytics-sql-functions-reference.md). The `apply_changes` argument is required: pass `false` to preview the changes without modifying the table, or `true` to apply them. Run a dry run first, then apply.

```
-- Preview the schema changes
SELECT aurora_analytics_refresh_foreign_table('ft_my_table', false);
-- Apply them
SELECT aurora_analytics_refresh_foreign_table('ft_my_table', true);
```

Alternatively, recreate the foreign table with schema inference.

```
DROP FOREIGN TABLE ft_my_table;
CREATE FOREIGN TABLE ft_my_table ()
SERVER aurora_analytics_server
OPTIONS (location 's3://...', format 'parquet', region 'us-east-1');
-- Check inferred schema
\d ft_my_table
```

**Note**  
If `aurora_analytics.lowercase_unquoted_column_name` is set to `true` (default), columns are lowercased. A Parquet column named `OrderDate` becomes `orderdate` in PostgreSQL.

#### Unsupported column type error
<a name="aurora-analytics-ts-unsupported-type"></a>

**Symptom**: Creating a foreign table fails with the following error.

```
ERROR:  unsupported data type for column "complex_column"
```

**Solution**: Enable skipping of unsupported columns, then recreate the foreign table. The unsupported columns are skipped.

```
SET aurora_analytics.skip_unsupported_columns = true;
-- Recreate the table, unsupported columns are skipped
DROP FOREIGN TABLE ft_my_table;
CREATE FOREIGN TABLE ft_my_table ()
SERVER aurora_analytics_server
OPTIONS (location 's3://...', format 'parquet', region 'us-east-1');
```

### Connection and session issues
<a name="aurora-analytics-ts-connections"></a>

The following are common connection and session issues.

#### Long-running queries blocking other work
<a name="aurora-analytics-ts-long-running"></a>

**Symptom**: A few analytical queries consume most of the instance's resources, slowing down performance. In Amazon CloudWatch, this shows up as sustained high `CPUUtilization` together with a high `AuroraAnalyticsActiveThreads` count, even though only a few sessions are active. Those sessions report the `Extension:AuroraAnalyticsExecute` wait event in the average active sessions (AAS) chart. A few sessions can drive high CPU because each analytical query runs on many worker threads; see [Interpreting the active thread count](#aurora-analytics-active-thread-count).

**Diagnostic**: Run the following query to find the long-running analytical queries.

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

**Solution**: Set a `statement_timeout` for analytical users to bound query runtime.

```
ALTER USER analyst SET statement_timeout = '30min';
```

To stop a query that is already running, cancel or terminate its backend.

```
SELECT pg_cancel_backend(<pid>);     -- cancel the query
SELECT pg_terminate_backend(<pid>);  -- terminate the session
```

#### Connection storms
<a name="aurora-analytics-ts-connection-storms"></a>

**Symptom**: `DatabaseConnections` spikes suddenly, and queries slow down or fail.

**Solution**: Implement connection pooling (for example, Amazon RDS Proxy) to manage analytical connections, and set appropriate `statement_timeout` values to prevent runaway queries.

### Global Database switchover and failover
<a name="aurora-analytics-ts-global-database"></a>

The following are common issues after a Global Database switchover or failover.

#### Cross-Region Amazon S3 latency after switchover
<a name="aurora-analytics-cross-region-latency"></a>

**Symptom**: After a Global Database switchover or failover, analytical queries become slower.

**Cause**: The foreign tables still point to Amazon S3 buckets in the original Region, so the new primary reads cross-Region.

**Confirm the cause with metrics**: Elevated `AuroraAnalyticsRemoteRead` and `AuroraAnalyticsS3GetRequest` after the switchover, especially when queries that previously served from cache now show sustained remote reads, indicate that the new primary is fetching from the original Region rather than locally. A low `AuroraAnalyticsCacheHitRatio` on the new primary is expected until its cache warms.

These volume metrics alone don't distinguish cross-Region reads from a cold cache re-warming locally, because both raise remote-read volume right after a switchover. Amazon S3 request latency is what separates them: a spike in per-request latency points to cross-Region reads, while a local cold cache re-warms at normal latency. Aurora PostgreSQL doesn't emit a remote-read latency metric, so to measure this, enable Amazon S3 Request Metrics on the bucket and watch `TotalRequestLatency` (average and p99) in the `AWS/S3` Amazon CloudWatch namespace. Amazon S3 Request Metrics are not enabled by default.

**To resolve this issue**: Do the following.
+ Replicate your data to the target Region before switchover or failover, for example with Amazon S3 Cross-Region Replication (CRR).
+ Make sure target-Region networking is ready (Amazon S3 gateway VPC endpoint, proper subnet routing).
+ After switchover or failover, update foreign table definitions to point to the local-Region replica bucket.

  ```
  ALTER FOREIGN TABLE ft_orders OPTIONS (SET location 's3://my-bucket-target-region/data/orders/');
  ALTER FOREIGN TABLE ft_orders OPTIONS (SET region 'us-west-2');
  ```
+ Wait for the replication to complete before expecting full performance on the new primary.

**Note**  
A foreign table's `location` and `region` are a single replicated definition, with no per-Region override. Repointing a foreign table to the new writer's Region makes the former primary read cross-Region instead, and no configuration lets both Regions read Region-locally at the same time.

#### Missing IAM role association in the secondary Region
<a name="aurora-analytics-ts-missing-iam-role"></a>

**Symptom**: Queries fail with the following error.

```
ERROR:  credential to access AWS service is unavailable
HINT:  Please attach IAM role with proper permission policy to this cluster with the feature name "AuroraAnalytics".
```

**Cause**: The IAM role was never associated with this Region's cluster.

**Solution**: Associate the IAM role with the feature name `AuroraAnalytics`, then wait for its status to become `Active`.

#### IAM role has no permissions in the secondary Region
<a name="aurora-analytics-ts-iam-no-permissions"></a>

**Symptom**: For Parquet in Amazon S3, queries fail with the following error.

```
ERROR:  [Aurora Analytics] Executor Error: ... HTTP 403 Forbidden
        AccessDenied: User: arn:aws:sts::<account>:assumed-role/AuroraAnalyticsRole/...
        is not authorized to perform: s3:GetObject on resource: "arn:aws:s3:::<bucket>/<key>"
```

For Iceberg through AWS Glue, queries fail with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: User: ... is not authorized to perform:
        glue:GetTable on resource: arn:aws:glue:<region>:<account>:catalog
```

**Cause**: The role is associated, but its policy lacks the required permissions.

**Solution**: Attach a policy that grants the required actions. The error names the exact action and resource that was denied.

#### No network path to Amazon S3 or AWS Glue in the secondary Region
<a name="aurora-analytics-ts-no-network-path"></a>

**Symptom**: For Amazon S3, queries fail with the following error.

```
ERROR:  [Aurora Analytics] Executor Error: ... Timeout was reached error for HTTP HEAD to
        'https://<bucket>.s3.<region>.amazonaws.com/<key>'
```

For AWS Glue, queries fail with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: curlCode: 28,
        Timeout was reached; Details: Connection timed out after 300 milliseconds
```

**Cause**: There is no VPC endpoint or NAT path in this Region's VPC.

**Solution**: Create an Amazon S3 gateway endpoint, an AWS Glue interface endpoint, and an AWS STS interface endpoint.

**Note**  
Amazon S3 timeouts are long, with minutes of retries. Set `statement_timeout` and use retry logic.

### Enabling detailed logging
<a name="aurora-analytics-ts-detailed-logging"></a>

For transient or hard-to-reproduce issues, enable verbose logging temporarily.

```
-- As rds_superuser
SET aurora_analytics.enable_logging = true;
SET aurora_analytics.logging_level = 'DEBUG1';

-- Reproduce the issue
SELECT * FROM ft_problematic_table WHERE ...;

-- Reset logging level after investigation
RESET aurora_analytics.logging_level;
RESET aurora_analytics.enable_logging;
```

Analytics engine diagnostic messages are written to the PostgreSQL error log. For the parameter reference and the three ways to retrieve the log, see [Logging](#aurora-analytics-logging).
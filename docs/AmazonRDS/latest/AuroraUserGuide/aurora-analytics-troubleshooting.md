

# Troubleshooting
<a name="aurora-analytics-troubleshooting"></a>

This topic describes specific symptoms, their causes, and how to resolve them. For the metrics, wait events, and diagnostic queries used to watch a workload, see [Monitoring](aurora-analytics-monitoring.md).

## Setup and configuration issues
<a name="aurora-analytics-ts-setup"></a>

The following are common setup and configuration issues.

### Extension not available
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

### Feature not enabled
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

### Permission denied to create extension
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

### IAM role not active
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

## Amazon S3 and data access errors
<a name="aurora-analytics-ts-data-access"></a>

The following are common Amazon S3 and data access errors.

### Access denied reading Amazon S3
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

### AWS Glue timeout or connection error
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

### AWS Glue table not found
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

### Wrong format specified
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

### DNS resolution failure
<a name="aurora-analytics-ts-dns-failure"></a>

**Symptom**: A query fails with the following error.

```
ERROR:  [Aurora Analytics] Glue GetTable API failed: curlCode: 6, Could not resolve host: glue.<region>.amazonaws.com
```

**Cause**: Wrong Region in the AWS Glue ARN, or the VPC endpoint is not available in that Region.

**Solution**: Do the following.
+ Verify that the Region in your AWS Glue ARN matches the Region where your VPC endpoint is deployed.
+ Verify that the VPC endpoint has Private DNS enabled.

## Query performance issues
<a name="aurora-analytics-ts-performance"></a>

The following are common query performance issues.

### Queries are slow
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

### Out of memory errors
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

### Out of storage due to query spills
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

## Foreign table issues
<a name="aurora-analytics-ts-foreign-tables"></a>

The following are common foreign table issues.

### Schema mismatch
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

### Unsupported column type error
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

## Connection and session issues
<a name="aurora-analytics-ts-connections"></a>

The following are common connection and session issues.

### Long-running queries blocking other work
<a name="aurora-analytics-ts-long-running"></a>

**Symptom**: A few analytical queries consume most of the instance's resources, slowing down performance. In Amazon CloudWatch, this shows up as sustained high `CPUUtilization` together with a high `AuroraAnalyticsActiveThreads` count, even though only a few sessions are active. Those sessions report the `Extension:AuroraAnalyticsExecute` wait event in the average active sessions (AAS) chart. A few sessions can drive high CPU because each analytical query runs on many worker threads; see [Interpreting the active thread count](aurora-analytics-monitoring.md#aurora-analytics-active-thread-count).

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

### Connection storms
<a name="aurora-analytics-ts-connection-storms"></a>

**Symptom**: `DatabaseConnections` spikes suddenly, and queries slow down or fail.

**Solution**: Implement connection pooling (for example, Amazon RDS Proxy) to manage analytical connections, and set appropriate `statement_timeout` values to prevent runaway queries.

## Global Database switchover and failover
<a name="aurora-analytics-ts-global-database"></a>

The following are common issues after a Global Database switchover or failover.

### Cross-Region Amazon S3 latency after switchover
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

### Missing IAM role association in the secondary Region
<a name="aurora-analytics-ts-missing-iam-role"></a>

**Symptom**: Queries fail with the following error.

```
ERROR:  credential to access AWS service is unavailable
HINT:  Please attach IAM role with proper permission policy to this cluster with the feature name "AuroraAnalytics".
```

**Cause**: The IAM role was never associated with this Region's cluster.

**Solution**: Associate the IAM role with the feature name `AuroraAnalytics`, then wait for its status to become `Active`.

### IAM role has no permissions in the secondary Region
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

### No network path to Amazon S3 or AWS Glue in the secondary Region
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

## Enabling detailed logging
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

Analytics engine diagnostic messages are written to the PostgreSQL error log. For the parameter reference and the three ways to retrieve the log, see [Logging](aurora-analytics-monitoring.md#aurora-analytics-logging).
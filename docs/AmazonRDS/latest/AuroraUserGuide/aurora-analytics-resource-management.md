

# Resource management
<a name="aurora-analytics-resource-management"></a>

Aurora PostgreSQL manages four types of resources to run queries against foreign tables that reference your Iceberg and Parquet data.
+ **Query memory**: The working memory (from instance memory) that a query uses for hash tables, sorting, aggregation, and intermediate results, controlled by the `aurora_analytics.query_mem` parameter. For more information, see [Query memory](#aurora-analytics-query-memory).
+ **Disk spilling**: When a query exceeds its memory budget, Aurora PostgreSQL writes intermediate data to temporary files on local storage and then automatically deletes them when the query finishes. This allows most large queries to complete without failing, though queries with very large intermediate results might still exhaust the available spill space. For more information, see [Disk spilling](#aurora-analytics-disk-spilling).
+ **Worker threads**: The CPU parallelism the engine uses to run a query. Aurora manages this automatically and scales it from the query's memory budget. For more information, see [Worker threads](#aurora-analytics-worker-threads).
+ **On-disk read cache**: Local storage (NVMe or Amazon EBS) that caches Amazon S3 data so repeated reads are served locally. For more information, see [On-disk read cache](#aurora-analytics-on-disk-read-cache).

This topic explains how each resource is allocated, how they interact, and how you can tune them for your workload.

**Topics**
+ [Query memory](#aurora-analytics-query-memory)
+ [Disk spilling](#aurora-analytics-disk-spilling)
+ [Worker threads](#aurora-analytics-worker-threads)
+ [On-disk read cache](#aurora-analytics-on-disk-read-cache)
+ [Memory protection (query cancellation under memory pressure)](#aurora-analytics-memory-protection)

## Query memory
<a name="aurora-analytics-query-memory"></a>

Aurora PostgreSQL allocates a per-query memory budget from instance memory for hash tables, sorting, aggregation buffers, and intermediate results during query execution. The `aurora_analytics.query_mem` parameter controls this budget, and it works as follows.
+ It sets the maximum memory a single query can use.
+ You can specify it as a string with a unit (for example, `'4GB'` or `'16GB'`) or as an integer in kilobytes (kB).
+ The effective limit is capped at instance memory minus the memory reserved for PostgreSQL `shared_buffers`. Setting `query_mem` above that cap has no additional effect.
+ When a query's intermediate results exceed its budget, Aurora PostgreSQL spills to temporary local storage so the query still completes instead of failing. For more information, see [Disk spilling](#aurora-analytics-disk-spilling).
+ Its default value is derived from instance memory.

### Memory budget across concurrent sessions
<a name="aurora-analytics-query-memory-concurrent"></a>

By default, `shared_buffers` reserves approximately two-thirds of instance memory. The remainder is shared by `query_mem` and PostgreSQL's other memory needs. Queries involving foreign tables do not use `shared_buffers`, which leaves the effective memory available for concurrent foreign table queries at roughly the following.

```
available_memory ≈ instance_memory − shared_buffers
```

If you run workloads that are predominantly foreign table queries, reducing `shared_buffers` frees more memory for `query_mem` and is often the most effective tuning step.

Aurora PostgreSQL includes built-in memory protection that cancels queries when system-wide memory pressure becomes critical. To reduce the risk of cancellations, do the following.
+ Reduce `shared_buffers`.
+ Lower `query_mem`.
+ Limit concurrent sessions.

Because actual memory consumption per query varies with the data and the plan, there is no fixed formula for the safe number of concurrent queries. Monitor `AuroraAnalyticsMemoryUsage` in Amazon CloudWatch and adjust the preceding settings based on observed memory pressure.

## Disk spilling
<a name="aurora-analytics-disk-spilling"></a>

When a query's intermediate results exceed `query_mem`, Aurora PostgreSQL spills data to temporary files on local storage. Due to the spill, the query completes slowly instead of failing with an out-of-memory error.

### Common causes of spilling
<a name="aurora-analytics-disk-spilling-causes"></a>

The following are common causes of spilling.
+ Large `ORDER BY` without `LIMIT`.
+ Hash joins between two large unfiltered tables.
+ `GROUP BY` with high cardinality (millions of distinct groups).

### Performance impact
<a name="aurora-analytics-disk-spilling-performance"></a>

Spilling lets a query finish even when its data is larger than memory, but it does not guarantee completion. Queries with very large intermediate results might still exhaust the available spill space. Because reading and writing to disk is slower than working in memory, a query that spills runs more slowly than one that stays in memory. If a query spills often, increase memory or reduce the data it processes.

### Impact on other workloads
<a name="aurora-analytics-disk-spilling-other-workloads"></a>

Spilling creates I/O contention on the same local storage used by the read cache. When multiple concurrent sessions spill simultaneously, the following can occur.
+ **Disk space is shared**: Spill files and the read cache both occupy local storage.
+ **OLTP impact**: On instances running mixed workloads, heavy spilling can create local storage I/O contention that indirectly affects local PostgreSQL operations.

The following table compares spilling, out-of-memory errors, and query cancellation.


**Spilling compared with out-of-memory errors and query cancellation**  

| Scenario | What happens | Query completes? | 
| --- | --- | --- | 
| Intermediate results exceed query\_mem | Spills to local storage, query runs slowly | Yes | 
| Cannot allocate memory due to insufficient query\_mem | out of memory error | No | 
| System-wide memory pressure is critical | Query cancelled by memory protection | No | 
| Spill files exhaust local storage | No space left on device error | No | 

Monitor the Amazon CloudWatch metric `AuroraAnalyticsDiskSpillSize` to detect when queries are routinely spilling, and consider increasing `query_mem` or optimizing the query.

## Worker threads
<a name="aurora-analytics-worker-threads"></a>

Aurora PostgreSQL uses a multi-threaded execution engine for each query. Threads are used for both computation and cache I/O (fetching data from the on-disk cache or Amazon S3).
+ **Query execution threads**: Execute the query plan. Aurora PostgreSQL manages the number of these threads automatically, scaled from the query's memory budget.
+ **Cache I/O threads**: Read from the on-disk cache or download Amazon S3 data in parallel on cache misses. These are separate from query execution threads and are also managed internally.

Both kinds of threads are internal to the engine and managed by Aurora PostgreSQL. You do not configure either one.

The `AuroraAnalyticsActiveThreads` Amazon CloudWatch metric reports the active worker threads. For how to interpret it, see [Interpreting the active thread count](aurora-analytics-monitoring-troubleshooting.md#aurora-analytics-active-thread-count).

## On-disk read cache
<a name="aurora-analytics-on-disk-read-cache"></a>

Aurora PostgreSQL caches data fetched from Amazon S3 on local storage to accelerate repeated access. The cache is sized automatically based on the instance's available memory and storage, and a larger instance provides a larger cache. On instances with local NVMe storage (such as `db.r8gd`) and using Aurora I/O-Optimized, the cache uses NVMe for higher performance. On Amazon EBS-only instances (such as `db.r8g` and `db.r8i`), the cache uses Amazon EBS storage.

On the first query, data is fetched from Amazon S3 in fixed-size blocks and stored in the read cache, and that first read's latency includes the Amazon S3 network round-trip. Subsequent queries read that data from local storage at NVMe or Amazon EBS speeds, which is significantly faster than reading from Amazon S3. A background worker monitors cache and disk usage and evicts the oldest (least-recently-accessed) blocks when thresholds are exceeded.

**Note**  
The on-disk cache is cleared when a DB instance restarts or fails over.

### Cache and data freshness
<a name="aurora-analytics-on-disk-read-cache-freshness"></a>

New Parquet files added to an existing Amazon S3 prefix are discovered and cached on the next query, and for Iceberg tables the cache never affects which snapshot you see. If you overwrite an existing Parquet file, an open connection can read stale data briefly because it holds a cached file handle. To see the updated data right away, reconnect. You do not need to clear the cache.

### Cache management functions
<a name="aurora-analytics-on-disk-read-cache-functions"></a>

Aurora PostgreSQL provides the following functions to manage the on-disk read cache.


**Cache management functions**  

| Function | Description | Required permission | 
| --- | --- | --- | 
| aurora\_analytics\_cache\_size() | Returns the current cache size in bytes. | All users. | 
| aurora\_analytics\_clear\_cache() | Clears the entire on-disk cache. | rds\_superuser only. | 

### When to clear the cache
<a name="aurora-analytics-on-disk-read-cache-clear"></a>

Consider clearing the cache in the following situations.
+ **Disk space pressure**: When the `FreeLocalStorage` or `FreeEphemeralStorage` Amazon CloudWatch metrics are low and you need immediate disk space for query spills.
+ **Performance testing**: When benchmarking cold-cache performance.

## Memory protection (query cancellation under memory pressure)
<a name="aurora-analytics-memory-protection"></a>

Aurora PostgreSQL includes a built-in memory protection mechanism that prevents runaway queries from consuming all instance memory and forcing the DB instance to restart. When free instance memory drops low enough that continuing to allocate would risk the stability of the DB instance, Aurora PostgreSQL gracefully cancels an in-progress query to reduce pressure and keep the DB instance stable for all workloads. The threshold is managed by Aurora based on available instance memory. It is not a value you configure.

This protection is provided by the Aurora PostgreSQL improved memory management feature, which is enabled by default. For more information, see [Improved memory management in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.html) in the *Amazon Aurora User Guide*.

### How it works
<a name="aurora-analytics-memory-protection-how-it-works"></a>

When total memory consumption by sessions running foreign table queries approaches the point where further allocation would risk DB instance stability, the mechanism cancels one or more currently running queries to reduce memory pressure. It acts on in-progress queries that are consuming memory, not on queries that have not started yet. A new query submitted after pressure is relieved runs normally. The cancelled query receives an error, but the DB instance remains stable and all other sessions continue unaffected.

When a query is cancelled, it returns the following error.

```
ERROR:  [Aurora Analytics] Out of Memory Error: Failed to allocate memory for query execution.
DETAIL:  Transaction cancelled due to insufficient memory
```

### How to reduce query cancellations
<a name="aurora-analytics-memory-protection-reduce"></a>

To reduce query cancellations, do the following.
+ **Reduce per-session memory**: Lower `query_mem` so each session uses less memory, allowing more headroom.
+ **Reduce concurrency**: Fewer concurrent foreign table queries means less total memory pressure.
+ **Scale up the instance**: A larger DB instance provides more instance memory for the same workload.

**Note**  
Improved memory management is controlled by the `rds.enable_memory_management` parameter (enabled by default). We recommend keeping it enabled. Disabling it removes the protection against workload-induced DB instance restarts from memory exhaustion. For more information, see [Improved memory management in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.html) in the *Amazon Aurora User Guide*.

**Note**  
Queries run by users with the `rds_superuser` role are exempt from memory pressure cancellation.
For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Monitoring and Configuration Optimization for Timestream for InfluxDB 2

## Overview

Effective monitoring and configuration optimization are critical for maintaining optimal performance, reliability, and cost-efficiency in your Timestream for InfluxDB deployment. This guide provides comprehensive guidance on CloudWatch metrics, performance thresholds, and configuration tuning strategies to help you proactively manage your InfluxDB instances.

## CloudWatch Metrics Reference

Amazon CloudWatch provides detailed metrics for monitoring your Timestream for InfluxDB instances. Understanding these metrics and their thresholds is essential for maintaining system health and performance.

### Resource Utilization Metrics

| CloudWatch Metric Name | Dimensions     | Description                         | Unit    | Recommended Thresholds                                                                    |
| ---------------------- | -------------- | ----------------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| CPUUtilization         | DbInstanceName | Percentage of CPU being used        | Percent | • Development/Growing: < 70%<br>• Production: < 80%<br>• Critical Alert: > 90% for 5+ min |
| MemoryUtilization      | DbInstanceName | Percentage of memory being used     | Percent | • Development/Growing: < 70%<br>• Production: < 80%<br>• Critical Alert: > 90%            |
| HeapMemoryUsage        | DbInstanceName | Amount of heap memory in use        | Bytes   | • Monitor for steady growth or spikes<br>• Alert: Approaching max heap size               |
| ActiveMemoryAllocation | DbInstanceName | Current active memory allocation    | Bytes   | • Monitor for unexpected spikes<br>• Compare against total available memory               |
| DiskUtilization        | DbInstanceName | Percentage of disk space being used | Percent | • Development/Growing: < 70%<br>• Production: < 75%<br>• Critical Alert: > 85%            |

### I/O Operations Metrics

| CloudWatch Metric Name | Dimensions     | Description                                    | Unit         | Recommended Thresholds                                                                    |
| ---------------------- | -------------- | ---------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------- |
| ReadOpsPerSec          | DbInstanceName | Number of read operations per second           | Count/Second | Maintain ≥ 30% headroom below provisioned IOPSExample: 12K IOPS → keep < 8,400 IOPS total |
| WriteOpsPerSec         | DbInstanceName | Number of write operations per second          | Count/Second | Maintain ≥ 30% headroom below provisioned IOPSExample: 12K IOPS → keep < 8,400 IOPS total |
| TotalIOpsPerSec        | DbInstanceName | Total I/O operations per second (read + write) | Count/Second | Maintain ≥ 30% headroom below provisioned IOPSMonitor against instance class capabilities |

### Throughput Metrics

| CloudWatch Metric Name | Dimensions     | Description           | Unit         | Recommended Thresholds                    |
| ---------------------- | -------------- | --------------------- | ------------ | ----------------------------------------- |
| ReadThroughput         | DbInstanceName | Data read throughput  | Bytes/Second | Monitor against storage throughput limits |
| WriteThroughput        | DbInstanceName | Data write throughput | Bytes/Second | Monitor against storage throughput limits |

### API Performance Metrics

| CloudWatch Metric Name | Dimensions                       | Description                                                                  | Unit         | Recommended Thresholds                                                                                                      |
| ---------------------- | -------------------------------- | ---------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| APIRequestRate         | DbInstanceName, Endpoint, Status | Rate of API requests to specific endpoints with status codes (2xx, 4xx, 5xx) | Count/Second | Error rates:<br>• 4xx errors: < 1% of requests<br>• 5xx errors: < 0.1% of requests<br>• Alert: Sudden spikes in error rates |
| QueryResponseVolume    | DbInstanceName, Endpoint, Status | Volume of query responses by endpoint and status code                        | Bytes        | • Monitor for unusually large responses<br>• Alert: Responses > 10MB consistently                                           |

### Query Execution Metrics

| CloudWatch Metric Name | Dimensions             | Description                                                                                       | Unit  | Recommended Thresholds                                                                                             |
| ---------------------- | ---------------------- | ------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| QueryRequestsTotal     | DbInstanceName, Result | Total count of query requests by result type (success, runtime_error, compile_error, queue_error) | Count | Success rate: > 99%<br>Error rates:<br>• runtime_error: < 0.5%<br>• compile_error: < 0.1%<br>• queue_error: < 0.1% |

### Data Organization Metrics

| CloudWatch Metric Name | Dimensions             | Description                              | Unit  | Critical Thresholds                                                                                                                                                                                                      |
| ---------------------- | ---------------------- | ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SeriesCardinality      | DbInstanceName, Bucket | Number of unique time series in a bucket | Count | • < 100K: Excellent performance<br>• < 1M: Good performance<br>• 1M - 5M: Moderate impact, requires tuning<br>• 5M - 10M: Significant impact, careful optimization required<br>• > 10M: CRITICAL - Consider InfluxDB 3.0 |
| TotalBuckets           | DbInstanceName         | Total number of buckets in the instance  | Count | • Monitor growth over time<br>• Consider consolidation if > 100 buckets                                                                                                                                                  |

### System Health Metrics

| CloudWatch Metric Name | Dimensions     | Description                               | Unit    | Recommended Thresholds                                           |
| ---------------------- | -------------- | ----------------------------------------- | ------- | ---------------------------------------------------------------- |
| EngineUptime           | DbInstanceName | Time the InfluxDB engine has been running | Seconds | Monitor for unexpected restartsAlert: Uptime resets unexpectedly |
| WriteTimeouts          | DbInstanceName | Number of write operations that timed out | Count   | Alert: > 0.1% of write operationsCritical: Increasing trend      |

### Task Management Metrics

| CloudWatch Metric Name | Dimensions     | Description                      | Unit  | Recommended Thresholds                                                     |
| ---------------------- | -------------- | -------------------------------- | ----- | -------------------------------------------------------------------------- |
| ActiveTaskWorkers      | DbInstanceName | Number of active task workers    | Count | Monitor against configured task worker limitAlert: Consistently at maximum |
| TaskExecutionFailures  | DbInstanceName | Number of failed task executions | Count | Alert: > 1% of task executionsCritical: Increasing failure rate            |

### Understanding Key Metric Relationships

#### IOPS and Throughput Relationship

**The 30% Headroom Rule:** Always maintain at least **30% headroom** between your sustained operations per second and your provisioned IOPS. This provides buffer for:

- Compaction operations (can spike IOPS significantly)
- Any database restart to run smoothly
- Query bursts during peak usage
- Write spikes from batch ingestion
- Index maintenance operations

**Example Calculation:**

- Provisioned IOPS: 12,000
- Target Maximum Sustained IOPS (TotalIOpsPerSec): 8,400 (70% utilization)
- Reserved Headroom: 3,600 IOPS (30%)

If TotalIOpsPerSec consistently exceeds 8,400: → Upgrade storage tier or optimize workload

**Monitoring Formula:**

IOPS Utilization % = (ReadOpsPerSec + WriteOpsPerSec) / Provisioned IOPS × 100

- Target: Keep IOPS Utilization < 70%
- Warning: IOPS Utilization > 70%
- Critical: IOPS Utilization > 90%

### Understanding Series Cardinality Performance Impact

Series cardinality has a multiplicative effect on system resources:

| **Series Count** | **Memory Impact** | **Query Performance Impact** | **Index Size Impact** | **Recommendation**                |
| ---------------- | ----------------- | ---------------------------- | --------------------- | --------------------------------- |
| < 100K           | Minimal           | Negligible                   | Small                 | Standard configuration            |
| 100K<br>• 1M     | Moderate          | 10-20% slower                | Medium                | Tune cache settings               |
| 1M<br>• 5M       | Significant       | 30-50% slower                | Large                 | Aggressive optimization required  |
| 5M<br>• 10M      | High              | 50-70% slower                | Very Large            | Maximum tuning, consider redesign |
| > 10M            | Severe            | 70%+ slower                  | Excessive             | **Migrate to InfluxDB 3.0**       |

**Why 10M is the Critical Threshold:**

- InfluxDB 2.x architecture uses in-memory indexing
- Beyond 10M series, index operations become prohibitively expensive
- Memory requirements grow non-linearly
- Query planning overhead increases dramatically
- InfluxDB 3.0 uses a columnar storage engine designed for high cardinality

## Instance Sizing and Performance Guidelines

The following table provides guidance on appropriate instance sizing based on your series cardinality and workload characteristics:

| **Max Series Count** | **Writes (lines/sec)** | **Reads (queries/sec)** | **Recommended Instance**    | **Storage Type**       | **Use Case**                            |
| -------------------- | ---------------------- | ----------------------- | --------------------------- | ---------------------- | --------------------------------------- |
| **< 100K**           | ~50,000                | < 10                    | db.influx.large             | Influx IO Included 3K  | Small deployments, development, testing |
| **< 1M**             | ~150,000               | < 25                    | db.influx.2xlarge           | Influx IO Included 3K  | Small to medium production workloads    |
| **~1M**              | ~200,000               | ~25                     | db.influx.4xlarge           | Influx IO Included 3K  | Medium production workloads             |
| **< 5M**             | ~250,000               | ~35                     | db.influx.4xlarge           | Influx IO Included 12K | Large production workloads              |
| **< 10M**            | ~500,000               | ~50                     | db.influx.8xlarge           | Influx IO Included 12K | Very large production workloads         |
| **~10M**             | < 750,000              | < 100                   | db.influx.12xlarge          | Influx IO Included 12K | Maximum InfluxDB 2.x capacity           |
| **> 10M**            | N/A                    | N/A                     | **Migrate to InfluxDB 3.0** | N/A                    | Beyond InfluxDB 2.x optimal range       |

## Configuration Optimization by Metric

### High CPU Utilization (CPUUtilization > 70%)

**Symptoms:**

- **CPUUtilization** > 70% sustained
- **QueryRequestsTotal** (high volume or slow queries)
- **ActiveTaskWorkers** (high task load)

**Configuration Adjustments:**

**Priority 1: Control Query Concurrency**

- query-concurrency: Set to 50-75% of vCPU count
- Example: 8 vCPU instance → query-concurrency = 4-6

**Priority 2: Limit Query Complexity**

- influxql-max-select-series: 10000 (prevent unbounded queries)
- influxql-max-select-point: 100000000
- query-queue-size: 2048 (prevent queue buildup)

**Priority 3: Enable Query Analysis**

- flux-log-enabled: TRUE (temporarily for debugging)
- log-level: info (or debug for detailed analysis)

**Important Considerations:**

Reducing `query-concurrency` will limit the number of queries that can execute simultaneously, which may increase queued queries and lead to higher query latency during peak periods. Users may experience slower dashboard loads or report timeouts if query demand exceeds the reduced concurrency limit.

Setting protective limits (`influxql-max-select-series`, `influxql-max-select-point`) will cause queries that exceed these thresholds to fail with **compile_error** or **runtime_error** in **QueryRequestsTotal**. While this protects the system from resource exhaustion, it may break existing queries that previously worked.

**Best Practice:** Before applying these changes, analyze your query patterns using **QueryResponseVolume** and **QueryRequestsTotal** metrics. Identify and optimize the most expensive queries first - look for queries without time range filters, queries spanning high-cardinality series, or queries requesting excessive data points. Optimizing queries at the application level is always preferable to imposing hard limits that may break functionality.

**Hardware Actions:**

- Scale to next instance class with more vCPUs
- Review query patterns for optimization opportunities

### High Memory Utilization (MemoryUtilization > 70%)

**Symptoms:**

- **MemoryUtilization** > 70% sustained
- **HeapMemoryUsage** trending upward
- **ActiveMemoryAllocation** showing spikes
- **SeriesCardinality** (high cardinality increases memory usage)

**Configuration Adjustments:**

**Priority 1: Reduce Cache Memory**

- storage-cache-max-memory-size: Set to 10-15% of total RAM
- Example: 32GB RAM → 3,355,443,200 to 5,033,164,800 bytes
- storage-cache-snapshot-memory-size: 26,214,400 (25MB)

**Priority 2: Limit Query Memory**

- query-memory-bytes: Set to 60-70% of total RAM
- query-max-memory-bytes: Same as query-memory-bytes
- query-initial-memory-bytes: 10% of query-memory-bytes

**Priority 3: Optimize Series Cache**

- storage-series-id-set-cache-size: Reduce if high cardinality
- High memory: 100-200
- Normal: 500-1000

**Important Considerations:**

While these changes will reduce memory pressure, they will have a direct negative impact on application performance. Reducing `storage-cache-max-memory-size` means less data is cached in memory, forcing more disk reads and increasing query latency - you'll likely see **ReadOpsPerSec** increase and **QueryResponseVolume** response times degrade.

Limiting `query-memory-bytes` will cause memory-intensive queries to fail with **runtime_error** in **QueryRequestsTotal**, particularly queries that aggregate large datasets or return substantial result sets. Users may encounter "out of memory" errors for queries that previously succeeded.

Reducing `storage-series-id-set-cache-size` degrades performance for queries against high-cardinality data, as the system must recalculate series results more frequently instead of retrieving them from cache. This particularly impacts dashboards that repeatedly query the same series combinations.

**Best Practice:** Before applying these restrictive changes, analyze your query patterns and optimize them first:

- Review **QueryResponseVolume** to identify queries returning excessive data
- Use **QueryRequestsTotal** to find frequently executed queries that could benefit from optimization
- Add time range filters to reduce data scanning to what's necessary for your workload
- Implement query result caching at the application level
- Consider pre-aggregating data using downsampling tasks
- Review **SeriesCardinality** and optimize your data model to reduce unnecessary tags

Query optimization should always be your first approach - configuration restrictions should be a last resort when optimization isn't sufficient.

**Hardware Actions:**

- Increase instance size for more RAM

### High Storage Utilization (DiskUtilization > 70%)

**CloudWatch Metrics to Monitor:**

- **DiskUtilization** > 70%
- **WriteThroughput** patterns
- **TotalBuckets** (many buckets increase overhead)

**Configuration Adjustments:**

**Priority 1: Check Logging Configuration**

- log-level: Ensure set to "info" (not "debug")
- flux-log-enabled: Set to FALSE unless actively debugging

**Priority 2: Aggressive Retention**

- storage-retention-check-interval: 15m0s (more frequent cleanup)

**Priority 3: Optimize Compaction**

- storage-compact-full-write-cold-duration: 2h0m0s (more frequent)
- storage-cache-snapshot-write-cold-duration: 5m0s

**Priority 4: Reduce Index Size**

- storage-max-index-log-file-size: 524,288 (512KB for faster compaction)

**Important Considerations:**

**Critical First Step - Check Your Logging Configuration:** Before making any other changes, verify your logging settings. **Debug logging and Flux query logs can consume as much or more disk space than your actual time-series data**, and this is one of the most common causes of unexpected storage exhaustion.

**Logging Impact:**

- `log-level: debug` generates extremely verbose logs, potentially hundreds of MB per hour
- `flux-log-enabled: TRUE` logs every Flux query execution with full details, creating massive log files
- These logs accumulate rapidly and are often overlooked during capacity planning
- Log files can fill disk space faster than data ingestion, especially on smaller instances
- Unlike time-series data, logs are kept in local storage for 24 hours before deletion

**Immediate Actions if Logs are Large:**

1. Set `log-level: info` (from debug)
2. Set `flux-log-enabled: FALSE`
3. Monitor **DiskUtilization** for immediate improvement

**Compaction Configuration Trade-offs:**

These configuration changes are specifically designed for workloads with **high ingestion throughput and short retention windows** where disk usage fluctuates substantially. They force the compaction engine to work more aggressively, which is only beneficial in specific scenarios.

**Critical Trade-offs:** Increasing compaction frequency will significantly increase resource consumption:

- **CPUUtilization** will rise as compaction operations consume CPU cycles
- **MemoryUtilization** will increase during compaction as data is loaded and processed
- **WriteOpsPerSec** and **WriteThroughput** will spike during compaction windows, potentially exceeding your 30% IOPS headroom
- **WriteTimeouts** may increase if compaction I/O competes with application writes

These changes can create a cascading performance problem where aggressive compaction consumes resources needed for query and write operations, degrading overall system performance even while reducing disk usage.

**Best Practice:** Before adjusting compaction settings, focus on data and logging management:

1. **Check Logging First (Most Common Issue):** Verify log-level is "info" and flux-log-enabled is FALSE
2. **Review Your Data Model:** Are you writing data you don't actually need? Can you reduce measurement or field granularity?
3. **Optimize Retention Policies:** Check **TotalBuckets** and review retention settings for each bucket
4. **Monitor Compaction Impact:** Baseline your **CPUUtilization**, **MemoryUtilization**, and **WriteOpsPerSec** before changes

**Alternative Approaches:**

- Increase storage capacity (often simpler and more cost-effective)
- Implement data downsampling or aggregation strategies
- Consolidate buckets (reduce **TotalBuckets**) to decrease overhead
- Review and enforce retention policies more strictly

Only apply aggressive compaction settings if you've optimized data management and confirmed your instance has sufficient CPU, memory, and IOPS headroom to handle the increased load.

**Hardware Actions:**

- Increase storage capacity

### High IOPS Utilization (ReadIOPS/WriteIOPS/TotalOperationsPerSecond > 70% of provisioned)

**CloudWatch Metrics to Monitor:**

- **ReadOpsPerSec** + **WriteOpsPerSec** = **TotalIOpsPerSec**
- **ReadThroughput** and **WriteThroughput**
- Compare against provisioned IOPS (3K, 12K, or 16K)

**Configuration Adjustments:**

**Priority 1: Control Compaction I/O**

- storage-max-concurrent-compactions: 2-3 (limit concurrent compactions)
- storage-compact-throughput-burst: Adjust based on disk capability
- 3K IOPS: 25,165,824 (24MB/s)
- 12K IOPS: 50,331,648 (48MB/s)

**Priority 2: Optimize Write Operations**

- storage-wal-max-concurrent-writes: 8-12
- storage-wal-max-write-delay: 5m0s

**Priority 3: Adjust Snapshot Timing**

- storage-cache-snapshot-write-cold-duration: 15m0s (less frequent)
- storage-compact-full-write-cold-duration: 6h0m0s (less frequent)

**Important Considerations:**

These changes create significant trade-offs between I/O utilization and system performance:

**Limiting Compaction I/O:**

- Reducing `storage-max-concurrent-compactions` will slow down compaction operations, causing TSM files to accumulate and **DiskUtilization** to increase more rapidly
- Lower `storage-compact-throughput-burst` extends compaction duration, keeping the compactor active longer and potentially blocking other operations
- Slower compaction means query performance degrades over time as the storage engine must read from more, smaller TSM files instead of consolidated ones
- You may see **QueryRequestsTotal** runtime_error rates increase as queries timeout while waiting for I/O

**Reducing Snapshot Frequency:**

- Increasing `storage-cache-snapshot-write-cold-duration` and `storage-compact-full-write-cold-duration` means data stays in the write-ahead log (WAL) longer
- This increases **MemoryUtilization** as more data is held in cache before being flushed to disk
- Risk of data loss increases slightly if the instance crashes before cached data is persisted
- Recovery time after a restart increases as more WAL data must be replayed

**Write Operation Tuning:**

- Reducing `storage-wal-max-concurrent-writes` will serialize write operations more, potentially increasing **WriteTimeouts** during high-throughput periods
- Increasing `storage-wal-max-write-delay` means writes may wait longer before being rejected, which can mask capacity problems but frustrate users with slow responses

**Best Practice:** High IOPS utilization usually indicates you've outgrown your storage tier rather than a configuration problem. Before restricting I/O, analyze I/O patterns and optimize before restricting.

**Hardware Actions:**

- Upgrade to higher IOPS storage tier (3K → 12K)
- Ensure 30% IOPS headroom is maintained

### High Series Cardinality (SeriesCardinality > 1M)

**CloudWatch Metrics to Monitor:**

- **SeriesCardinality** per bucket and total
- **MemoryUtilization** (increases with cardinality)
- **CPUUtilization** (query planning overhead)
- **QueryRequestsTotal** (runtime_error rate may increase)

**Configuration Adjustments:**

**Priority 1: Optimize Series Handling**

- storage-series-id-set-cache-size: 1000-2000 (increase cache)
- storage-series-file-max-concurrent-snapshot-compactions: 4-8

**Priority 2: Set Protective Limits**

- influxql-max-select-series: 10000 (prevent runaway queries)
- influxql-max-select-buckets: 1000

**Priority 3: Optimize Index Operations**

- storage-max-index-log-file-size: 2,097,152 (2MB)

**Important Considerations:**

High series cardinality is fundamentally a data modeling problem, not a configuration problem. Configuration changes can only mitigate symptoms - they cannot solve the underlying issue.

**Configuration Trade-offs:**

Increasing `storage-series-id-set-cache-size` will improve query performance by caching series lookups, but at the cost of increased **MemoryUtilization**. Each cache entry consumes memory, and with millions of series, this can be substantial. Monitor **HeapMemoryUsage** and **ActiveMemoryAllocation** after making this change.

Setting protective limits (`influxql-max-select-series`, `influxql-max-select-buckets`) will cause legitimate queries to fail with **compile_error** in **QueryRequestsTotal** if they exceed these thresholds. Dashboards that previously worked may break, and users will need to modify their queries. This is particularly problematic for:

- Monitoring dashboards that aggregate across many hosts/services
- Analytics queries that need to compare multiple entities
- Alerting queries that evaluate fleet-wide conditions

Adjusting `storage-max-index-log-file-size` to smaller values increases index compaction frequency, which raises **CPUUtilization** and **WriteOpsPerSec** as the system performs more frequent index maintenance.

**Critical Understanding:**

When **SeriesCardinality** exceeds 5M, you're approaching the architectural limits of InfluxDB 2.x. At 10M+ series, performance degrades exponentially regardless of configuration:

- Query planning becomes prohibitively expensive (high **CPUUtilization**)
- Memory requirements grow non-linearly (high **MemoryUtilization**)
- Index operations dominate I/O (**ReadOpsPerSec**, **WriteOpsPerSec**)
- **QueryRequestsTotal** runtime_error rates increase as queries timeout or exhaust memory

**Best Practice:** Configuration changes are temporary band-aids. You must address the root cause:

1. **Analyze Your Data Model:**
   - Review **SeriesCardinality** per bucket to identify problem areas
   - Identify which tags have high unique value counts
   - Look for unbounded tag values (UUIDs, timestamps, user IDs, session IDs)
   - Find tags that should be fields instead

**Data Model Actions:**

- Review tag design to reduce unnecessary cardinality
- Consider consolidating similar series
- **If > 10M series:** Plan migration to InfluxDB 3.0

### Query Performance Issues

**CloudWatch Metrics to Monitor:**

- **QueryRequestsTotal** by result type (success, runtime_error, compile_error, queue_error)
- **APIRequestRate** with Status=500 or Status=499
- **QueryResponseVolume** (large responses indicate expensive queries)

**Configuration Adjustments:**

**Priority 1: Increase Query Resources**

- query-concurrency: Increase to 75% of vCPUs
- query-memory-bytes: Allocate 70% of total RAM
- query-queue-size: 4096

**Priority 2: Optimize Query Execution**

- storage-series-id-set-cache-size: 1000 (increase for better caching)
- http-read-timeout: 60s (prevent premature timeouts)

**Priority 3: Set Reasonable Limits**

- influxql-max-select-point: 100000000
- influxql-max-select-series: 10000
- influxql-max-select-buckets: 1000

**Important Considerations:**

Increasing query resources creates resource competition and potential system instability:

**Resource Allocation Trade-offs:**

Increasing `query-concurrency` allows more queries to run simultaneously, but each query competes for CPU and memory:

- **CPUUtilization** will increase, potentially reaching saturation during peak query periods
- **MemoryUtilization** will rise as more queries allocate memory simultaneously
- If you increase concurrency without adequate resources, all queries slow down instead of just some queuing
- Risk of cascading failure if concurrent queries exhaust available resources

Allocating more `query-memory-bytes` means less memory available for caching and other operations:

- **HeapMemoryUsage** will increase
- `storage-cache-max-memory-size` may need to be reduced to compensate
- Fewer cache hits means higher **ReadOpsPerSec** and slower query performance
- System becomes more vulnerable to memory exhaustion if queries use their full allocation

Increasing `query-queue-size` only delays the problem - it doesn't solve capacity issues:

- Queries wait longer in queue, increasing end-to-end latency
- Users perceive the system as slower even though throughput may be unchanged
- Large queues can mask underlying capacity problems
- **QueryRequestsTotal** queue_error rate decreases, but user experience may not improve

Increasing `http-read-timeout` prevents premature query cancellation, but:

- Long-running queries consume resources longer, reducing capacity for other queries
- Users wait longer before receiving timeout errors
- Can hide inefficient queries that should be optimized
- May lead to resource exhaustion if many slow queries accumulate

**Best Practice:** Query performance problems are usually caused by inefficient queries, not insufficient resources. Before increasing resource allocation:

1. **Analyze Query Patterns:**
   - Review **QueryResponseVolume** to identify queries returning excessive data (> 1MB)
   - Check **QueryRequestsTotal** runtime_error patterns - what's causing failures?
   - Look for **APIRequestRate** with Status=499 (client timeouts) - queries are too slow
   - Identify frequently executed expensive queries

2. **Optimize Queries First:**

Common Query Anti-patterns:

    * Missing time range filters → Add explicit time bounds
    * Querying all series → Add specific tag filters
    * Excessive aggregation windows → Use appropriate intervals
    * Unnecessary fields in SELECT → Request only needed data
    * No LIMIT clauses → Add reasonable limits

3. **Application-Level Solutions:**
   - Implement query result caching (Redis, Memcached)
   - Use tasks to pre-aggregate common patterns
   - Add pagination for large result sets
   - Implement query rate limiting per user/dashboard
   - Use downsampled data for historical queries

4. **Verify Resource Availability:**
   - Check **CPUUtilization** - if already > 70%, increasing concurrency will make things worse
   - Check **MemoryUtilization** - if already > 70%, allocating more query memory will cause OOM
   - Verify **TotalIOpsPerSec** has 30% headroom before increasing query load

**Recommended Approach:**

1. Start by optimizing the top 10 most expensive queries (by **QueryResponseVolume**)
2. Implement query result caching at the application level
3. Only increase resource allocation if queries are optimized and metrics show headroom
4. Scale to a larger instance class if workload has outgrown current capacity

**Hardware Actions:**

- Scale your compute capacity, queries benefit from extra processing power (vCPUs)

#### RegEx Performance Pitfalls in Flux Queries

When filtering data in Flux, avoid using regular expressions for exact matches or simple pattern matching, as this introduces significant performance penalties. RegEx operations in Flux are **single-threaded** and **bypass the underlying TSM index entirely**. Instead of leveraging InfluxDB's optimized tag indexes for fast lookups, RegEx filters force the query engine to retrieve all matching series from storage and perform text comparisons sequentially against each value. This becomes particularly problematic when:

- **Filtering on exact tag values** - Use the equality operator (`==`) or the `contains()` function instead of RegEx patterns like `/^exact_value$/`
- **Matching multiple specific values** - Use the `in` operator with an array of values rather than alternation patterns like `/(value1|value2|value3)/`
- **Simple prefix or suffix matching** - Consider using `strings.hasPrefix()` or `strings.hasSuffix()` functions, which are more efficient than RegEx anchors

For scenarios requiring multiple pattern matches, restructure your query to use multiple filter predicates combined with logical operators, or pre-filter using tag equality before applying more complex string operations. Reserve RegEx exclusively for cases requiring true pattern matching that cannot be expressed through simpler comparison operators.

### Write Performance Issues

**CloudWatch Metrics to Monitor:**

- **WriteTimeouts** (increasing count)
- **WriteOpsPerSec** and **WriteThroughput**
- **APIRequestRate** with Status=500 for write endpoints
- **QueryRequestsTotal** with result=runtime_error during writes

**Configuration Adjustments:**

**Priority 1: Optimize WAL Writes**

- storage-wal-max-concurrent-writes: 12-16
- storage-wal-max-write-delay: 10m0s
- http-write-timeout: 60s

**Priority 2: Optimize Cache Snapshots**

- storage-cache-snapshot-memory-size: 52,428,800 (50MB)
- storage-cache-snapshot-write-cold-duration: 10m0s

**Priority 3: Control Field Validation**

- storage-no-validate-field-size: TRUE (if data source is trusted)

**Important Considerations:**

Write performance tuning involves careful trade-offs between throughput, reliability, and resource consumption:

**WAL Configuration Trade-offs:**

Increasing `storage-wal-max-concurrent-writes` allows more parallel write operations, but:

- **CPUUtilization** increases as more write threads compete for CPU
- **MemoryUtilization** rises as more data is buffered in memory before WAL flush
- **WriteOpsPerSec** will spike, potentially exceeding your 30% IOPS headroom
- Increased contention for disk I/O may actually slow down individual writes
- If you exceed disk I/O capacity, **WriteTimeouts** may increase rather than decrease

Increasing `storage-wal-max-write-delay` means writes wait longer before timing out:

- Masks capacity problems by making writes wait instead of failing quickly
- Users experience slower write response times even when writes eventually succeed
- Can lead to write queue buildup and memory pressure
- Doesn't actually increase capacity - just delays the timeout

Increasing `http-write-timeout` similarly delays timeout errors:

- Allows larger batch writes to complete
- But also allows slow writes to consume resources longer
- Can hide underlying performance problems
- May lead to resource exhaustion if many slow writes accumulate

**Cache Snapshot Trade-offs:**

Increasing `storage-cache-snapshot-memory-size` means more data accumulates in memory before flushing:

- **MemoryUtilization** increases significantly
- Risk of data loss increases if instance crashes before snapshot
- Larger snapshots take longer to write, creating bigger **WriteOpsPerSec** spikes
- Can improve write throughput by batching more data, but at cost of memory and reliability

Increasing `storage-cache-snapshot-write-cold-duration` delays snapshots:

- Further increases **MemoryUtilization** as data stays in cache longer
- Increases data loss risk window
- Reduces **WriteOpsPerSec** frequency but creates larger spikes when snapshots occur
- Recovery time after restart increases as more WAL must be replayed

**Field Validation Trade-off:**

Setting `storage-no-validate-field-size: TRUE` disables field size validation:

- Improves write throughput by skipping validation checks
- **Critical Risk:** Allows malformed or malicious data to be written
- Can lead to data corruption if writes contain invalid field sizes
- Makes debugging data problems much harder
- **Only use if you have complete control and trust of your data source**

**Best Practice:** Write performance problems usually indicate capacity limits or inefficient write patterns. Before tuning configuration:

1. **Analyze Write Patterns:**
   - Review **WriteThroughput** and **WriteOpsPerSec** trends
   - Check **WriteTimeouts** correlation with write load
   - Monitor **APIRequestRate** for write endpoints by status code
   - Identify write batch sizes and frequency

2. **Optimize Write Operations First:**

Common Write Anti-patterns:

    * Writing individual points → Batch writes (5,000-10,000 points)
    * Too-frequent writes → Buffer and batch
    * Synchronous writes → Implement async write queues
    * Unbounded write bursts → Implement rate limiting
    * Writing unnecessary precision → Round timestamps appropriately

3. **Verify I/O Capacity:**
   - Check **TotalIOpsPerSec** - if already > 70%, increasing WAL concurrency will make things worse
   - Review **WriteOpsPerSec** during peak periods
   - Ensure 30% IOPS headroom exists before tuning write settings
   - Consider whether 3K IOPS is sufficient or if 12K IOPS tier is needed

4. **Application-Level Improvements:**
   - Implement write buffering with configurable batch sizes
   - Add write retry logic with exponential backoff
   - Use asynchronous write operations
   - Implement write rate limiting during peak periods
   - Monitor write queue depth and apply backpressure

**Recommended Approach:**

1. Start by optimizing write batch sizes at the application level (aim for 5,000-10,000 points per batch)
2. Implement write buffering and async operations
3. Verify **TotalIOpsPerSec** has adequate headroom
4. Upgrade to the next storage tier (3K IOPS → 12K IOPS → 16K IOPS) if consistently above 70% utilization
5. Only tune WAL settings if writes are optimized and I/O capacity is adequate
6. **Never** disable field validation unless you have complete control of data sources

**Hardware Actions:**

- Upgrade to higher IOPS storage (3K → 12K → 16K)
- Ensure I/O headroom is adequate
- Scale to larger instance class if CPU or memory constrained

## Monitoring Best Practices

### CloudWatch Alarms Configuration

**Critical Alarms (Immediate Action Required):**

**CPUUtilization:**

- Threshold: > 90% for 5 minutes
- Action: Implement traffic remediation measures or Compute Scaling

**MemoryUtilization:**

- Threshold: > 90% for 5 minutes
- Action: Implement traffic remediation measures or Compute Scaling

**DiskUtilization:**

- Threshold: > 85%
- Action: Try to free up space by deleting old buckets, updating retention configurations or Storage Scaling

**TotalIOpsPerSec:**

- Threshold: > 90% of provisioned for 10 minutes
- Action: Implement traffic remediation measures or Increase IOPS

**SeriesCardinality:**

- Threshold: > 10,000,000
- Action: Review your Data model, if no changes are possible explore migrate to InfluxDB 3 or shard your data

**EngineUptime:**

- Threshold: Unexpected reset (< 300 seconds)
- Action: Check is it coincides with a maintenance window, if not create a ticket to Timestream support.

**Warning Alarms (Investigation Required):**

**CPUUtilization:**

- Threshold: > 70% for 15 minutes
- Action: review changes in workload or traffic

**MemoryUtilization:**

- Threshold: > 70% for 15 minutes
- Action: review changes in workload or traffic

**DiskUtilization:**

- Threshold: > 70%
- Action: Review retention policies

**TotalIOpsPerSec:**

- Threshold: > 70% of provisioned for 15 minutes
- Action: review changes in workload or traffic

**QueryRequestsTotal (runtime_error):**

- Threshold: > 1% of total queries
- Action: review changes in workload or traffic

**WriteTimeouts:**

- Threshold: > 1% of write operations
- Action: review changes in workload or traffic

**SeriesCardinality:**

- Threshold: > 5,000,000
- Action: Review data model optimization

### Proactive Monitoring Checklist

**Daily:**

- Review APIRequestRate for error spikes (400, 404, 499, 500)
- Check QueryRequestsTotal for runtime_error and queue_error rates
- Verify WriteTimeouts count is minimal
- Check for any critical alarms
- Verify EngineUptime (no unexpected restarts)

**Weekly:**

- Review CPUUtilization, MemoryUtilization, and DiskUtilization trends
- Analyze QueryRequestsTotal patterns by result type
- Check SeriesCardinality growth rate per bucket
- Review TotalIOpsPerSec utilization trends
- Verify configuration parameters are optimal
- Review TaskExecutionFailures patterns

**Monthly:**

- Capacity planning review (project 3-6 months ahead)
- Compare current metrics against sizing table
- Review and optimize retention policies
- Analyze query patterns from APIRequestRate and QueryResponseVolume
- Review SeriesCardinality and data model efficiency
- Assess need for instance scaling or configuration changes
- Review TotalBuckets and consolidation opportunities

## Troubleshooting Guide

### Scenario: Sudden Performance Degradation

**Investigation Steps:**

**Check Recent Changes:**

- Configuration parameter modifications in the AWS Management Console
- Application deployment changes
- Query pattern changes
- Data model modifications
- Infrastructure changes (instance type, storage)

**Review CloudWatch Metrics:**

- **CPU spike?** → Check CPUUtilization, QueryRequestsTotal
- **Memory pressure?** → Check MemoryUtilization, HeapMemoryUsage, ActiveMemoryAllocation
- **IOPS saturation?** → Check TotalIOpsPerSec, ReadOpsPerSec, WriteOpsPerSec
- **Series cardinality jump?** → Check SeriesCardinality growth
- **Error rate increase?** → Check QueryRequestsTotal (runtime_error), APIRequestRate (Status=500)
- **Unexpected restart?** → Check EngineUptime

**Enable Detailed Logging:**

Configuration changes:

- log-level: debug
- flux-log-enabled: TRUE

Monitor for 1-2 hours, then review logs

Return to log-level: info after investigation

**Resolution Steps:**

- Apply appropriate configuration changes based on findings
- Scale resources if limits are reached
- Optimize queries or data model if needed
- Implement rate limiting if sudden load increase

### Scenario: Memory Exhaustion

**Symptoms:**

- MemoryUtilization > 90%
- HeapMemoryUsage approaching maximum
- QueryRequestsTotal showing runtime_error (out of memory)
- APIRequestRate showing Status=500

**Resolution Steps:**

Immediate Actions (if critical):

1. Restart instance to clear memory (if safe to do so)
2. Reduce query-concurrency temporarily
3. Eliminate long-running queries if possible

Configuration Changes:

**Priority 1: Reduce Cache Memory**

- storage-cache-max-memory-size: Reduce to 10% of RAM
- Example: 32GB → 3,355,443,200 bytes
- storage-cache-snapshot-memory-size: 26,214,400 (25MB)

**Priority 2: Limit Query Memory**

- query-memory-bytes: Set to 60% of total RAM
- query-max-memory-bytes: Match query-memory-bytes
- query-initial-memory-bytes: 10% of query-memory-bytes

**Priority 3: Set Protective Limits**

- influxql-max-select-series: 10000
- influxql-max-select-point: 100000000
- query-concurrency: Reduce to 50% of vCPUs

**Long-Term Solutions:**

- Optimize data model to reduce **SeriesCardinality**
- Implement query result size limits at application level
- Add query timeout enforcement
- Review most common queries to ensure these are following best practices mentioned in the section [Query Performance Issues](#query-performance-issues "#query-performance-issues")

### Scenario: High Series Cardinality Impact

**Review CloudWatch metrics:**

- **SeriesCardinality** > 5M
- **MemoryUtilization** high
- **QueryRequestsTotal** showing increased runtime_error
- **CPUUtilization** elevated due to query planning overhead

**Investigation Steps:**

**Analyze Cardinality Growth:**

- SeriesCardinality growth rate (daily/weekly)
- Projection to 10M threshold
- Identify sources of high cardinality
- Review tag design and usage

**Assess Performance Impact:**

- Compare **QueryRequestsTotal** success rate before/after cardinality increase
- Review **MemoryUtilization** correlation
- Check **CPUUtilization** patterns
- Analyze **QueryResponseVolume** trends

**Identify Cardinality Sources:**

Review data model:

- Which buckets have highest SeriesCardinality?
- Which tags have high unique value counts?
- Are there unnecessary tags?
- Are tag values unbounded (UUIDs, timestamps, etc.)?

**Review Current Configuration:**

Check optimization parameters:

- storage-series-id-set-cache-size: Current value?
- influxql-max-select-series: Is it limiting runaway queries?
- storage-max-index-log-file-size: Appropriate for cardinality?

**Resolution Steps:**

Immediate Configuration Changes:

**Priority 1: Optimize Series Handling**

- storage-series-id-set-cache-size: 1500-2000
- storage-series-file-max-concurrent-snapshot-compactions: 6-8
- storage-max-index-log-file-size: 2,097,152 (2MB)

**Priority 2: Set Protective Limits**

- influxql-max-select-series: 10000
- influxql-max-select-buckets: 1000
- query-concurrency: Reduce if memory constrained

**Priority 3: Increase Resources**

- Scale to next instance tier
- Increase memory allocation
- Consider 12K IOPS storage tier

**Migration Planning (if > 10M series):**

- **InfluxDB 3.0 offers superior high-cardinality performance**
- Plan migration timeline (2-3 months)
- Test with subset of data first
- Prepare application for migration
- InfluxDB 3.0 uses columnar storage optimized for billions of series

### Scenario: Query Queue Buildup

**Review CloudWatch metrics:**

- **QueryRequestsTotal** with result=queue_error increasing (queries being rejected)
- **APIRequestRate** with Status=429 or Status=503 (service unavailable/too many requests)
- **CPUUtilization** may be elevated (> 70%) indicating resource saturation
- **MemoryUtilization** may be high (> 70%) limiting query capacity
- **QueryResponseVolume** showing large response sizes (queries taking excessive resources)

**Investigation Steps:**

**Analyze Queue and Concurrency Metrics:**

- Review **QueryRequestsTotal** breakdown by result type:
  - High queue_error count indicates queries are being rejected
  - Compare success rate to baseline - is it dropping?
  - Check for runtime_error increases (queries failing after starting)

- Monitor **APIRequestRate** patterns:
  - Look for Status=429 (too many requests) or Status=503 (service unavailable)
  - Identify which endpoints are experiencing rejections
  - Check request rate trends over time

**Review Resource Utilization:**

- **CPUUtilization** during high queue periods:
  - If > 70%, queries are CPU-bound and can't execute faster
  - If < 50%, queue limits may be too restrictive

- **MemoryUtilization** correlation:
  - High memory may be limiting query concurrency
  - Check **HeapMemoryUsage** and **ActiveMemoryAllocation** for memory pressure

- **TotalIOpsPerSec** patterns:
  - High I/O may be slowing query execution
  - Check if queries are I/O bound

**Identify Query Patterns:**

- Review **QueryResponseVolume**:
  - Are queries returning excessive data (> 1MB)?
  - Identify endpoints with largest response volumes
  - Look for patterns in expensive queries

- Analyze **QueryRequestsTotal** rate:
  - What's the queries per second rate?
  - Are there burst patterns or sustained high load?
  - Compare to instance capacity from sizing table

- Check **APIRequestRate** by endpoint:
  - Which query endpoints have highest traffic?
  - Are there duplicate or redundant queries?

**Check Resource Availability:**

- Compare current metrics to sizing table recommendations:
  - **SeriesCardinality** vs. instance class capacity
  - Query rate vs. recommended queries per second
  - **CPUUtilization** and **MemoryUtilization** headroom

- Verify IOPS capacity:
  - **TotalIOpsPerSec** should have 30% headroom
  - Check if queries are waiting on disk I/O

**Resolution Steps:**

Configuration Changes:

**Priority 1: Increase Queue Capacity**

- query-queue-size: 4096 (from default 1024)

**Priority 2: Increase Concurrency (if resources allow)**

- query-concurrency: Increase to 75% of vCPUs
- Example: 16 vCPU → query-concurrency = 12
- Verify CPUUtilization stays < 80% after change
- Verify MemoryUtilization stays < 80% after change

**Priority 3: Optimize Query Execution**

- query-memory-bytes: Ensure adequate allocation
- storage-series-id-set-cache-size: 1000-1500
- http-read-timeout: 120s (prevent premature timeouts)

**Priority 4: Set Protective Limits**

- influxql-max-select-series: 10000
- influxql-max-select-point: 100000000

**Application-Level Solutions:**

- **Implement query result caching** (Redis, Memcached)
  - Cache results for frequently executed queries
  - Set appropriate TTLs based on data freshness requirements
  - Monitor cache hit rates

- **Use continuous queries** to pre-aggregate common patterns
  - Pre-calculate common aggregations
  - Query pre-aggregated data instead of raw data

- **Add pagination** for large result sets
  - Limit initial query size
  - Load additional data on demand

- **Implement query rate limiting** per user/dashboard
  - Prevent single users from overwhelming the system
  - Set fair-use quotas

- **Use downsampled data** for historical queries
  - Query lower-resolution data for older time ranges
  - Reserve full-resolution queries for recent data

**Scaling Decision:**

- If CPUUtilization > 70% sustained: Scale to larger instance
- If MemoryUtilization > 70% sustained: Scale to memory-optimized instance
- If query rate exceeds instance capacity: Scale to next tier per sizing table

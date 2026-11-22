

# Monitoring distributed KV caching

Monitor a distributed key-value (KV) caching cluster to make sure that it has enough storage, that clients reach it, and that it serves requests at the latency that you expect. You monitor in two places:
+ LMCache reports the KV cache hit rate, which shows how often requests find their KV state in the cache. On each GPU host, read the `/metrics` endpoint of the LMCache HTTP API. By default, the endpoint is `http://127.0.0.1:8080/metrics`, with the API key as a bearer token. The share of prompt tokens that the cluster serves is the rate of `lmcache_mp_lookup_hit_l2_tokens_total` divided by the rate of `lmcache_mp_lookup_prompt_tokens_total`. Failed reads from the cluster show in `lmcache_mp_l2_prefetch_failure_chunks_total`.
+ ElastiCache publishes Amazon CloudWatch metrics for the cluster. For information about accessing ElastiCache metrics through CloudWatch, see [Monitoring use with CloudWatch Metrics](CacheMetrics.md).

**Topics**
+ [Metrics to watch](#distributed-kv-caching-monitoring.metrics)
+ [How existing metrics apply to distributed KV caching](#distributed-kv-caching-monitoring.existing-metrics)
+ [Node-level detail with INFO largeobj](#distributed-kv-caching-monitoring.info)
+ [OpenTelemetry metrics](#distributed-kv-caching-monitoring.otel)
+ [Recommended alarms](#distributed-kv-caching-monitoring.alarms)

## Metrics to watch
<a name="distributed-kv-caching-monitoring.metrics"></a>

ElastiCache publishes large object metrics and Elastic Fabric Adapter (EFA) metrics for distributed KV caching clusters. For the definition, unit, and statistic of each metric, see [Metrics for Valkey and Redis OSS](CacheMetrics.Redis.md) and [Host-Level Metrics](CacheMetrics.HostLevel.md). Use the metrics as follows:
+ To make sure that the cluster has enough storage, watch `LargeObjectDiskUtilization`, `LargeObjectDiskUsedBytes`, and `Evictions`.
+ To make sure that clients use the cluster, watch `LargeObjectBasedCmds`. With the `rdma` transport, also watch the host-level metrics `EFABytesIn` and `EFABytesOut`.
+ To find slow requests, watch `LargeObjectBasedCmdsLatency`. It includes the time for disk and remote direct memory access (RDMA) transfers.
+ `LargeObjectDRAMHitRate` shows the share of reads that the dynamic random-access memory (DRAM) cache of the node serves. It isn't the KV cache hit rate. For the KV cache hit rate, use the LMCache metrics.

## How existing metrics apply to distributed KV caching
<a name="distributed-kv-caching-monitoring.existing-metrics"></a>

Some existing ElastiCache metrics behave differently on distributed KV caching clusters.


**Existing metrics on distributed KV caching clusters**  

| Metric | Behavior on distributed KV caching clusters | 
| --- | --- | 
| Evictions | Includes objects evicted by the maxmemory-policy. | 
| GetTypeCmds, SetTypeCmds, GetTypeCmdsLatency, SetTypeCmdsLatency | Include the large object read and write commands. BLOB.INFO counts as a read command. | 
| NetworkBytesIn, NetworkBytesOut, NetworkPackets\* | Don't include EFA traffic. Use EFABytesIn and EFABytesOut for RDMA traffic. | 
| BytesUsedForCache, DatabaseMemoryUsagePercentage | Include the full DRAM cache that the node reserves for objects, including unused space. The cache is allocated in 1 GiB segments and doesn't shrink right away when objects are removed. These metrics can be high even when few objects are stored. | 
| DatabaseCapacityUsagePercentage, BytesReadFromDisk, BytesWrittenToDisk | Apply to data tiering only. They don't include the Non-Volatile Memory Express (NVMe) storage for objects. Use LargeObjectDiskUsedBytes and LargeObjectDiskUtilization instead. | 
| MemoryFragmentationRatio, AllocatorFragmentation\* | Don't show free space inside the DRAM cache for objects. Active defragmentation doesn't apply to objects. | 

## Node-level detail with INFO largeobj
<a name="distributed-kv-caching-monitoring.info"></a>

`INFO largeobj` gives node-level detail. It returns data for only the node that you're connected to, so connect to each primary node to check every shard. After RDMA traffic starts, the RDMA error counters must stay at 0. If they don't, check the security group rules and the Availability Zone (see [Step 2: Create a security group](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.security-group)). For more information about what each field means and when to act on it, see [What to watch](https://valkey.io/topics/large-object-configuration/#what-to-watch) on the valkey.io website.

## OpenTelemetry metrics
<a name="distributed-kv-caching-monitoring.otel"></a>

The large object metrics and the EFA metrics are available only in CloudWatch (namespace `AWS/ElastiCache`). They are not part of the OpenTelemetry metric set. For more information about OpenTelemetry metrics, see [Monitoring ElastiCache with OpenTelemetry metrics](otel-metrics.md).

## Recommended alarms
<a name="distributed-kv-caching-monitoring.alarms"></a>

We recommend that you create CloudWatch alarms on the following metrics:
+ `LargeObjectDiskUtilization` and `Evictions` – When both are high, the cluster evicts objects to make space, and it needs more storage. For more information, see [Sizing and scaling](distributed-kv-caching-limits.md#distributed-kv-caching-limits.scaling).
+ `LargeObjectBasedCmdsLatency` – To detect slow disk or RDMA transfers.

For more information about ElastiCache metrics, see [Monitoring use with CloudWatch Metrics](CacheMetrics.md).
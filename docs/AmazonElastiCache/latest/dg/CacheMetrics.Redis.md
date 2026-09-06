

# Metrics for Valkey and Redis OSS
<a name="CacheMetrics.Redis"></a>

The `AWS/ElastiCache` namespace includes the following Valkey and Redis OSS metrics. These metrics are the same when using the Valkey engine.

With the exception of `ReplicationLag`, `EngineCPUUtilization`, `SuccessfulWriteRequestLatency`, and `SuccessfulReadRequestLatency`, these metrics are derived from the **info** command. Each metric is calculated at the cache node level.

For complete documentation of the **info** command, see [http://valkey.io/commands/info](https://valkey.io/commands/info). 

**See Also**
+ [Host-Level Metrics](CacheMetrics.HostLevel.md)



- **`ActiveDefragHits`**
  - **Description:** The number of value reallocations per minute performed by the active defragmentation process. This is derived from active\_defrag\_hits statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Number

- **`AuthenticationFailures`**
  - **Description:** The total number of failed attempts to authenticate to Valkey or Redis OSS using the AUTH command. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **`DatabaseAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to access databases they don't have permission to access. This is triggered when a user's access string includes db= restrictions and the user attempts to SELECT or operate on a disallowed database. We suggest setting an alarm on this metric to detect unauthorized access attempts. Available for Valkey 9.1 and later.
  - **Unit:** Count

- **`BytesUsedForCache`**
  - **Description:** The total number of bytes allocated by Valkey or Redis OSS for all purposes, including the dataset, buffers, and so on.  / **Unit:** Bytes
  - **Description:** Dimension: Tier=Memory for Valkey or Redis OSS clusters using [Data tiering in ElastiCache](data-tiering.md): The total number of bytes used for cache by memory. This is the value of used\_memory statistic at [INFO](https://valkey.io/commands/info).  / **Unit:** Bytes
  - **Description:** Dimension: Tier=SSD for Valkey or Redis OSS clusters using [Data tiering in ElastiCache](data-tiering.md): The total number of bytes used for cache by SSD. / **Unit:** Bytes

- **`BytesReadFromDisk`**
  - **Description:** The total number of bytes read from disk per minute. Supported only for clusters using [Data tiering in ElastiCache](data-tiering.md).
  - **Unit:** Bytes

- **`BytesWrittenToDisk`**
  - **Description:** The total number of bytes written to disk per minute. Supported only for clusters using [Data tiering in ElastiCache](data-tiering.md).
  - **Unit:** Bytes

- **`CacheHits`**
  - **Description:** The number of successful read-only key lookups in the main dictionary. This is derived from keyspace\_hits statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`CacheMisses`**
  - **Description:** The number of unsuccessful read-only key lookups in the main dictionary. This is derived from keyspace\_misses statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`CommandAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to run commands they don’t have permission to call. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **`CacheHitRate`**
  - **Description:** Indicates the usage efficiency of the Valkey or Redis OSS instance. If the cache ratio is lower than about 0.8, it means that a significant amount of keys are evicted, expired, or don't exist. This is calculated using cache\_hits and cache\_misses statistics in the following way: cache\_hits /(cache\_hits \+ cache\_misses).
  - **Unit:** Percent

- **`ChannelAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to access channels they do not have permission to access. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this metric to detect unauthorized access attempts.
  - **Unit:** Count

- **`CurrConnections`**
  - **Description:** The number of client connections, excluding connections from read replicas. ElastiCache uses 4 to 6 of the connections to monitor the cluster in each case. This is derived from the connected\_clients statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`CurrItems`**
  - **Description:** The number of items in the cache. This is derived from the keyspace statistic, summing all of the keys in the entire keyspace. / **Unit:** Count
  - **Description:** Dimension: Tier=Memory for clusters using [Data tiering in ElastiCache](data-tiering.md). The number of items in memory. / **Unit:** Count
  - **Description:** Dimension: Tier=SSD (solid state drives) for clusters using [Data tiering in ElastiCache](data-tiering.md). The number of items in SSD. / **Unit:** Count

- **`CurrVolatileItems`**
  - **Description:** Total number of keys in all databases that have a ttl set. This is derived from the expires statistic, summing all of the keys with a ttl set in the entire keyspace.
  - **Unit:** Count

- **`CurrItemsWithVolatileFields`**
  - **Description:** The number of keys that contain hash fields with expiration set. Available for Valkey 9.0 and later.
  - **Unit:** Count

- **`ReclaimedFields`**
  - **Description:** The number of expired hash fields reclaimed by the active expiration process. Available for Valkey 9.0 and later.
  - **Unit:** Count

- **`DatabaseCapacityUsagePercentage`**
  - **Description:** Percentage of the total data capacity for the cluster that is in use.<br />On Data Tiered instances, the metric is calculated as `(used_memory - mem_not_counted_for_evict + SSD used) / (maxmemory + SSD total capacity)`, where `used_memory` and `maxmemory` are taken from [INFO](https://valkey.io/commands/info/).<br />In all other cases, the metric is calculated using `used_memory/maxmemory`.
  - **Unit:** Percent

- **`DatabaseCapacityUsageCountedForEvictPercentage`**
  - **Description:** Percentage of the total data capacity for the cluster that is in use, excluding the memory used for overhead and COB. This metric is calculated as:<br />`used_memory - mem_not_counted_for_evict/maxmemory`<br />On Data Tiered instances, the metric is calculated as:<br />`(used_memory + SSD used) / (maxmemory + SSD total capacity) `<br />where `used_memory` and `maxmemory` are taken from [INFO](https://valkey.io/commands/info/)
  - **Unit:** Percent

- **`DatabaseMemoryUsagePercentage`**
  - **Description:**  Percentage of the memory for the cluster that is in use. This is calculated using used\_memory/maxmemory from [INFO](https://valkey.io/commands/info). 
  - **Unit:** Percent

- **`DatabaseMemoryUsageCountedForEvictPercentage`**
  - **Description:**  Percentage of the memory for the cluster that is in use, excluding memory used for overhead and COB. This is calculated using used\_memory-mem\_not\_counted\_for\_evict/maxmemory from [INFO](https://valkey.io/commands/info). 
  - **Unit:** Percent

- **`DB0AverageTTL`**
  - **Description:**  Exposes avg\_ttl of DBO from the keyspace statistic of [INFO](https://valkey.io/commands/info) command. This metric is relevant only for primary nodes. Replicas do not expire keys directly. Instead, they wait for the primary node to expire or evict keys and then receive the resulting DEL commands. Because replicas do not track TTL, ignore this metric on replica nodes. 
  - **Unit:** Milliseconds

- **`EngineCPUUtilization`**
  - **Description:** Provides CPU utilization of the Valkey or Redis OSS engine thread. Because Valkey and Redis OSS are single-threaded, you can use this metric to analyze the load of the process itself. The `EngineCPUUtilization` metric provides a more precise visibility of the process. You can use it in conjunction with the `CPUUtilization` metric. `CPUUtilization` exposes CPU utilization for the server instance as a whole, including other operating system and management processes. For larger node types with four vCPUs or more, use the `EngineCPUUtilization` metric to monitor and set thresholds for scaling.  On an ElastiCache host, background processes monitor the host to provide a managed database experience. These background processes can take up a significant portion of the CPU workload. This is not significant on larger hosts with more than two vCPUs. But it can affect smaller hosts with 2vCPUs or fewer. If you only monitor the `EngineCPUUtilization` metric, you will be unaware of situations where the host is overloaded with both high CPU usage from Valkey or Redis OSS and high CPU usage from the background monitoring processes. Therefore, we recommend monitoring the `CPUUtilization` metric for hosts with two vCPUs or less. 
  - **Unit:** Percent

- **`Evictions`**
  - **Description:** The number of keys that have been evicted due to the maxmemory limit. This is derived from the evicted\_keys statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`GlobalDatastoreReplicationLag`**
  - **Description:** This is the lag between the secondary Region's primary node and the primary Region's primary node. For cluster mode enabled Valkey or Redis OSS, the lag indicates the maximum delay among the shards. 
  - **Unit:** Seconds

- **`IamAuthenticationExpirations`**
  - **Description:** The total number of expired IAM-authenticated Valkey or Redis OSS connections. You can find more information about [Authenticating with IAM](auth-iam.md) in the user guide.
  - **Unit:** Count

- **`IamAuthenticationThrottling`**
  - **Description:** The total number of throttled IAM-authenticated Valkey or Redis OSS AUTH or HELLO requests. You can find more information about [Authenticating with IAM](auth-iam.md) in the user guide. 
  - **Unit:** Count

- **`IsMaster`**
  - **Description:** Indicates whether the node is the primary node of current shard/cluster. The metric can be either 0 (not primary) or 1 (primary). 
  - **Unit:** Count

- **`KeyAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to access keys they don’t have permission to access. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **` KeysTracked`**
  - **Description:**  The number of keys being tracked by Valkey or Redis OSS key tracking as a percentage of tracking-table-max-keys. Key tracking is used to aid client-side caching and notifies clients when keys are modified. 
  - **Unit:** Count

- **`MemoryFragmentationRatio`**
  - **Description:**  Indicates the efficiency in the allocation of memory of the Valkey or Redis OSS engine. Certain thresholds signify different behaviors. The recommended value is to have fragmentation above 1.0. This is calculated from the mem\_fragmentation\_ratio statistic of [INFO](https://valkey.io/commands/info). 
  - **Unit:** Number

- **`NewConnections`**
  - **Description:** The total number of connections that have been accepted by the server during this period. This is derived from the total\_connections\_received statistic at [INFO](https://valkey.io/commands/info). If you are using ElastiCache for Redis OSS version 5 or lower, between two and four of the connections reported by this metric are used by ElastiCache to monitor the cluster. However, when using ElastiCache for Redis OSS version 6 or above, the connections used by ElastiCache to monitor the cluster are not included in this metric.
  - **Unit:** Count

- **`NumItemsReadFromDisk`**
  - **Description:** The total number of items retrieved from disk per minute. Supported only for clusters using [Data tiering in ElastiCache](data-tiering.md).
  - **Unit:** Count

- **`NumItemsWrittenToDisk`**
  - **Description:** The total number of items written to disk per minute. Supported only for clusters using [Data tiering in ElastiCache](data-tiering.md).
  - **Unit:** Count

- **`MasterLinkHealthStatus`**
  - **Description:** This status has two values: 0 or 1. The value 0 indicates that data in the ElastiCache primary node is not in sync with Valkey or Redis OSS on EC2. The value of 1 indicates that the data is in sync. To complete the migration, use the [CompleteMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CompleteMigration.html) API operation.
  - **Unit:** Boolean

- **`Reclaimed`**
  - **Description:** The total number of key expiration events. This is derived from the expired\_keys statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`ReplicationBytes`**
  - **Description:** For nodes in a replicated configuration, ReplicationBytes reports the number of bytes that the primary is sending to all of its replicas. This metric is representative of the write load on the replication group. This is derived from the master\_repl\_offset statistic at [INFO](https://valkey.io/commands/info). 
  - **Unit:** Bytes

- **`ReplicationLag`**
  - **Description:** This metric is only applicable for a node running as a read replica. It represents how far behind, in seconds, the replica is in applying changes from the primary node. For Valkey 7.2 and onwards, and Redis OSS 5.0.6 onwards, the lag can be measured in milliseconds.
  - **Unit:** Seconds

- **`SaveInProgress`**
  - **Description:** This binary metric returns 1 whenever a background save (forked or forkless) is in progress, and 0 otherwise. A background save process is typically used during snapshots and syncs. These operations can cause degraded performance. Using the SaveInProgress metric, you can diagnose whether degraded performance was caused by a background save process. This is derived from the rdb\_bgsave\_in\_progress statistic at [INFO](https://valkey.io/commands/info).
  - **Unit:** Boolean

- **`TrafficManagementActive`**
  - **Description:** Indicates whether ElastiCache for Redis OSS is actively managing traffic by adjusting traffic allocated to incoming commands, monitoring or replication. Traffic is managed when more commands are sent to the node than can be processed by Valkey or Redis OSS and is used to maintain the stability and optimal operation of the engine. Any data points of 1 may indicate that the node is underscaled for the workload being provided.  If this metric remains active, evaluate the cluster to decide if scaling up or scaling out is necessary. Related metrics include `NetworkBandwidthOutAllowanceExceeded` and `EngineCPUUtilization`.  
  - **Unit:** Boolean

- **`SuccessfulWriteRequestLatency`**
  - **Description:** Latency of successful write requests. <br /> Valid statistics: Average, Sum, Min, Max, Sample Count, any percentile between p0 and p100. The sample count includes only the commands that were successfully executed.
  - **Unit:** Microseconds

- **`SuccessfulReadRequestLatency`**
  - **Description:** Latency of successful read requests.<br /> Valid statistics: Average, Sum, Min, Max, Sample Count, any percentile between p0 and p100. The sample count includes only the commands that were successfully executed.
  - **Unit:** Microseconds

- **`ErrorCount`**
  - **Description:** The total number of failed commands during the specified time period. <br />Valid statistics: Average, Sum, Min, Max
  - **Unit:** Count

- **`SearchNumberOfIndexes`**
  - **Description:** Number of created indexes
  - **Unit:** Count

- **`SearchTotalIndexedDocuments`**
  - **Description:** Total number of keys in all indexes
  - **Unit:** Count

- **`SearchUsedMemoryBytes`**
  - **Description:** Number of bytes of memory consumed in all search data structures
  - **Unit:** Bytes

- **`BlockedConnections`**
  - **Description:** The number of clients currently in a blocked state, waiting on blocking commands such as BLPOP. This is derived from the blocked\_clients field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`RejectedConnections`**
  - **Description:** The number of connections that the engine has rejected, primarily when the number of connected clients has reached the maxclients limit. This is derived from the rejected\_connections field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`PubSubChannels`**
  - **Description:** The number of active pub/sub channels on this node that have at least one subscriber. This count does not include sharded pub/sub channels. This is derived from the pubsub\_channels field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`PubSubShardChannels`**
  - **Description:** The number of active sharded pub/sub channels on this node that have at least one subscriber. Sharded channels route messages only within the shard rather than broadcasting cluster-wide. If pub/sub channel counts are growing with utilization, consider switching to sharded pub/sub to scale horizontally. This is derived from the pubsubshard\_channels field at [INFO](https://valkey.io/commands/info). Available on Valkey 7.2 and later, and Redis OSS 7.0 and later.
  - **Unit:** Count

- **`UsedMemoryDataset`**
  - **Description:** An estimate of memory in bytes used by actual user data (keys and values), excluding overhead such as replication buffers, client output buffers, and internal metadata. This is derived from the used\_memory\_dataset field at [INFO](https://valkey.io/commands/info). Use this metric together with BytesUsedForCache to understand how much of your allocated memory is consumed by actual data versus overhead. Available on Valkey 7.2 and later, and Redis OSS 4.0 and later.
  - **Unit:** Bytes

- **`AllocatorFragmentationBytes`**
  - **Description:** The amount of memory in bytes wasted due to allocator fragmentation. Unlike MemoryFragmentationRatio, which reflects total process RSS overhead including non-actionable OS-level factors, this metric isolates fragmentation that the activedefrag engine parameter can address. This is derived from the allocator\_frag\_bytes field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Bytes

- **`AllocatorFragmentationRatio`**
  - **Description:** The ratio of allocator fragmentation relative to total allocated memory. Values above 1.0 represent fragmentation; the higher the value, the more severe the fragmentation. Unlike MemoryFragmentationRatio, which reflects total process RSS overhead including non-actionable OS-level factors, this metric isolates fragmentation that the activedefrag engine parameter can address. This is derived from the allocator\_frag\_ratio field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Number

- **`ProcessedCommands`**
  - **Description:** The total number of commands processed by the engine. Commands rejected before execution are not counted. This is derived from the total\_commands\_processed field at [INFO](https://valkey.io/commands/info).
  - **Unit:** Count

- **`DurabilityLag`**
  - **Description:** The age of the oldest write acknowledged to the client but not yet persisted to the Multi-AZ transactional log. Only for durability-enabled clusters.
  - **Unit:** Milliseconds

- **`DurabilityBufferExceededErrorCount`**
  - **Description:** Write commands rejected due to exceeding the 10-second durability window. Only for async writes.
  - **Unit:** Count



The following are aggregations of certain kinds of commands, derived from **info commandstats**. The commandstats section provides statistics based on the command type, including the number of calls, the total CPU time consumed by these commands, and the average CPU consumed per command execution. For each command type, the following line is added: `cmdstat_XXX: calls=XXX,usec=XXX,usec_per_call=XXX`.

The latency metrics listed following are calculated using commandstats statistic from [INFO](https://valkey.io/commands/info). They are calculated in the following way: `delta(usec)/delta(calls)`. `delta` is calculated as the diff within one minute. Latency is defined as CPU time taken by ElastiCache to process the command. Note that for clusters using data tiering, the time taken to fetch items from SSD is not included in these measurements.

For a full list of available commands, see [commands](https://valkey.io/commands) in the Valkey documentation. 


| Metric  | Description  | Unit  | 
| --- | --- | --- | 
| ClusterBasedCmds | The total number of commands that are cluster-based. This is derived from the commandstats statistic by summing all of the commands that act upon a cluster (cluster slot, cluster info, and so on).  | Count | 
| ClusterBasedCmdsLatency | Latency of cluster-based commands. | Microseconds | 
| EvalBasedCmds | The total number of commands for eval-based commands. This is derived from the commandstats statistic by summing eval, evalsha. | Count | 
| EvalBasedCmdsLatency | Latency of eval-based commands. | Microseconds | 
| GeoSpatialBasedCmds | The total number of commands for geospatial-based commands. This is derived from the commandstats statistic. It's derived by summing all of the geo type of commands: geoadd, geodist, geohash, geopos, georadius, and georadiusbymember. | Count | 
| GeoSpatialBasedCmdsLatency | Latency of geospatial-based commands.  | Microseconds | 
| GetTypeCmds | The total number of read-only type commands. This is derived from the commandstats statistic by summing all of the read-only type commands (get, hget, scard, lrange, and so on.) | Count | 
|  GetTypeCmdsLatency |  Latency of read commands.  | Microseconds | 
| HashBasedCmds | The total number of commands that are hash-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more hashes (hget, hkeys, hvals, hdel, and so on). | Count | 
|  HashBasedCmdsLatency |  Latency of hash-based commands.  | Microseconds | 
| HyperLogLogBasedCmds | The total number of HyperLogLog-based commands. This is derived from the commandstats statistic by summing all of the pf type of commands (pfadd, pfcount, pfmerge, and so on.). | Count | 
|  HyperLogLogBasedCmdsLatency |  Latency of HyperLogLog-based commands.  | Microseconds | 
| JsonBasedCmds | The total number of JSON commands, including both read and write commands. This is derived from the commandstats statistic by summing all JSON commands that act upon JSON keys. | Count | 
| JsonBasedCmdsLatency | Latency of all JSON commands, including both read and write commands. | Microseconds | 
| JsonBasedGetCmds | The total number of JSON read-only commands. This is derived from the commandstats statistic by summing all JSON read commands that act upon JSON keys. | Count | 
| JsonBasedGetCmdsLatency | Latency of JSON read-only commands. | Microseconds | 
| JsonBasedSetCmds | The total number of JSON write commands. This is derived from the commandstats statistic by summing all JSON write commands that act upon JSON keys. | Count | 
| JsonBasedSetCmdsLatency | Latency of JSON write commands. | Microseconds | 
| KeyBasedCmds | The total number of commands that are key-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more keys across multiple data structures (del, expire, rename, and so on.). | Count | 
|  KeyBasedCmdsLatency |  Latency of key-based commands.  | Microseconds | 
| ListBasedCmds | The total number of commands that are list-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more lists (lindex, lrange, lpush, ltrim, and so on). | Count | 
|  ListBasedCmdsLatency |  Latency of list-based commands.  | Microseconds | 
| NonKeyTypeCmds | The total number of commands that are not key-based. This is derived from the commandstats statistic by summing all of the commands that do not act upon a key, for example, acl, dbsize or info. | Count | 
| NonKeyTypeCmdsLatency | Latency of non-key-based commands. | Microseconds | 
| PubSubBasedCmds | The total number of commands for pub/sub functionality. This is derived from the commandstatsstatistics by summing all of the commands used for pub/sub functionality: psubscribe, publish, pubsub, punsubscribe, ssubscribe, sunsubscribe, spublish, subscribe, and unsubscribe. | Count | 
| PubSubBasedCmdsLatency | Latency of pub/sub-based commands. | Microseconds | 
| SetBasedCmds | The total number of commands that are set-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more sets (scard, sdiff, sadd, sunion, and so on). | Count | 
|  SetBasedCmdsLatency |  Latency of set-based commands.  | Microseconds | 
| SetTypeCmds | The total number of write types of commands. This is derived from the commandstats statistic by summing all of the mutative types of commands that operate on data (set, hset, sadd, lpop, and so on.) | Count | 
|  SetTypeCmdsLatency |  Latency of write commands.  | Microseconds | 
| SortedSetBasedCmds | The total number of commands that are sorted set-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more sorted sets (zcount, zrange, zrank, zadd, and so on). | Count | 
|  SortedSetBasedCmdsLatency |  Latency of sorted-based commands.  | Microseconds | 
| StringBasedCmds | The total number of commands that are string-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more strings (strlen, setex, setrange, and so on). | Count | 
|  StringBasedCmdsLatency |  Latency of string-based commands.  | Microseconds | 
| StreamBasedCmds | The total number of commands that are stream-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more streams data types (xrange, xlen, xadd, xdel, and so on). | Count | 
|  StreamBasedCmdsLatency |  Latency of stream-based commands.  | Microseconds | 
| SearchBasedCmds | The total number of Search commands, including both read and write commands. This is derived from the commandstats statistic by summing all Search commands. | Count | 
| SearchBasedCmdsLatency | Latency of all Search commands, including both read and write commands. | Microseconds | 
| SearchBasedGetCmds | The total number of Search read-only commands. This is derived from the commandstats statistic by summing all Search read commands. | Count | 
| SearchBasedGetCmdsLatency | Latency of Search read-only commands. | Microseconds | 
| SearchBasedSetCmds | The total number of Search write commands. This is derived from the commandstats statistic by summing all Search write commands. | Count | 
| SearchBasedSetCmdsLatency | Latency of Search write commands. | Microseconds | 
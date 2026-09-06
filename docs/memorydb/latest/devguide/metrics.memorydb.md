

# Metrics for MemoryDB
<a name="metrics.memorydb"></a>

The `AWS/MemoryDB` namespace includes the following metrics.

With the exception of `ReplicationLag`, `EngineCPUUtilization`, `SuccessfulWriteRequestLatency`, and `SuccessfulReadRequestLatency`, these metrics are derived from the Valkey and Redis OSS **info** command. Each metric is calculated at the node level.

For complete documentation of the **INFO** command, see [INFO](http://valkey.io/commands/info). 

**See also:**
+ [Host-Level Metrics](metrics.HostLevel.md)



- **`ActiveDefragHits`**
  - **Description:** The number of value reallocations per minute performed by the active defragmentation process. This is derived from active\_defrag\_hits statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Number

- **`AuthenticationFailures`**
  - **Description:** The total number of failed attempts to authenticate using the AUTH command. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **`BytesUsedForMemoryDB`**
  - **Description:** The total number of bytes allocated by MemoryDB for all purposes, including the dataset, buffers, and so on.  / **Unit:** Bytes
  - **Description:** Dimension: Tier=SSD for clusters using [Data tiering](data-tiering.md): The total number of bytes used by SSD.  / **Unit:** Bytes
  - **Description:** Dimension: Tier=Memory for clusters using [Data tiering](data-tiering.md): The total number of bytes used by memory. This is the value of used\_memory statistic at [INFO](http://valkey.io/commands/info).  / **Unit:** Bytes

- **`BytesReadFromDisk`**
  - **Description:** The total number of bytes read from disk per minute. Supported only for clusters using [Data tiering](data-tiering.md).
  - **Unit:** Bytes

- **`BytesWrittenToDisk`**
  - **Description:** The total number of bytes written to disk per minute. Supported only for clusters using [Data tiering](data-tiering.md).
  - **Unit:** Bytes

- **`CommandAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to run commands they don’t have permission to call. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **`CurrConnections`**
  - **Description:** The number of client connections, excluding connections from read replicas. MemoryDB uses 2 to 4 of the connections to monitor the cluster in each case. This is derived from the connected\_clients statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **`CurrItems`**
  - **Description:** The number of items in the cache. This is derived from the keyspace statistic, summing all of the keys in the entire keyspace. / **Unit:** Count
  - **Description:** Dimension: Tier=Memory for clusters using [Data tiering](data-tiering.md). The number of items in memory. / **Unit:** Count
  - **Description:** Dimension: Tier=SSD (solid state drives) for clusters using [Data tiering](data-tiering.md). The number of items in SSD. / **Unit:** Count

- **`DatabaseMemoryUsagePercentage`**
  - **Description:**  Percentage of the memory available for the cluster that is in use. This is calculated using used\_memory/maxmemory from [INFO](http://valkey.io/commands/info). 
  - **Unit:** Percent

- **`DatabaseCapacityUsagePercentage`**
  - **Description:** Percentage of the total data capacity for the cluster that is in use. <br />On Data Tiered instances, the metric is calculated as `(used_memory - mem_not_counted_for_evict + SSD used) / (maxmemory + SSD total capacity)`, where `used_memory` and `maxmemory` are taken from [INFO](https://valkey.io/commands/info/).<br />In all other cases, the metric is calculated using `used_memory/maxmemory`.
  - **Unit:** Percent

- **`DB0AverageTTL`**
  - **Description:**  Exposes avg\_ttl of DBO from the keyspace statistic of [INFO](http://valkey.io/commands/info) command. 
  - **Unit:** Milliseconds

- **`EngineCPUUtilization`**
  - **Description:** Provides CPU utilization of the Valkey or Redis OSS engine thread. Because the engine is single-threaded, you can use this metric to analyze the load of the process itself. The `EngineCPUUtilization` metric provides a more precise visibility of the process. You can use it in conjunction with the `CPUUtilization` metric. `CPUUtilization` exposes CPU utilization for the server instance as a whole, including other operating system and management processes. For larger node types with four vCPUs or more, use the `EngineCPUUtilization` metric to monitor and set thresholds for scaling.  On a MemoryDB host, background processes monitor the host to provide a managed database experience. These background processes can take up a significant portion of the CPU workload. This is not significant on larger hosts with more than two vCPUs. But it can affect smaller hosts with 2vCPUs or fewer. If you only monitor the `EngineCPUUtilization` metric, you will be unaware of situations where the host is overloaded with both high CPU usage from the Valkey or Redis OSS engine and high CPU usage from the background monitoring processes. Therefore, we recommend monitoring the `CPUUtilization` metric for hosts with two vCPUs or less. 
  - **Unit:** Percent

- **`Evictions`**
  - **Description:** The number of keys that have been evicted due to the maxmemory limit. This is derived from the evicted\_keys statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **`IsPrimary`**
  - **Description:** Indicates whether the node is primary node of current shard. The metric can be either 0 (not primary) or 1 (primary). 
  - **Unit:** Count

- **`KeyAuthorizationFailures`**
  - **Description:** The total number of failed attempts by users to access keys they don’t have permission to access. You can find more information about individual authentication failures using the [ACL LOG](https://valkey.io/commands/acl-log) command. We suggest setting an alarm on this to detect unauthorized access attempts. 
  - **Unit:** Count

- **`KeyspaceHits`**
  - **Description:** The number of successful read-only key lookups in the main dictionary. This is derived from keyspace\_hits statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **`KeyspaceMisses`**
  - **Description:** The number of unsuccessful read-only key lookups in the main dictionary. This is derived from keyspace\_misses statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **` KeysTracked`**
  - **Description:**  The number of keys being tracked by key tracking as a percentage of tracking-table-max-keys. Key tracking is used to aid client-side caching and notifies clients when keys are modified. 
  - **Unit:** Count

- **`MaxReplicationThroughput`**
  - **Description:** The maximum observed throughput. Throughput is sampled over short time intervals to identify traffic bursts. The maximum of the sampled values is reported. Sampling occurs at 1 minute frequency. For example, if 1MB of data is written during a 10ms period, then the value for this metric will be 100MBps. Note that higher write latency maybe observed when this metric goes beyond 100MBps, due to write throughput throttling.
  - **Unit:** Bytes per second

- **`MemoryFragmentationRatio`**
  - **Description:**  Indicates the efficiency in the allocation of memory of the Valkey or Redis OSS engine. Certain thresholds signify different behaviors. The recommended value is to have fragmentation above 1.0. This is calculated from the mem\_fragmentation\_ratio statistic of [INFO](http://valkey.io/commands/info). 
  - **Unit:** Number

- **`MultiRegionClusterReplicationLag`**
  - **Description:**  In a MemoryDB Multi Region cluster, MultiRegionClusterReplicationLag measures the elapsed time between an update written to the multi-AZ transaction log of a regional cluster, and the time this update is written to the primary node of another regional cluster in the Multi Region cluster. This metric is emitted for every source- and destination-Region pair at the shard-level.
  - **Unit:** Milliseconds

- **`NewConnections`**
  - **Description:** The total number of connections that have been accepted by the server during this period. This is derived from the total\_connections\_received statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **`NumItemsReadFromDisk`**
  - **Description:** The total number of items retrieved from disk per minute. Supported only for clusters using [Data tiering](data-tiering.md).
  - **Unit:** Count

- **`NumItemsWrittenToDisk`**
  - **Description:** The total number of items written to disk per minute. Supported only for clusters using [Data tiering](data-tiering.md).
  - **Unit:** Count

- **`PrimaryLinkHealthStatus`**
  - **Description:** This status has two values: 0 or 1. The value 0 indicates that data in the MemoryDB primary node is not in sync with the Valkey or Redis OSS engine on EC2. The value of 1 indicates that the data is in sync. 
  - **Unit:** Boolean

- **`Reclaimed`**
  - **Description:** The total number of key expiration events. This is derived from the expired\_keys statistic at [INFO](http://valkey.io/commands/info).
  - **Unit:** Count

- **`ReplicationBytes`**
  - **Description:** For nodes in a replicated configuration, ReplicationBytes reports the number of bytes that the primary is sending to all of its replicas. This metric is representative of the write load on the cluster. This is derived from the master\_repl\_offset statistic at [INFO](http://valkey.io/commands/info). 
  - **Unit:** Bytes

- **`ReplicationDelayedWriteCommands`**
  - **Description:** Number of write commands that were delayed due to synchronous replication. Replication can be delayed due to various factors, for example network congestion or exceeding [maximum replication throughput](https://docs.aws.amazon.com/memorydb/latest/devguide/metrics.whichshouldimonitor.html#metrics-replication). 
  - **Unit:** Count

- **`ReplicationLag`**
  - **Description:** This metric is only applicable for a node running as a read replica. It represents how far behind, in seconds, the replica is in applying changes from the primary node.
  - **Unit:** Seconds

- **`SuccessfulWriteRequestLatency`**
  - **Description:** Latency of successful write requests.<br /> Valid statistics: Average, Sum, Min, Max, Sample Count, any percentile between p0 and p100. The sample count includes only the commands that were successfully executed. [Available Valkey 7.2 onwards](https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-memorydb-valkey-cloudwatch-metrics-monitor-server-response-time/).
  - **Unit:** Microseconds

- **`SuccessfulReadRequestLatency`**
  - **Description:** Latency of successful read requests.<br /> Valid statistics: Average, Sum, Min, Max, Sample Count, any percentile between p0 and p100. The sample count includes only the commands that were successfully executed. [Available Valkey 7.2 onwards](https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-memorydb-valkey-cloudwatch-metrics-monitor-server-response-time/).
  - **Unit:** Microseconds

- **`ErrorCount`**
  - **Description:** The total number of failed commands during the specified time period. <br /> Valid statistics: Average, Sum, Min, Max
  - **Unit:** Count



The following are aggregations of certain kinds of commands, derived from **info commandstats**. The commandstats section provides statistics based on the command type, including the number of calls.

For a full list of available commands, see [commands](https://valkey.io/commands). 


| Metric  | Description  | Unit  | 
| --- | --- | --- | 
| EvalBasedCmds | The total number of commands for eval-based commands. This is derived from the commandstats statistic by summing eval and evalsha. | Count | 
| GeoSpatialBasedCmds | The total number of commands for geospatial-based commands. This is derived from the commandstats statistic. It's derived by summing all of the geo type of commands: geoadd, geodist, geohash, geopos, georadius, and georadiusbymember. | Count | 
| GetTypeCmds | The total number of read-only type commands. This is derived from the commandstats statistic by summing all of the read-only type commands (get, hget, scard, lrange, and so on.) | Count | 
| HashBasedCmds | The total number of commands that are hash-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more hashes (hget, hkeys, hvals, hdel, and so on). | Count | 
| HyperLogLogBasedCmds | The total number of HyperLogLog-based commands. This is derived from the commandstats statistic by summing all of the pf type of commands (pfadd, pfcount, pfmerge, and so on.). | Count | 
|  JsonBasedCmds |  The total number of commands that are JSON-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more JSON document objects.  | Count | 
| KeyBasedCmds | The total number of commands that are key-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more keys across multiple data structures (del, expire, rename, and so on.). | Count | 
| ListBasedCmds | The total number of commands that are list-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more lists (lindex, lrange, lpush, ltrim, and so on). | Count | 
| PubSubBasedCmds | The total number of commands for pub/sub functionality. This is derived from the commandstats statistics by summing all of the commands used for pub/sub functionality: psubscribe, publish, pubsub, punsubscribe, subscribe, and unsubscribe. | Count | 
| SearchBasedCmds | The total number of secondary index and search commands, including both read and write commands. This is derived from the commandstats statistic by summing all search commands that act upon secondary indexes. | Count | 
| SearchBasedGetCmds | Total number of secondary index and search read-only commands. This is derived from the commandstats statistic by summing all secondary index and search get commands. | Count | 
| SearchBasedSetCmds | Total number of secondary index and search write commands. This is derived from the commandstats statistic by summing all secondary index and search set commands. | Count | 
| SearchNumberOfIndexes | Total number of indexes.  | Count | 
| SearchNumberOfIndexedKeys | Total number of indexed keys  | Count | 
| SearchTotalIndexSize | Memory (bytes) used by all the indexes.  | Bytes | 
| SetBasedCmds | The total number of commands that are set-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more sets (scard, sdiff, sadd, sunion, and so on). | Count | 
| SetTypeCmds | The total number of write types of commands. This is derived from the commandstats statistic by summing all of the mutative types of commands that operate on data (set, hset, sadd, lpop, and so on.) | Count | 
| SortedSetBasedCmds | The total number of commands that are sorted set-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more sorted sets (zcount, zrange, zrank, zadd, and so on). | Count | 
| StringBasedCmds | The total number of commands that are string-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more strings (strlen, setex, setrange, and so on). | Count | 
| StreamBasedCmds | The total number of commands that are stream-based. This is derived from the commandstats statistic by summing all of the commands that act upon one or more streams data types (xrange, xlen, xadd, xdel, and so on). | Count | 
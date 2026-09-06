

# Limitations
<a name="Durability.Limitations"></a>
+ Durability for ElastiCache is supported on Valkey 9.0 or later.
+ Durability for ElastiCache is supported for the following instance type families: R8g, R7g, R6g, M8g, M7g, M6g, C8gn, and C7gn.
+ Durability is enabled during cluster creation by selecting either synchronous or asynchronous writes. You can switch between the two options after creation, but you cannot disable durability once enabled. You cannot enable durability on an existing non-durable cluster.
+ Durability is not supported with ElastiCache Serverless.
+ Durability is not supported with Global Datastores, Outposts, Local Zones, or data tiering.
+ Durability enabled clusters support up to 100 MiBps of write throughput per primary node.
+ Durability for ElastiCache is not supported for Cluster Mode Disabled (CMD) clusters.
+ Durability for ElastiCache requires Multi-AZ enabled with at least one replica per shard.
+ Durability requires and automatically enables encryption at-rest, and requires encryption in-transit (TLS) to be enabled at cluster creation.
+ Online migration from self-hosted Valkey or Redis OSS to a durable cluster is not supported.
+ When durability is enabled and search indexes are configured, write commands targeting indexed keys may be throttled to maintain transactional log performance. For details, see [Search write throttling](Durability.SearchThrottling.md).
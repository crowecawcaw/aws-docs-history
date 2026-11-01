

# Limitations
<a name="Durability.Limitations"></a>
+ Durability for ElastiCache is supported on Valkey 9.0 or later.
+ Durability for ElastiCache is supported for the following instance type families: R8g, R7g, R6g, M8g, M7g, M6g, C8gn, and C7gn.
+ Durability is not supported with ElastiCache Serverless.
+ Durability is not supported with Global Datastores, Outposts, Local Zones, or data tiering.
+ Durability enabled clusters support up to 100 MiBps of write throughput per primary node.
+ Durability for ElastiCache is not supported for Cluster Mode Disabled (CMD) clusters.
+ Durability for ElastiCache requires Multi-AZ enabled with at least one replica per shard.
+ Durability requires and automatically enables encryption at-rest.
+ Changing durability on an existing cluster requires encryption in transit (TLS) to be enabled.
+ Online migration from self-hosted Valkey or Redis OSS to a durable cluster is not supported.
+ When durability is enabled and search indexes are configured, write commands targeting indexed keys may be throttled to maintain transactional log performance. For details, see [Search write throttling](Durability.SearchThrottling.md).
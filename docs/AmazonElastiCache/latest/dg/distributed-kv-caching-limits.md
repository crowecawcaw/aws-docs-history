

# Requirements and limits for distributed KV caching

Distributed key-value (KV) caching is available only on node-based clusters that use the `cache.i8ge.48xlarge` node type and run ElastiCache for Valkey 9.1 or later. The `cache.i8ge.48xlarge` node type is an Elastic Fabric Adapter (EFA)-enabled node type based on the Amazon Elastic Compute Cloud (Amazon EC2) I8ge instance type. For the node specifications, see [Current Generation (Valkey)](CacheNodes.SupportedTypes.md#CacheNodes.CurrentGen-Valkey). For the supported Regions, see [Distributed KV caching](distributed-kv-caching.md). Distributed KV caching is not available on ElastiCache Serverless.

Read these requirements and limits before you create a cluster. You set most of them when you create the cluster, and you can't change them later.

**Topics**
+ [Cluster requirements](#distributed-kv-caching-limits.requirements)
+ [Size limits](#distributed-kv-caching-limits.sizes)
+ [Sizing and scaling](#distributed-kv-caching-limits.scaling)

## Cluster requirements
<a name="distributed-kv-caching-limits.requirements"></a>

A distributed KV caching cluster must use the following settings.


**Distributed KV caching cluster requirements**  

| Setting | Requirement | 
| --- | --- | 
| API operation | You must create the cluster with CreateReplicationGroup. You can't use CreateCacheCluster. | 
| Cluster mode | Enabled | 
| Replicas per shard | 0 | 
| Automatic failover | Enabled. Cluster mode requires it, also with 0 replicas. | 
| Availability Zone | All shards in the same Availability Zone. Multi-AZ is off by default, and you can't turn it on. | 
| Encryption in transit | TransitEncryptionMode set to required. You can't turn it off or change it. | 
| Encryption at rest | Always on. You can't turn it off. | 
| Snapshots, backups, restore, and replication | Not supported, because the large object data type is not RDB compatible. Automatic backups are off by default, and you can't turn them on. For data loss on node events, see [Resilience and data persistence](distributed-kv-caching-how-it-works.md#distributed-kv-caching-how-it-works.resilience). | 
| Global Datastore and Multi-Region caches | Not supported | 
| Durability | Not supported. Service updates and engine upgrades remove all stored objects. Apply updates in a maintenance window, and expect the cache to be empty after the update. | 
| Network type | IPv4, IPv6, or dual stack. The network type doesn't affect the EFA path. For more information, see [Choosing a network type in ElastiCache](network-type.md). | 
| Node type change | You can't change or migrate an existing cluster to or from the cache.i8ge.48xlarge node type. To use this node type, create a new cluster. | 
| Number of shards | One or more, set when you create the cluster. For more information, see [Sizing and scaling](#distributed-kv-caching-limits.scaling). | 

## Size limits
<a name="distributed-kv-caching-limits.sizes"></a>

The following limits apply to each value and to each node.


**Object size limits**  

| Limit | Value | 
| --- | --- | 
| Maximum size of a value, for the large object (BLOB.\*) commands and for SET and GET | 512 MiB | 
| Maximum size of a large object that is cached in dynamic random-access memory (DRAM) | 256 MiB | 


**Storage limits**  

| Limit | Value | 
| --- | --- | 
| Total Non-Volatile Memory Express (NVMe) instance storage per node | 120 TB | 

Large objects are stored on this NVMe storage. The large object module and the file system also use some of it. To see the storage in use, monitor the `LargeObjectDiskUsedBytes` metric.

## Sizing and scaling
<a name="distributed-kv-caching-limits.scaling"></a>

You can't add or remove shards or replicas, rebalance slots, or use auto scaling on a distributed KV caching cluster, because large object keys can't move between shards. To change capacity, create a new cluster and reload the data.

Choose the number of shards when you create the cluster. Base it on the larger of your total object storage and your peak read bandwidth. Each large object uses its length rounded up to 4 KiB of NVMe storage. For the storage per node, see [Size limits](#distributed-kv-caching-limits.sizes).

Before you create the cluster, you can estimate the benefit of distributed KV caching with KVTrace. KVTrace records the KV cache events of your running vLLM or SGLang fleet, simulates a shared cache at different numbers of cache nodes, and reports the estimated hit rate, the savings, and the break-even price of the cache. KVTrace models only the DRAM of each node, so its hit rate is a lower bound. For more information, see [KVTrace](https://github.com/aws-samples/amazon-elasticache-samples/tree/main/kvtrace) on the GitHub website.
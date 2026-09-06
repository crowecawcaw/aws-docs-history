

# Replication: Valkey and Redis OSS Cluster Mode Disabled vs. Enabled
<a name="Replication.Redis-RedisCluster"></a>

With Valkey and Redis OSS, you have the ability to create one of two distinct types of clusters (API/CLI: replication groups). A Valkey or Redis OSS (cluster mode disabled) cluster always has a single shard (API/CLI: node group) with up to 5 read replica nodes. A Valkey or Redis OSS (cluster mode enabled) cluster has up to 500 shards with 1 to 5 read replica nodes in each.

![Image: Valkey or Redis OSS (cluster mode disabled), and Valkey or Redis OSS (cluster mode enabled) clusters](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/ElastiCache-NodeGroups.png)


*Valkey or Redis OSS (cluster mode disabled), and Valkey or Redis OSS (cluster mode enabled) clusters*

The following table summarizes important differences between Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled) clusters.


**Comparing Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled) Clusters**  

| Feature | Valkey or Redis OSS (cluster mode disabled) | Valkey or Redis OSS (cluster mode enabled) | 
| --- | --- | --- | 
| Modifiable | Yes. Supports adding and deleting replica nodes, and scaling up node type. | Limited. For more information, see [Version Management for ElastiCache](VersionManagement.md) and [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md). | 
| Data Partitioning | No | Yes | 
| Shards | 1 | 1 to 500  | 
| Read replicas | 0 to 5 If you have no replicas and the node fails, you experience total data loss. | 0 to 5 per shard. If you have no replicas and a node fails, you experience loss of all data in that shard. | 
| Multi-AZ  | Yes, with at least 1 replica. Optional. On by default. | YesOptional. On by default. | 
| Snapshots (Backups) | Yes, creating a single .rdb file. | Yes, creating a unique .rdb file for each shard. | 
| Restore | Yes, using a single .rdb file from a Valkey or Redis OSS (cluster mode disabled) cluster. | Yes, using .rdb files from either a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) cluster. | 
| Supported by | All Valkey and Redis OSS versions | All Valkey and Redis OSS versions | 
| Engine upgradeable | Yes, with some limits. For more information, see [Version Management for ElastiCache](VersionManagement.md). | Yes, with some limits. For more information, see [Version Management for ElastiCache](VersionManagement.md). | 
| Encryption | All Valkey versions, and Redis OSS 4.0.10 and later. | All Valkey versions, and Redis OSS 4.0.10 and later. | 
| HIPAA Eligible | All Valkey versions, and Redis OSS 4.0.10 and later. | All Valkey versions, and Redis OSS 4.0.10 and later. | 
| PCI DSS Compliant | All Valkey versions, and Redis OSS 4.0.10 and later. | All Valkey versions, and Redis OSS 4.0.10 and later. | 
| Online resharding | N/A | All Valkey versions, and Redis OSS 4.0.10 and later. | 

## Which should I choose?
<a name="Replication.Redis-RedisCluster.Choose"></a>

When choosing between Valkey or Redis OSS (cluster mode disabled) or Valkey or Redis OSS (cluster mode enabled), consider the following factors:
+ **Scaling v. partitioning** – Business needs change. You need to either provision for peak demand or scale as demand changes. Valkey or Redis OSS (cluster mode disabled) supports scaling. You can scale read capacity by adding or deleting replica nodes, or you can scale capacity by scaling up to a larger node type. Both of these operations take time. For more information, see [Scaling replica nodes for Valkey or Redis OSS (Cluster Mode Disabled)](Scaling.RedisReplGrps.md).

   

  Valkey or Redis OSS (cluster mode enabled) supports partitioning your data across up to 500 node groups. You can dynamically change the number of shards as your business needs change. One advantage of partitioning is that you spread your load over a greater number of endpoints, which reduces access bottlenecks during peak demand. Additionally, you can accommodate a larger data set since the data can be spread across multiple servers. For information on scaling your partitions, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md).

   
+ **Node size v. number of nodes** – Because a Valkey or Redis OSS (cluster mode disabled) cluster has only one shard, the node type must be large enough to accommodate all the cluster's data plus necessary overhead. On the other hand, because you can partition your data across several shards when using a Valkey or Redis OSS (cluster mode enabled) cluster, the node types can be smaller, though you need more of them. For more information, see [Choosing your node size](CacheNodes.SelectSize.md).

   
+ **Reads v. writes** – If the primary load on your cluster is applications reading data, you can scale a Valkey or Redis OSS (cluster mode disabled) cluster by adding and deleting read replicas. However, there is a maximum of 5 read replicas. If the load on your cluster is write-heavy, you can benefit from the additional write endpoints of a Valkey or Redis OSS (cluster mode enabled) cluster with multiple shards.

Whichever type of cluster you choose to implement, be sure to choose a node type that is adequate for your current and future needs.
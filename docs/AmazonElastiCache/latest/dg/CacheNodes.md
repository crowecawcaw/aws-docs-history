

# Managing nodes in ElastiCache
<a name="CacheNodes"></a>

A node is the smallest building block of an Amazon ElastiCache deployment. It is a fixed-size chunk of secure, network-attached RAM. Each node runs the engine that was chosen when the cluster was created or last modified. Each node has its own Domain Name Service (DNS) name and port. Multiple types of ElastiCache nodes are supported, each with varying amounts of associated memory and computational power.

For a more detailed discussion of which node size to use, see [Choosing your node size](CacheNodes.SelectSize.md). 

Generally speaking, due to its support for sharding, Valkey or Redis OSS (cluster mode enabled) deployments have a number of smaller nodes. In contrast, Valkey or Redis OSS (cluster mode disabled) deployments have fewer, larger nodes in a cluster. For a more detailed discussion of which node size to use, see [Choosing your node size](CacheNodes.SelectSize.md). 

**Topics**
+ [Viewing ElastiCache Node Status](Nodes.viewing.md)
+ [Valkey or Redis OSS nodes and shards](CacheNodes.NodeGroups.md)
+ [Connecting to nodes](nodes-connecting.md)
+ [Supported node types](CacheNodes.SupportedTypes.md)
+ [Rebooting nodes](nodes.rebooting.md)
+ [Replacing nodes (Valkey and Redis OSS)](CacheNodes.NodeReplacement.md)
+ [Replacing nodes (Memcached)](CacheNodes.NodeReplacement-mc.md)
+ [Reserved nodes](CacheNodes.Reserved.md)
+ [Migrating previous generation nodes](CacheNodes.NodeMigration.md)

Some important operations involving nodes are the following: 
+ [Adding nodes to an ElastiCache cluster](Clusters.AddNode.md)
+ [Removing nodes from an ElastiCache cluster](Clusters.DeleteNode.md)
+ [Scaling ElastiCache](Scaling.md)
+ [Finding connection endpoints in ElastiCache](Endpoints.md)
+ [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md)
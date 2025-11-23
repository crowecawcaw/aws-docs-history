# Managing nodes in ElastiCache

A node is the smallest building block of an Amazon ElastiCache deployment. It
is a fixed-size chunk of secure, network-attached RAM. Each node runs the engine that was
chosen when the cluster was created or last modified. Each node has its own Domain Name
Service (DNS) name and port. Multiple types of ElastiCache nodes are supported, each with varying
amounts of associated memory and computational power.

For a more detailed discussion of which node size to use, see [Choosing your node size](CacheNodes.md "CacheNodes.md").

Generally speaking, due to its support for sharding, Valkey or Redis OSS (cluster mode enabled)
deployments have a number of smaller nodes. In contrast, Valkey or Redis OSS (cluster mode disabled) deployments have
fewer, larger nodes in a cluster. For a more detailed discussion of which node size to use,
see [Choosing your node size](CacheNodes.md "CacheNodes.md").

###### Topics

- [Viewing ElastiCache Node Status](Nodes.md "Nodes.md")
- [Valkey or Redis OSS nodes and shards](CacheNodes.md "CacheNodes.md")
- [Connecting to nodes](nodes-connecting.md "nodes-connecting.md")
- [Supported node types](CacheNodes.md "CacheNodes.md")
- [Rebooting nodes](nodes.md "nodes.md")
- [Replacing nodes (Valkey and Redis OSS)](CacheNodes.md "CacheNodes.md")
- [Replacing nodes (Memcached)](CacheNodes.md "CacheNodes.md")
- [Reserved nodes](CacheNodes.md "CacheNodes.md")
- [Migrating previous generation nodes](CacheNodes.md "CacheNodes.md")
  Some important operations involving nodes are the following:

- [Adding nodes to an ElastiCache cluster](Clusters.md "Clusters.md")
- [Removing nodes from an ElastiCache cluster](Clusters.md "Clusters.md")
- [Scaling ElastiCache](Scaling.md "Scaling.md")
- [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md")
- [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md "AutoDiscovery.md")

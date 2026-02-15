# MemoryDB nodes and shards

A shard is a hierarchical arrangement of nodes, each
wrapped in a cluster. Shards support replication. Within a shard, one node functions as
the read/write primary node. All the other nodes in a shard function as read-only
replicas of the primary node. MemoryDB supports multiple shards within
a cluster. This support enables partitioning of
your data in a MemoryDB cluster.

MemoryDB supports replication via shards. The API operation
[DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") lists the shards with the member nodes,
the node names, endpoints and also other information.

After a MemoryDB cluster is created, it can be altered (scaled in or out). For more information, see [Scaling](scaling.md "scaling.md") and [Replacing nodes](nodes.md "nodes.md").

When you create a new cluster, you can seed it with data from the old cluster so it doesn't
start out empty. Doing this can be helpful if you need change your node type, engine version or migrate from Amazon ElastiCache (Redis OSS). For more information, see [Making manual snapshots](snapshots-manual.md "snapshots-manual.md") and [Restoring from a snapshot](snapshots-restoring.md "snapshots-restoring.md").

# Managing nodes

A node is the smallest building block of a MemoryDB deployment.
A node belongs to a shard which belongs to a cluster.
Each node runs the engine version that was chosen when the cluster was created or last modified.
Each node has its own Domain Name Service (DNS) name and port. Multiple types of MemoryDB nodes are supported,
each with varying amounts of associated memory and computational power.

###### Topics

- [MemoryDB nodes and shards](nodes.md "nodes.md")
- [Supported node types](nodes.md "nodes.md")
- [MemoryDB reserved nodes](nodes.md "nodes.md")
- [Replacing nodes](nodes.md "nodes.md")
  Important operations involving nodes include:

- [Adding / Removing nodes from a cluster](clusters.md "clusters.md")
- [Scaling](scaling.md "scaling.md")
- [Finding connection endpoints](endpoints.md "endpoints.md")

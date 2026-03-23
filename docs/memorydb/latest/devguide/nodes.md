# Managing nodes

A node is the smallest building block of a MemoryDB deployment.
A node belongs to a shard which belongs to a cluster.
Each node runs the engine version that was chosen when the cluster was created or last modified.
Each node has its own Domain Name Service (DNS) name and port. Multiple types of MemoryDB nodes are supported,
each with varying amounts of associated memory and computational power.

###### Topics

- [MemoryDB nodes and shards](nodes.nodegroups.md "nodes.nodegroups.md")
- [Supported node types](nodes.supportedtypes.md "nodes.supportedtypes.md")
- [MemoryDB reserved nodes](nodes.reservednodes.md "nodes.reservednodes.md")
- [Replacing nodes](nodes.nodereplacement.md "nodes.nodereplacement.md")
  Important operations involving nodes include:

- [Adding / Removing nodes from a cluster](clusters.deletenode.md "clusters.deletenode.md")
- [Scaling](scaling.md "scaling.md")
- [Finding connection endpoints](endpoints.md "endpoints.md")



# Managing nodes
<a name="nodes"></a>

A node is the smallest building block of a MemoryDB deployment. A node belongs to a shard which belongs to a cluster. Each node runs the engine version that was chosen when the cluster was created or last modified. Each node has its own Domain Name Service (DNS) name and port. Multiple types of MemoryDB nodes are supported, each with varying amounts of associated memory and computational power.

**Topics**
+ [MemoryDB nodes and shards](nodes.nodegroups.md)
+ [Supported node types](nodes.supportedtypes.md)
+ [MemoryDB reserved nodes](nodes.reservednodes.md)
+ [Replacing nodes](nodes.nodereplacement.md)

Important operations involving nodes include: 
+ [Adding / Removing nodes from a cluster](clusters.deletenode.md)
+ [Scaling](scaling.md)
+ [Finding connection endpoints](endpoints.md)
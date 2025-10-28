# Online vertical scaling by modifying node type

By using online vertical scaling with MemoryDB, you can scale
your cluster dynamically with minimal downtime. This allows your cluster
to serve requests even while scaling.

###### Note

Scaling is not supported between a data tiering cluster (for example, a cluster using an r6gd node type) and a cluster that does not use data tiering
(for example, a cluster using an r6g node type). For more information, see [Data tiering](data-tiering.md "data-tiering.md").

You can do the following:

- **Scale up** –
  Increase read and write capacity by adjusting the node type of your MemoryDB cluster to use a larger node type.

MemoryDB dynamically resizes your cluster while remaining online and serving requests.

- **Scale down** –
  Reduce read and write capacity by adjusting the node type down to use a smaller node. Again, MemoryDB dynamically resizes your cluster while remaining online and serving requests. In this case,
  you reduce costs by downsizing the node.

###### Note

The scale up and scale down processes rely on creating clusters with newly selected node types and synchronizing the new nodes with the previous ones. To ensure a smooth scale up/down flow,
do the following:

- While the vertical scaling process is designed to remain fully online, it does rely on synchronizing data between the old node and the new node. We recommend that you initiate scale up/down
  during hours when you expect data traffic to be at its minimum.
- Test your application behavior during scaling in a staging environment, if possible.

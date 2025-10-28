# Understanding MemoryDB replication

MemoryDB implements replication with data partitioned across up to 500
shards.

Each shard in a cluster has a single read/write primary node and up to 5 read-only replica nodes. Each primary node can sustain up to 100 MB/s.

You can create a cluster with higher number of shards and lower number of replicas totaling up to 500 nodes per cluster. This cluster configuration can range from 500 shards and 0 replicas to 100 shards and 4 replicas, which is the maximum number of replicas allowed.

## Replication in a cluster

Each read replica in a shard maintains a copy of the data from the shard's primary node.

Asynchronous replication mechanisms using the transaction logs are used to keep the read replicas synchronized with the primary.
Applications can read from any node in the cluster.
Applications can write only to the primary nodes.
Read replicas enhance read scalability. Since MemoryDB stores the data in durable transaction logs, there is no risk that data will be lost.
Data is partitioned across the shards in a MemoryDB cluster.

Applications use the MemoryDB cluster's _cluster endpoint_
to connect with the nodes in the cluster.
For more information, see [Finding connection endpoints](endpoints.md "endpoints.md").

MemoryDB clusters are regional and can contain nodes only from one Region.

To improve fault tolerance, you must provision primaries and read replicas across multiple Availability Zones

within that region.

Using replication, which provides you with Multi-AZ, is strongly recommended for all MemoryDB clusters. For
more information, see [Minimizing downtime in MemoryDB with Multi-AZ](autofailover.md "autofailover.md").



# Planned failover
<a name="msk-replicator-planned-failover"></a>

You can conduct a planned failover to test the resiliency of your application against an unexpected event in your primary AWS Region. A planned failover should not result in data loss.

------
#### [ Identical topic name replication ]

1. Shut down all producers and consumers connecting to your source cluster.

1. Create a new MSK Replicator to replicate data from your MSK cluster in the secondary Region to your MSK cluster in the primary Region with Identical topic name replication (**Keep the same topics name** in console). This is required to copy data written to the secondary Region back to the primary Region for failback.

1. Start producers and consumers connected to the target cluster in the secondary AWS Region.

------
#### [ Prefixed topic name replication ]

1. Shut down all producers and consumers connecting to your source cluster.

1. Create a new MSK Replicator to replicate data from your MSK cluster in the secondary Region to your MSK cluster in the primary Region. This is required for failback.

1. Start producers on the target cluster in the secondary AWS Region.

1. If your application does not require message ordering, start consumers in the secondary AWS Region that read from both the local (for example, `topic`) and replicated topics (for example, `<sourceKafkaClusterAlias>.topic`) using a wildcard operator (for example, `.*topic`).

   If your application requires message ordering, start consumers only for the replicated topics on the target cluster (for example, `<sourceKafkaClusterAlias>.topic`) but not the local topics.

1. Wait for all the consumers of replicated topics on the target MSK cluster to finish processing all data, so that consumer lag is 0. Then, stop consumers for the replicated topics.

1. Start consumers for the local topics (for example, `topic`) on the target MSK cluster.

------
# Perform a planned failover to the

secondary AWS Region

You can conduct a planned failover to test the resiliency of your application against an unexpected event in your primary AWS region which has your source MSK cluster. A planned failover should not result in data loss.

If you’re using Identical topic name replication configuration, follow these steps:

1. Shutdown all producers and consumers connecting to your source cluster.
2. Create a new MSK Replicator to replicate data from your MSK cluster in the secondary Region to your MSK cluster in the primary Region with Identical topic name replication (**Keep the same topics name** in console). This is required to copy the data that you will be writing to the secondary region back to the primary Region so that you can failback to the primary Region after the unexpected event has ended.
3. Start producers and consumers connected to the target cluster in the secondary AWS Region.
   If you’re using Prefixed topic name configuration, follow these steps to failover:

4. Shutdown all producers and consumers connecting to your source cluster.
5. Create a new MSK Replicator to replicate data from your MSK cluster in the secondary Region to your MSK cluster in the primary Region. This is required to copy the data that you will be writing to the secondary region back to the primary Region so that you can failback to the primary Region after the unexpected event has ended.
6. Start producers on target cluster in the secondary AWS Region.
7. Depending on your application’s message ordering requirements, follow the steps in one of the following tabs.

No message orderingIf your application does not require message ordering, start consumers in the secondary AWS Region that read from both the local (for example, topic) and replicated topics (for example, `<sourceKafkaClusterAlias>.topic`) using a wildcard operator (for example, `.*topic`).

Message ordering
If your application requires message ordering, start consumers only for the replicated topics on target cluster (for example, `<sourceKafkaClusterAlias>.topic`) but not the local topics (for example, `topic`). 5. Wait for all the consumers of replicated topics on the target MSK cluster to finish processing all data, so that consumer lag is 0 and the number of records processed is also 0. Then, stop consumers for the replicated topics on target cluster. At this point, all records that were replicated from the source MSK cluster to target MSK cluster have been consumed. 6. Start consumers for the local topics (for example, `topic`) on the target MSK cluster.

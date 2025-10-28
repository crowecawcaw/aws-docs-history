# Perform an unplanned failover to the

secondary AWS Region

You can conduct an unplanned failover when there is a service event in the primary AWS Region which has your source MSK cluster and you want to temporarily redirect your traffic to the secondary Region which has your target MSK cluster. An unplanned failover could result in some data loss as MSK Replicator replicates data asynchronously. You can track the message lag using the metrics in [Monitor replication](msk-replicator-monitor.md "msk-replicator-monitor.md").

If you’re using Identical topic name replication configuration (**Keep the same topics name** in console), follow these steps:

1. Attempt to shut down all producers and consumers connecting to the source MSK cluster in the primary Region. This operation might not succeed due to impairments in that region.
2. Start producers and consumers connecting to the target MSK cluster in the secondary AWS Region to complete the failover. As MSK Replicator also replicates metadata including read ACLs and consumer group offsets, your producers and consumers will seamlessly resume processing from near where they left off before failover.
   If you’re using `PREFIX` topic name configuration, follow these steps to failover:

3. Attempt to shut down all producers and consumers connecting to the source MSK cluster in the primary Region. This operation might not succeed due to impairments in that region.
4. Start producers and consumers connecting to the target MSK cluster in the secondary AWS Region to complete the failover. As MSK Replicator also replicates metadata including read ACLs and consumer group offsets, your producers and consumers will seamlessly resume processing from near where they left off before failover.
5. Depending on your application’s message ordering requirements, follow the steps in one of the following tabs.

No message orderingIf your application does not require message ordering, start consumers in the target AWS Region that read from both the local (for example, `topic`) and replicated topics (for example, `<sourceKafkaClusterAlias>.topic`) using a wildcard operator (for example, `.*topic`).

Message ordering

    1. Start consumers only for the replicated topics on target cluster (for example, `<sourceKafkaClusterAlias>.topic`) but not the local topics (for example, `topic`).
    2. Wait for all the consumers of replicated topics on the target MSK cluster to finish processing all data, so that offset lag is 0 and the number of records processed is also 0. Then, stop consumers for the replicated topics on target cluster. At this point, all records that were replicated from the source MSK cluster to target MSK cluster have been consumed.
    3. Start consumers for the local topics (for example, `topic`) on the target MSK cluster.

4. Once the service event has ended in the primary Region, create a new MSK Replicator to replicate data from your MSK cluster in the secondary Region to your MSK cluster in the primary Region with Replicator starting position set to _earliest_. This is required to copy the data that you will be writing to the secondary Region back to the primary Region so that you can failback to the primary Region after the service event has ended. If you don't set the Replicator starting position to _earliest_, any data you produced to the cluster in the secondary region during the service event in the primary region will not be copied back to the cluster in the primary region.

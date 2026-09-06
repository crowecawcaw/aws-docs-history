

# Failback
<a name="msk-replicator-failback"></a>

You can failback to the primary AWS Region after the service event in that Region has ended.

------
#### [ Identical topic name replication ]

1. Create a new MSK Replicator with your secondary cluster as source and primary cluster as target, starting position set to *earliest* and Identical topic name replication (**Keep the same topics name** in console). This starts copying all data written to the secondary cluster after failover back to the primary Region.

1. Monitor the `MessageLag` metric on the new replicator in Amazon CloudWatch until it reaches `0`, which indicates all data has been replicated from secondary to primary.

1. After all data has been replicated, stop all producers connecting to the secondary cluster and start producers connecting to the primary cluster.

1. Wait for `MaxOffsetLag` metric for your consumers connecting to the secondary cluster to become `0` to ensure they have processed all the data. See [Monitor consumer lags](consumer-lag.md).

1. Once all data has been processed, stop consumers in the secondary Region and start consumers connecting to the primary cluster to complete the failback.

1. Delete the Replicator you created in the first step that is replicating data from your secondary cluster to primary.

1. Verify that your existing Replicator copying data from primary to secondary cluster has status as "RUNNING" and `ReplicatorThroughput` metric in Amazon CloudWatch is greater than `0`.

   Note that when you create a new Replicator with starting position as *Earliest* for failback, it starts reading all data in your secondary cluster's topics. Depending on your data retention settings, your topics may have data that came from your source cluster. While MSK Replicator automatically filters those messages, you will still incur data processing and transfer charges for all the data in your secondary cluster. You can track the total data processed by replicator using `ReplicatorBytesInPerSec`.

------
#### [ Prefixed topic name replication ]

You should initiate failback steps only after replication from the cluster in the secondary Region to the cluster in the primary Region has caught up and the `MessageLag` metric in Amazon CloudWatch is close to 0. A planned failback should not result in any data loss.

1. Shut down all producers and consumers connecting to the MSK cluster in the secondary Region.

1. For active-passive topology, delete the Replicator that is replicating data from the cluster in the secondary Region to the primary Region. You do not need to delete the Replicator for active-active topology.

1. Start producers connecting to the MSK cluster in the primary Region.

1. If your application does not require message ordering, start consumers in the primary AWS Region that read from both the local and replicated topics using a wildcard operator. If your application requires message ordering, start consumers only for the replicated topics first, wait for lag to reach 0, then switch to local topics.

1. Verify that the existing Replicator from the cluster in the primary Region to the cluster in the secondary Region is in RUNNING state and working as expected using the `ReplicatorThroughput` and latency metrics.

------
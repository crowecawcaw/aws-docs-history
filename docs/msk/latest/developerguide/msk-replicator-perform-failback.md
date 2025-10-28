# Perform failback to the primary AWS

Region

You can failback to the primary AWS region after the service event in that
region has ended.

If you’re using Identical topic name replication configuration, follow these steps:

1. Create a new MSK Replicator with your secondary cluster as source and primary cluster as target, starting position set to _earliest_ and Identical topic name replication (**Keep the same topics name** in console).

This will start the process of copying all data written to the secondary cluster after failover back to the primary region. 2. Monitor the `MessageLag` metric on the new replicator in Amazon CloudWatch until it reaches `0`, which indicates all data has been replicated from secondary to primary. 3. After all data has been replicated, stop all producers connecting to the secondary cluster and start producers connecting to the primary cluster. 4. Wait for `MaxOffsetLag` metric for your consumers connecting to secondary cluster to become `0` to ensure they have processed all the data. See [Monitor consumer lags](consumer-lag.md "consumer-lag.md"). 5. Once all data has been processed, stop consumers in the secondary region and start consumers connecting to the primary cluster to complete the failback. 6. Delete the Replicator you created in the first step that is replicating data from your secondary cluster to primary. 7. Verify that your existing Replicator copying data from primary to secondary cluster has status as “RUNNING” and `ReplicatorThroughput` metric in Amazon CloudWatch `0`.

Note that when you create a new Replicator with starting position as _Earliest_ for failback, it starts reading all data in your secondary clusters’ topics. Depending on your data retention settings, your topics may have data that came from your source cluster. While MSK Replicator automatically filters those messages, you will still incur data processing and transfer charges for all the data in your secondary cluster. You can track the total data processed by replicator using `ReplicatorBytesInPerSec`. See [MSK Replicator metrics](msk-replicator-monitor.md#msk-replicator-metrics "msk-replicator-monitor.md#msk-replicator-metrics").
If you’re using Prefixed topic name configuration, follow these steps:

You should initiate failback steps only after replication from
the cluster in the secondary Region to the cluster in the primary Region has
caught up and the MessageLag metric in Amazon CloudWatch is close to 0. A planned failback
should not result in any data loss.

1. Shut down all producers and consumers connecting to the MSK cluster in
   the secondary Region.
2. For active-passive topology, delete the Replicator that is replicating
   data from cluster in the secondary Region to primary Region. You do not
   need to delete the Replicator for active-active topology.
3. Start producers connecting to the MSK cluster in the primary
   Region.
4. Depending on your application’s message ordering requirements, follow
   the steps in one of the following tabs.

No message ordering
If your application does not require message ordering,
start consumers in the primary AWS Region that read from
both the local (for example, `topic`) and
replicated topics (for example,
`<sourceKafkaClusterAlias>.topic`)
using a wildcard operator (for example,
`.*topic`). The consumers on local topics (e.g.:
topic) will resume from the last offset they consumed before
the failover. If there was any unprocessed data from before
the failover, it will get processed now. In the case of a
planned failover, there should be no such record.

Message ordering

    1. Start consumers only for the replicated topics on
     primary Region (for example,
     `<sourceKafkaClusterAlias>.topic`)
     but not the local topics (for example,
     `topic`).
    2. Wait for all the consumers of replicated topics on
     the cluster in the primary Region to finish
     processing all data, so that offset lag is 0 and the
     number of records processed is also 0. Then, stop
     consumers for the replicated topics on cluster in
     the primary Region. At this point, all records that
     were produced in the secondary Region after failover
     have been consumed in the primary Region.
    3. Start consumers for the local topics (for example,
     `topic`) on the cluster in the primary
     Region.

5. Verify that the existing Replicator from cluster in primary to cluster
   in secondary Region is in RUNNING state and working as expected using
   the `ReplicatorThroughput` and latency metrics.

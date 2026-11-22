

# Monitor and validate the upgrade

After you initiate the upgrade, monitor its progress as topics move from Standard brokers to Express brokers. When all topics are on Express brokers, validate your applications before you complete the upgrade. Your Standard brokers stay in the cluster until you complete the upgrade, so you can move topics back to them if you find an issue.

**Topics**
+ [Monitor upgrade progress](#msk-upgrade-monitor-progress)
+ [Validate your applications on Express brokers](#msk-upgrade-validate-applications)

## Monitor upgrade progress
<a name="msk-upgrade-monitor-progress"></a>

The upgrade typically takes a few hours, depending on the size of your cluster and the volume of data. You can monitor progress in the following ways:
+ **Cluster operations**: Track the overall upgrade on the **Cluster operations** tab in the Amazon MSK console, or use the `DescribeClusterOperation` API with the operation ARN that `UpdateBrokerType` returns. The operation status shows whether the upgrade is in progress, complete, or failed.
+ **Amazon CloudWatch metrics**: Graph `PartitionCount`, `BytesInPerSec`, and `BytesOutPerSec` by broker ID to watch partitions and throughput shift from your Standard brokers to your Express brokers.
+ **Topic reassignments**: Use the `ListTopicReassignments` API to see each reassignment operation and its status.
+ **Broker nodes**: Use the `ListNodes` API to list each broker with its broker node type, so that you can identify which brokers are Standard and which are Express.

```
# Status of the upgrade operation
aws kafka describe-cluster-operation \
    --cluster-operation-arn {{ClusterOperationArn}}

# Status of topic reassignments
aws kafka list-topic-reassignments \
    --cluster-arn {{ClusterArn}}

# Broker nodes and their types
aws kafka list-nodes \
    --cluster-arn {{ClusterArn}}
```

For more information, see [Monitor an Amazon MSK Provisioned cluster](monitoring.md).

## Validate your applications on Express brokers
<a name="msk-upgrade-validate-applications"></a>

After all topics have moved to Express brokers, validate your workload before you complete the upgrade. First, run `list-topic-reassignments` to confirm that all reassignments are complete, and confirm that `LeaderCount` is 0 on every Standard broker. Then do the following:
+ Verify that all topics, partitions, and consumer groups are present.
+ Confirm cluster health: `ActiveControllerCount` is 1 and `OfflinePartitionsCount` is 0.
+ Confirm that producer and consumer throughput and latency match your pre-upgrade baselines.
+ Confirm that stateful applications, such as Apache Flink and Kafka Streams applications, remain healthy and continue processing after partition leadership moves to Express brokers.

Run these checks for at least one full processing cycle of your workload. If a topic has issues, move it back to Standard brokers. For more information, see [Manage topic migration during upgrade](msk-upgrade-manage-topics.md).

**Important**  
Validate your applications before you complete the upgrade. After you complete the upgrade, you can't move topics back to Standard brokers.
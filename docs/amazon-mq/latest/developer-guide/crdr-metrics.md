# Cross-Region data replication metrics in Amazon CloudWatch

The Amazon MQ for ActiveMQ cross-Region data replication feature offers metrics for maintaining the reliability,
availability, and performance of your primary and replica brokers. During the replication process, a replica broker in a secondary Region receives asynchronously replicated data from the primary broker in the primary Region.
If the primary broker in the primary Region fails, you can promote the replica broker in the secondary Region to primary by initiating a switchover or failover.
For instructions on viewing metrics in Amazon CloudWatch, see [Accessing CloudWatch metrics for
Amazon MQ](amazon-mq-accessing-metrics.md "amazon-mq-accessing-metrics.md").

## CRDR timestamps

The following timestamps describe how the metrics found in Amazon CloudWatch are calculated.
There are five timestamps in the data replication process:

- Time of current observation (TCO): The current instant in time.
- Time of creation (TC): The instant in time an event was created on the
  replication queue by the primary broker. Available on both primary and replica
  brokers.
- Time of delivery (TD): The instant in time an event was successfully delivered
  to the replica broker. Only available on replica brokers.
- Time of processing (TP): The instant in time an event was successfully
  processed by the replica broker. Only available on replica brokers.
- Time of acknowledgement (TA): The instant in time an event was successfully
  acknowledged by the primary broker. Only available on primary brokers.

## Estimate switchover/failover performance with CRDR CloudWatch metrics

Amazon MQ enables metrics for your broker by default. You can view your broker metrics by accessing the Amazon CloudWatch console,
or by using the CloudWatch API.
The following metrics are useful for understanding the replication and switchover/failover performance of your CRDR brokers:

| Amazon MQ CloudWatch metric | Reason for CRDR use                                                                             |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| `TotalReplicationLag`       | The estimated time between TA and TC of the last unacknowledged event<br>on the primary broker. |
| `ReplicationLag`            | The estimated time between TP and TC of the last unacknowledged event<br>on the replica broker. |
| `PrimaryWaitTime`           | The estimated time between TCO and TC of the last processed event on<br>the primary broker.     |
| `ReplicaWaitTime`           | The estimated time between TCO and TP of the last processed<br>event on the replica broker.     |
| `QueueSize`                 | The total number of unacknowledged events in the replication queue on<br>the primary broker.    |

`TotalReplicationLag` and `ReplicationLag` describe the delayed replication between the primary and replica brokers.
The two metrics can also be used to estimate the time until the ongoing switchover or failover operation complete.

`PrimaryWaitTime` and `ReplicaWaitTime` can be used to identify any ongoing issues with the replication process.
If the value of the metric is constantly growing, this can indicate the replication process is degraded or paused.
Slow replication may happen due issues like to network partitioning, broker starts, and long recovery.

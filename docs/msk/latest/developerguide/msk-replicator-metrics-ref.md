

# Metrics reference
<a name="msk-replicator-metrics-ref"></a>

The following metrics describes performance or connection metrics for the MSK Replicator.

AuthError metrics do not cover topic-level auth errors. To monitor your MSK Replicator's topic-level auth errors, monitor Replicator's ReplicationLatency metrics and the source cluster's topic-level metrics, MessagesInPerSec. If a topic's ReplicationLatency dropped to 0 but the topic still has data being produced to it, it indicates that the Replicator has an Auth issue with the topic. Check that the Replicator's service execution IAM role has sufficient permission to access the topic.




- **Performance**
  - **Metric:** ReplicationLatency
  - **Description:** Time it takes records to replicate from the source to target cluster; duration between record produce time at source and replicated to target. If ReplicationLatency increases, check if clusters have enough partitions to support replication. High replication latency can occur when the partition count is too low for high throughput.
  - **Dimensions:** ReplicatorName / **Unit:** Milliseconds / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Maximum
  - **Dimensions:** ReplicatorName, Topic / **Unit:** Milliseconds / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Maximum

- **Performance**
  - **Metric:** MessageLag
  - **Description:** Monitors the sync between the MSK Replicator and the source cluster. MessageLag indicates the lag between the messages produced to the source cluster and messages consumed by the replicator. It is not the lag between the source and target cluster. Even if the source cluster is unavailable/interrupted, the replicator will finish writing the message it has consumed to the target cluster. After an outage, MessageLag shows an increase indicating the number of messages the replicator is behind the source cluster and this can be monitored until the number of messages is 0, showing that the replicator has caught up with the source cluster.
  - **Dimensions:** ReplicatorName / **Unit:** Count / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Sum
  - **Dimensions:** ReplicatorName, Topic / **Unit:** Count / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Sum

- **Performance**
  - **Metric:** ReplicatorBytesInPerSec
  - **Description:** Average number of bytes processed by the replicator per second. Data processed by MSK Replicator consists of all the data that MSK Replicator receives which includes the data replicated to target cluster and the data filtered by MSK Replicator (only if your Replicator is configured with Identical topic name configuration) to prevent the data being copied back to the same topic it originated from. If your Replicator is configured with "Prefixed" topic name configuration, both ReplicatorBytesInPerSec and ReplicatorThroughput metrics will have the same value as no data will be filtered by MSK Replicator.
  - **Dimensions:** ReplicatorName
  - **Unit:** BytesPerSecond
  - **Raw Metric Granularity:** ReplicatorName
  - **Raw Metric Aggregation Stat:** Sum

- **Performance**
  - **Metric:** ReplicatorThroughput
  - **Description:** Average number of bytes replicated per second. If ReplicatorThroughput drops for a topic, check KafkaClusterPingSuccessCount and AuthError metrics to ensure the Replicator can communicate with clusters, then check cluster metrics to ensure the cluster is not down.
  - **Dimensions:** ReplicatorName / **Unit:** BytesPerSecond / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Sum
  - **Dimensions:** ReplicatorName, Topic / **Unit:** BytesPerSecond / **Raw Metric Granularity:** Partition / **Raw Metric Aggregation Stat:** Sum

- **Performance**
  - **Metric:** ReplicationFailures
  - **Description:** Number of replication failures. Should be 0 for healthy replication. Non-zero may indicate message size limitations, timestamp violations, or record batch size problems.
  - **Dimensions:** ReplicatorName
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Debug**
  - **Metric:** AuthError
  - **Description:** The number of connections with failed authentication per second. If this metric is above 0, you can check if the service execution role policy for the replicator is valid and make sure there aren't deny permissions set for the cluster permissions. Based on clusterAlias dimension, you can identify if the source or target cluster is experiencing auth errors.
  - **Dimensions:** ReplicatorName, ClusterAlias
  - **Unit:** Count
  - **Raw Metric Granularity:** Worker
  - **Raw Metric Aggregation Stat:** Sum

- **Debug**
  - **Metric:** ThrottleTime
  - **Description:** The average time in ms a request was throttled by brokers on the cluster. Set throttling to avoid having the MSK Replicator overwhelm the cluster. If this metric is 0, replicationLatency is not high, and replicatorThroughput is as expected, then throttling is working as expected. If this metric is above 0, you can adjust throttling accordingly.
  - **Dimensions:** ReplicatorName, ClusterAlias
  - **Unit:** Milliseconds
  - **Raw Metric Granularity:** Worker
  - **Raw Metric Aggregation Stat:** Maximum

- **Debug**
  - **Metric:** ReplicatorFailure
  - **Description:** Number of failures that the replicator is experiencing.
  - **Dimensions:** ReplicatorName
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Debug**
  - **Metric:** KafkaClusterPingSuccessCount
  - **Description:** Indicates the health of the replicator connection to the kafka cluster. If this value is 1, the connection is healthy. If the value is 0 or no datapoint, the connection is unhealthy. If the value is 0, you can check network or IAM permission settings for the Kafka cluster. Based on ClusterAlias dimension, you can identify whether this metric is for source or target cluster.
  - **Dimensions:** ReplicatorName, ClusterAlias
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Consumer Group**
  - **Metric:** ConsumerGroupCount
  - **Description:** Number of consumer groups being synchronized. Verify it matches expected consumer groups.
  - **Dimensions:** ReplicatorName
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Consumer Group**
  - **Metric:** ConsumerGroupOffsetSyncFailure
  - **Description:** Number of consumer group offset sync failures. Should be 0. If greater than 0, check consumer groups are active and verify permissions.
  - **Dimensions:** ReplicatorName
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Consumer Group**
  - **Metric:** OffsetLag (MSK Cluster)
  - **Description:** Partition-level consumer lag on the MSK target cluster. Compare with OffsetLag (Non-MSK Cluster) to verify lag is equal.
  - **Dimensions:** Partition
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum

- **Consumer Group**
  - **Metric:** OffsetLag (Non-MSK Cluster)
  - **Description:** Partition-level consumer lag on the self-managed (non-MSK) source cluster. Compare with OffsetLag (MSK Cluster).
  - **Dimensions:** Partition
  - **Unit:** Count
  - **Raw Metric Granularity:** 
  - **Raw Metric Aggregation Stat:** Sum


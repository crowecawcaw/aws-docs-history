

# Monitor replication
<a name="msk-replicator-monitor"></a>

You can use [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/) in the target cluster Region to view metrics for `ReplicationLatency`, `MessageLag`, and `ReplicatorThroughput` at a topic and aggregate level for each MSK Replicator. Metrics are visible under **ReplicatorName** in the "AWS/Kafka" namespace. You can also see `ReplicatorFailure`, `AuthError`, and `ThrottleTime` metrics to check for issues.

The MSK console displays a subset of CloudWatch metrics for each MSK Replicator. From the console **Replicator** list, select the name of a Replicator and select the **Monitoring** tab.

You can also enable log forwarding for your MSK Replicator to gain deeper visibility into replication operations and simplify troubleshooting. MSK Replicator supports forwarding operational logs to Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose. By default, log delivery is not enabled. You can configure log delivery when you create or update a Replicator using the `logDelivery` configuration in the `CreateReplicator` or `UpdateReplicator` API request.

For more detailed information on monitoring, metrics, logs, and troubleshooting, see [Observability](msk-replicator-observability.md).
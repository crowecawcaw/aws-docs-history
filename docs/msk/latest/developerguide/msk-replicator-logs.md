

# MSK Replicator logs
<a name="msk-replicator-logs"></a>

MSK Replicator supports forwarding operational logs to help you monitor and troubleshoot replication. Log delivery is disabled by default. Enabling log delivery gives you deeper visibility into replication operations, authentication issues, and configuration problems.

**Note**  
When log delivery is enabled, your IAM role must have the additional permissions required to write to the configured log destination. For the required permissions, see [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions.html).

**Supported log destinations**  
MSK Replicator supports the following log destinations:
+ **Amazon CloudWatch Logs** — View logs in real time in the AWS Management Console. Supports log insights queries.
+ **Amazon S3** — Durably store logs for long-term retention and batch analysis.
+ **Amazon Data Firehose** — Stream logs to supported destinations such as Amazon OpenSearch Service, Splunk, or a custom HTTP endpoint.

**Configure log delivery**  
Configure log delivery by including the `logDelivery` parameter in your `CreateReplicator` or `UpdateReplicator` API request. By default, log delivery is not enabled.

Example `logDelivery` configuration:

```
# In CreateReplicator or UpdateReplicator API request:
"logDelivery": {
  "brokerLogs": {
    "cloudWatchLogs": {
      "enabled": true,
      "logGroup": "/aws/msk/replicator/my-replicator"
    },
    "s3": {
      "enabled": true,
      "bucket": "my-msk-logs-bucket",
      "prefix": "msk-replicator/"
    },
    "firehose": { "enabled": false }
  }
}
```

You can enable one or more destinations simultaneously based on your logging requirements.

**Log content**  
MSK Replicator logs include information about the following events and conditions:

1. Authorization failures for specific topics, record size errors when messages exceed configured limits and other common errors

1. Offset commit activity confirming replication progress

1. Replicated topic creation on the target cluster

1. Cluster connectivity warnings and errors

**Cost considerations**  
For more information about vended logs pricing, see the **Logs** tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).
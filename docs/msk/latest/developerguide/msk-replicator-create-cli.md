

# Create a replicator using the AWS CLI
<a name="msk-replicator-create-cli"></a>

Use the `create-replicator` command to create an MSK Replicator. Before you begin, make sure you have the [IAM permissions required to create an MSK Replicator](msk-replicator-create-iam-perms.md) and have completed [Prepare source and target clusters](msk-replicator-prepare-clusters.md).

**Note**  
The examples below show replication between two MSK clusters. MSK Replicator also supports replication between self-managed Apache Kafka clusters and MSK Provisioned clusters. For API examples covering that scenario, see [CreateReplicator API examples for self-managed Kafka clusters](msk-replicator-external-api-examples.md).

```
aws kafka create-replicator \
  --replicator-name "<replicator-name>" \
  --service-execution-role-arn "arn:aws:iam::<account-id>:role/<role-name>" \
  --kafka-clusters '[
    {
      "AmazonMskCluster": {"MskClusterArn": "<source-cluster-arn>"},
      "VpcConfig": {
        "SubnetIds": ["<subnet-1>", "<subnet-2>"],
        "SecurityGroupIds": ["<security-group-id>"]
      }
    },
    {
      "AmazonMskCluster": {"MskClusterArn": "<target-cluster-arn>"},
      "VpcConfig": {
        "SubnetIds": ["<subnet-1>", "<subnet-2>"],
        "SecurityGroupIds": ["<security-group-id>"]
      }
    }
  ]' \
  --replication-info-list '[
    {
      "SourceKafkaClusterArn": "<source-cluster-arn>",
      "TargetKafkaClusterArn": "<target-cluster-arn>",
      "TopicReplication": {
        "TopicsToReplicate": [".*"],
        "CopyTopicConfigurations": true,
        "CopyAccessControlListsForTopics": true,
        "DetectAndCopyNewTopics": true,
        "StartingPosition": {"Type": "LATEST"},
        "TopicNameConfiguration": {"Type": "PREFIXED"}
      },
      "ConsumerGroupReplication": {
        "ConsumerGroupsToReplicate": [".*"],
        "ConsumerGroupOffsetSyncMode": "LEGACY"
      },
      "TargetCompressionType": "NONE"
    }
  ]'
```

To enable log delivery when creating a replicator, include the `--log-delivery` parameter. The following example enables log delivery to Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose.

```
aws kafka create-replicator \
  --replicator-name "<replicator-name>" \
  --service-execution-role-arn "arn:aws:iam::<account-id>:role/<role-name>" \
  --kafka-clusters '[
    {
      "AmazonMskCluster": {"MskClusterArn": "<source-cluster-arn>"},
      "VpcConfig": {
        "SubnetIds": ["<subnet-1>", "<subnet-2>"],
        "SecurityGroupIds": ["<security-group-id>"]
      }
    },
    {
      "AmazonMskCluster": {"MskClusterArn": "<target-cluster-arn>"},
      "VpcConfig": {
        "SubnetIds": ["<subnet-1>", "<subnet-2>"],
        "SecurityGroupIds": ["<security-group-id>"]
      }
    }
  ]' \
  --replication-info-list '[
    {
      "SourceKafkaClusterArn": "<source-cluster-arn>",
      "TargetKafkaClusterArn": "<target-cluster-arn>",
      "TopicReplication": {
        "TopicsToReplicate": [".*"],
        "CopyTopicConfigurations": true,
        "CopyAccessControlListsForTopics": true,
        "DetectAndCopyNewTopics": true,
        "StartingPosition": {"Type": "LATEST"},
        "TopicNameConfiguration": {"Type": "PREFIXED"}
      },
      "ConsumerGroupReplication": {
        "ConsumerGroupsToReplicate": [".*"]
      },
      "TargetCompressionType": "NONE"
    }
  ]' \
  --log-delivery '{
    "ReplicatorLogDelivery": {
      "CloudWatchLogs": {
        "Enabled": true,
        "LogGroup": "/mskr/logs/<log-group-name>"
      },
      "S3": {
        "Enabled": true,
        "Bucket": "<s3-bucket-name>",
        "Prefix": "<optional-prefix>"
      },
      "Firehose": {
        "Enabled": true,
        "DeliveryStream": "<delivery-stream-name>"
      }
    }
  }'
```

You can enable one or more log delivery destinations. To enable only Amazon CloudWatch Logs, omit the `S3` and `Firehose` fields, or set their `Enabled` value to `false`. For more information about log delivery, see [MSK Replicator logs](msk-replicator-logs.md).

**Note**  
When log delivery is enabled, your IAM role must have the additional permissions required to write to the configured log destination. For the required permissions, see [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions.html).

For the full API reference, see [CreateReplicator](https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators.html#CreateReplicator) in the Amazon MSK API Reference.

## Selective topic replication
<a name="msk-replicator-cli-selective-topics"></a>

Use regex patterns in `topicsToReplicate` and `topicsToExclude` to control which topics are replicated. The following example replicates topics starting with `prod-` and excludes topics starting with `test-`:

```
"topicReplication": {
  "topicsToReplicate": ["prod-.*"],
  "topicsToExclude": ["test-.*"],
  "detectAndCopyNewTopics": true
}
```

## Verify Replicator status
<a name="msk-replicator-cli-verify-status"></a>

After creating a Replicator, check its status using the `describe-replicator` command:

```
aws kafka describe-replicator \
  --replicator-arn arn:aws:kafka:us-east-1:123456789012:replicator/my-replicator/xxx
```

The Replicator progresses through `CREATING` → `RUNNING` states. Allow approximately 30 minutes for the Replicator to reach `RUNNING` status. If it transitions to `FAILED`, see [Troubleshoot Amazon MSK Replicator](msk-replicator-troubleshooting.md).
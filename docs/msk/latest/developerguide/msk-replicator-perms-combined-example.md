

# Combined policy example
<a name="msk-replicator-perms-combined-example"></a>

The following example shows a complete service execution role policy for a replicator with all features enabled, including topic configuration replication and LEGACY offset sync mode. The example replicates topics matching `my-app-.*` between two MSK clusters. Replace all placeholder values with your actual resource identifiers.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "SourceClusterPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:Connect",
                "kafka-cluster:DescribeCluster",
                "kafka-cluster:WriteDataIdempotently"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:cluster/${SourceClusterName}/${SourceClusterUUID}"
            ]
        },
        {
            "Sid": "TargetClusterPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:Connect",
                "kafka-cluster:DescribeCluster",
                "kafka-cluster:AlterCluster",
                "kafka-cluster:WriteDataIdempotently"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:cluster/${TargetClusterName}/${TargetClusterUUID}"
            ]
        },
        {
            "Sid": "SourceInternalTopicPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:CreateTopic",
                "kafka-cluster:ReadData",
                "kafka-cluster:WriteData",
                "kafka-cluster:DescribeTopic",
                "kafka-cluster:DescribeTopicDynamicConfiguration",
                "kafka-cluster:AlterTopic",
                "kafka-cluster:AlterTopicDynamicConfiguration"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/*__amazon_msk_replicator_*",
                "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/mskr-offset-syncs.*",
                "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/*.checkpoints.internal"
            ]
        },
        {
            "Sid": "SourceDataTopicPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:ReadData",
                "kafka-cluster:DescribeTopic",
                "kafka-cluster:DescribeTopicDynamicConfiguration"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/my-app-*"
            ]
        },
        {
            "Sid": "SourceConsumerGroupPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:DescribeGroup"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:group/${SourceClusterName}/${SourceClusterUUID}/my-app-group-*"
            ]
        },
        {
            "Sid": "TargetInternalTopicPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:CreateTopic",
                "kafka-cluster:ReadData",
                "kafka-cluster:WriteData",
                "kafka-cluster:DescribeTopic",
                "kafka-cluster:DescribeTopicDynamicConfiguration",
                "kafka-cluster:AlterTopic",
                "kafka-cluster:AlterTopicDynamicConfiguration"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/*__amazon_msk_replicator_*",
                "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/mskr-offset-syncs.*",
                "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/*.checkpoints.internal"
            ]
        },
        {
            "Sid": "TargetDataTopicPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:CreateTopic",
                "kafka-cluster:WriteData",
                "kafka-cluster:DescribeTopic",
                "kafka-cluster:DescribeTopicDynamicConfiguration",
                "kafka-cluster:AlterTopicDynamicConfiguration",
                "kafka-cluster:AlterTopic"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/*.my-app-*"
            ]
        },
        {
            "Sid": "TargetGroupPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:AlterGroup",
                "kafka-cluster:DescribeGroup"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:group/${TargetClusterName}/${TargetClusterUUID}/*__amazon_msk_replicator_*",
                "arn:aws:kafka:${region}:${account}:group/${TargetClusterName}/${TargetClusterUUID}/my-app-group-*"
            ]
        }
    ]
}
```

**Tip**  
Start with the [Topic replication permissions](msk-replicator-perms-topic-replication.md) policy and only add the statements for optional features you have enabled. This follows the principle of least privilege and makes it easier to audit your permissions.


# Topic replication permissions
<a name="msk-replicator-perms-topic-replication"></a>

Use Amazon MSK Replicator to replicate topics between clusters. Grant the service execution role permissions to connect to both clusters, manage internal replicator topics, read data from source topics, and write replicated data to the target cluster.

The permissions for data topics on the target cluster differ based on the `topicNameConfiguration` setting:
+ **PREFIXED\_WITH\_SOURCE\_CLUSTER\_ALIAS** (default) — Replicated topics on the target are named with the source cluster alias as a prefix (for example, `source-alias.my-topic`). Because the full source alias is not known at creation time, use `*.${topicPattern}` as the IAM target data topic resource. For Kafka ACLs on non-MSK clusters, use the first 28 characters of the MSK cluster name as a PREFIXED pattern.
+ **IDENTICAL** — Replicated topics on the target keep the same name as on the source. The target data topic resource uses the same pattern as the source.

## Service execution role IAM policy (MSK clusters)
<a name="msk-replicator-perms-topic-replication-iam"></a>

Attach the following policy to the service execution role. Replace the placeholder values with your cluster names, UUIDs, and topic patterns. Choose the `TargetDataTopicPermissions` statement that matches your `topicNameConfiguration` setting.

**PREFIXED\_WITH\_SOURCE\_CLUSTER\_ALIAS (default)**  
Replicated topics on the target are named with the source cluster alias as a prefix (for example, `source-alias.my-topic`). Because the full alias is not known until the replicator is created, use a wildcard prefix with the topic pattern (for example, `*.${topicPattern}`) in the target data topic resource. IAM supports multiple wildcards in a resource ARN.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "ClusterPermissions",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:Connect",
                "kafka-cluster:DescribeCluster",
                "kafka-cluster:WriteDataIdempotently"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:cluster/${SourceClusterName}/${SourceClusterUUID}",
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
                "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/${topicPattern}"
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
                "kafka-cluster:DescribeTopicDynamicConfiguration"
            ],
            "Resource": [
                "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/*.${topicPattern}"
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
                "arn:aws:kafka:${region}:${account}:group/${TargetClusterName}/${TargetClusterUUID}/*__amazon_msk_replicator_*"
            ]
        }
    ]
}
```

**IDENTICAL**  
Replicated topics on the target keep the same name as on the source. Replace the `TargetDataTopicPermissions` statement with the following:

```
{
    "Sid": "TargetDataTopicPermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:CreateTopic",
        "kafka-cluster:WriteData",
        "kafka-cluster:DescribeTopic",
        "kafka-cluster:DescribeTopicDynamicConfiguration"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/${topicPattern}"
    ]
}
```

Replace `${topicPattern}` with the topic name or pattern you configured for replication (for example, `my-app-*` or a specific topic name).

**Note**  
Both MSK clusters require permissions for all internal topics (`*__amazon_msk_replicator_*`, `mskr-offset-syncs.*`, and `*.checkpoints.internal`). Use this policy to cover both clusters regardless of which cluster is non-MSK.

## Kafka ACLs (non-MSK clusters)
<a name="msk-replicator-perms-topic-replication-acls"></a>

When your source or target is a self-managed Apache Kafka cluster, configure the following ACLs using the `kafka-acls` CLI. All ACLs use the `ALLOW` permission type and the principal that your replicator authenticates as. Unless otherwise noted, ACLs use the `PREFIXED` pattern type.

When a non-MSK cluster is involved, the replicator places most internal topics (offset-syncs, checkpoints, worker group state) on the MSK cluster. The non-MSK cluster hosts only heartbeat topics and data topics.

**Non-MSK as source**  
When the source is a self-managed cluster, the replicator places all internal topics on the MSK target. The non-MSK source only needs ACLs for heartbeat topics and reading data topics.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Cluster | `kafka-cluster` (LITERAL) | Create, Describe, IdempotentWrite, DescribeConfigs | 
| Topic (heartbeat) | `__amazon_msk_replicator_` (PREFIXED) | Create, Read, Write, Describe, DescribeConfigs, Alter, AlterConfigs | 
| Topic (data) | PREFIXED or LITERAL per topic | Read, Describe, DescribeConfigs | 

**Non-MSK as target**  
When the target is a self-managed cluster, the replicator places all internal topics on the MSK source. The non-MSK target only needs ACLs for heartbeat topics and writing data topics. The data topic pattern depends on your `topicNameConfiguration` setting.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Cluster | `kafka-cluster` (LITERAL) | Create, Describe, IdempotentWrite, DescribeConfigs | 
| Topic (heartbeat) | `__amazon_msk_replicator_` (PREFIXED) | Create, Read, Write, Describe, DescribeConfigs, Alter, AlterConfigs | 
| Topic (replicated heartbeat) | `${first28CharsOfSourceClusterName}` (PREFIXED) | Create, Read, Write, Describe, DescribeConfigs, Alter, AlterConfigs | 
| Topic (data) | `${first28CharsOfSourceClusterName}` (PREFIXED) | Create, Write, Describe, DescribeConfigs, Alter, AlterConfigs | 

If you use `IDENTICAL` topic naming, replace the data topic row with the following.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Topic (data) | PREFIXED or LITERAL per topic (same name as source) | Create, Write, Describe, DescribeConfigs, Alter, AlterConfigs | 
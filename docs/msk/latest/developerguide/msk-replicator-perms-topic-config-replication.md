

# Topic configuration replication permissions
<a name="msk-replicator-perms-topic-config-replication"></a>

When `copyTopicConfigurations` is enabled (the default), the replicator reads topic-level configurations from the source cluster. These include `retention.ms`, `cleanup.policy`, and `max.message.bytes`. The replicator then applies these configurations to the corresponding replicated topics on the target cluster, keeping them in sync with source changes.

## Service execution role IAM policy (MSK clusters)
<a name="msk-replicator-perms-topic-config-replication-iam"></a>

Add the following statements to the topic replication policy. The source cluster permissions are the same regardless of naming mode. The target cluster permissions differ based on your `topicNameConfiguration` setting.

**Source cluster**  
The source cluster requires permission to read topic configurations.

```
{
    "Sid": "SourceTopicConfigReadPermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:DescribeTopicDynamicConfiguration"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/${topicPattern}"
    ]
}
```

**Target cluster — PREFIXED\_WITH\_SOURCE\_CLUSTER\_ALIAS (default)**  
The target cluster requires permission to alter topic configurations and partitions on the replicated topics. Because the full alias is not known until the replicator is created, use a wildcard prefix with the topic pattern.

```
{
    "Sid": "TargetTopicConfigWritePermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:DescribeTopicDynamicConfiguration",
        "kafka-cluster:AlterTopicDynamicConfiguration",
        "kafka-cluster:AlterTopic"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/*.${topicPattern}"
    ]
}
```

**Target cluster — IDENTICAL**  
When using identical topic naming, replicated topics keep the same name as on the source. Use the same topic pattern as the source.

```
{
    "Sid": "TargetTopicConfigWritePermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:DescribeTopicDynamicConfiguration",
        "kafka-cluster:AlterTopicDynamicConfiguration",
        "kafka-cluster:AlterTopic"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/${topicPattern}"
    ]
}
```

**Note**  
If `copyTopicConfigurations` is disabled, the `AlterTopicDynamicConfiguration` and `AlterTopic` permissions on the target data topics are not required. You can also omit `DescribeTopicDynamicConfiguration` from the source data topics if both `copyTopicConfigurations` and `detectAndCopyNewTopics` are disabled.

## Kafka ACLs (non-MSK clusters)
<a name="msk-replicator-perms-topic-config-replication-acls"></a>

**Non-MSK as source**  
When topic configuration replication is enabled and the source is a non-MSK cluster, the replicator needs to describe topic configurations.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Topic (data) | PREFIXED or LITERAL per topic | DescribeConfigs | 

**Non-MSK as target — PREFIXED\_WITH\_SOURCE\_CLUSTER\_ALIAS**  
When topic configuration replication is enabled and the target is a non-MSK cluster, use a PREFIXED ACL with the first 28 characters of the source cluster name to cover all replicated topics.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Topic (data) | `${first28CharsOfSourceClusterName}` (PREFIXED) | DescribeConfigs, AlterConfigs, Alter | 

**Non-MSK as target — IDENTICAL**  
When using identical topic naming, use ACLs matching the same topic names as on the source.


| Resource type | Pattern | Operations | 
| --- | --- | --- | 
| Topic (data) | PREFIXED or LITERAL per topic (same as source) | DescribeConfigs, AlterConfigs, Alter | 
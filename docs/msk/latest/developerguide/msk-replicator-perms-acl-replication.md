# ACL replication permissions

When `copyAccessControlListsForTopics` is enabled (the default), the replicator copies access control lists from the source cluster to the target cluster. Consumers on the target can then use the same authorization configuration.

## Service execution role IAM policy (MSK clusters)

###### Source cluster

The service execution role must have permission to read ACLs from the source cluster.

```
{
    "Sid": "SourceAclReadPermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:Connect",
        "kafka-cluster:DescribeCluster"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:cluster/${SourceClusterName}/${SourceClusterUUID}"
    ]
}
```

###### Target cluster

The service execution role must have permission to write ACLs to the target cluster.

```
{
    "Sid": "TargetAclWritePermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:Connect",
        "kafka-cluster:DescribeCluster",
        "kafka-cluster:AlterCluster"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:cluster/${TargetClusterName}/${TargetClusterUUID}"
    ]
}
```

## Kafka ACLs (non-MSK clusters)

###### Non-MSK as source

The replicator must have permission to describe ACLs on the source cluster.

| Resource type | Pattern                   | Operations |
| ------------- | ------------------------- | ---------- |
| Cluster       | `kafka-cluster` (LITERAL) | Describe   |

###### Non-MSK as target

The replicator must have permission to alter ACLs on the target cluster.

| Resource type | Pattern                   | Operations |
| ------------- | ------------------------- | ---------- |
| Cluster       | `kafka-cluster` (LITERAL) | Alter      |

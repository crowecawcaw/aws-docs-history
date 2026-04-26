# IAM permissions reference

The following table summarizes the IAM actions related to MSK Replicator.

| Action                        | Description                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| `kafka:CreateReplicator`      | Grants permission to create a replicator.                                                |
| `kafka:DescribeReplicator`    | Grants permission to describe a replicator.                                              |
| `kafka:UpdateReplicationInfo` | Grants permission to update replication info of a replicator.                            |
| `kafka:DeleteReplicator`      | Grants permission to delete a replicator.                                                |
| `kafka:ListReplicators`       | Grants permission to list replicators.                                                   |
| `kafka:TagResource`           | Grants permission to tag a replicator. Only needed if tags are provided during creation. |
| `kafka:ListTagsForResource`   | Grants permission to list tags for a replicator.                                         |

For the service execution role, the following cluster-level permissions are required:

- `kafka-cluster:Connect`
- `kafka-cluster:DescribeCluster`
- `kafka-cluster:AlterCluster`
- `kafka-cluster:DescribeTopic`
- `kafka-cluster:CreateTopic`
- `kafka-cluster:AlterTopic`
- `kafka-cluster:WriteData`
- `kafka-cluster:WriteDataIdempotently`
- `kafka-cluster:ReadData`
- `kafka-cluster:DescribeGroup`
- `kafka-cluster:AlterGroup`
- `kafka-cluster:DescribeClusterDynamicConfiguration`
- `kafka-cluster:DescribeTopicDynamicConfiguration`
- `kafka-cluster:AlterTopicDynamicConfiguration`

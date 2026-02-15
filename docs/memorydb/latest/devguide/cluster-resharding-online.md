# Online resharding for MemoryDB

By using online resharding and with MemoryDB, you can scale
your MemoryDB dynamically with no downtime. This approach means that your cluster
can continue to serve requests even while scaling or rebalancing is in process.

You can do the following:

- **Scale out** –
  Increase read and write capacity by adding shards
  to your MemoryDB cluster.

If you add one or more shards to your cluster, the number of nodes in each new
shard is the same as the number of nodes in the smallest of the existing
shards.

- **Scale in** –
  Reduce read and write capacity,
  and thereby costs, by removing shards from your MemoryDB cluster.

Currently, the following limitations apply to MemoryDB online resharding:

- There are limitations with slots or keyspaces and large items:

If any of the keys in a shard contain a large item, that key isn't migrated to a
new shard when scaling out . This functionality can result in
unbalanced shards.

If any of the keys in a shard contain a large item (items greater than 256 MB after
serialization), that shard isn't deleted when scaling in. This
functionality can result in some shards not being deleted.

- When scaling out, the number of nodes in any new shards equals the number of nodes in the
  existing shards.
  For more information, see [Best practices: Online cluster resizing](best-practices-online-resharding.md "best-practices-online-resharding.md").

You can horizontally scale your MemoryDB clusters using the AWS Management Console, the
AWS CLI, and the MemoryDB API.

## Adding shards with online

resharding

You can add shards to your MemoryDB cluster using the AWS Management Console, AWS CLI, or MemoryDB
API.

You can use the AWS Management Console to add one or more shards to your MemoryDB
cluster. The following procedure describes the process.

######

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. From the list of clusters, choose the cluster name from which you want to add a shard.
3. Under the **Shards and nodes** tab, choose **Add/Delete shards**
4. In **New number of shards**, enter the the number of shards you want.
5. Choose **Confirm** to keep the changes or **Cancel** to discard.

The following process describes how to reconfigure the shards in your MemoryDB
cluster by adding shards using the AWS CLI.

Use the following parameters with `update-cluster`.

###### Parameters

- `--cluster-name` –
  Required. Specifies which cluster (cluster)
  the shard reconfiguration operation is to be performed on.
- `--shard-configuration` – Required. Allows you to set
  the number of shards.
  - `ShardCount` – Set this property to specify the number of shards you want.

###### Example

The following example modifies the number of shards in the cluster
`my-cluster` to 2.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name my-cluster \
    --shard-configuration \
        ShardCount=2
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name my-cluster ^
    --shard-configuration ^
        ShardCount=2
```

It returns the following JSON response:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "updating",
        "NumberOfShards": 2,
        "AvailabilityMode": "MultiAZ",
        "ClusterEndpoint": {
            "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
            "Port": 6379
        },
        "NodeType": "db.r6g.large",
        "EngineVersion": "6.2",
        "EnginePatchVersion": "6.2.6",
        "ParameterGroupName": "default.memorydb-redis6",
        "ParameterGroupStatus": "in-sync",
        "SubnetGroupName": "my-sg",
        "TLSEnabled": true,
        "ARN": `"arn:aws:memorydb:us-east-1:xxxxxxexamplearn:cluster/my-cluster"`,
        "SnapshotRetentionLimit": 0,
        "MaintenanceWindow": "wed:03:00-wed:04:00",
        "SnapshotWindow": "04:30-05:30",
        "DataTiering": "false",
        "AutoMinorVersionUpgrade": true
    }
}
```

To view the details of the updated cluster once its status changes from _updating_ to _available_, use the following command:

For Linux, macOS, or Unix:

```
aws memorydb describe-clusters \
    --cluster-name my-cluster
    --show-shard-details

```

For Windows:

```
aws memorydb describe-clusters ^
    --cluster-name my-cluster
    --show-shard-details

```

It will return the following JSON response:

```
{
    "Clusters": [
        {
            "Name": "my-cluster",
            "Status": "available",
            "NumberOfShards": 2,
            "Shards": [
                {
                    "Name": "0001",
                    "Status": "available",
                    "Slots": "0-8191",
                    "Nodes": [
                        {
                            "Name": "my-cluster-0001-001",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1a",
                            "CreateTime": "2021-08-21T20:22:12.405000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0001-002",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1b",
                            "CreateTime": "2021-08-21T20:22:12.405000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 2
                },
                {
                    "Name": "0002",
                    "Status": "available",
                    "Slots": "8192-16383",
                    "Nodes": [
                        {
                            "Name": "my-cluster-0002-001",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1b",
                            "CreateTime": "2021-08-22T14:26:18.693000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0002-002",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1a",
                            "CreateTime": "2021-08-22T14:26:18.765000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 2
                }
            ],
            "ClusterEndpoint": {
                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                "Port": 6379
            },
            "NodeType": "db.r6g.large",
            "EngineVersion": "6.2",
            "EnginePatchVersion": "6.2.6",
            "ParameterGroupName": "default.memorydb-redis6",
            "ParameterGroupStatus": "in-sync",
            "SubnetGroupName": "my-sg",
            "TLSEnabled": true,
            "ARN": `"arn:aws:memorydb:us-east-1:xxxxxxexamplearn:cluster/my-cluster"`,
            "SnapshotRetentionLimit": 0,
            "MaintenanceWindow": "wed:03:00-wed:04:00",
            "SnapshotWindow": "04:30-05:30",
            "ACLName": "my-acl",
            "DataTiering": "false",
            "AutoMinorVersionUpgrade": true
        }
    ]
}
```

For more information, see [update-cluster](../../../cli/latest/reference/memorydb/update-cluster.md "../../../cli/latest/reference/memorydb/update-cluster.md") in the AWS CLI Command Reference.

You can use the MemoryDB API to reconfigure the shards in your MemoryDB cluster
online by using the `UpdateCluster` operation.

Use the following parameters with `UpdateCluster`.

###### Parameters

- `ClusterName` –
  Required. Specifies which cluster
  the shard reconfiguration operation is to be performed on.
- `ShardConfiguration` – Required. Allows you to set
  the number of shards.

      + `ShardCount` – Set this property to specify the number of shards you want.

  For more information, see [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md").

## Removing shards with online

resharding

You can remove shards from your MemoryDB cluster using the AWS Management Console, AWS CLI, or
MemoryDB API.

The following process describes how to reconfigure the shards in your MemoryDB
cluster by removing shards using the AWS Management Console.

###### Important

Before removing shards from your cluster, MemoryDB makes sure that
all your data will fit in the remaining shards. If the data will fit,
shards are deleted from the cluster as requested. If the data
won't fit in the remaining shards, the process is terminated and the cluster is left with the same shard configuration as before the request was made.

You can use the AWS Management Console to remove one or more shards from your MemoryDB cluster.
You cannot remove all the shards in a cluster. Instead, you must
delete the cluster. For more information, see [Step 5: Deleting a cluster](getting-started.md#clusters.delete "getting-started.md#clusters.delete"). The following procedure
describes the process for removing one or more shards.

######

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. From the list of clusters, choose the cluster name from which you want to remove a shard.
3. Under the **Shards and nodes** tab, choose **Add/Delete shards**
4. In **New number of shards**, enter the the number of shards you want (with a minimum of 1).
5. Choose **Confirm** to keep the changes or **Cancel** to discard.

The following process describes how to reconfigure the shards in your MemoryDB
cluster by removing shards using the AWS CLI.

###### Important

Before removing shards from your cluster, MemoryDB makes sure that
all your data will fit in the remaining shards. If the data will fit,
shards are deleted from
the cluster as requested and their keyspaces mapped into the
remaining shards. If the data will not fit in the remaining shards, the process is terminated and the cluster is left with the same shard configuration as before the request was made.

You can use the AWS CLI to remove one or more shards from your MemoryDB cluster. You
cannot remove all the shards in a cluster. Instead, you must
delete the cluster. For more information, see [Step 5: Deleting a cluster](getting-started.md#clusters.delete "getting-started.md#clusters.delete").

Use the following parameters with `update-cluster`.

###### Parameters

- `--cluster-name` –
  Required. Specifies which cluster (cluster)
  the shard reconfiguration operation is to be performed on.
- `--shard-configuration` – Required. Allows you to set
  the number of shards using the `ShardCount` property:

`ShardCount` – Set this property to specify the number of shards you want.

###### Example

The following example modifies the number of shards in the cluster
`my-cluster` to 2.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name my-cluster \
    --shard-configuration \
        ShardCount=2
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name my-cluster ^
    --shard-configuration ^
        ShardCount=2
```

It returns the following JSON response:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "updating",
        "NumberOfShards": 2,
        "AvailabilityMode": "MultiAZ",
        "ClusterEndpoint": {
            "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
            "Port": 6379
        },
        "NodeType": "db.r6g.large",
        "EngineVersion": "6.2",
        "EnginePatchVersion": "6.2.6",
        "ParameterGroupName": "default.memorydb-redis6",
        "ParameterGroupStatus": "in-sync",
        "SubnetGroupName": "my-sg",
        "TLSEnabled": true,
        "ARN": `"arn:aws:memorydb:us-east-1:xxxxxxexamplearn:cluster/my-cluster"`,
        "SnapshotRetentionLimit": 0,
        "MaintenanceWindow": "wed:03:00-wed:04:00",
        "SnapshotWindow": "04:30-05:30",
        "DataTiering": "false",
        "AutoMinorVersionUpgrade": true
    }
}
```

To view the details of the updated cluster once its status changes from _updating_ to _available_, use the following command:

For Linux, macOS, or Unix:

```
aws memorydb describe-clusters \
    --cluster-name my-cluster
    --show-shard-details

```

For Windows:

```
aws memorydb describe-clusters ^
    --cluster-name my-cluster
    --show-shard-details

```

It will return the following JSON response:

```
{
    "Clusters": [
        {
            "Name": "my-cluster",
            "Status": "available",
            "NumberOfShards": 2,
            "Shards": [
                {
                    "Name": "0001",
                    "Status": "available",
                    "Slots": "0-8191",
                    "Nodes": [
                        {
                            "Name": "my-cluster-0001-001",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1a",
                            "CreateTime": "2021-08-21T20:22:12.405000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0001-002",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1b",
                            "CreateTime": "2021-08-21T20:22:12.405000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 2
                },
                {
                    "Name": "0002",
                    "Status": "available",
                    "Slots": "8192-16383",
                    "Nodes": [
                        {
                            "Name": "my-cluster-0002-001",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1b",
                            "CreateTime": "2021-08-22T14:26:18.693000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0002-002",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1a",
                            "CreateTime": "2021-08-22T14:26:18.765000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 2
                }
            ],
            "ClusterEndpoint": {
                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                "Port": 6379
            },
            "NodeType": "db.r6g.large",
            "EngineVersion": "6.2",
            "EnginePatchVersion": "6.2.6",
            "ParameterGroupName": "default.memorydb-redis6",
            "ParameterGroupStatus": "in-sync",
            "SubnetGroupName": "my-sg",
            "TLSEnabled": true,
            "ARN": `"arn:aws:memorydb:us-east-1:xxxxxxexamplearn:cluster/my-cluster"`,
            "SnapshotRetentionLimit": 0,
            "MaintenanceWindow": "wed:03:00-wed:04:00",
            "SnapshotWindow": "04:30-05:30",
            "ACLName": "my-acl",
            "DataTiering": "false",
            "AutoMinorVersionUpgrade": true
        }
    ]
}
```

For more information, see [update-cluster](../../../cli/latest/reference/memorydb/update-cluster.md "../../../cli/latest/reference/memorydb/update-cluster.md") in the AWS CLI Command Reference.

You can use the MemoryDB API to reconfigure the shards in your MemoryDB cluster
online by using the `UpdateCluster` operation.

The following process describes how to reconfigure the shards in your MemoryDB
cluster by removing shards using the MemoryDB API.

###### Important

Before removing shards rom your cluster, MemoryDB makes sure that
all your data will fit in the remaining shards. If the data will fit,
shards are deleted from the
cluster as requested and their keyspaces mapped into the
remaining shards. If the data will not fit in the remaining shards, the process is terminated and the cluster is left with the same shard configuration as before the request was made.

You can use the MemoryDB API to remove one or more shards from your MemoryDB cluster.
You cannot remove all the shards in a cluster. Instead, you must
delete the cluster. For more information, see [Step 5: Deleting a cluster](getting-started.md#clusters.delete "getting-started.md#clusters.delete").

Use the following parameters with `UpdateCluster`.

###### Parameters

- `ClusterName` –
  Required. Specifies which cluster (cluster)
  the shard reconfiguration operation is to be performed on.
- `ShardConfiguration` – Required. Allows you to set
  the number of shards using the `ShardCount` property:

`ShardCount` – Set this property to specify the number of shards you want.

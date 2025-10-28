# Changing the number of replicas

You can dynamically increase or decrease the number of read replicas in your MemoryDB

cluster using the AWS Management Console, the AWS CLI, or the MemoryDB API. All shards must have the same
number of replicas.

## Increasing the number of replicas in a cluster

You can increase the number of replicas in a MemoryDB cluster up to a maximum of five per shard. You can do so using the AWS Management Console, the AWS CLI,
or the MemoryDB API.

###### Topics

- [Using the AWS Management Console](#increase-replica-count-con "#increase-replica-count-con")
- [Using the AWS CLI](#increase-replica-count-cli "#increase-replica-count-cli")
- [Using the MemoryDB API](#increase-replica-count-api "#increase-replica-count-api")

### Using the AWS Management Console

To increase the number of replicas in a MemoryDB cluster (console), see [Adding / Removing nodes from a cluster](clusters.md "clusters.md").

### Using the AWS CLI

To increase the number of replicas in a MemoryDB cluster, use the
`update-cluster` command with the following parameters:

- `--cluster-name` – Required. Identifies which
  cluster you want to increase the number of replicas in.
- `--replica-configuration` – Required. Allows you to set
  the number of replicas. To increase the replica count, set the `ReplicaCount` property to the number of replicas that you
  want in this shard at the end of this operation.

The following example increases the number of replicas in the cluster
`my-cluster` to 2.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name my-cluster \
    --replica-configuration \
        ReplicaCount=2
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name my-cluster ^
    --replica-configuration ^
        ReplicaCount=2
```

It returns the following JSON response:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "updating",
        "NumberOfShards": 1,
        "ClusterEndpoint": {
            "Address": `"clustercfg.my-cluster.xxxxx.memorydb.us-east-1.amazonaws.com"`,
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
            "NumberOfShards": 1,
            "Shards": [
                {
                    "Name": "0001",
                    "Status": "available",
                    "Slots": "0-16383",
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
                        },
                        {
                            "Name": "my-cluster-0001-003",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1a",
                            "CreateTime": "2021-08-22T12:59:31.844000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 3
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

For more information about increasing the number of replicas using the CLI, see
[update-cluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") in the _AWS CLI Command Reference._

### Using the MemoryDB API

To increase the number of replicas in a MemoryDB shard, use the
`UpdateCluster` action with the following parameters:

- `ClusterName` – Required. Identifies which
  cluster you want to increase the number of replicas in.
- `ReplicaConfiguration` – Required. Allows you to set the
  number of replicas. To increase the replica count, set the `ReplicaCount` property to the number of replicas that you
  want in this shard at the end of this operation.

The following example increases the number of replicas in the cluster
`sample-cluster` to three. When the example is finished, there
are three replicas in each shard. This number applies whether this is a MemoryDB cluster with a single shard or a MemoryDB cluster with
multiple shards.

```
https://memory-db.us-east-1.amazonaws.com/
      ?Action=UpdateCluster
      &ReplicaConfiguration.ReplicaCount=3
      &ClusterName=sample-cluster
      &Version=2021-01-01
      &SignatureVersion=4
      &SignatureMethod=HmacSHA256
      &Timestamp=20210802T192317Z
      &X-Amz-Credential=<credential>
```

For more information about increasing the number of replicas using the API, see
[UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md").

## Decreasing the number of replicas in a cluster

You can decrease the number of replicas in a cluster for MemoryDB. You can decrease the number of replicas to zero, but you can't
failover to a replica if your primary node fails.

You can use the AWS Management Console, the AWS CLI or the MemoryDB API to decrease the number of replicas
in a cluster.

###### Topics

- [Using the AWS Management Console](#decrease-replica-count-con "#decrease-replica-count-con")
- [Using the AWS CLI](#decrease-replica-count-cli "#decrease-replica-count-cli")
- [Using the MemoryDB API](#decrease-replica-count-api "#decrease-replica-count-api")

### Using the AWS Management Console

To decrease the number of replicas in a MemoryDB cluster (console), see [Adding / Removing nodes from a cluster](clusters.md "clusters.md").

### Using the AWS CLI

To decrease the number of replicas in a MemoryDB cluster, use the
`update-cluster` command with the following parameters:

- `--cluster-name` – Required. Identifies which
  cluster you want to decrease the number of replicas in.
- `--replica-configuration` – Required.

`ReplicaCount` – Set this property to specify the number of replica nodes you want.

The following example uses `--replica-configuration` to decrease the
number of replicas in the cluster `my-cluster` to the
value specified.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name my-cluster \
    --replica-configuration \
        ReplicaCount=1
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name my-cluster ^
    --replica-configuration ^
        ReplicaCount=1 ^
```

It will return the following JSON response:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "updating",
        "NumberOfShards": 1,
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
            "NumberOfShards": 1,
            "Shards": [
                {
                    "Name": "0001",
                    "Status": "available",
                    "Slots": "0-16383",
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

For more information about decreasing the number of replicas using the CLI, see
[update-cluster](../../../cli/latest/reference/memorydb/update-cluster.md "../../../cli/latest/reference/memorydb/update-cluster.md") in the _AWS CLI Command Reference._

### Using the MemoryDB API

To decrease the number of replicas in a MemoryDB cluster, use the
`UpdateCluster` action with the following parameters:

- `ClusterName` – Required. Identifies which
  cluster you want to decrease the number of replicas in.
- `ReplicaConfiguration` – Required. Allows you to set
  the number of replicas.

`ReplicaCount` – Set this property to specify the number of replica nodes you want.

The following example uses `ReplicaCount` to decrease the number
of replicas in the cluster `sample-cluster` to one. When
the example is finished, there is one replica in each shard. This number
applies whether this is a MemoryDB cluster with a single shard or a MemoryDB cluster with multiple shards.

```
https://memory-db.us-east-1.amazonaws.com/
      ?Action=UpdateCluster
      &ReplicaConfiguration.ReplicaCount=1
      &ClusterName=sample-cluster
      &Version=2021-01-01
      &SignatureVersion=4
      &SignatureMethod=HmacSHA256
      &Timestamp=20210802T192317Z
      &X-Amz-Credential=<credential>
```

For more information about decreasing the number of replicas using the API, see
[UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md").

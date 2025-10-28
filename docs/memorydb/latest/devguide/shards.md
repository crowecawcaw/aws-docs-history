# Working with shards

A shard is a collection of one to 6 nodes.

You can create a cluster with higher number of shards and lower number of replicas totaling up to 500 nodes per cluster. This cluster configuration can range from 500 shards and 0 replicas to 100 shards and 4 replicas, which is the maximum number of replicas allowed.

The cluster's data is partitioned across the cluster's shards.
If there is more than one node in a shard, the shard implements replication
with one node being the read/write primary node and the other nodes read-only
replica nodes.

When you create a MemoryDB cluster using the AWS Management Console,
you specify the number of shards in the cluster and the number of
nodes in the shards. For more information, see [Creating a MemoryDB cluster](getting-started.md#clusters.create "getting-started.md#clusters.create").

Each node in a shard has the same compute, storage and memory specifications.
The MemoryDB API lets you control cluster-wide attributes, such as the number of nodes,
security settings, and system maintenance windows.

For more information, see [Offline resharding for MemoryDB](cluster-resharding-offline.md "cluster-resharding-offline.md") and [Online resharding for MemoryDB](cluster-resharding-online.md "cluster-resharding-online.md").

## Finding a shard's name

You can find a shard's name using the AWS Management Console, the AWS CLI or the MemoryDB API.

The following procedure uses the AWS Management Console to find a MemoryDB's cluster's
shard names.

######

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. On the left navigation pane, choose **Clusters**.
3. Choose the cluster under **Name** whose shard names you want to find.
4. Under the **Shards and nodes** tab, view the list of shards under **Name**. You can also expand each one to view details of their nodes.

To find shard (shard) names for MemoryDB clusters use the AWS CLI operation `describe-clusters` with the following
optional parameter.

- **`--cluster-name`**—An optional parameter
  which when used limits the output to the details of the specified cluster. If this
  parameter is omitted, the details of up to 100 clusters is returned.
- **`--show-shard-details`**—Returns details of the shards, including their names.
  This command returns the details for `my-cluster`.

For Linux, macOS, or Unix:

```
aws memorydb describe-clusters \
    --cluster-name `my-cluster`
    --show-shard-details

```

For Windows:

```
aws memorydb describe-clusters ^
    --cluster-name `my-cluster`
    --show-shard-details

```

It returns the following JSON response:

Line breaks are added for ease of reading.

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
                                "Address": `"clustercfg.my-cluster.xxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0001-002",
                            "Status": "available",
                            "AvailabilityZone": "us-east-1b",
                            "CreateTime": "2021-08-21T20:22:12.405000-07:00",
                            "Endpoint": {
                                "Address": `"clustercfg.my-cluster.xxxxx.memorydb.us-east-1.amazonaws.com"`,
                                "Port": 6379
                            }
                        }
                    ],
                    "NumberOfNodes": 2
                }
            ],
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
            "ARN": `"arn:aws:memorydb:us-east-1:xxxxxexamplearn:cluster/my-cluster"`,
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

To find shard ids for MemoryDB clusters use the API operation `DescribeClusters` with the following
optional parameter.

- **`ClusterName`**—An optional parameter
  which when used limits the output to the details of the specified cluster. If this
  parameter is omitted, the details of up to 100 clusters is
  returned.
- **`ShowShardDetails`**—Returns details of the shards, including their names.
  This command returns the details for `my-cluster`.

For Linux, macOS, or Unix:

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeClusters
   &ClusterName=sample-cluster
   &ShowShardDetails=true
   &Version=2021-01-01
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

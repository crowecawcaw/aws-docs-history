# Finding connection endpoints

Your application connects to your cluster using the endpoint.
An endpoint is a cluster's unique address. Use the cluster's _Cluster Endpoint_ for all operations.

The following sections guide you through discovering the endpoint you'll need.

###### To find a MemoryDB cluster's endpoint

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. From the navigation pane, choose **Clusters**.

The clusters screen will appear with a list of clusters. Choose the cluster you wish to connect to. 3. To find the cluster's endpoint, choose the cluster's name (not the radio button). 4. The **Cluster endpoint** is displayed under
**Cluster details**. To copy it, choose the _copy_ icon to the left of the endpoint.
You can use the `describe-clusters` command to discover the endpoint for a cluster.

The command returns the cluster's endpoint.

The following operation retrieves the endpoint, which in this example is represented as a `sample`, for the
cluster `mycluster`.

It returns the following JSON response:

```
aws memorydb describe-clusters \
  --cluster-name `mycluster`
```

For Windows:

```
aws memorydb describe-clusters ^
   --cluster-name `mycluster`

```

```
{
    "Clusters": [
        {
            "Name": "my-cluster",
            "Status": "available",
            "NumberOfShards": 1,
            "ClusterEndpoint": {
                "Address": `"clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com"`,
                "Port": 6379
            },
            "NodeType": "db.r6g.large",
            "EngineVersion": "6.2",
            "EnginePatchVersion": "6.2.4",
            "ParameterGroupName": "default.memorydb-redis6",
            "ParameterGroupStatus": "in-sync",
            "SubnetGroupName": "my-sg",
            "TLSEnabled": true,
            "ARN": `"arn:aws:memorydb:us-east-1:zzzexamplearn:cluster/my-cluster"`,
            "SnapshotRetentionLimit": 0,
            "MaintenanceWindow": "wed:03:00-wed:04:00",
            "SnapshotWindow": "04:30-05:30",
            "ACLName": "my-acl",
            "AutoMinorVersionUpgrade": true
        }
    ]
}
```

For more information, see [describe-clusters](../../../cli/latest/reference/memorydb/describe-clusters.md "../../../cli/latest/reference/memorydb/describe-clusters.md").

You can use the MemoryDB API to discover the endpoint of a cluster.

### Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)

You can use the MemoryDB API to discover the endpoint for a cluster with the
`DescribeClusters` action.
The action returns the cluster's endpoint.

The following operation retrieves the cluster endpoint for the
cluster `mycluster`.

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=DescribeClusters
    &ClusterName=mycluster
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210802T192317Z
    &Version=2021-01-01
    &X-Amz-Credential=<credential>
```

For more information, see [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md").

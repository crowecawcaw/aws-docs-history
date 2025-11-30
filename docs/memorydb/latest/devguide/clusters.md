# Viewing a cluster's details

You can view detail information about one or more clusters using the MemoryDB console, AWS CLI, or MemoryDB API.

The following procedure details how to view the details of a MemoryDB cluster using the MemoryDB console.

######

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see details of a cluster, choose the radio button to the left of the cluster's
   name and then choose **View details**. You can also click directly on the cluster to view the cluster details page.

The **Cluster details** page displays details about the cluster,
including the cluster endpoint. You can view more details using the multiple tabs available in the **Cluster details** page. 3. Choose the **Shards and nodes** tab to see a listing of the cluster's shards and the number of nodes in each shard. 4. To view specific information on a node, expand the shard in the table below. Alternatively you can also search for the shard using the search box.

Doing this displays information about each node, including its Availability Zone, slots/keyspaces and status. 5. Choose the **Metrics** tab to
monitor their respective processes, such as **CPU Utilization** and **Engine CPU Utilization**.
For more information, see [Metrics for MemoryDB](metrics.md "metrics.md"). 6. Choose the **Network and security** tab to see details of the subnet group and security groups.

    1. In **Subnet group**, you can see the subnet group's name, a link to the VPC that subnet belongs to and
     the subnet group's Amazon Resource Name (ARN).
    2. In **Security groups**, you can see the security group ID, name and description.

7. Choose the **Maintenace and snapshot** tab to see details of the snapshot settings.
   1. In **Snapshot**, you can see whether Automated Snapshots are enabled, the snapshot retention period and
      the snapshot window.
   2. In **Snapshots**, you will see a list of any snapshots to this cluster, including the snapshot name, size, number of shards and status.For more information, see [Snapshot and restore](snapshots.md "snapshots.md") .

8. Choose the **Maintenace and snapshot** tab to see details of the Maintenance Window, along with any pending ACL, Resharding or Service updates. For more information, see [Managing maintenance](maintenance-window.md "maintenance-window.md").
9. Choose the **Service Updates** tab to see details of the any service updates that are applicable to this cluster. For more information, see
   [Service updates in MemoryDB](service-updates.md "service-updates.md").
10. Choose the **Tags** tab to see details of any resource or cost-allocation tags that are associated with this cluster. For more information, see
    [Tagging snapshots](snapshots-tagging.md "snapshots-tagging.md").
    You can view the details for a cluster using the AWS CLI `describe-clusters` command.
    If the `--cluster-name` parameter is omitted, details for multiple clusters, up to `--max-results`, are returned.
    If the `--cluster-name` parameter is included, details for the specified cluster are returned.
    You can limit the number of records returned with the `--max-results` parameter.

The following code lists the details for `my-cluster`.

```
aws memorydb describe-clusters --cluster-name `my-cluster`
```

The following code list the details for up to 25 clusters.

```
aws memorydb describe-clusters --max-results `25`
```

For Linux, macOS, or Unix:

```
aws memorydb describe-clusters \
    --cluster-name `my-cluster` \
    --show-shard-details
```

For Windows:

```
aws memorydb describe-clusters ^
    --cluster-name `my-cluster` ^
    --show-shard-details
```

The following JSON output shows the response:

```
{
    "Clusters": [
        {
            "Name": "my-cluster",
            "Description": "my cluster",
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
                            "CreateTime": 1629230643.961,
                            "Endpoint": {
                                "Address": "my-cluster-0001-001.my-cluster.abcdef.memorydb.us-east-1.amazonaws.com",
                                "Port": 6379
                            }
                        },
                        {
                            "Name": "my-cluster-0001-002",
                            "Status": "available",
                            "CreateTime": 1629230644.025,
       	       	       	    "Endpoint":	{
       	       	       	       	"Address": "my-cluster-0001-002.my-cluster.abcdef.memorydb.us-east-1.amazonaws.com",
       	       	       	       	"Port":	6379
       	       	       	    }
                        }
                    ],
                    "NumberOfNodes": 2
                }
            ],
            "ClusterEndpoint": {
                "Address": "clustercfg.my-cluster.abcdef.memorydb.us-east-1.amazonaws.com",
                "Port": 6379
            },
            "NodeType": "db.r6g.large",
            "EngineVersion": "6.2",
            "EnginePatchVersion": "6.2.6",
            "ParameterGroupName": "default.memorydb-redis6",
            "ParameterGroupStatus": "in-sync",
            "SubnetGroupName": "default",
            "TLSEnabled": true,
            "ARN": "arn:aws:memorydb:us-east-1:000000000:cluster/my-cluster",
            "SnapshotRetentionLimit": 0,
            "MaintenanceWindow": "sat:06:30-sat:07:30",
            "SnapshotWindow": "04:00-05:00",
            "ACLName": "open-access",
            "DataTiering": "false",
            "AutoMinorVersionUpgrade": true,
        }

```

For more information, see the AWS CLI for MemoryDB topic [`describe-clusters`](../../../cli/latest/reference/memorydb/describe-clusters.md "../../../cli/latest/reference/memorydb/describe-clusters.md").

You can view the details for a cluster using the MemoryDB API `DescribeClusters` action.
If the `ClusterName` parameter is included, details for the specified cluster are returned.
If the `ClusterName` parameter is omitted, details for up to `MaxResults` (default 100)
clusters are returned.
The value for `MaxResults` cannot be less than 20 or greater than 100.

The following code lists the details for `my-cluster`.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeClusters
   &ClusterName=my-cluster
   &Version=2021-01-01
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

The following code list the details for up to 25 clusters.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DescribeClusters
   &MaxResults=25
   &Version=2021-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

For more information, see the MemoryDB API reference topic [`DescribeClusters`](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md").

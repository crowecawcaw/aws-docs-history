# Describing Amazon DocumentDB

clusters

You can use either Amazon DocumentDB Management Console or the AWS CLI to see
details such as connection endpoints, security groups, VPCs, and
parameter groups pertaining to your Amazon DocumentDB clusters.

For more information, see the following:

- [Monitoring an Amazon DocumentDB cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md")
- [Finding a cluster's endpoints](db-cluster-endpoints-find.md "db-cluster-endpoints-find.md")

Using the AWS Management Console
Use the following procedure to view the details of a specified
Amazon DocumentDB cluster using the console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the list of clusters, choose the name of the cluster
that you want to see the details of. The information about
the cluster is organized into the following groupings:

    * **Summary** — General
     information about the cluster, including the engine
     version, cluster status, pending maintenance, and the
     status of its parameter group.
    * **Connectivity & Security**
     —The **Connect** section
     lists connection endpoints to connect to this cluster
     with the mongo shell or with an application. The
     **Security Groups** section lists
     the security groups associated with this cluster and
     their VPC ID and descriptions.
    * **Configuration** — The
     **Cluster details** section lists
     details about the cluster, including the cluster's
     Amazon Resource Name (ARN), endpoint, and parameter
     group. It also lists the cluster's backup information,
     maintenance details, and security and network
     settings. The **Cluster instances**
     section lists the instances that belong to this cluster
     with each instance's role and cluster parameter group
     status.
    * **Monitoring** — The
     Amazon CloudWatch Logs metrics for this cluster. For more
     information, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").
    * **Events & tags** — The
     **Recent events** section lists the
     recent events for this cluster. Amazon DocumentDB keeps a
     record of events that relate to your clusters,
     instances, snapshots, security groups, and cluster
     parameter groups. This information includes the date,
     time, and message associated with each event. The
     **Tags** section lists the tags
     attached to this cluster.

Using the AWS CLI
To view the details of your Amazon DocumentDB clusters using the AWS CLI,
use the `describe-db-clusters` command as shown in the
examples below. For more information, see [`DescribeDBClusters`](API_DescribeDBClusters.md "API_DescribeDBClusters.md")
in the _Amazon DocumentDB Resource Management API Reference_.

###### Note

For certain management features such as cluster and instance
lifecycle management, Amazon DocumentDB leverages operational technology
that is shared with Amazon RDS. The `filterName=engine,Values=docdb`
filter parameter returns only Amazon DocumentDB clusters.

**Example 1: List all Amazon DocumentDB clusters**

The following AWS CLI code lists the details for all Amazon DocumentDB
clusters in a region.

```
aws docdb describe-db-clusters --filter Name=engine,Values=docdb
```

Output from this operation looks something like the following.

```
{
    "DBClusters": [
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-1",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        },
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-2",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        },
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-3",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        }
    ]
}

```

**Example 2: List all details for a
specified Amazon DocumentDB cluster**

The following AWS CLI code lists the details for the cluster
`sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb describe-db-clusters \
   --filter Name=engine,Values=docdb \
   --db-cluster-identifier sample-cluster
```

For Windows:

```
aws docdb describe-db-clusters ^
   --filter Name=engine,Values=docdb ^
   --db-cluster-identifier sample-cluster
```

Output from this operation looks something like the following.

```
{
    "DBClusters": [
        {
            "AllocatedStorage": 1,
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1a",
                "us-east-1d"
            ],
            "BackupRetentionPeriod": 2,
            "DBClusterIdentifier": "sample-cluster",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            "EarliestRestorableTime": "2023-11-07T22:34:08.148000+00:00",
            "Endpoint": "sample-cluster.node.us-east-1.amazon.com",
            "ReaderEndpoint": "sample-cluster.node.us-east-1.amazon.com",
            "MultiAZ": false,
            "Engine": "docdb",
            "EngineVersion": "5.0.0",
            "LatestRestorableTime": "2023-11-10T07:21:16.772000+00:00",
            "Port": 27017,
            "MasterUsername": "chimeraAdmin",
            "PreferredBackupWindow": "22:22-22:52",
            "PreferredMaintenanceWindow": "sun:03:01-sun:03:31",
            "ReadReplicaIdentifiers": [],
            "DBClusterMembers": [
                {
                    "DBInstanceIdentifier": "sample-instance-1",
                    "IsClusterWriter": true,
                    "DBClusterParameterGroupStatus": "in-sync",
                    "PromotionTier": 1
                },
                {
                    "DBInstanceIdentifier": "sample-instance-2",
                    "IsClusterWriter": true,
                    "DBClusterParameterGroupStatus": "in-sync",
                    "PromotionTier": 1
                },

            ],
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-9084c2ec",
                    "Status": "active"
                }
            ],
            "HostedZoneId": "Z06853723JYKYBXTJ49RB",
            "StorageEncrypted": false,
            "DbClusterResourceId": "cluster-T4LGLANHVAPGQYYULWUDKLVQL4",
            "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster",
            "AssociatedRoles": [],
            "IAMDatabaseAuthenticationEnabled": false,
            "ClusterCreateTime": "2023-11-06T18:05:41.568000+00:00",
            "EngineMode": "provisioned",
            "DeletionProtection": false,
            "HttpEndpointEnabled": false,
            "CopyTagsToSnapshot": false,
            "CrossAccountClone": false,
            "DomainMemberships": [],
            "TagList": [],
            "StorageType": "iopt1",
            "AutoMinorVersionUpgrade": false,
            "NetworkType": "IPV4",
            "IOOptimizedNextAllowedModificationTime": "2023-12-07T18:05:41.580000+00:00"
        }
    ]
}
```

**Example 3: List specific details for
a Amazon DocumentDB cluster**

To list a subset of the clusters' details using the AWS CLI,
add a `--query` that specifies which cluster
members the `describe-db-clusters` operation is to
list. The `--db-cluster-identifier` parameter is the
identifier for the particular cluster that you want to display
the details of. For more information on queries, see [How to Filter the Output with the `--query` Option](../../../cli/latest/userguide/cli-usage-output.md#controlling-output-filter "../../../cli/latest/userguide/cli-usage-output.md#controlling-output-filter")
in the _AWS Command Line Interface User Guide_.

The following example lists the instances in an Amazon DocumentDB
cluster.

For Linux, macOS, or Unix:

```
aws docdb describe-db-clusters \
    --filter Name=engine,Values=docdb \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].[DBClusterMembers]'
```

For Windows:

```
aws docdb describe-db-clusters ^
    --filter Name=engine,Values=docdb ^
    --db-cluster-identifier sample-cluster ^
    --query 'DBClusters[*].[DBClusterMembers]'
```

Output from this operation looks something like the following.

```
[
    [
        [
            {
                "DBInstanceIdentifier": "sample-instance-1",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            },
            {
                "DBInstanceIdentifier": "sample-instance-2",
                "IsClusterWriter": false,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            }
        ]
    ]
]

```

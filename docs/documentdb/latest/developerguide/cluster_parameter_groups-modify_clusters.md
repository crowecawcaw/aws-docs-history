# Modifying Amazon DocumentDB clusters to use custom cluster parameter groups

When you create an Amazon DocumentDB cluster, a `default.docdb4.0` parameter group is automatically created for that cluster. You can't modify the `default` cluster parameter group. Instead, you can modify your Amazon DocumentDB cluster to associate a new customized parameter group with it.

This section explains how to modify an existing Amazon DocumentDB cluster to use a custom cluster parameter group using the AWS Management Console and the AWS Command Line Interface (AWS CLI).

Using the AWS Management Console

###### To modify an Amazon DocumentDB cluster to use a new, non-default cluster parameter group

1. Before you begin, make sure you have created an Amazon DocumentDB cluster and a cluster parameter group. See [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md") and [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md") for further instructions.
2. After creating your cluster parameter group, open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb"). In the navigation pane, choose **Clusters** to add your new parameter group to a cluster.
3. Choose the cluster that you want to associate your parameter group with. Choose **Actions**, and then choose **Modify** to modify your cluster.
4. Under **Cluster options**, choose the new parameter group that you want to associate your cluster with.
5. Choose **Continue** to view a summary of your modifications.
6. After verifying your changes, you can apply them immediately or during the next maintenance window under **Scheduling of modifications**.
7. Choose **Modify cluster** to update your cluster with your new parameter group.

Using the AWS CLI
Before you begin, make sure that you have created an Amazon DocumentDB cluster and a cluster
parameter group. You can [create an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md") using the AWS CLI `create-db-cluster`
operation. You can [create a cluster parameter group](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md") using the AWS CLI
`create-db-cluster-parameter-group` operation.

To add your new cluster parameter group to your cluster, use the AWS CLI
`modify-db-cluster` operation with the following parameters.

- **--db-cluster-identifier** — The name of your cluster
  (for example, `sample-cluster`).
- **--db-cluster-parameter-group-name** — The name of the
  parameter group that you want to associate your cluster with (for example,
  `sample-parameter-group`).

###### Example

```
aws docdb modify-db-cluster \
    --db-cluster-identifier `sample-cluster` \
    --db-cluster-parameter-group-name `sample-parameter-group`
```

Output from this operation looks something like the following (JSON format).

```
"DBCluster": {
    "AvailabilityZones": [
            "us-west-2c",
            "us-west-2b",
            "us-west-2a"
    ],
    "BackupRetentionPeriod": 1,
    "DBClusterIdentifier": "`sample-cluster`",
    "DBClusterParameterGroup": "`sample-parameter-group`",
    "DBSubnetGroup": "default",
   ...
}
```

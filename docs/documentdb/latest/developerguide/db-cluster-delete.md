# Deleting an Amazon DocumentDB cluster

You can delete an Amazon DocumentDB cluster using the AWS Management Console or the AWS CLI. To delete a cluster, the cluster must be in the _available_ state and must not have any instances associated with it. If the cluster is stopped, first start the cluster, wait for the cluster to become _available_, and then delete the cluster. For more information, see [Stopping and starting an
Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

## Deletion protection

To protect your cluster from accidental deletion, you can enable
_deletion protection_. Deletion protection is
enabled by default when you create a cluster using the console.
However, deletion protection is disabled by default if you create
a cluster using the AWS CLI.

Amazon DocumentDB enforces deletion protection for a cluster whether you
perform the delete operation using the console or the AWS CLI. If
deletion protection is enabled, you can't delete a cluster. To
delete a cluster that has deletion protection enabled, you must
first modify the cluster and disable deletion protection.

When using the console with deletion protection enabled on a cluster, you can't delete the cluster's last instance because doing so also deletes the cluster. You can delete the last instance of a deletion protected cluster using the AWS CLI. However, the cluster itself still exists, and your data is preserved. You can access the data by creating new instances for the cluster. For more information about enabling and disabling deletion protection, see:

- [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md")
- [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md")

Using the AWS Management Console
To delete a cluster using the AWS Management Console, deletion protection
must be disabled.

###### To determine whether a cluster has deletion protection

enabled:

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. Note that in the Clusters navigation box, the **Cluster
identifier** column shows both clusters and instances. Instances are listed underneath clusters, similar to the screenshot below.

![Image: the Clusters navigation box showing a list of existing cluster links and their corresponding instance links.](images/clusters.png) 4. Choose the cluster's name, and select the
**Configuration** tab. In the
**Cluster details** section, locate
**Deletion protection**. If deletion
protection is enabled, modify the cluster to disable deletion
protection. For information about modifying a cluster, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

After **Deletion protection** is disabled,
you are ready to delete the cluster.

###### To delete a cluster:

1. In the navigation pane, choose **Clusters**.
2. Determine whether the cluster has any instances by
   checking the **Cluster identifier** column for instances
   listed below it. Before
   you can delete a cluster, you must delete all of its
   instances. For more information, see [Deleting an Amazon DocumentDB instance](db-instance-delete.md "db-instance-delete.md").
3. Depending on whether your cluster has any instances, do
   one of the following steps.
   - If the cluster has no instances, select the
     button to the left of the cluster name and choose
     **Actions**. From the dropdown menu,
     choose **Delete**. Complete the
     **Delete <cluster-name>** dialog
     box, and then choose **Delete**.
   - If the cluster has one or more instances, do the
     following:
     1. In the navigation pane, choose
        **Clusters**.
     2. Delete each of the cluster's instances by selecting the
        checkbox to the left of the cluster's name. Select
        **Actions**, and then choose
        **Delete**. Complete the
        **Delete <cluster-name>** dialog
        box, and then choose **Delete**.

     When you delete the last instance, the cluster will also
     be deleted. For more information about deleting instances,
     see [Deleting an Amazon DocumentDB instance](db-instance-delete.md "db-instance-delete.md").

It takes several minutes for the cluster to be deleted. To
monitor the status of the cluster, see [Monitoring an Amazon DocumentDB cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md").

Using the AWS CLI
You cannot delete a cluster that has any instances associated
with it. To determine which instances are associated with your
cluster, run the `describe-db-clusters` command and
delete all of the cluster's instances. Then, if needed, disable
deletion protection on your cluster, and finally, delete the
cluster.

1. **First, delete all of the cluster's
   instances.**

To determine which instances you need to delete, run the
following command.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].[DBClusterIdentifier,DBClusterMembers[*].DBInstanceIdentifier]'
```

Output from this operation looks something like the following (JSON format).

```
[
    [
        "sample-cluster",
        [
            "sample-instance-1",
            "sample-instance-2"
        ]
    ]
]

```

If the cluster you want to delete has any instances,
delete them as shown below.

```
aws docdb delete-db-instance \
    --db-instance-identifier sample-instance
```

2. **Second, disable deletion protection.**

Using the AWS CLI to delete all of a cluster's instances
does not delete the cluster. You must also delete the
cluster, but you can do this only if deletion protection is
disabled.

To determine whether the cluster has deletion protection
enabled, run the following command.

###### Tip

To see the deletion protection status of all your
Amazon DocumentDB clusters, omit the `--db-cluster-identifier`
parameter.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].[DBClusterIdentifier,DeletionProtection]'
```

Output from this operation looks something like the following.

```
[
    [
        "sample-cluster",
        "true"
    ]
]

```

If the cluster has deletion protection enabled, modify
the cluster and disable deletion protection. To disable
deletion protection on the cluster, run the following command.

```
aws docdb modify-db-cluster \
    --db-cluster-identifier sample-cluster \
    --no-deletion-protection \
    --apply-immediately

```

3. **Finally, delete the cluster.**

After deletion protection is disabled, you are ready to
delete the cluster. To delete a cluster, use the
`delete-db-cluster` operation with the following
parameters.

    * `--db-cluster-identifier`—Required.
     The identifier of the cluster that you want to delete.
    * `--final-db-snapshot-identifier`—Optional.
     If you want a final snapshot, you must include this
     parameter with a name for the final snapshot. You must
     include either `--final-db-snapshot-identifier`
     or `--skip-final-snapshot`.


    Naming constraints:




    	+ Length is [1—63] letters, numbers, or hyphens.
    	+ First character must be a letter.
    	+ Cannot end with a hyphen or contain two
    	 consecutive hyphens.
    	+ Must be unique for all clusters across Amazon RDS, Amazon Neptune, and Amazon DocumentDB per AWS account, per Region.
    * `--skip-final-snapshot`—Optional.
     Use this parameter only if you don't want to take a
     final snapshot before deleting your cluster. The
     default setting is to take a final snapshot. You must
     include either `--final-db-snapshot-identifier`
     or `--skip-final-snapshot`.

The following AWS CLI code deletes the cluster `sample-cluster`
with a final snapshot. The operation fails if there are any
instances associated with the cluster or if deletion protection
is enabled.

For Linux, macOS, or Unix:

```
aws docdb delete-db-cluster \
    --db-cluster-identifier sample-cluster \
    --final-db-snapshot-identifier sample-cluster-final-snapshot
```

For Windows:

```
aws docdb delete-db-cluster ^
    --db-cluster-identifier sample-cluster ^
    --final-db-snapshot-identifier sample-cluster-final-snapshot
```

The following AWS CLI code deletes the cluster
`sample-cluster` without taking a final snapshot.

For Linux, macOS, or Unix:

```
aws docdb delete-db-cluster \
    --db-cluster-identifier sample-cluster \
    --skip-final-snapshot
```

For Windows:

```
aws docdb delete-db-cluster ^
    --db-cluster-identifier sample-cluster ^
    --skip-final-snapshot
```

The output of the `delete-db-cluster` operation
is the cluster you are deleting.

It takes several minutes for the cluster to be deleted.
To monitor the status of the cluster, see [Monitoring a cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md").

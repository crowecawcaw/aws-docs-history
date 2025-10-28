# Deleting Aurora DB clusters and DB instances

You can delete an Aurora DB cluster when you no longer need it. Deleting the cluster removes
the cluster volume containing all your data. Before deleting the cluster, you can save a
snapshot of your data. You can restore the snapshot later to create a new cluster containing the
same data.

You can also delete DB instances from a cluster while preserving the cluster itself and the
data that it contains. Deleting DB instances can help you reduce your charges if the cluster
isn't busy, or you don't need the computation capacity of multiple DB
instances.

###### Topics

- [Deleting an Aurora DB cluster](#USER_DeleteCluster.DeleteCluster "#USER_DeleteCluster.DeleteCluster")
- [Deletion protection for Aurora clusters](#USER_DeletionProtection "#USER_DeletionProtection")
- [Deleting a stopped Aurora cluster](#USER_Deletion_Stopped_Cluster "#USER_Deletion_Stopped_Cluster")
- [Deleting Aurora MySQL clusters that are read replicas](#USER_DeleteInstance.AuroraReplica "#USER_DeleteInstance.AuroraReplica")
- [The final snapshot when deleting a cluster](#USER_Deletion_Final_Snapshot "#USER_Deletion_Final_Snapshot")
- [Deleting a DB instance from an Aurora DB cluster](#USER_DeleteInstance "#USER_DeleteInstance")

## Deleting an Aurora DB cluster

Aurora doesn't provide a single-step method to delete a DB cluster. This design choice is intended to prevent you from
accidentally losing data or taking your application offline. Aurora applications are typically mission-critical and require high
availability. Thus, Aurora makes it easy to scale the capacity of the cluster up and down by adding and removing DB instances.
Removing the DB cluster itself requires you to make a separate deletion.

Use the following general procedure to remove all the DB instances from a cluster and then delete the cluster itself.

1. Delete any reader instances in the cluster. Use the procedure in [Deleting a DB instance from an Aurora DB cluster](#USER_DeleteInstance "#USER_DeleteInstance").

If the cluster has any reader instances, deleting one of the instances only reduces the computation capacity of the
cluster. Deleting the reader instances first ensures that the cluster remains available throughout the procedure and
doesn't perform unnecessary failover operations. 2. Delete the writer instance from the cluster. Again, use the procedure in [Deleting a DB instance from an Aurora DB cluster](#USER_DeleteInstance "#USER_DeleteInstance").

When you delete the DB instances, the cluster and its associated cluster volume remain even after you delete all the
DB instances. 3. Delete the DB cluster.

    * **AWS Management Console** – Choose the cluster, then choose **Delete** from the
     **Actions** menu. You can choose the following options to preserve the data from the
     cluster in case you need it later:




    	+ Create a final snapshot of the cluster volume. The default setting is to create a final
    	 snapshot.
    	+ Retain automated backups. The default setting is not to retain automated backups.


    	###### Note

    	Automated backups for Aurora Serverless v1 DB clusters aren't retained.
    Aurora also requires you to confirm that you intend to delete the cluster.
    * **CLI and API** – Call the `delete-db-cluster` CLI command or
     `DeleteDBCluster` API operation. You can choose the following options to preserve the data from
     the cluster in case you need it later:




    	+ Create a final snapshot of the cluster volume.
    	+ Retain automated backups.


    	###### Note

    	Automated backups for Aurora Serverless v1 DB clusters aren't retained.

###### Topics

- [Deleting an empty Aurora cluster](#USER_DeleteInstance.Empty "#USER_DeleteInstance.Empty")
- [Deleting an Aurora cluster with a single DB instance](#USER_DeleteInstance.SingleInstance "#USER_DeleteInstance.SingleInstance")
- [Deleting an Aurora cluster with multiple DB instances](#USER_DeleteInstance.MultipleInstances "#USER_DeleteInstance.MultipleInstances")

### Deleting an empty Aurora cluster

You can delete an empty DB cluster using the AWS Management Console, AWS CLI, or Amazon RDS API.

###### Tip

You can keep a cluster with no DB instances to preserve your data without incurring
CPU charges for the cluster. You can quickly start using the cluster again by creating one
or more new DB instances for the cluster. However, you can only add new DB instances by
using the AWS CLI or the RDS API. You can't add new DB instances by using the Amazon RDS console.
You can perform Aurora-specific administrative operations on the cluster while it doesn't
have any associated DB instances. You just can't access the data or perform any
operations that require connecting to a DB instance.

###### To delete a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB cluster that you
   want to delete.
3. For **Actions**, choose **Delete**.
4. To create a final DB snapshot for the DB cluster, choose **Create final snapshot?**. This
   is the default setting.
5. If you chose to create a final snapshot, enter the **Final snapshot name**.
6. To retain automated backups, choose **Retain automated backups**. This is not the default
   setting.
7. Enter `delete me` in the box.
8. Choose **Delete**.
   To delete an empty Aurora DB cluster by using the AWS CLI, call the [delete-db-cluster](../../../cli/latest/reference/rds/delete-db-cluster.md "../../../cli/latest/reference/rds/delete-db-cluster.md") command.

Suppose that the empty cluster `deleteme-zero-instances` was only used for development and testing and
doesn't contain any important data. In that case, you don't need to preserve a snapshot of the cluster
volume when you delete the cluster. The following example demonstrates that a cluster doesn't contain any DB
instances, and then deletes the empty cluster without creating a final snapshot or retaining automated
backups.

```
`$` aws rds describe-db-clusters --db-cluster-identifier `deleteme-zero-instances` --output text \
  --query '*[].["Cluster:",DBClusterIdentifier,DBClusterMembers[*].["Instance:",DBInstanceIdentifier,IsClusterWriter]]
`Cluster: `deleteme-zero-instances``

`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-zero-instances` \
  --skip-final-snapshot \
  --delete-automated-backups
`{
 "DBClusterIdentifier": "`deleteme-zero-instances`",
 "Status": "available",
 "Engine": "aurora-mysql"
}`

```

To delete an empty Aurora DB cluster by using the Amazon RDS API, call the [DeleteDBCluster](../APIReference/API_DeleteDBCluster.md "../APIReference/API_DeleteDBCluster.md") operation.

### Deleting an Aurora cluster with a single DB instance

You can delete the last DB instance, even if the DB cluster has deletion protection enabled. In this case, the DB cluster itself
still exists and your data is preserved. You can access the data again by attaching a new DB instance to the cluster.

The following example shows how the `delete-db-cluster` command doesn't work when the cluster still has any
associated DB instances. This cluster has a single writer DB instance. When we examine the DB instances in the cluster, we
check the `IsClusterWriter` attribute of each one. The cluster could have zero or one writer DB instance. A value
of `true` signifies a writer DB instance. A value of `false` signifies a reader DB instance. The
cluster could have zero, one, or many reader DB instances. In this case, we delete the writer DB instance using the
`delete-db-instance` command. As soon as the DB instance goes into `deleting` state, we can delete
the cluster also. For this example also, suppose that the cluster doesn't contain any data worth preserving. Therefore,
we don't create a snapshot of the cluster volume or retain automated backups.

```
`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-writer-only` --skip-final-snapshot
`An error occurred (InvalidDBClusterStateFault) when calling the DeleteDBCluster operation:
 Cluster cannot be deleted, it still contains DB instances in non-deleting state.`

$ aws rds describe-db-clusters --db-cluster-identifier `deleteme-writer-only` \
  --query '*[].[DBClusterIdentifier,Status,DBClusterMembers[*].[DBInstanceIdentifier,IsClusterWriter]]'
`[
 [
 "`deleteme-writer-only`",
 "available",
 [
 [
 "instance-2130",
 true
 ]
 ]
 ]
]`

`$` aws rds delete-db-instance --db-instance-identifier `instance-2130`
`{
 "DBInstanceIdentifier": "instance-2130",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-writer-only` \
  --skip-final-snapshot \
  --delete-automated-backups
`{
 "DBClusterIdentifier": "`deleteme-writer-only`",
 "Status": "available",
 "Engine": "aurora-mysql"
}`

```

### Deleting an Aurora cluster with multiple DB instances

If your cluster contains multiple DB instances, typically there is a single writer instance and one or more reader instances.
The reader instances help with high availability, by being on standby to take over if the writer instance encounters a
problem. You can also use reader instances to scale the cluster up to handle a read-intensive workload without adding
overhead to the writer instance.

To delete a cluster with multiple reader DB instances, you delete the reader instances first and then the writer instance.
Deleting the writer instance leaves the cluster and its data in place. You delete the cluster through a separate
action.

- For the procedure to delete an Aurora DB instance, see [Deleting a DB instance from an Aurora DB cluster](#USER_DeleteInstance "#USER_DeleteInstance").
- For the procedure to delete the writer DB instance in an Aurora cluster, see [Deleting an Aurora cluster with a single DB instance](#USER_DeleteInstance.SingleInstance "#USER_DeleteInstance.SingleInstance").
- For the procedure to delete an empty Aurora cluster, see [Deleting an empty Aurora cluster](#USER_DeleteInstance.Empty "#USER_DeleteInstance.Empty").

This CLI example shows how to delete a cluster containing both a writer DB instance and a single reader DB instance. The
`describe-db-clusters` output shows that `instance-7384` is the writer instance and
`instance-1039` is the reader instance. The example deletes the reader instance first, because deleting the
writer instance while a reader instance still existed would cause a failover operation. It doesn't make sense to
promote the reader instance to a writer if you plan to delete that instance also. Again, suppose that these
`db.t2.small` instances are only used for development and testing, and so the delete operation skips the
final snapshot and doesn't retain automated backups..

```
`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-writer-and-reader` --skip-final-snapshot

`An error occurred (InvalidDBClusterStateFault) when calling the DeleteDBCluster operation:
 Cluster cannot be deleted, it still contains DB instances in non-deleting state.`

`$` aws rds describe-db-clusters --db-cluster-identifier `deleteme-writer-and-reader` --output text \
  --query '*[].["Cluster:",DBClusterIdentifier,DBClusterMembers[*].["Instance:",DBInstanceIdentifier,IsClusterWriter]]
`Cluster: `deleteme-writer-and-reader`
Instance: `instance-1039` False
Instance: `instance-7384` True`

`$` aws rds delete-db-instance --db-instance-identifier `instance-1039`
`{
 "DBInstanceIdentifier": "instance-1039",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-instance --db-instance-identifier `instance-7384`
`{
 "DBInstanceIdentifier": "instance-7384",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-writer-and-reader` \
  --skip-final-snapshot \
  --delete-automated-backups
`{
 "DBClusterIdentifier": "`deleteme-writer-and-reader`",
 "Status": "available",
 "Engine": "aurora-mysql"
}`

```

The following example shows how to delete a DB cluster containing a writer DB instance and multiple reader DB instances. It uses
concise output from the `describe-db-clusters` command to get a report of the writer and reader instances. Again,
we delete all reader DB instances before deleting the writer DB instance. It doesn't matter what order we delete the
reader DB instances in.

Suppose that this cluster with several DB instances does contain data worth preserving. Thus, the
`delete-db-cluster` command in this example includes the `--no-skip-final-snapshot` and
`--final-db-snapshot-identifier` parameters to specify the details of the snapshot to create. It also
includes the `--no-delete-automated-backups` parameter to retain automated backups.

```
`$` aws rds describe-db-clusters --db-cluster-identifier `deleteme-multiple-readers` --output text \
  --query '*[].["Cluster:",DBClusterIdentifier,DBClusterMembers[*].["Instance:",DBInstanceIdentifier,IsClusterWriter]]
`Cluster: `deleteme-multiple-readers`
Instance: `instance-1010` False
Instance: `instance-5410` False
Instance: `instance-9948` False
Instance: `instance-8451` True`

`$` aws rds delete-db-instance --db-instance-identifier `instance-1010`
`{
 "DBInstanceIdentifier": "instance-1010",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-instance --db-instance-identifier `instance-5410`
`{
 "DBInstanceIdentifier": "instance-5410",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-instance --db-instance-identifier `instance-9948`
`{
 "DBInstanceIdentifier": "instance-9948",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-instance --db-instance-identifier `instance-8451`
`{
 "DBInstanceIdentifier": "instance-8451",
 "DBInstanceStatus": "deleting",
 "Engine": "aurora-mysql"
}`

`$` aws rds delete-db-cluster --db-cluster-identifier `deleteme-multiple-readers` \
  --no-delete-automated-backups \
  --no-skip-final-snapshot \
  --final-db-snapshot-identifier `deleteme-multiple-readers-final-snapshot`
`{
 "DBClusterIdentifier": "`deleteme-multiple-readers`",
 "Status": "available",
 "Engine": "aurora-mysql"
}`

```

The following example shows how to confirm that Aurora created the requested snapshot. You can request details for the specific
snapshot by specifying its identifier `deleteme-multiple-readers-final-snapshot`. You can also get a report of
all snapshots for the cluster that was deleted by specifying the cluster identifier `deleteme-multiple-readers`.
Both of those commands return information about the same snapshot.

```
`$` aws rds describe-db-cluster-snapshots \
  --db-cluster-snapshot-identifier `deleteme-multiple-readers-final-snapshot`
`{
 "DBClusterSnapshots": [
 {
 "AvailabilityZones": [],
 "DBClusterSnapshotIdentifier": "`deleteme-multiple-readers-final-snapshot`",
 "DBClusterIdentifier": "`deleteme-multiple-readers`",
 "SnapshotCreateTime": "11T01:40:07.354000+00:00",
 "Engine": "aurora-mysql",
...`

`$` aws rds describe-db-cluster-snapshots --db-cluster-identifier `deleteme-multiple-readers`
`{
 "DBClusterSnapshots": [
 {
 "AvailabilityZones": [],
 "DBClusterSnapshotIdentifier": "`deleteme-multiple-readers-final-snapshot`",
 "DBClusterIdentifier": "`deleteme-multiple-readers`",
 "SnapshotCreateTime": "11T01:40:07.354000+00:00",
 "Engine": "aurora-mysql",
...`

```

## Deletion protection for Aurora clusters

You can't delete clusters that have deletion protection enabled. You can delete DB instances within the cluster, but not the
cluster itself. That way, the cluster volume containing all your data is safe from accidental deletion. Aurora enforces deletion
protection for a DB cluster whether you try to delete the cluster using the console, the AWS CLI, or the RDS API.

Deletion protection is enabled by default when you create a production DB cluster using the AWS Management Console. However, deletion
protection is disabled by default if you create a cluster using the AWS CLI or API. Enabling or disabling deletion protection
doesn't cause an outage. To be able to delete the cluster, modify the cluster and disable deletion protection. For more
information about turning deletion protection on and off, see [Modifying the DB cluster by using the console, CLI, and API](Aurora.md#Aurora.Modifying.Cluster "Aurora.md#Aurora.Modifying.Cluster").

###### Tip

Even if all the DB instances are deleted, you can access the data by creating a new DB instance in the cluster.

## Deleting a stopped Aurora cluster

You can't delete a cluster if it's in the `stopped` state. In this case, start the cluster before deleting
it. For more information, see [Starting an Aurora DB cluster](aurora-cluster-stop-start.md#aurora-cluster-start "aurora-cluster-stop-start.md#aurora-cluster-start").

## Deleting Aurora MySQL clusters that are read replicas

For Aurora MySQL, you can't delete a DB instance in a DB cluster if both of the following conditions are true:

- The DB cluster is a read replica of another Aurora DB cluster.
- The DB instance is the only instance in the DB cluster.

To delete a DB instance in this case, first promote the DB cluster so that it's no longer a read replica. After the promotion
completes, you can delete the final DB instance in the DB cluster. For more information, see [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

## The final snapshot when deleting a cluster

Throughout this section, the examples show how you can choose whether to take a final snapshot when you delete an Aurora cluster.
If you choose to take a final snapshot but the name you specify matches an existing snapshot, the operation stops with an error.
In this case, examine the snapshot details to confirm if it represents your current detail or if it is an older snapshot. If the
existing snapshot doesn't have the latest data that you want to preserve, rename the snapshot and try again, or specify a
different name for the **final snapshot** parameter.

## Deleting a DB instance from an Aurora DB cluster

You can delete a DB instance from an Aurora DB cluster as part of the process of deleting the entire cluster. If your cluster
contains a certain number of DB instances, then deleting the cluster requires deleting each of those DB instances. You can also
delete one or more reader instances from a cluster while leaving the cluster running. You might do so to reduce compute capacity
and associated charges if your cluster isn't busy.

To delete a DB instance, you specify the name of the instance.

You can delete a DB instance using the AWS Management Console, the AWS CLI, or the RDS API.

###### Note

When an Aurora Replica is deleted, its instance endpoint is removed immediately, and the Aurora Replica is removed from the
reader endpoint. If there are statements running on the Aurora Replica that is being deleted, there is a three-minute grace
period. Existing statements can finish during the grace period. When the grace period ends, the Aurora Replica is shut down
and deleted.

For Aurora DB clusters, deleting a DB instance doesn't necessarily delete the entire cluster. You can delete a DB instance in
an Aurora cluster to reduce compute capacity and associated charges when the cluster isn't busy. For information about the
special circumstances for Aurora clusters that have one DB instance or zero DB instances, see [Deleting an Aurora cluster with a single DB instance](#USER_DeleteInstance.SingleInstance "#USER_DeleteInstance.SingleInstance") and [Deleting an empty Aurora cluster](#USER_DeleteInstance.Empty "#USER_DeleteInstance.Empty").

###### Note

You can't delete a DB cluster when deletion protection is enabled for it. For more information, see [Deletion protection for Aurora clusters](#USER_DeletionProtection "#USER_DeletionProtection").

You can disable deletion protection by modifying the DB cluster. For more information, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

###### To delete a DB instance in a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB instance that you
   want to delete.
3. For **Actions**, choose **Delete**.
4. Enter `delete me` in the box.
5. Choose **Delete**.
   To delete a DB instance by using the AWS CLI, call the
   [delete-db-instance](../../../cli/latest/reference/rds/delete-db-instance.md "../../../cli/latest/reference/rds/delete-db-instance.md") command and specify the
   `--db-instance-identifier` value.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance \
    --db-instance-identifier `mydbinstance`
```

For Windows:

```
aws rds delete-db-instance ^
    --db-instance-identifier `mydbinstance`
```

To delete a DB instance by using the Amazon RDS API, call the
[DeleteDBInstance](../APIReference/API_DeleteDBInstance.md "../APIReference/API_DeleteDBInstance.md") operation and
specify the `DBInstanceIdentifier` parameter.

###### Note

When the status for a DB instance is `deleting`, its CA certificate value doesn't appear
in the RDS console or in output for AWS CLI commands or RDS API operations. For more information about CA
certificates, see [Using SSL/TLS to encrypt a connection to a DB
cluster](UsingWithRDS.md "UsingWithRDS.md").



# Creating a DB Cluster Snapshot in Neptune

Neptune creates a storage volume snapshot of your DB cluster, backing up the entire DB cluster and not just individual databases. When you create a DB cluster snapshot, you need to identify which DB cluster you are going to back up. Then give your DB cluster snapshot a name so that you can restore from it later. The amount of time it takes to create a DB cluster snapshot varies with the size of your databases. The snapshot includes the entire storage volume. So the size of files (such as temporary files) also affects the amount of time it takes to create the snapshot.

You can create a DB cluster snapshot using the AWS Management Console, the AWS CLI, or the Neptune API.

## Using the Console to Create a DB Cluster Snapshot
<a name="backup-restore-create-snapshot-console"></a>

**To create a DB cluster snapshot**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Databases**.

1. In the list of DB instances, choose the primary instance for the DB cluster.

1. Choose **Instance actions**, and then choose **Take snapshot**.

   The **Take DB Snapshot** window appears.

1. Enter the name of the DB cluster snapshot in the **Snapshot name** box. 

1. Choose **Take Snapshot**.

1. To confirm that you created the snapshot, select **Snapshots** on the navigation pane. Your new snapshot appears in the list with a status of **Creating**. When the snapshot is ready, the status changes to **Available**, which indicates that you can restore from it.

## Learn more
<a name="backup-restore-create-snapshot-learn-more"></a>

For more information about working with DB cluster snapshots, see the following topics:
+ [Restoring from a DB Cluster Snapshot](backup-restore-restore-snapshot.md)
+ [Backing up and restoring an Amazon Neptune DB cluster](backup-restore.md)
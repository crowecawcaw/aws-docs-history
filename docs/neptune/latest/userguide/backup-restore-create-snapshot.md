# Creating a DB Cluster Snapshot in Neptune

Neptune creates a storage volume snapshot of your DB cluster, backing up the entire DB
cluster and not just individual databases. When you create a DB cluster snapshot, you need to
identify which DB cluster you are going to back up. Then give your DB cluster snapshot a name so
that you can restore from it later. The amount of time it takes to create a DB cluster snapshot
varies with the size of your databases. The snapshot includes the entire storage volume. So the
size of files (such as temporary files) also affects the amount of time it takes to create the
snapshot.

You can create a DB cluster snapshot using the AWS Management Console, the AWS CLI, or the Neptune
API.

## Using the Console to Create a DB

Cluster Snapshot

###### To create a DB cluster snapshot

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. In the list of DB instances, choose the primary instance for the DB cluster.
4. Choose **Instance actions**, and then choose **Take
   snapshot**.

The **Take DB Snapshot** window appears. 5. Enter the name of the DB cluster snapshot in the **Snapshot name** box. 6. Choose **Take Snapshot**.

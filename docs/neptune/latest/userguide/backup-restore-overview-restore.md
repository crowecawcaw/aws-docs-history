# Restoring data from a Neptune backup

You can recover your data by creating a new Neptune DB cluster from the backup data
that Neptune retains, or from a DB cluster snapshot that you have saved. You can
quickly restore a new copy of a DB cluster created from backup data to any point in
time during your backup retention period. The continuous and incremental nature of
Neptune backups during the backup retention period means you don't need to take
frequent snapshots of your data to improve restore times.

To determine the latest or earliest restorable time for a DB instance, look for
the `Latest Restorable Time` or `Earliest Restorable Time`
values on the Neptune console. The latest restorable time for a DB cluster is the
most recent point at which you can restore your DB cluster, typically within
5 minutes of the current time. The earliest restorable time specifies how far back
within the backup retention period that you can restore your cluster volume.

You can determine when the restore of a DB cluster is complete by checking the
`Latest Restorable Time` and `Earliest Restorable Time`
values. The `Latest Restorable Time` and `Earliest Restorable
 Time` values return NULL until the restore operation is complete. You
can't request a backup or restore operation if `Latest Restorable
 Time` or `Earliest Restorable Time` returns NULL.

###### To restore a DB instance to a specified time using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Instances**. Choose the
   primary instance for the DB cluster that you want to restore.
3. Choose **Instance actions**, and then choose
   **Restore to point in time**.

In the **Launch DB Instance** window, choose
**Custom** under **Restore time**. 4. Specify the date and time that you want to restore to under
**Custom**. 5. Type a name for the new, restored DB instance for **DB instance
identifier** under **Settings**. 6. Choose **Launch DB Instance** to launch the restored DB
instance.

A new DB instance is created with the name you specified, and a new DB cluster
is created. The DB cluster name is the new DB instance name followed by `–cluster`.
For example, if the new DB instance name is `myrestoreddb`, the new DB cluster name is
`myrestoreddb-cluster`.

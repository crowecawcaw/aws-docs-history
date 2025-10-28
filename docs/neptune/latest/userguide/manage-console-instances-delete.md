# Deleting a DB Instance in Amazon Neptune

You can delete an Amazon Neptune DB instance in any state and at any time, as long
the instance has been started.

###### Warning

If you delete the last remaining instance in a cluster using the **web console**, it will
also delete the underlying cluster storage volume.

## Taking a Final Snapshot of

Your DB Instance Before Deleting It

To delete a DB instance, you must specify the name of the instance and whether
you want to have a final DB snapshot taken of the instance. If the DB instance that
you're deleting has a status of **Creating**, you can't have a final
DB snapshot taken. If the DB instance is in a failure state with a status of
**failed**, **incompatible-restore**, or
**incompatible-network**, you can only delete the instance when the
`SkipFinalSnapshot` parameter is set to `true`.

If you delete all Neptune DB instances in a DB cluster using the AWS Management Console, the entire
DB cluster is deleted automatically. If you are using the AWS CLI or SDK, you must
delete the DB cluster manually after you delete the last instance.

###### Important

If you delete an entire DB cluster, all its automated backups are deleted
at the same time, and cannot be recovered. This means that unless you choose to create
a final DB snapshot manually, you can't restore the DB instance to its final state at
a later time. Manual snapshots of an instance are not deleted when the cluster is deleted.

If the DB instance that you want to delete has a read replica, you should either
promote the read replica or delete it.

In the following examples, you delete a DB instance both with and without a final DB
snapshot.

## Deleting a DB Instance with No Final Snapshot

If you want to quickly delete a DB instance, you can skip creating a final DB snapshot.
When you delete a DB instance, all automated backups are deleted and cannot be recovered.
Manual snapshots are not deleted.

###### To delete a DB instance with no final DB snapshot using the Neptune console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. In the **Instances** list, choose the radio button next to the DB
   instance that you want to delete.
4. Choose **Instance actions**, and then choose
   **Delete**.
5. Choose **No** in the **Create final snapshot?**
   box.
6. Choose **Delete**.

## Deleting a DB Instance with a Final Snapshot

If you want to be able to restore a deleted DB instance at a later time, you can create a
final DB snapshot. All automated backups are also deleted and cannot be recovered. Manual
snapshots are not deleted.

###### To delete a DB instance with a final DB snapshot using the Neptune console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. In the **Instances** list, choose the radio button next to the DB
   instance that you want to delete.
4. Choose **Instance actions**, and then choose
   **Delete**.
5. Choose **Yes** in the **Create final snapshot?**
   box.
6. In the **Final snapshot name** box, enter the name of your final DB
   snapshot.
7. Choose **Delete**.

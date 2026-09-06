

# Deleting a snapshot
<a name="snapshots-deleting"></a>

An automatic snapshot is automatically deleted when its retention limit expires. If you delete a cluster, all of its automatic snapshots are also deleted.

MemoryDB provides a deletion API operation that lets you delete a snapshot at any time, regardless of whether the snapshot was created automatically or manually. Because manual snapshots don't have a retention limit, manual deletion is the only way to remove them.

You can delete a snapshot using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Deleting a snapshot (Console)
<a name="snapshots-deleting-CON"></a>

The following procedure deletes a snapshot using the MemoryDB console.

**To delete a snapshot**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. In the left navigation pane, choose **Snapshots**.

   The Snapshots screen appears with a list of your snapshots.

1. Choose the radio button to the left of the name of the snapshot you want to delete.

1. Choose **Actions** and then choose **Delete**.

1. If you want to delete this snapshot, enter `delete` in the text box and then choose **Delete**. To cancel the delete, choose **Cancel**. The status changes to *deleting*.

## Deleting a snapshot (AWS CLI)
<a name="snapshots-deleting-CLI"></a>

Use the delete-snapshot AWS CLI operation with the following parameter to delete a snapshot.
+ `--snapshot-name` – Name of the snapshot to be deleted.

The following code deletes the snapshot `myBackup`.

```
aws memorydb delete-snapshot --snapshot-name {{myBackup}}
```

For more information, see [delete-snapshot](https://docs.aws.amazon.com/cli/latest/reference/memorydb/delete-snapshot.html) in the *AWS CLI Command Reference*.

## Deleting a snapshot (MemoryDB API)
<a name="snapshots-deleting-API"></a>

Use the `DeleteSnapshot` API operation with the following parameter to delete a snapshot.
+ `SnapshotName` – Name of the snapshot to be deleted.

The following code deletes the snapshot `myBackup`.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DeleteSnapshot
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &SnapshotName=myBackup
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

For more information, see [DeleteSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSnapshot.html).
# Delete an Amazon EBS snapshot

After you no longer need an Amazon EBS snapshot of a volume, you can delete it. Deleting a snapshot
has no effect on the volume. Deleting a volume has no effect on the snapshots made from it.

###### Topics

- [Considerations for deleting snapshots](#ebs-delete-snapshot-considerations "#ebs-delete-snapshot-considerations")
- [How deleting incremental snapshots works](#ebs-deleting-snapshot-incremental "#ebs-deleting-snapshot-incremental")
- [Delete a snapshot](#ebs-delete-snapshot "#ebs-delete-snapshot")
- [Delete multi-volume snapshots](#ebs-delete-snapshot-multi-volume "#ebs-delete-snapshot-multi-volume")

## Considerations for deleting snapshots

The following considerations apply to deleting snapshots:

- You can't delete a snapshot of the root device of an EBS volume used by a registered
  AMI. This consideration applies even if the registered AMI is deprecated or disabled.
  You must first deregister the AMI before you can delete the snapshot. For more
  information, see [Deregister your AMI](../../../AWSEC2/latest/UserGuide/deregister-ami.md "../../../AWSEC2/latest/UserGuide/deregister-ami.md").
- You can't delete a snapshot that is managed by the AWS Backup service using Amazon EC2. Instead,
  use AWS Backup to delete the corresponding recovery points in the backup vault. For more information,
  see [Deleting
  backups](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md") in the _AWS Backup Developer Guide_.
- You can create, retain, and delete snapshots manually, or you can use Amazon Data Lifecycle Manager to
  manage your snapshots for you. For more information, see [Amazon Data Lifecycle Manager](snapshot-lifecycle.md "snapshot-lifecycle.md").
- Although you can delete a snapshot that is still in progress, the snapshot must complete
  before the deletion takes effect. This might take a long time. If you are also at your
  concurrent snapshot limit, and you attempt to take an
  additional snapshot, you might get a `ConcurrentSnapshotLimitExceeded`
  error. For more information, see the [Service Quotas](../../../general/latest/gr/ebs-service.md#limits_ebs "../../../general/latest/gr/ebs-service.md#limits_ebs") for Amazon EBS in the _Amazon Web Services General Reference_.
- If you delete a snapshot that matches a Recycle Bin retention rule, the snapshot
  is retained in the Recycle Bin instead of being immediately deleted. For more information,
  see [Recycle Bin](recycle-bin.md "recycle-bin.md").
- You can't delete snapshots associated with disabled EBS-backed AMIs. For more information,
  see [Disable an AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md "../../../AWSEC2/latest/UserGuide/disable-an-ami.md").
- You can't delete snapshots that are shared with you.
- If you delete a shared snapshot that you own, all accounts with which the snapshot is
  shared lose access to it.

## How deleting incremental snapshots works

If you make periodic snapshots of a volume, the snapshots are _incremental_. This means that only the blocks on the device that have changed
after your most recent snapshot are saved in the new snapshot. Even though snapshots are
saved incrementally, the snapshot deletion process is designed so that you need to retain
only the most recent snapshot in order to create volumes.

If data was present on a volume held
in an earlier snapshot or series of snapshots, and that data is subsequently deleted from the volume
later on, the data is still considered to be unique data of the earlier snapshots. Unique data is
only deleted from the sequence of snapshots if all snapshots that reference the unique data
are deleted.

When you delete a snapshot, only the data that is referenced exclusively by that
snapshot is removed. Unique data is only deleted if all of the snapshots that reference it
are deleted. Deleting previous snapshots of a volume does not affect your ability to create
volumes from later snapshots of that volume.

Deleting a snapshot might not reduce your organization's data storage costs. Other
snapshots might reference that snapshot's data, and referenced data is always preserved. If
you delete a snapshot containing data being used by a later snapshot, costs associated with
the referenced data are allocated to the later snapshot. For more information about how
snapshots store data, see [How Amazon EBS snapshots work](how_snapshots_work.md "how_snapshots_work.md") and the following example.

In the following diagram, Volume 1 is shown at three points in time. A snapshot has
captured each of the first two states, and in the third, a snapshot has been deleted.

- In **state 1**, the volume has 10 GiB of data. Because
  Snap A is the first snapshot taken of the volume, the entire 10 GiB of data must be copied.
  In this state, you are charged for storing 10 GiB of snapshot data.
- In **state 2**, the volume still contains 10 GiB of data,
  but 4 GiB have changed. Snap B stores only the 4 GiB that changed after Snap A was taken,
  and it references the 6 GiB of unchanged data that is already stored in Snap A. In this
  state, you are charged for storing 14 GiB of snapshot data (10 Gib from Snap A + 4 GiB from
  Snap B).
- In **state 3**, the volume is unchanged but Snap A is
  deleted. Since the 6 GiB of unchanged data in Snap A is still referenced by Snap B, that
  data is retained and it is associated with Snap B. The 4 GiB of unique data in Snap A is
  deleted since it is no longer referenced by other snapshots. In this state, you are charged
  for storing 10 GiB of snapshot data (6 GiB of data retained from Snap A + 4 GiB of data in
  Snap B).

Deleting a snapshot with some of its data referenced by
another snapshot

![Snap A contains 6 GiB of referenced data. When Snap A is deleted, that data is merged into Snap B.](images/snapshot_1b.png)

## Delete a snapshot

Console

###### To delete a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot.
4. Choose **Actions**, **Delete snapshot**.
5. When prompted for confirmation, enter `delete` and then
   choose **Delete**.

AWS CLI

###### To delete a snapshot

Use the [delete-snapshot](../../../cli/latest/reference/ec2/delete-snapshot.md "../../../cli/latest/reference/ec2/delete-snapshot.md") command.

```
aws ec2 delete-snapshot --snapshot-id `snap-0abcdef1234567890`
```

PowerShell

###### To delete a snapshot

Use the [Remove-EC2Snapshot](../../../powershell/latest/reference/items/Remove-EC2Snapshot.md "../../../powershell/latest/reference/items/Remove-EC2Snapshot.md") cmdlet.

```
Remove-EC2Snapshot -SnapshotId `snap-0abcdef1234567890`
```

###### Troubleshooting tip

If you get a `Failed to delete snapshot` error indicating that the snapshot
is currently in use by an AMI, you must [deregister the associated AMI](../../../AWSEC2/latest/UserGuide/deregister-ami.md "../../../AWSEC2/latest/UserGuide/deregister-ami.md") before you can delete the snapshot. You can't delete snapshots that
are associated with an AMI.

If you're using the console and the associated AMI is disabled, you must select the
**Disabled images** filter on the **AMIs** screen to
view disabled AMIs.

## Delete multi-volume snapshots

To delete multi-volume snapshots, retrieve all of the snapshots for your multi-volume
snapshot set using the tag you applied to the set when you created the snapshots. Then,
delete the snapshots individually.

You will not be prevented from deleting individual snapshots in the multi-volume snapshot
set. If you delete a snapshot while it is in the `pending state`, only that snapshot
is deleted. The other snapshots in the multi-volume snapshot set still complete successfully.

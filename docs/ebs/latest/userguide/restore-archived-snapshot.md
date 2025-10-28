# Restore an archived Amazon EBS snapshot

Before you can use an archived snapshot, you must first restore it to the standard tier. The
restored snapshot has the same snapshot ID, encryption status, IAM permissions, owner information,
and resource tags that it had before it was archived. After it is restored, you can use it in the same
way that you use any other snapshot in your account. The restored snapshot is always a full snapshot.

When you restore a snapshot, you can choose to restore it **permanently**
or **temporarily**.

If you restore a snapshot permanently, the snapshot is moved from the archive tier to the standard
tier permanently. The snapshot remains restored and ready for use until you manually re-archive it or
you manually delete it. When you permanently restore a snapshot, the snapshot is removed from the
archive tier.

If you restore a snapshot temporarily, the snapshot is copied from the archive tier to the standard
tier for a restore period that you specify. The snapshot remains restored and ready for use for the
restore period only. During the restore period, a copy of the snapshot remains in the archive tier.
After the period expires, the snapshot is automatically removed from the standard tier. You can increase
or decrease the restore period or change the restore type to permanent at any time during the restore
period. For more information, see [Modify the restore period for a temporarily restored Amazon EBS snapshot](modify-temp-restore-period.md "modify-temp-restore-period.md").

If you are restoring snapshots that are associated with a disabled AMI, and you intend
to use that AMI, you must first **permanently restore** all of
the associated snapshots and then [re-enable a disabled AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md#re-enable-a-disabled-ami "../../../AWSEC2/latest/UserGuide/disable-an-ami.md#re-enable-a-disabled-ami") before you can use it. You can't enable an AMI if the
associated snapshots are temporarily restored. You can use the following command to find
all of the snapshots associated with an AMI.

```
aws ec2 describe-images --image-id `ami_id` \
  --query Images[*].BlockDeviceMappings[*].Ebs[].SnapshotId[]
```

Console

###### To restore a snapshot from the archive

Open the Amazon EC2 console at
[https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").

1. In the navigation pane, choose **Snapshots**.
2. In the list of snapshots, select the archived snapshot to restore, and then
   choose **Actions**, **Restore snapshot from
   archive**.
3. Specify the type of restore to perform. For **Restore type**, do one of
   the following:
   - To restore the snapshot permanently, select **Permanent**.
   - To restore the snapshot temporarily, select **Temporary**, and then
     for **Temporary restore period**, enter the number of days for which to
     restore the snapshot.

4. To confirm, choose **Restore snapshot**.

AWS CLI

###### To permanently restore an archived snapshot

Use the [restore-snapshot-tier](../../../cli/latest/reference/ec2/restore-snapshot-tier.md "../../../cli/latest/reference/ec2/restore-snapshot-tier.md") AWS CLI command with the `--permanent-restore` option.
For `--snapshot-id`, specify the ID of the snapshot to restore.

```
aws ec2 restore-snapshot-tier \
    --snapshot-id `snap-0abcdef1234567890` \
    --permanent-restore
```

The following is example output.

```
{
    "SnapshotId": "snap-0abcdef1234567890",
    "IsPermanentRestore": true
}
```

###### To temporarily restore an archived snapshot

Use the [restore-snapshot-tier](../../../cli/latest/reference/ec2/restore-snapshot-tier.md "../../../cli/latest/reference/ec2/restore-snapshot-tier.md") AWS CLI command. Omit the `--permanent-restore` option.
For `--temporary-restore-days`, specify the number of days for which to restore the snapshot.
The allowed range is 1 to 180 days. If you do not specify a value, the default is 1 day.

The following example temporarily restores the specified snapshot
for a restore period of 5 days.

```
aws ec2 restore-snapshot-tier \
    --snapshot-id `snap-0abcdef1234567890` \
    --temporary-restore-days 5
```

The following is example output.

```
{
    "SnapshotId": "snap-0abcdef1234567890",
    "RestoreDuration": 5,
    "IsPermanentRestore": false
}
```

PowerShell

###### To permanently restore an archived snapshot

Use the [Restore-EC2SnapshotTier](../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md "../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md") cmdlet.

```
Restore-EC2SnapshotTier `
    -SnapshotId `snap-0abcdef1234567890` `
    -PermanentRestore $true
```

###### To temporarily restore an archived snapshot

Use the [Restore-EC2SnapshotTier](../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md "../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md") cmdlet.

```
Restore-EC2SnapshotTier `
    -SnapshotId `snap-0abcdef1234567890` `
    -TemporaryRestoreDays 5
```

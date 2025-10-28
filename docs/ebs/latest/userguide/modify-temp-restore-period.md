# Modify the restore period for a temporarily restored Amazon EBS snapshot

When you restore a snapshot temporarily, you must specify the number of days for which
the snapshot is to remain restored in your account. After the restore period expires, the
snapshot is automatically removed from the standard tier.

You can change the restore period for a temporarily restored snapshot at any time.

You can choose to either increase or decrease the restore period, or you can change the
restore type from temporary to permanent.

If you change the restore period, the new restore period is effective from the current
date. For example, if you specify a new restore period of `5` days, the snapshot
will remain restored for five days from the current date.

###### Note

You can end a temporary restore early by setting the restore period to 1 day.

If you change the restore type from temporary to permanent, the snapshot copy is deleted
from the archive tier, and the snapshot remains available in your account until you manually
re-archive it or delete it.

Console

###### To modify the restore period or restore type

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. In the list of snapshots, select the snapshot that you previously temporarily
   restored, and then choose **Actions**, **Restore snapshot
   from archive**.
4. For **Restore type**, do one of the following:
   - To change the restore type from temporary to permanent, select **Permanent**.
   - To increase or decrease the restore period, keep **Temporary**, and then for
     **Temporary restore period**, enter the new restore period in days.

5. To confirm, choose **Restore snapshot**.

AWS CLI

###### To modify the restore period or change the restore type

Use the [restore-snapshot-tier](../../../cli/latest/reference/ec2/restore-snapshot-tier.md "../../../cli/latest/reference/ec2/restore-snapshot-tier.md") command. For `--snapshot-id`, specify the ID of the
snapshot that you previously temporarily restored. To change the restore type from temporary to
permanent, specify `--permanent-restore` and omit `--temporary-restore-days`.
To increase or decrease the restore period, omit `--permanent-restore` and for
`--temporary-restore-days`, specify the new restore period in days.

###### Example: Increase or decrease the restore period

The following command changes the restore period for the specified snapshot
to `10` days.

```
aws ec2 restore-snapshot-tier \
    --snapshot-id `snap-0abcdef1234567890` \
    --temporary-restore-days 10
```

The following is example output.

```
{
    "SnapshotId": "snap-0abcdef1234567890",
    "RestoreDuration": 10,
    "IsPermanentRestore": false
}
```

###### Example: Change restore type to permanent

The following command changes the restore type for the specified snapshot
from temporary to permanent.

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

PowerShell

###### To modify the restore period or change the restore type

Use the [Restore-EC2SnapshotTier](../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md "../../../powershell/latest/reference/items/Restore-EC2SnapshotTier.md") cmdlet. For `-SnapshotId`, specify the ID of the
snapshot that you previously temporarily restored. To change the restore type from temporary to
permanent, specify `-PermanentRestore` and omit `-TemporaryRestoreDays`.
To increase or decrease the restore period, omit `-PermanentRestore` and for
`-TemporaryRestoreDays`, specify the new restore period in days.

###### Example: Increase or decrease the restore period

The following command changes the restore period for the specified snapshot
to `10` days.

```
Restore-EC2SnapshotTier `
    -SnapshotId `snap-0abcdef1234567890` `
    -TemporaryRestoreDays 10
```

###### Example: Change restore type to permanent

The following command changes the restore type for the specified snapshot
from temporary to permanent.

```
Restore-EC2SnapshotTier `
    -SnapshotId `snap-0abcdef1234567890` `
    -PermanentRestore $true
```

# View archived Amazon EBS snapshots

Console

###### To view storage tier information for a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. In the list of snapshots, select the snapshot and choose the **Storage tier** tab.

The tab provides the following information:

    * **Last tier change started on** — The date and time when the last archive
     or restore was started.
    * **Tier change progress** — The progress of the last archive or restore action, as
     a percentage.
    * **Storage tier** — The storage tier for the snapshot. Always `archive` for
     archived snapshots, and `standard` for snapshots stored on the standard tier, including temporarily
     restored snapshots.
    * **Tiering status** — The status of the last archive or restore action.
    * **Archive completed on** — The date and time when the archive completed.
    * **Temporary restore expires on** — The date and time when a temporarily restored
     snapshot is set to expire.

AWS CLI

###### To view archival information about an archived snapshot

Use the [describe-snapshot-tier-status](../../../cli/latest/reference/ec2/describe-snapshot-tier-status.md "../../../cli/latest/reference/ec2/describe-snapshot-tier-status.md") command. Specify the `snapshot-id` filter, and for the
filter value, specify the snapshot ID. Alternatively, to view all archived snapshots, omit the filter.

```
--filters "Name=snapshot-id, Values=`snapshot_id`"
```

The output includes the following response parameters:

- `Status` — The status of the snapshot. Always `completed` for archived
  snapshots. Only snapshots that are in the `completed` state can be archived.
- `LastTieringStartTime` — The date and time that the archival process started,
  in UTC time format (YYYY-MM-DDTHH:MM:SSZ).
- `LastTieringOperationState` — The current state of the archival process. Possible
  states include: `archival-in-progress` | `archival-completed` | `archival-failed` |
  `permanent-restore-in-progress` | `permanent-restore-completed` | `permanent-restore-failed` |
  `temporary-restore-in-progress` | `temporary-restore-completed` | `temporary-restore-failed`
- `LastTieringProgress` — The progress of the snapshot archival process, as a
  percentage.
- `StorageTier` — The storage tier for the snapshot. Always `archive` for
  archived snapshots, and `standard` for snapshots stored on the standard tier, including temporarily
  restored snapshots.
- `ArchivalCompleteTime` — The date and time that the archival process completed,
  in UTC time format (YYYY-MM-DDTHH:MM:SSZ).

###### Example: Describe a snapshot

The following example displays information about the specified snapshot.

```
aws ec2 describe-snapshot-tier-status \
    --filters "Name=snapshot-id, Values=`snap-0abcdef1234567890`"
```

The following is example output.

```
{
    "SnapshotTierStatuses": [
        {
            "Status": "completed",
            "ArchivalCompleteTime": "2021-09-15T17:33:16.147Z",
            "LastTieringProgress": 100,
            "Tags": [],
            "VolumeId": "vol-01234567890abcdef",
            "LastTieringOperationState": "archival-completed",
            "StorageTier": "archive",
            "OwnerId": "123456789012",
            "SnapshotId": "snap-0abcdef1234567890",
            "LastTieringStartTime": "2021-09-15T16:44:37.574Z"
        }
    ]
}
```

###### To view archived and standard tier snapshots

Use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md")
command. For `--snapshot-ids`, specify the ID of the snapshot.

```
aws ec2 describe-snapshots --snapshot-ids `snap-0abcdef1234567890`
```

The following is example output. The `StorageTier` response parameter indicates whether
the snapshot is currently archived. `archive` indicates that the snapshot is currently archived
and stored in the archive tier, and `standard` indicates that the snapshot is currently not
archived and that it is stored in the standard tier.

In the following example output, only `Snap A` is archived. `Snap
 B` and `Snap C` are not archived.

Additionally, the `RestoreExpiryTime` response parameter is returned only for snapshots that
are temporarily restored from the archive. It indicates when temporarily restored snapshots are to be
automatically removed from the standard tier. It is **not** returned for snapshots
that are permanently restored.

In the following example output, `Snap C` is temporarily restored, and
it will be automatically removed from the standard tier at 2021-09-19T21:00:00.000Z
(September 19, 2021 at 21:00 UTC).

```
{
    "Snapshots": [
        {
            "Description": "Snap A",
            "Encrypted": false,
            "VolumeId": "vol-01234567890aaaaaa",
            "State": "completed",
            "VolumeSize": 8,
            "StartTime": "2021-09-07T21:00:00.000Z",
            "Progress": "100%",
            "OwnerId": "123456789012",
            "SnapshotId": "snap-01234567890aaaaaa",
            "StorageTier": "archive",
            "Tags": []
        },
        {
            "Description": "Snap B",
            "Encrypted": false,
            "VolumeId": "vol-09876543210bbbbbb",
            "State": "completed",
            "VolumeSize": 10,
            "StartTime": "2021-09-14T21:00:00.000Z",
            "Progress": "100%",
            "OwnerId": "123456789012",
            "SnapshotId": "snap-09876543210bbbbbb",
            "StorageTier": "standard",
            "RestoreExpiryTime": "2019-09-19T21:00:00.000Z",
            "Tags": []
        },
        {
            "Description": "Snap C",
            "Encrypted": false,
            "VolumeId": "vol-054321543210cccccc",
            "State": "completed",
            "VolumeSize": 12,
            "StartTime": "2021-08-01T21:00:00.000Z",
            "Progress": "100%",
            "OwnerId": "123456789012",
            "SnapshotId": "snap-054321543210cccccc",
            "StorageTier": "standard",
            "Tags": []
        }
    ]
}
```

###### To view only snapshots that are stored in the archive tier or the standard tier

Use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md")
command. Include the `--filter` option, with the filter
name `storage-tier`. For the filter value specify either `archive`
or `standard`. The following example displays only archived snapshots.

```
aws ec2 describe-snapshots --filters "Name=storage-tier,Values=archive"
```

PowerShell

###### To view archival information about an archived snapshot

Use the [Get-EC2SnapshotTierStatus](../../../powershell/latest/reference/items/Get-EC2SnapshotTierStatus.md "../../../powershell/latest/reference/items/Get-EC2SnapshotTierStatus.md") cmdlet.

```
Get-EC2SnapshotTierStatus `
    -Filter @{Name="snapshot-id"; Values="`snap-0abcdef1234567890`"}
```

###### To view archived and standard tier snapshots

Use the [Get-EC2Snapshot](../../../powershell/latest/reference/items/Get-EC2Snapshot.md "../../../powershell/latest/reference/items/Get-EC2Snapshot.md") cmdlet.

```
Get-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890`
```

###### To view only snapshots that are stored in the archive tier or the standard tier

Use the [Get-EC2Snapshot](../../../powershell/latest/reference/items/Get-EC2Snapshot.md "../../../powershell/latest/reference/items/Get-EC2Snapshot.md") cmdlet. The following example displays only archived snapshots.

```
Get-EC2Snapshot `
    -Filter @{Name="storage-tier"; Values="archive"}
```

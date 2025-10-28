# Archive an Amazon EBS snapshot

You can archive any snapshot that is in the `completed` state and that you own in
your account. You can't archive snapshots that are in the `pending` or `error`
states, or snapshots that are shared with you. For more information, see
[Considerations and limitations for archiving Amazon EBS snapshots](snapshot-archive-considerations.md "snapshot-archive-considerations.md").

If the snapshot is associated with one or more AMIs, then you must first disable those
associated AMIs before you can archive the snapshot. For more information, see
[Disable an AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md "../../../AWSEC2/latest/UserGuide/disable-an-ami.md").

Archived snapshots retain their snapshot ID, encryption status, AWS Identity and Access Management (IAM) permissions,
owner information, and resource tags. However, fast snapshot restore and snapshot sharing are
automatically disabled after the snapshot is archived.

You can continue to use the snapshot while the archive is in process. As soon as the snapshot
tiering status reaches the `archival-complete` state, you can no longer use the snapshot.

Console

###### To archive a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. In the list of snapshots, select the snapshot to archive and then choose **Actions**,
   **Archive snapshot**.
4. To confirm, choose **Archive snapshot**.

AWS CLI

###### To archive a snapshot

Use the [modify-snapshot-tier](../../../cli/latest/reference/ec2/modify-snapshot-tier.md "../../../cli/latest/reference/ec2/modify-snapshot-tier.md") AWS CLI command. For `--snapshot-id`, specify the ID of the
snapshot to archive. For `--storage-tier`, specify `archive`.

```
aws ec2 modify-snapshot-tier \
    --snapshot-id `snap-0abcdef1234567890` \
    --storage-tier archive
```

The following is example output. The `TieringStartTime` response parameter indicates
the date and time at which the archive process was started, in UTC time format (YYYY-MM-DDTHH:MM:SSZ).

```
{
    "SnapshotId": "snap-0abcdef1234567890",
    "TieringStartTime": "2021-09-15T16:44:37.574Z"
}
```

PowerShell

###### To archive a snapshot

Use the [Edit-EC2SnapshotTier](../../../powershell/latest/reference/items/Edit-EC2SnapshotTier.md "../../../powershell/latest/reference/items/Edit-EC2SnapshotTier.md") cmdlet. The following example archives the specified
snapshot.

```
Edit-EC2SnapshotTier `
    -SnapshotId `snap-0abcdef1234567890` `
    -StorageTier "archive"
```

# Check the fast snapshot restore state for an Amazon EBS snapshot

Fast snapshot restore for a snapshot can be in one of the following states.

- `enabling` — A request was made to enable fast snapshot restore.
- `optimizing` — Fast snapshot restore is being enabled.
  It takes 60 minutes per TiB to optimize a snapshot. Snapshots in this state offer some
  performance benefit when restoring volumes.
- `enabled` — Fast snapshot restore is enabled. Snapshots that are
  in this state and that have sufficient volume creation credits offer the full performance
  benefit when restoring volumes.
- `disabling` — A request was made to disable fast snapshot restore,
  or a request to enable fast snapshot restore failed.
- `disabled` — Fast snapshot restore is disabled. You can enable
  fast snapshot restore again as needed.
  You can view the state of fast snapshot restore for a snapshot that you own or
  for a snapshot that is shared with you.

Console

###### To view the state of fast snapshot restore

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot.
4. On the **Details** tab, **Fast snapshot restore**,
   indicates the state of fast snapshot restore.

AWS CLI

###### To view snapshots with fast snapshot restore enabled

Use the [describe-fast-snapshot-restores](../../../cli/latest/reference/ec2/describe-fast-snapshot-restores.md "../../../cli/latest/reference/ec2/describe-fast-snapshot-restores.md")
command.

```
aws ec2 describe-fast-snapshot-restores --filters Name=state,Values=enabled
```

The following is example output.

```
{
    "FastSnapshotRestores": [
        {
            "SnapshotId": "snap-0e946653493cb0447",
            "AvailabilityZone": "us-east-2a",
            "State": "enabled",
            "StateTransitionReason": "Client.UserInitiated - Lifecycle state transition",
            "OwnerId": "123456789012",
            "EnablingTime": "2020-01-25T23:57:49.596Z",
            "OptimizingTime": "2020-01-25T23:58:25.573Z",
            "EnabledTime": "2020-01-25T23:59:29.852Z"
        },
        {
            "SnapshotId": "snap-0e946653493cb0447",
            "AvailabilityZone": "us-east-2b",
            "State": "enabled",
            "StateTransitionReason": "Client.UserInitiated - Lifecycle state transition",
            "OwnerId": "123456789012",
            "EnablingTime": "2020-01-25T23:57:49.596Z",
            "OptimizingTime": "2020-01-25T23:58:25.573Z",
            "EnabledTime": "2020-01-25T23:59:29.852Z"
        }
    ]
}

```

PowerShell

###### To view snapshots with fast snapshot restore enabled

Use the [Get-EC2FastSnapshotRestore](../../../powershell/latest/reference/items/Get-EC2FastSnapshotRestore.md "../../../powershell/latest/reference/items/Get-EC2FastSnapshotRestore.md") cmdlet.

```
Get-EC2FastSnapshotRestore `
    -Filter @{Name="state"; Values="enabled"}
```

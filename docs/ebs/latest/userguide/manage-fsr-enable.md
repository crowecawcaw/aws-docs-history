# Configure fast snapshot restore for an Amazon EBS snapshot

Fast snapshot restore is disabled for a snapshot by default. You can enable
or disable fast snapshot restore for snapshots that you own and for snapshots
that are shared with you. When you enable or disable fast snapshot restore
for a snapshot, the changes apply to your account only.

###### Note

When you enable fast snapshot restore for a snapshot, your account
is billed for each minute that fast snapshot restore is enabled in a
particular Availability Zone. Charges are pro-rated and have a minimum
of one hour.

When you delete a snapshot that you own, fast snapshot restore is automatically
disabled for that snapshot in your account. If you enabled fast snapshot restore
for a snapshot that is shared with you, and the snapshot owner deletes or
unshares it, fast snapshot restore is automatically disabled for the shared
snapshot in your account.

If you enabled fast snapshot restore for a snapshot that is shared with you, and it has
been encrypted using a custom CMK, fast snapshot restore is not automatically disabled for the
snapshot when the snapshot owner revokes your access to the custom CMK. You must manually
disable fast snapshot restore for that snapshot.

After you enable fast snapshot restore for a snapshot, it enters the `optimizing`
state. Snapshots that are in the `optimizing` state provide some performance
benefits when using them to restore volumes. They start to provide the full performance benefits
of fast snapshot restore only after they enter the `enabled` state.

Console

###### To configure fast snapshot restore

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot, and choose **Actions**, **Manage
   fast snapshot restore**.
4. The **Fast snapshot restore settings** section lists all of
   the Availability Zones in which you can enable fast snapshot restore for the selected
   snapshot. The **Current status** volume indicates whether fast
   snapshot restore is current enabled or disabled for each zone.

To enable fast snapshot restore in a zone where it is currently disabled,
select the zone, choose **Enable**, and then to confirm, choose
**Enable**.

To disable fast snapshot restore in a zone where it is currently enabled,
select the zone, and then choose **Disable**. 5. After you have made the required changes, choose **Close**.

AWS CLI

###### To enable fast snapshot restore

Use the [enable-fast-snapshot-restores](../../../cli/latest/reference/ec2/enable-fast-snapshot-restores.md "../../../cli/latest/reference/ec2/enable-fast-snapshot-restores.md") command.

```
aws ec2 enable-fast-snapshot-restores \
    --availability-zones `us-east-1a` `us-east-1b` \
    --source-snapshot-ids `snap-0abcdef1234567890`
```

###### To disable fast snapshot restore

Use the [disable-fast-snapshot-restores](../../../cli/latest/reference/ec2/disable-fast-snapshot-restores.md "../../../cli/latest/reference/ec2/disable-fast-snapshot-restores.md") command.

```
aws ec2 disable-fast-snapshot-restores \
    --availability-zones `us-east-1a` \
    --source-snapshot-ids `snap-0abcdef1234567890`
```

The following example uses the [describe-fast-snapshot-restores](../../../cli/latest/reference/ec2/describe-fast-snapshot-restores.md "../../../cli/latest/reference/ec2/describe-fast-snapshot-restores.md") command to describe your disabled fast snapshot restores.

```
aws ec2 describe-fast-snapshot-restores \
    --filters Name=state,Values=disabled
```

PowerShell

###### To enable fast snapshot restore

Use the [Enable-EC2FastSnapshotRestore](../../../powershell/latest/reference/items/Enable-EC2FastSnapshotRestore.md "../../../powershell/latest/reference/items/Enable-EC2FastSnapshotRestore.md") cmdlet.

```
Enable-EC2FastSnapshotRestore `
    -AvailabilityZone `us-east-1a` `us-east-1b` `
    -SourceSnapshotId `snap-0abcdef1234567890`
```

###### To disable fast snapshot restore

Use the [Disable-EC2FastSnapshotRestore](../../../powershell/latest/reference/items/Disable-EC2FastSnapshotRestore.md "../../../powershell/latest/reference/items/Disable-EC2FastSnapshotRestore.md") cmdlet.

```
Disable-EC2FastSnapshotRestore `
    -AvailabilityZone `us-east-1a` `
    -SourceSnapshotId `snap-0abcdef1234567890`
```

The following example uses the [Get-EC2FastSnapshotRestore](../../../powershell/latest/reference/items/Get-EC2FastSnapshotRestore.md "../../../powershell/latest/reference/items/Get-EC2FastSnapshotRestore.md") cmdlet to describe your disabled fast snapshot restores.

```
Get-EC2FastSnapshotRestore `
    -Filter @{Name="state"; Values="disabled"}
```

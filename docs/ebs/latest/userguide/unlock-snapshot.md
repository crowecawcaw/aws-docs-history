# Unlock an Amazon EBS snapshot

You can unlock a snapshot only if it is locked in governance mode, or if it is locked
in compliance mode and it is still within the cooling-off period.

Console

###### To unlock a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot to unlock and choose **Actions**,
   **Snapshot settings**, **Manage snapshot lock**.
4. Choose **Unlock snapshot** and then choose **Unlock
   snapshot** again to confirm.

AWS CLI

###### To unlock a snapshot

Use the [unlock-snapshot](../../../cli/latest/reference/ec2/unlock-snapshot.md "../../../cli/latest/reference/ec2/unlock-snapshot.md")
command.

```
aws ec2 unlock-snapshot --snapshot-id `snap-0abcdef1234567890`
```

PowerShell

###### To unlock a snapshot

Use the [Unlock-EC2Snapshot](../../../powershell/latest/reference/items/Unlock-EC2Snapshot.md "../../../powershell/latest/reference/items/Unlock-EC2Snapshot.md") cmdlet.

```
Unlock-EC2Snapshot -SnapshotId `snap-0abcdef1234567890`
```

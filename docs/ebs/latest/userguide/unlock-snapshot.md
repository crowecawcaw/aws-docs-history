

# Unlock an Amazon EBS snapshot
<a name="unlock-snapshot"></a>

You can unlock a snapshot only if it is locked in governance mode, or if it is locked in compliance mode and it is still within the cooling-off period.

------
#### [ Console ]

**To unlock a snapshot**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Snapshots**.

1. Select the snapshot to unlock and choose **Actions**, **Snapshot settings**, **Manage snapshot lock**.

1. Choose **Unlock snapshot** and then choose **Unlock snapshot** again to confirm.

------
#### [ AWS CLI ]

**To unlock a snapshot**  
Use the [unlock-snapshot](https://docs.aws.amazon.com/cli/latest/reference/ec2/unlock-snapshot.html) command.

```
aws ec2 unlock-snapshot --snapshot-id {{snap-0abcdef1234567890}}
```

------
#### [ PowerShell ]

**To unlock a snapshot**  
Use the [Unlock-EC2Snapshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Unlock-EC2Snapshot.html) cmdlet.

```
Unlock-EC2Snapshot -SnapshotId {{snap-0abcdef1234567890}}
```

------
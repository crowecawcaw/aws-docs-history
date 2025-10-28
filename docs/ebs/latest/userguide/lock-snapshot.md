# Lock an Amazon EBS snapshot

You can lock a snapshot that is in the `pending` or `completed`
state. For more information, see [Considerations for Amazon EBS snapshot lock](snapshot-lock-considerations.md "snapshot-lock-considerations.md").

Console

###### To lock a snapshot

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  In the navigation pane, choose **Snapshots**.
3.  Select the snapshot to lock and choose **Actions**,
    **Snapshot settings**, **Manage snapshot lock**.
4.  Select **Lock snapshot**.
5.  For **Lock mode**, choose either **Governance mode**
    or **Compliance mode**. For more information, see [Lock mode](snapshot-lock-concepts.md#lock-mode "snapshot-lock-concepts.md#lock-mode").
6.  For **Lock duration**, do one of the following:

        * To lock the snapshot for a specific period, choose **Lock snapshot for**,
         and then enter the period in either days or years.
        * To lock the snapshot until a specific date and time, choose **Lock snapshot
         until**, and then select the expiration date and time.

    For more information, see [Lock duration](snapshot-lock-concepts.md#lock-duration "snapshot-lock-concepts.md#lock-duration").

7.  (_Compliance mode only_) For **Cooling-off period**,
    specify a cooling-off period during which you can unlock the snapshot and modify the lock
    configuration. For more information, see [Cooling-off period](snapshot-lock-concepts.md#cool-off "snapshot-lock-concepts.md#cool-off").
8.  (_Compliance mode only_) To confirm that you want to lock the snapshot
    in compliance mode and that you will not be able to unlock the snapshot after the cooling-off
    period expires, choose **Acknowledge**.
9.  Choose **Save lock settings**.

AWS CLI

###### To lock a snapshot in governance mode

Use the [lock-snapshot](../../../cli/latest/reference/ec2/lock-snapshot.md "../../../cli/latest/reference/ec2/lock-snapshot.md")
command. For `--lock-mode`, specify `governance`. To lock the snapshot
for a specific period, for `--lock-duration`, specify the period, in days.

```
aws ec2 lock-snapshot \
    --snapshot-id `snap-0abcdef1234567890` \
    --lock-mode governance \
    --lock-duration `30`
```

To lock the snapshot until a specific date, for `--expiration-date`,
specify the date and time at which the lock must expire, in the UTC time zone.

```
aws ec2 lock-snapshot \
    --snapshot-id `snap-0abcdef1234567890` \
    --lock-mode governance \
    --expiration-date `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

###### To lock a snapshot in compliance mode

Use the [lock-snapshot](../../../cli/latest/reference/ec2/lock-snapshot.md "../../../cli/latest/reference/ec2/lock-snapshot.md") command. For `--lock-mode`, specify
`compliance`. For `--cool-off-period`, optionally specify a
cooling-off period, in hours. To lock the snapshot for a specific period, for
`--lock-duration`, specify the number of days to lock the snapshot.

```
aws ec2 lock-snapshot \
    --snapshot-id `snap-0abcdef1234567890` \
    --lock-mode compliance \
    --cool-off-period `24` \
    --lock-duration `30`
```

To lock the snapshot until a specific date, for `--expiration-date`,
specify the date and time at which the lock must expire, in the UTC time
zone.

```
aws ec2 lock-snapshot \
    --snapshot-id `snap-0abcdef1234567890` \
    --lock-mode compliance \
    --expiration-date `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

PowerShell

###### To lock a snapshot in governance mode

Use the [Lock-EC2Snapshot](../../../powershell/latest/reference/items/Lock-EC2Snapshot.md "../../../powershell/latest/reference/items/Lock-EC2Snapshot.md") cmdlet. You can optionally specify the
duration of the snapshot lock, in days.

```
Lock-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890` `
    -LockMode "governance" `
    -LockDuration `30`
```

Alternatively, you can lock the snapshot until a specific date, in the UTC time zone.

```
Lock-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890` `
    -LockMode "governance" `
    -ExpirationDate `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

###### To lock a snapshot in compliance mode

Use the [Lock-EC2Snapshot](../../../powershell/latest/reference/items/Lock-EC2Snapshot.md "../../../powershell/latest/reference/items/Lock-EC2Snapshot.md") cmdlet. You can optionally specify a cooling-off
period, in hours. You can also optionally specify the duration of the
snapshot lock, in days.

```
Lock-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890` `
    -LockMode "compliance" `
    -CoolOffPeriod `24` `
    -LockDuration `30`
```

Alternatively, you can lock the snapshot until a specific date, in the UTC time zone.

```
Lock-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890` `
    -LockMode "compliance" `
    -ExpirationDate `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

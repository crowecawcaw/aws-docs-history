# Update Amazon EBS snapshot lock settings

The allowed updates depend on the lock state:

- `governance` — you can change the lock mode and increase or decrease the
  lock duration or expiration date.
- `compliance-cooloff` — you can change the lock mode, increase or decrease the
  cooling-off period, and increase or decrease the lock duration or expiration date.
- `compliance` — you can only increase the lock duration or expiration date.

Console

###### To update snapshot lock settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot for which to modify the lock settings and choose
   **Actions**, **Snapshot settings**,
   **Manage snapshot lock**.
4. Update the settings as needed, and then choose **Save lock
   settings**.

AWS CLI

###### To update snapshot lock settings

Use the [lock-snapshot](../../../cli/latest/reference/ec2/lock-snapshot.md "../../../cli/latest/reference/ec2/lock-snapshot.md")
command. Specify the ID of the snapshot and the options to modify. The following
example changes the expiration date.

```
aws ec2 lock-snapshot \
    --snapshot-id `snap-0abcdef1234567890` \
    --lock-mode governance \
    --expiration-date `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

PowerShell

###### To update snapshot lock settings

Use the [Lock-EC2Snapshot](../../../powershell/latest/reference/items/Lock-EC2Snapshot.md "../../../powershell/latest/reference/items/Lock-EC2Snapshot.md") cmdlet. Specify the ID of the snapshot and the options to modify.
The following example changes the expiration date.

```
Lock-EC2Snapshot `
    -SnapshoId `snap-0abcdef1234567890` `
    -LockMode "governance" `
    -ExpirationDate `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss`.`sss`Z
```

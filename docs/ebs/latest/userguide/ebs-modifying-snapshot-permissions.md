# Share an Amazon EBS snapshot with other AWS accounts

You can modify the permissions of a snapshot if you want to share it with other AWS
accounts. You can share snapshots publicly with all other AWS accounts, or you can share
them privately with individual AWS accounts that you specify. Users that you have authorized
can use the snapshots that you share to create their own EBS volumes, while your original
snapshot remains unaffected.

###### Important

When you share a snapshot, you are giving others access to all of the data on the
snapshot. Share snapshots only with people that you trust with _all_ of
your snapshot data.

To prevent the public sharing of snapshots, you can enable [Block public access for Amazon EBS snapshots](block-public-access-snapshots.md "block-public-access-snapshots.md").

###### Topics

- [Before you share a snapshot](#share-snapshot-considerations "#share-snapshot-considerations")
- [Share a snapshot](#share-unencrypted-snapshot "#share-unencrypted-snapshot")
- [Share a KMS key](share-kms-key.md "share-kms-key.md")
- [Use shared snapshots](view-shared-snapshot.md "view-shared-snapshot.md")
- [Determine the use of snapshots that
  you share](#shared-snapshot-cloudtrail-logging "#shared-snapshot-cloudtrail-logging")

## Before you share a snapshot

The following considerations apply to sharing snapshots:

- If block public access for snapshots is enabled for the Region, attempts to
  publicly share snapshots will be blocked. Snapshots can still be privately shared.
- Snapshots are constrained to the Region in which they were created. To share a
  snapshot with another Region, copy the snapshot to that Region and then share the
  copy. For more information, see [Copy an Amazon EBS snapshot](ebs-copy-snapshot.md "ebs-copy-snapshot.md").
- You can't share snapshots that are encrypted with the default AWS managed key.
  You can only share snapshots that are encrypted with a customer managed key. For more
  information, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in
  the _AWS Key Management Service Developer Guide_.
- You can share only unencrypted snapshots publicly.
- When you share an encrypted snapshot, you must also share the customer managed key
  used to encrypt the snapshot. For more information, see [Share the KMS key used to encrypt a shared Amazon EBS snapshot](share-kms-key.md "share-kms-key.md").

## Share a snapshot

You can share a snapshot publicly or with specific AWS accounts.

Console

###### To share a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot to share, and then choose **Actions**,
   **Modify permissions**.
4. Specify the snapshot's permissions. _Current setting_
   indicates the snapshot's current sharing permissions.
   - To share the snapshot publicly with all AWS accounts, choose
     **Public**.
   - To share the snapshot privately with specific AWS accounts, choose
     **Private**. Then, in the **Sharing
     accounts** section, choose **Add account**, and
     enter the 12-digit account ID (without hyphens) of the account to share
     with.

5. Choose **Save changes**.

AWS CLI
The permissions for a snapshot are specified using the `createVolumePermission`
attribute of the snapshot. To make a snapshot public, set the group to `all`. To share
a snapshot with a specific AWS account, set the user to the ID of the AWS account.

###### To share a snapshot publicly

Use the [modify-snapshot-attribute](../../../cli/latest/reference/ec2/modify-snapshot-attribute.md "../../../cli/latest/reference/ec2/modify-snapshot-attribute.md") command.

For `--attribute`, specify `createVolumePermission`. For
`--operation-type`, specify `add`. For `--group-names`, specify
`all`.

```
aws ec2 modify-snapshot-attribute \
    --snapshot-id `snap-0abcdef1234567890` \
    --attribute createVolumePermission \
    --operation-type add \
    --group-names all
```

###### To share a snapshot privately

Use the [modify-snapshot-attribute](../../../cli/latest/reference/ec2/modify-snapshot-attribute.md "../../../cli/latest/reference/ec2/modify-snapshot-attribute.md") command.

For `--attribute`, specify `createVolumePermission`. For
`--operation-type`, specify `add`. For `--user-ids`,
specify the 12-digit IDs of the AWS accounts with which to share the snapshots.

```
aws ec2 modify-snapshot-attribute \
    --snapshot-id `snap-0abcdef1234567890` \
    --attribute createVolumePermission \
    --operation-type add \
    --user-ids `123456789012` `111122223333`
```

PowerShell
The permissions for a snapshot are specified using the `createVolumePermission`
attribute of the snapshot. To make a snapshot public, set the group to `all`. To share
a snapshot with a specific AWS account, set the user to the ID of the AWS account.

###### To share a snapshot publicly

Use the [Edit-EC2SnapshotAttribute](../../../powershell/latest/reference/items/Edit-EC2SnapshotAttribute.md "../../../powershell/latest/reference/items/Edit-EC2SnapshotAttribute.md")
cmdlet.

For `-Attribute`, specify `CreateVolumePermission`. For
`-OperationType`, specify `Add`. For `-GroupName`,
specify `all`.

```
Edit-EC2SnapshotAttribute `
    -SnapshotId `snap-0abcdef1234567890` `
    -Attribute CreateVolumePermission `
    -OperationType Add `
    -GroupName all
```

###### To share a snapshot privately

Use the [Edit-EC2SnapshotAttribute](../../../powershell/latest/reference/items/Edit-EC2SnapshotAttribute.md "../../../powershell/latest/reference/items/Edit-EC2SnapshotAttribute.md")
cmdlet.

For `-Attribute`, specify `CreateVolumePermission`. For
`-OperationType`, specify `Add`. For `UserId`,
specify the 12-digit IDs of the AWS accounts with which to share the snapshots.

```
Edit-EC2SnapshotAttribute `
    -SnapshotId `snap-0abcdef1234567890` `
    -Attribute CreateVolumePermission `
    -OperationType Add `
    -UserId `123456789012` `111122223333`
```

## Determine the use of snapshots that

you share

You can use AWS CloudTrail to monitor whether a snapshot that you have shared with others is copied or
used to create a volume. The following events are logged in CloudTrail when an action is taken on a snapshot
you have shared::

- **SharedSnapshotCopyInitiated** — A shared snapshot is being copied.
- **SharedSnapshotVolumeCreated** — A shared snapshot is being used to create a volume.

For more information about using CloudTrail, see [Log Amazon EC2 and Amazon EBS API calls with AWS CloudTrail](../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md "../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md").

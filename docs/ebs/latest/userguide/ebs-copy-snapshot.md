# Copy an Amazon EBS snapshot

After you create a snapshot, and it has reached the `completed` state, you
can create a copy of it. The snapshot copy is an exact copy of the original, but it has a
unique resource ID. You can copy snapshots that you own and snapshots that are shared with
you, privately or publicly. You might need to copy a snapshot for the following use cases:

- Geographic expansion — You need to launch your applications in a new Region.
- Migration — You need to move an application to a new destination, to enable better
  availability or to minimize cost.
- Disaster recovery — You need to back up your data and logs to secondary Regions
  for data redundancy purposes.
- Encryption — You need to encrypt a previously unencrypted snapshot or reencrypt
  an encrypted snapshot using a different KMS key.
- Copy a shared snapshot — You need to copy a snapshot that is shared with you.
- Data retention and auditing requirements — You need to copy encrypted snapshots
  from one AWS account to another to preserve data for auditing or data retention. Using a
  different account protects you if your main AWS account is compromised.
  To copy multi-volume snapshots, identify all of the snapshots that are part of that set
  using the tags that you assigned during creation, and then copy them individually.

For information about copying an Amazon RDS snapshot, see [Copying a DB Snapshot](../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md") in the
_Amazon RDS User Guide_.

###### Pricing

For pricing information about copying snapshots, see [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

###### Contents

- [Considerations for copying snapshots](#snapshot-copy-consids "#snapshot-copy-consids")
- [Destinations for snapshot copies](#snapshot-copy-destinations "#snapshot-copy-destinations")
- [Incremental snapshot copying](#ebs-incremental-copy "#ebs-incremental-copy")
- [Time-based copies](time-based-copies.md "time-based-copies.md")
- [Encryption and snapshot copying](#creating-encrypted-snapshots "#creating-encrypted-snapshots")
- [Copy a snapshot](#ebs-snapshot-copy "#ebs-snapshot-copy")

## Considerations for copying snapshots

- You can copy AWS Marketplace, VM Import/Export, and Storage Gateway snapshots, but you must
  verify that the snapshot is supported in the destination Region.
- There is a limit of `20` concurrent snapshot copy requests per destination.
  If you exceed this quota, you receive a `ResourceLimitExceeded` error. If you
  receive this error, wait for one or more of the copy requests to complete before making a
  new snapshot copy request.
- User-defined tags are not copied from the source snapshot to the snapshot copy.
  You can add user-defined tags during or after the copy operation.
- Snapshots created by a snapshot copy operation have an arbitrary volume ID, such as
  `vol-ffff` or `vol-ffffffff`. These arbitrary volume IDs should not
  be used for any purpose.
- Resource-level permissions specified for the snapshot copy operation
  can apply to the snapshot copy and the source snapshot. For an example, see [Example: Copying snapshots](security_iam_id-based-policy-examples.md#iam-copy-snapshot "security_iam_id-based-policy-examples.md#iam-copy-snapshot").
- If you copy a snapshot that is enabled for fast snapshot restore, the snapshot copy
  is not automatically enabled for fast snapshot restore. You must explicitly enable fast
  snapshot restore for the snapshot copy.
- If you copy a snapshot and encrypt it to a new KMS key, a complete
  (non-incremental) copy is created. This results in additional storage costs.
- If you copy a snapshot to a new Region, a full (non-incremental) copy is created.
  This results in additional storage costs.
- If you use external or cross-Region data transfers, additional [EC2 data transfer](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/") charges will apply. If you delete any snapshots
  after initiation, you are still charged for the data that has already been transferred.

## Destinations for snapshot copies

The location of the source snapshot determines whether you can copy it or not.

- If the source snapshot is in a Region, you can copy it within that Region, to
  another Region, to an Outpost associated with that Region, or to a Local Zone
  in that Region.
- If the source snapshot is in a Local Zone, you can copy it within the same
  Local Zone, to another Local Zone in the same zone group, or to the parent Region
  of that Local Zone.
- If the source snapshot is on an Outpost, you can't copy it.

## Incremental snapshot copying

Snapshot copy operations within the same account and Region using the same
KMS key are always incremental copies. However, if you encrypt the snapshot
copy using a different KMS key, the copy is a full copy.

When you copy a snapshot across Regions or accounts, the copy is an incremental
copy if the following conditions are met:

- The snapshot was copied to the destination Region or account previously.
- The most recent snapshot copy still exists in the destination Region or
  account.
- The most recent snapshot copy has not been archived.
- All copies of the snapshot in the destination Region or account are either
  unencrypted or were encrypted using the same KMS key.

###### Tip

We recommend that you tag your snapshot copies with the volume ID and creation
time so that you can keep track of the most recent snapshot copy of a volume in the
destination Region or account.

To see whether your snapshot copies are incremental, check the
[copySnapshot](ebs-cloud-watch-events.md#copy-snapshot-complete "ebs-cloud-watch-events.md#copy-snapshot-complete") CloudWatch event.

## Encryption and snapshot copying

###### Note

Amazon S3 server-side encryption (256-bit AES) protects a snapshot's data in transit during
a copy operation.

You can create an encrypted snapshot copy of a source snapshot that is unencrypted.
And you can encrypt a snapshot copy with a KMS key that is different from the source
snapshot. However, changing the encryption status of a snapshot copy during a copy
operation could result in a full (not incremental) copy, which might incur greater data
transfer and storage charges.

###### Tip

When using an encrypted snapshot that is shared with you, we recommend that you
re-encrypt the snapshot by copying it and using a KMS key that you own. This protects
you if the original KMS key is compromised, or if the owner revokes your access,
which could cause you to lose access to the snapshot and any encrypted volumes that
you created from it.

###### Permissions for copying encrypted snapshots

To copy an encrypted snapshot, your user must have the following permissions to
use Amazon EBS encryption.

- - `kms:DescribeKey`
  - `kms:CreateGrant`
  - `kms:GenerateDataKey`
  - `kms:GenerateDataKeyWithoutPlaintext`
  - `kms:ReEncrypt`
  - `kms:Decrypt`
- To copy an encrypted snapshot that is shared from another AWS account, you must
  have permissions to use customer managed key that was used to encrypt that snapshot. For more
  information, see [Share the KMS key used to encrypt a shared Amazon EBS snapshot](share-kms-key.md "share-kms-key.md").

###### Encryption outcomes for snapshot copies

The following table describes the encryption outcomes when copying snapshots that
you own and snapshots that are shared with you.

| Encryption by default for destination Region | Source snapshot | Snapshot copy encryption outcome | Note                                                                                                                                                                          |
| -------------------------------------------- | --------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disabled                                     | Unencrypted     | Optional encryption              | If you encrypt the copy, you can specify the KMS key to use. If you encrypt<br>the copy but do not specify a KMS key, the key specified for encryption by default<br>is used. |
| Disabled                                     | Encrypted       | Automatically encrypted          | You can specify the KMS key to use. If you do not specify a KMS key, the<br>AWS managed key (`aws/ebs`) is used.                                                              |
| Enabled                                      | Unencrypted     | Automatically encrypted          | You can specify the KMS key to use. If you do not specify a KMS key, the key<br>specified for encryption by default is used.                                                  |
| Enabled                                      | Encrypted       | Automatically encrypted          | You can specify the KMS key to use. If you do not specify a KMS key, the key<br>specified for encryption by default is used.                                                  |

## Copy a snapshot

You can copy snapshots from one Region to another. You can copy an unencrypted snapshot
to an encrypted snapshot. However, if you attempt to copy an encrypted snapshot without
having permissions to use the encryption key, the operation fails silently and the snapshot
copy receives the "Given key ID is not accessible" status message.

Console

###### To copy a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot to copy, and then choose **Actions**,
   **Copy snapshot**.
4. For **Description**, enter a brief description for the
   snapshot copy.

By default, the description includes information about the source snapshot
so that you can identify a copy from the original. 5. Specify the destination for the snapshot copy.

    * To copy the snapshot to the same Region or to a different Region, select
     **AWS Region** and then select the destination Region.
    * To copy the snapshot to a Local Zone, select **AWS Local Zone**
     and then select the destination Local Zone.
    * (*Outpost customers only*) To copy the snapshot to an
     Outpost, select **AWS Outpost** and then enter the ARN of
     the destination Outpost.

6. If you need the snapshot copy to be completed within a specific timeframe, select
   **Enable time-based copy**. For **Completion duration**,
   enter the required completion duration, in 15-minute increments. For more information,
   [Time-based copies for Amazon EBS snapshots and EBS-backed AMIs](time-based-copies.md "time-based-copies.md").

If you do not need the snapshot copy to be completed in a specific timeframe, do
not enable time-based copy. In this case, the snapshot copy is completed on a best-effort
basis. 7. (_Outpost customers only_) To create the snapshot copy
on an Outpost in the selected Region, for **Snapshot destination**
choose **AWS Outpost**, and then for **Destination Outpost
ARN**, enter the ARN of the Outpost to which to copy the snapshot. The
**Snapshot destination** field appears only if you have and Outpost
in the selected Region. 8. Specify the encryption status for the snapshot copy.

If the source snapshot is encrypted, or if your account is enabled for [encryption by default](encryption-by-default.md "encryption-by-default.md"), the snapshot
copy is automatically encrypted. If the source snapshot is unencrypted and
your account is not enabled for encryption by default, encryption is optional. 9. Choose **Copy snapshot**.

AWS CLI

###### To copy a snapshot to another Region

Use the [copy-snapshot](../../../cli/latest/reference/ec2/copy-snapshot.md "../../../cli/latest/reference/ec2/copy-snapshot.md")
command. The following example copies the specified snapshot from the source
Region to the current Region, which is specified by the `--region` option.

```
aws ec2 copy-snapshot \
    --source-snapshot-id `snap-0abcdef1234567890` \
    --source-region `us-east-1` \
    --region `us-west-2`
```

###### To copy an unencrypted snapshot to an encrypted snapshot

Use the [copy-snapshot](../../../cli/latest/reference/ec2/copy-snapshot.md "../../../cli/latest/reference/ec2/copy-snapshot.md")
command. The following example copies the specified unencrypted snapshot from the
source Region to the current Region, encrypting the new snapshot using the
specified KMS key.

```
aws ec2 copy-snapshot \
    --source-snapshot-id `snap-0abcdef1234567890` \
    --source-region `us-east-1` \
    --encrypted \
    --kms-key-id `alias/my-kms-key`
```

PowerShell

###### To copy a snapshot to another Region

Use the [Copy-EC2Snapshot](../../../powershell/latest/reference/items/Copy-EC2Snapshot.md "../../../powershell/latest/reference/items/Copy-EC2Snapshot.md")
cmdlet. The following example copies the specified snapshot from the source Region
to the current Region, which is specified by the `--region` option.

```
 Copy-EC2Snapshot `
    -SourceSnapshotId `snap-0abcdef1234567890` `
    -SourceRegion `us-east-1` `
    -Region `us-west-2`
```

###### To copy an unencrypted snapshot to an encrypted snapshot

Use the [Copy-EC2Snapshot](../../../powershell/latest/reference/items/Copy-EC2Snapshot.md "../../../powershell/latest/reference/items/Copy-EC2Snapshot.md") cmdlet. The following example copies the specified
unencrypted snapshot from the source Region to the current Region, encrypting the
new snapshot using the specified KMS key.

```
 Copy-EC2Snapshot `
    -SourceSnapshotId `snap-0abcdef1234567890` `
    -SourceRegion `us-east-1` `
    -Encrypted $true `
    -KmsKeyId `alias/my-kms-key`
```

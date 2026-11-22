

# Associated KMS keys

An *associated KMS key* is an additional customer managed KMS key that you associate with an encrypted snapshot. A principal with access to the associated KMS key can access the snapshot's data for cross-account sharing and copying, without being granted access to the existing KMS key that encrypts the snapshot. The associated KMS key does not replace or change the existing KMS key that encrypts the snapshot, it does not grant access to that key, and associating it does not re-encrypt the snapshot's data.

When an Amazon EBS snapshot is encrypted, it's protected by a single AWS KMS key, and only those with access to that key can access the snapshot's data or copy the snapshot to another account. If the snapshot is encrypted under an AWS managed key, you can't share it with or copy it to another account, because an AWS managed key's key policy can't be modified to grant access to another account.

Associated KMS keys help you share an encrypted snapshot with another AWS account without granting access to the existing KMS key that encrypts the snapshot — for example, for cross-account backup, disaster recovery, or compliance. You can associate a KMS key that you also share with the other account, and the other account can then copy the snapshot using the associated KMS key. This also enables you to share snapshots encrypted with an AWS managed key, which otherwise can't be shared across accounts.

To use an associated KMS key across accounts, both of the following must be true:
+ The associated KMS key's key policy must allow the other account's principal to use the key.
+ That principal's IAM policy in their own account must allow them to use the associated KMS key.

Granting one without the other is not sufficient. For more information, see [How AWS KMS evaluates access to a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

## Associate or disassociate a KMS key
<a name="associate-disassociate-kms-key"></a>

You can associate a customer managed key with an encrypted snapshot, disassociate a KMS key from a snapshot, or view the KMS keys associated with a snapshot, using one of the following methods.

------
#### [ Console ]

**To associate a KMS key with a snapshot**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Snapshots**.

1. Select the snapshot, and then choose **Actions**, **Snapshot settings**, **Manage associated KMS keys**.

1. Specify a customer managed key, and then choose **Add**.

**To disassociate a KMS key from a snapshot**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Snapshots**.

1. Select the snapshot, and then choose **Actions**, **Snapshot settings**, **Manage associated KMS keys**.

1. Next to the associated KMS key ARN, choose **Disassociate**.

------
#### [ AWS CLI ]

**To associate a KMS key with a snapshot**  
Use the [associate-kms-key-id](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-kms-key-id.html) command. The following example associates a customer managed key with a snapshot.

```bash
aws ec2 associate-kms-key-id \
    --snapshot-id {{snap-1234567890abcdef0}} \
    --kms-key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}
```

**To disassociate a KMS key from a snapshot**  
Use the [disassociate-kms-key-id](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-kms-key-id.html) command. The following example disassociates a KMS key from a snapshot.

```bash
aws ec2 disassociate-kms-key-id \
    --snapshot-id {{snap-1234567890abcdef0}} \
    --kms-key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}
```

**To view the KMS keys associated with a snapshot**  
Use the [describe-snapshots](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-snapshots.html) command and check the `AssociatedKmsKeys` field. The following example describes a snapshot.

```bash
aws ec2 describe-snapshots \
    --filters Name=snapshot-id,Values={{snap-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To associate a KMS key with a snapshot**  
Use the [Register-EC2KmsKeyId](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-EC2KmsKeyId.html) cmdlet. The following example associates a customer managed key with a snapshot.

```powershell
Register-EC2KmsKeyId `
    -SnapshotId {{snap-1234567890abcdef0}} `
    -KmsKeyId {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}
```

**To disassociate a KMS key from a snapshot**  
Use the [Unregister-EC2KmsKeyId](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-EC2KmsKeyId.html) cmdlet. The following example disassociates a KMS key from a snapshot.

```powershell
Unregister-EC2KmsKeyId `
    -SnapshotId {{snap-1234567890abcdef0}} `
    -KmsKeyId {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}
```

**To view the KMS keys associated with a snapshot**  
Use the [Get-EC2Snapshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Snapshot.html) cmdlet and check the `AssociatedKmsKeys` property. The following example describes a snapshot.

```powershell
Get-EC2Snapshot `
    -SnapshotId {{snap-1234567890abcdef0}}
```

------

## Considerations
<a name="associated-kms-keys-considerations"></a>
+ You can associate a KMS key only with an encrypted snapshot.
+ The associated KMS key must be a customer managed key. You can't associate an AWS managed key.
+ You can't associate a KMS key that the snapshot already uses, whether it's the existing KMS key that encrypts the snapshot or a KMS key that's already associated with the snapshot.
+ You can't associate a KMS key with a snapshot in the Archive tier.
+ To create a volume from an encrypted snapshot, you must have access to the existing KMS key that encrypts the snapshot.
+ You can associate a KMS key with Local snapshots and regional snapshots in Local Zones, and with Amazon EBS Local snapshots on Outposts.

## Permissions
<a name="associated-kms-keys-permissions"></a>

To associate or disassociate a KMS key, you need the `ec2:AssociateKmsKeyId` and `ec2:DisassociateKmsKeyId` IAM permissions, plus the AWS KMS permissions that Amazon EBS requires to use a KMS key. For the full set of required AWS KMS permissions, see [Requirements for Amazon EBS encryption](ebs-encryption-requirements.md).

## Troubleshooting
<a name="associated-kms-keys-troubleshooting"></a>

If an associate, disassociate, or copy request fails with an authorization error, the error identifies the KMS key or keys that you're not authorized to use. Make sure you have permission to use that key — both the key's policy and your IAM policy must allow it. To see which KMS key a request used, review your [CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).
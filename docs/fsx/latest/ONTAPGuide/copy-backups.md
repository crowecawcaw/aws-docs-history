# Copying backups

With Amazon FSx, you can manually copy volume backups to another AWS Region (cross-Region copies)
or within the same AWS Region (in-Region copies). Both copy types operate within the same AWS
account. You can make cross-Region copies only within the same AWS partition. You can create user-initiated backup copies using the
Amazon FSx console, AWS CLI, or API. When you create a user-initiated backup copy, it has the type
`USER_INITIATED`.

You can also use AWS Backup to copy backups across AWS Regions and across AWS accounts.
With AWS Backup, a fully managed backup management service, you can manage policy-based backup plans
from a central interface. With its cross-account management, you can use
backup policies to apply backup plans across the accounts within your organization.

## Cross-Region backup copies

Cross-Region backup copies are particularly valuable for cross-Region disaster recovery.
You take backups and copy them to another AWS Region. Then, if a disaster affects the primary
AWS Region, you can restore from backup and quickly recover availability in the other Region. You
can also use backup copies to clone a volume's data to another AWS Region or within the same AWS
Region. You make backup copies within the same AWS account (cross-Region or in-Region) by using
the Amazon FSx console, AWS CLI, or Amazon FSx API. You can also use [AWS Backup](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md") to perform backup copies,
either on-demand or policy-based.

## Cross-account backup copies

Use cross-account backup copies to meet regulatory compliance requirements and copy backups to
an isolated account. They also provide an additional layer of data protection. This helps prevent
accidental or malicious deletion of backups, loss of credentials, or compromise of AWS KMS keys.
Cross-account backups support two patterns. With _fan-in_, you copy
backups from multiple primary accounts to one isolated account. With _fan-out_, you copy backups from one primary account to multiple isolated
accounts.

You can make cross-account backup copies by using AWS Backup with AWS Organizations support. Account
boundaries for cross-account copies are defined by AWS Organizations policies. For more information about
using AWS Backup to make cross-account backup copies, see [Creating backup copies across
AWS accounts](../../../aws-backup/latest/devguide/create-cross-account-backup.md "../../../aws-backup/latest/devguide/create-cross-account-backup.md") in the _AWS Backup Developer Guide_.

## Backup copy limitations

The following are some limitations when you copy backups:

- Cross-Region backup copies are supported only between any two commercial AWS Regions,
  between the China (Beijing) and China (Ningxia) Regions, and between the
  AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, but not across those sets
  of Regions.
- You can make in-Region backup copies within any AWS Region.
- The source backup must have a status of `AVAILABLE` before you can copy it.
- You cannot delete a source backup if it is being copied. There might be a short delay
  between when the destination backup becomes available and when you are allowed to delete
  the source backup. You should keep this delay in mind if you retry deleting a source backup.
- You can have up to five backup copy requests in progress for a single volume to a single
  destination AWS Region and AWS KMS key.
- You can have up to 1,000 backup copy requests in progress per account. If you exceed this limit,
  Amazon FSx rejects the request; retry the copy after one or more of your in-progress copies complete.
- Amazon FSx doesn't support copying backups of FlexGroup volumes.
- Cross-account backup copies aren't supported in the China (Beijing) or China (Ningxia) Regions.

## Permissions for cross-Region backup copies

You use an IAM policy statement to grant permissions to perform a backup copy operation.
To request a cross-Region backup copy, the requester must communicate with the source AWS Region.
The requester (IAM role or IAM user) must have access to the source backup and
the source AWS Region.

You use the policy to grant permissions to the `CopyBackup` action
for the backup copy operation. You specify the action in the policy's `Action` field,
and you specify the resource value in the policy's `Resource` field, as in the
following example.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "fsx:CopyBackup",
            "Resource": "arn:aws:fsx:*:111122223333:backup/*"
        }
    ]
}
```

For more information about IAM policies, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_.

## Full and incremental copies

When you copy a backup to a different AWS Region from the source backup, the first copy is
always a full backup copy. This is the case even if you use the same AWS KMS key to encrypt both the
source and destination copies of the backup. After the first copy, all subsequent backup copies to
the same destination Region within the same AWS account are incremental. This applies as long as
you haven't deleted all previously-copied backups in that Region and have been using the same
AWS KMS key. If both conditions aren't met, the copy operation results in a full (not incremental)
backup copy.

To learn how to copy backups of your volumes, see
[Copying backups within the same AWS account](copying-backups-same-account.md "copying-backups-same-account.md").

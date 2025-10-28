# Copying backups

You can use Amazon FSx to manually copy backups within the same AWS account to another AWS Region
(cross-Region copies) or within the same AWS Region (in-Region copies). You can make cross-Region
copies only within the same AWS partition. You can create user-initiated backup copies using the
Amazon FSx console, AWS CLI, or API. When you create a user-initiated backup copy, it has the type
`USER_INITIATED`.

You can also use AWS Backup to copy backups across AWS Regions and across AWS accounts.
AWS Backup is a fully managed backup management service that provides a central interface for
policy-based backup plans. With its cross-account management, you can automatically use
backup policies to apply backup plans across the accounts within your organization.

_Cross-Region backup copies_ are particularly valuable for
cross-Region disaster recovery. You take backups and copy them to another AWS Region so
that in the event of a disaster in the primary AWS Region, you can restore from backup and recover
availability quickly in the other AWS Region. You can also use backup copies to clone your file
dataset to another AWS Region or within the same AWS Region. You make backup copies within the same AWS
account (cross-Region or in-Region) by using the Amazon FSx console, AWS CLI, or Amazon FSx for Lustre API. You can also
use [AWS Backup](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md") to perform backup copies, either on-demand or policy-based.

_Cross-account backup copies_ are valuable for meeting your
regulatory compliance requirements to copy backups to an isolated account. They also provide an
additional layer of data protection to help prevent accidental or malicious deletion of backups,
loss of credentials, or compromise of AWS KMS keys. Cross-account backups support _fan-in_ (copy backups from multiple primary accounts to one isolated
backup copy account) and _fan-out_ (copy backups from one
primary account to multiple isolated backup copy accounts).

You can make cross-account backup copies by using AWS Backup with AWS Organizations support. Account
boundaries for cross-account copies are defined by AWS Organizations policies. For more information about
using AWS Backup to make cross-account backup copies, see [Creating backup copies across AWS accounts](../../../aws-backup/latest/devguide/create-cross-account-backup.md "../../../aws-backup/latest/devguide/create-cross-account-backup.md") in the
_AWS Backup Developer Guide_.

## Backup copy limitations

The following are some limitations when you copy backups:

- Backups of file systems using the Intelligent-Tiering storage class do not support backup copies.
- Cross-Region backup copies are supported only between any two commercial AWS Regions,
  between the China (Beijing) and China (Ningxia) Regions, and between the
  AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, but not across those sets
  of Regions.
- Cross-Region backup copies are not supported in opt-in Regions.
- You can make in-Region backup copies within any AWS Region.
- The source backup must have a status of `AVAILABLE` before you can copy it.
- You cannot delete a source backup if it is being copied. There might be a short delay
  between when the destination backup becomes available and when you are allowed to delete
  the source backup. You should keep this delay in mind if you retry deleting a source backup.
- You can have up to five backup copy requests in progress to a single destination AWS Region
  per account.

## Permissions for cross-Region backup copies

You use an IAM policy statement to grant permissions to perform a backup copy operation.
To communicate with the source AWS Region to request a cross-Region backup copy,
the requester (IAM role or IAM user) must have access to the source backup and
the source AWS Region.

You use the policy to grant permissions to the `CopyBackup` action
for the backup copy operation. You specify the action in the policy's `Action` field,
and you specify the resource value in the policy's `Resource` field, as in the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fsx:CopyBackup",
 "Resource": "arn:aws:fsx:*:`111122223333`:backup/*"
 }
 ]
}`

```

For more information on IAM policies, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_.

## Full and incremental copies

When you copy a backup to a different AWS Region from the source backup,
the first copy is a full backup copy. After the first backup copy, all subsequent
backup copies to the same destination Region within the same AWS account are
incremental, provided that you haven't deleted all previously-copied backups in
that Region and have been using the same AWS KMS key. If both conditions aren't
met, the copy operation results in a full (not incremental) backup copy.

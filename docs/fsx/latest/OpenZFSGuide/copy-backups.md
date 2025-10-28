# Copying backups

You can use Amazon FSx to manually copy backups within the same AWS account to another AWS
Region (cross-Region copies) or within the same AWS Region (in-Region copies). You can make cross-Region
copies only within the same AWS partition. You can create user-initiated backup copies using the
Amazon FSx console, AWS CLI, or API. When you create a user-initiated backup copy, it has the type
`USER_INITIATED`.

_Cross-Region backup copies_ are particularly valuable for
cross-Region disaster recovery. You take backups and copy them to another AWS Region so
that in the event of a disaster in the primary AWS Region, you can restore from backup and recover
availability quickly in the other AWS Region. You can also use backup copies to clone your file
dataset to another AWS Region or within the same AWS Region. You make backup copies within the same AWS
account (cross-Region or in-Region) by using the Amazon FSx console, AWS CLI, or Amazon FSx API.

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
 "Resource": "arn:aws:fsx:*:111111111111:backup/*"
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

To copy a backup (Amazon FSx console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane, choose **Backups**.
3. In the **Backups** table, choose the backup that you want to copy, and
   then choose **Copy backup**.
4. In the **Settings** section, do the following:
   - In the **Destination Region** list, choose a destination AWS Region to copy the
     backup to. The destination can be in another AWS Region (cross-Region copy) or within the same
     AWS Region (in-Region copy).
   - (Optional) Select **Copy Tags** to copy tags from
     the source backup to the destination backup. If you select **Copy Tags**
     and also add tags at step 6, all the tags are merged.

5. For **Encryption**, choose the AWS KMS encryption key to encrypt the copied
   backup.
6. For **Tags - optional**, enter a key and value to add tags for your
   copied backup. If you add tags here and also selected **Copy Tags** at step
   4, all the tags are merged.
7. Choose **Copy backup**.

Your backup is copied within the same AWS account to the selected AWS Region.

To copy a backup (AWS CLI)

- Use the `copy-backup` CLI command or the [CopyBackup](../APIReference/API_CopyBackup.md "../APIReference/API_CopyBackup.md") API operation to copy a backup within the same AWS account,
  either across an AWS Region or within an AWS Region.

The following command copies a backup with an ID of `backup-0abc123456789cba7` from
the `us-east-1` Region.

```
aws fsx copy-backup \
  --source-backup-id backup-0abc123456789cba7 \
  --source-region us-east-1
```

The response shows the description of the copied backup.

You can view your backups on the Amazon FSx console or programmatically using the
`describe-backups` CLI command or the [DescribeBackups](../APIReference/API_DescribeBackups.md "../APIReference/API_DescribeBackups.md") API
operation.

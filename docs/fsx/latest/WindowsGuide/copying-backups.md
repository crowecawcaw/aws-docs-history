# Copying backups within the same account

You can use the AWS Management Console and AWS CLI to manually copy backups within the same AWS account to another AWS Region
(cross-Region copies) or within the same AWS Region (in-Region copies) using the following procedures.

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

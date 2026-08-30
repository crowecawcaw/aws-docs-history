# Copying backups within the same AWS account

You can copy volume backups on FSx for ONTAP file systems using the AWS Management Console, CLI, and API, as described in the following
procedures.

###### To copy a backup within the same account (cross-Region or in-Region) using the console

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

Your backup is copied within the same AWS account to the selected AWS Region. 8. You can monitor the progress of the operation using the `ProgressPercent` property in the
response of the `describe-backups` CLI command or the [DescribeBackups](../APIReference/API_DescribeBackups.md "../APIReference/API_DescribeBackups.md") API
operation.

###### To copy a backup within the same account (cross-Region or in-Region) using the CLI

- Use the `copy-backup` CLI command or the [CopyBackup](../APIReference/API_CopyBackup.md "../APIReference/API_CopyBackup.md") API operation to copy a backup within the same AWS account. You can copy the
  backup either across AWS Regions or within an AWS Region.

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

## Choosing between backup copies and NetApp SnapMirror

For cross-Region resilience, you can either copy backups to another AWS Region or use
NetApp SnapMirror to replicate data to a second FSx for ONTAP file system. Which
approach you choose depends on whether your primary goal is compliance or availability.

Copy backups to different AWS Regions or accounts if you have compliance requirements that
mandate storing offline copies of your data. These offline copies aren't immediately impacted by
security or availability incidents affecting the primary file system and its replicas. Backups are
logically separated from a file system, so your backup data remains secure and unaffected if your
file system is compromised. Copying backups within and across AWS Regions and accounts is the
simplest way to protect your data from these types of events. You don't need to provision and manage
secondary file systems or maintain a NetApp SnapMirror relationship.

Use NetApp SnapMirror to replicate data across FSx for ONTAP file systems for
cross-Region disaster recovery and improve the availability of your data. You can configure
replication with a Recovery Point Objective (RPO) as low as 5 minutes, compared to 60 minutes with
backups. You can also achieve a Recovery Time Objective (RTO) in single-digit minutes, compared to
minutes to hours with backups. The RTO for backups depends on the size of your backup. With
NetApp SnapMirror, you get the lowest recovery times in the event of a disaster
affecting the primary AWS Region. For more information, see [Replicating your data using NetApp SnapMirror](scheduled-replication.md "scheduled-replication.md").

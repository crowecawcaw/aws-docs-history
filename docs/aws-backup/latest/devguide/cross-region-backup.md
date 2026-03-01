# Creating backup copies across AWS Regions

Using AWS Backup, you can copy backups to multiple AWS Regions on demand or automatically
as part of a scheduled backup plan. Cross-Region replication is particularly valuable if you
have business continuity or compliance requirements to store backups a minimum distance away
from your production data. For a video tutorial, see [Managing cross-Region copies of
backups](https://www.youtube.com/watch?v=qMN18Lpj3PE "https://www.youtube.com/watch?v=qMN18Lpj3PE").

When you copy a backup to a new AWS Region for the first time, AWS Backup copies the backup
in full. In general, if a service supports incremental backups, subsequent copies of that
backup in the same AWS Region will be incremental. AWS Backup will re-encrypt your copy using
the customer managed key of your destination vault.

An exception is Amazon EBS, where changing the encryption status of a snapshot during a copy
operation [results in
a full (not incremental) copy](../../../ebs/latest/userguide/ebs-copy-snapshot.md#creating-encrypted-snapshots "../../../ebs/latest/userguide/ebs-copy-snapshot.md#creating-encrypted-snapshots").

###### Requirements

- Most AWS Backup-supported resources support cross-Region backup. For specifics, see [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").
- Most AWS Regions support cross-Region backup. For specifics, see [Feature availability by AWS Region](backup-feature-availability.md#features-by-region "backup-feature-availability.md#features-by-region").
- AWS Backup does not support cross-Region copies for storage in cold tiers.

## Cross-Region copy encryption

See [Encryption for a backup copy to a
different account or AWS Region](encryption.md#copy-encryption "encryption.md#copy-encryption") for details on how encryption works for copy
jobs.

## Cross-Region copy considerations with specific resources

###### Amazon RDS

AWS Backup does not pass the option group when you perform a cross-Region copy. Your target Region must have the same option group as the source Region for the cross-Region copy to succeed.

You can [copy an option group](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy"). For more information, see the _Amazon Relational Database Service User Guide_.

If you attempt a cross-Region copy without the same option group in your target Region, the copy job fails with an error message such as "The snapshot requires a target option group with the following options: ...."

## Performing on-demand cross-Region backup

###### To copy an existing backup on-demand

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Choose **Backup vaults**.
3. Choose the vault that contains the recovery point you want to copy.
4. In the **Backups** section, select a recovery point to
   copy.
5. Using the **Actions** dropdown button, choose
   **Copy**.
6. Enter the following values:

**Copy to destination**

Choose the destination AWS Region for the copy. You can add a new copy
rule per copy to a new destination.

**Destination Backup vault**

Choose the destination backup vault for the copy.

**Transition to cold storage**

Choose when to transition the backup copy to cold storage. Backups
transitioned to cold storage must be stored there for a minimum of 90 days. This
value cannot be changed after a copy has transitioned to cold storage.

To see the list of resources that you can transition to cold storage, see
the "Lifecycle to cold storage" section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table.
The cold storage expression is ignored for other resources.

**Retention period**

Choose specifies the number of days after creation that the copy is deleted.
This value must be greater than 90 days beyond the **Transition to cold
storage** value.

**IAM role**

Choose the IAM role that AWS Backup will use when creating the copy. The role
must also have AWS Backup listed as a trusted entity, which enables AWS Backup to assume
the role. If you choose **Default** and the AWS Backup default role
is not present in your account, one will be created for you with the correct
permissions. 7. Choose **Copy**.

## Scheduling cross-Region backup

You can use a scheduled backup plan to copy backups across AWS Regions.

###### To copy a backup using a scheduled backup plan

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In **My account**, choose **Backup plans**, and
   then choose **Create Backup plan**.
3. On the **Create Backup plan** page, choose **Build a new
   plan**.
4. For **Backup plan name**, enter a name for your backup
   plan.
5. In the **Backup rule configuration** section, add a backup rule
   that defines a backup schedule, backup window, and lifecycle rules. You can add more
   backup rules later.
   1. For **Backup rule name**, enter a name for your rule.
   2. For **Backup vault**, choose a vault from the list. Recovery
      points for this backup will be saved in this vault. You can create a new backup
      vault.
   3. For **Backup frequency**, choose how often you want to take
      backups.
   4. For services that support PITR, if you want this feature, choose
      **Enable continuous backups for point-in-time recovery
      (PITR)**. For a list a services that support PITR, see that section of
      the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource")
      table.
   5. For **Backup window**, choose **Use backup window
      defaults - _recommended_**. You can customize the
      backup window.
   6. For **Copy to destination**, Choose the destination
      AWS Region for your backup copy. Your backup will be copied to this Region. You
      can add a new copy rule per copy to a new destination. Then enter the following
      values:

   **Copy to another account's vault**

   Do not toggle this option. To learn more about cross-account copy, see
   [Creating
   backup copies across AWS accounts](create-cross-account-backup.md "create-cross-account-backup.md")

   **Destination Backup vault**

   Choose the backup vault in the destination Region where AWS Backup will copy
   your backup.

   If you would like to create a new backup vault for cross-Region copy,
   choose **Create new Backup vault**. Enter the information
   in the wizard. Then choose **Create Backup vault**.

6. Choose **Create plan**.

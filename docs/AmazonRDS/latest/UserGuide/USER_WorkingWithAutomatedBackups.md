

# Introduction to backups
<a name="USER_WorkingWithAutomatedBackups"></a>

Amazon RDS creates and saves automated backups of your DB instance or Multi-AZ DB cluster during the backup window of your DB instance. RDS creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases. RDS saves the automated backups of your DB instance according to the backup retention period that you specify. If necessary, you can recover your DB instance to any point in time during the backup retention period.

Automated backups follow these rules:
+ Your DB instance must be in the `available` state for automated backups to occur. Automated backups don't occur while your DB instance is in a state other than `available`, for example, `storage_full`.
+ Automated backups don't occur while a DB snapshot copy is running in the same AWS Region for the same database.

You can also back up your DB instance manually by creating a DB snapshot. For more information about manually creating a DB snapshot, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md). 

Snapshot and backup functionality supports multi-volume configurations. All backup operations include both the primary volume and any additional storage volumes. Snapshots capture the entire database storage configuration. Point-in-time recovery (PITR) works across all storage volumes.

The first snapshot of a DB instance contains the data for the full database. Subsequent snapshots of the same database are incremental, which means that only the data that has changed after your most recent snapshot is saved.

You can copy both automatic and manual DB snapshots, and share manual DB snapshots. For more information about copying a DB snapshot, see [Copying a DB snapshot for Amazon RDS](USER_CopySnapshot.md). For more information about sharing a DB snapshot, see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md).

## Backup storage
<a name="USER_WorkingWithAutomatedBackups.BackupStorage"></a>

Your Amazon RDS backup storage for each AWS Region is composed of the automated backups and manual DB snapshots for that Region. Total backup storage space equals the sum of the storage for all backups in that Region. Moving a DB snapshot to another Region increases the backup storage in the destination Region. Backups are stored in Amazon S3.

For more information about backup storage costs, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/). 

If you choose to retain automated backups when you delete a DB instance, the automated backups are saved for the full retention period. If you don't choose **Retain automated backups** when you delete a DB instance, all automated backups are deleted with the DB instance. However, DB snapshots (both final and manual) are independent of automated backups and are not affected by this deletion. If you choose to have Amazon RDS create a final DB snapshot before it deletes your DB instance, you can use that to recover your DB instance. Optionally, you can use a previously created manual snapshot. Manual snapshots are not deleted when an instance is deleted. You can have up to 100 manual snapshots per Region.

If you share a snapshot with another user, you remain the owner of that snapshot and its storage costs apply to you. To keep access to a snapshot that someone else shares with you, copy it; the storage costs for the copy then apply to your account. For more information, see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md) and [Copying a DB snapshot for Amazon RDS](USER_CopySnapshot.md).

### Free backup storage allowance
<a name="USER_WorkingWithAutomatedBackups.BackupStorage.FreeAllowance"></a>

Amazon RDS provides a free amount of backup storage equal to 100 percent of the total provisioned database storage in your AWS account for each Region. You receive this free allowance for DB snapshots and DB cluster snapshots.

The free allowance is applied as a percentage discount across all of your snapshots in that AWS account and Region, rather than subtracted from any single snapshot as a static value. Amazon RDS divides your free allowance by your total snapshot storage to determine the percentage of usage that is free, and then applies that same percentage discount to each snapshot.

For example, suppose that your total provisioned database storage is 100 GB, so your free allowance is 100 GB. Suppose also that you have two snapshots: snapshot A is 50 GB and snapshot B is 75 GB, for 125 GB of total snapshot storage. Your free allowance covers 100 of the 125 GB, or 80 percent of your snapshot storage. So Amazon RDS applies an 80 percent discount to each snapshot, and you are billed for the remaining 20 percent of each one:

```
Free percentage   = 100 GB (free allowance) / 125 GB (total snapshot storage) = 80%

Snapshot A billed = 50 GB * (1 - 0.80) = 10 GB
Snapshot B billed = 75 GB * (1 - 0.80) = 15 GB

Total billed      = 10 GB + 15 GB = 25 GB
```

Your total billed backup storage (25 GB) is the same as the total provisioned storage subtracted from your total snapshot storage (125 GB – 100 GB = 25 GB). The charges are attributed to each snapshot individually, and each snapshot receives a consistent percentage discount.

### How snapshot storage charges appear in Cost Explorer and the AWS Cost and Usage Report
<a name="USER_WorkingWithAutomatedBackups.BackupStorage.Attribution"></a>

Snapshot storage charges appear at the individual snapshot level in AWS Cost Explorer and in your AWS Cost and Usage Report (CUR). In the `ResourceId` field of your CUR, each DB snapshot shows its Amazon RDS snapshot ARN and each DB cluster snapshot shows its Amazon RDS cluster snapshot ARN. Each snapshot appears as its own line item. Your snapshot pricing and overall charges remain the same; only how the charges are attributed and presented changes.

Charges for snapshots whose source DB instance or Multi-AZ DB cluster has been deleted are attributed to the Amazon RDS snapshot or cluster snapshot ARN that incurs them. There are no line items with a blank `ResourceId`. Charges for cross-AWS Region or cross-account snapshots are attributed to the snapshot ARN in the destination account or Region.

**Important**  
Any rule that attributes snapshot charges by matching a DB instance ARN in the `ResourceId` field no longer matches those charges. This includes AWS Cost Categories, AWS Budgets filters, and chargeback jobs that read the `ResourceId` field of your CUR. Update those rules to match Amazon RDS snapshot ARNs, or apply cost allocation tags to your snapshots.

### Viewing a per-instance breakdown of snapshot charges
<a name="USER_WorkingWithAutomatedBackups.BackupStorage.PerInstance"></a>

Because snapshot storage charges are attributed to each snapshot rather than to a DB instance, you can use cost allocation tags to group snapshot charges by instance. For example, you can add a tag to each snapshot with the name of its source DB instance so that you can search for it in the CUR. Cost allocation tags work on a snapshot even after its source DB instance is deleted.

Because the free allowance is applied as a percentage discount across all of your snapshots, the per-instance totals in a tag-based breakdown don't match the per-instance totals that you saw before snapshot charges were attributed per snapshot, even though the overall charges in your AWS account and Region are unchanged. For more information about using cost allocation tags with snapshots, see [How cost allocation tags work with DB snapshots](USER_Tagging.md#Tagging.Billing.Snapshots) and [Copying tags to DB snapshots](USER_Tagging.md#USER_Tagging.CopyTags).
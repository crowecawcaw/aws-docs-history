

# Metering, costs, and billing for AWS Backup

## AWS Backup pricing
<a name="pricing"></a>

Current AWS Backup prices are available at [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**Important**  
To avoid additional charges, configure your retention policy with a warm storage duration of **at least one week**.  
For example, assume you take daily backups and retain them for one day. Further, assume that your protected resources are so large it takes the entire day to complete your backup. AWS Backup implements your retention period of one day and removes your backup from warm storage when your backup job completes. The next day, AWS Backup cannot create an incremental backup because you have no backup in warm storage. Since this retention period did not follow best practices, you run the risk and expense of creating a full backup every day.  
Contact AWS Support for further assistance.

## AWS Backup billing
<a name="metering"></a>

When a resource type supports full AWS Backup management, charges for AWS Backup activity (including storage, data transfers, restores, and early deletion) appear in the "Backup" section of your Amazon Web Services bill. For a list of services that support full AWS Backup management, see the Full AWS Backup management section in the [Feature availability by resource](backup-feature-availability.md#features-by-resource) table.

When a resource type does not support full AWS Backup management, some of your AWS Backup activity such as storage costs for your backups, have billing reflected by the respective AWS service. However, if you are using a [Logically air-gapped vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html#lag-compare-and-contrast), all storage or data transfer charges occur under AWS Backup.

**Copy Jobs**

You will only be charged once a recovery point has been created in the destination vault. There is no charge when a copy job fails and no recovery point is created.

When you configure cross account and cross Region copies, you will see the following billing depending on which resources you copy. For fully managed resources, the source account will see the data transfer charges, and for non fully managed resources, the destination account will see the data transfer charges.

## Cost allocation tags
<a name="cost-allocation-tags"></a>

You can use cost allocation tags to track and optimize AWS Backup costs on a detailed level, and view and filter those tags using AWS Cost Explorer.

To use cost allocation tags, see [Automating backups and optimizing backup costs for Amazon EFS using AWS Backup](https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/) and [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

## AWS Backup Audit Manager pricing
<a name="bam-cost"></a>

AWS Backup Audit Manager charges for usage based on the number of control evaluations. A control evaluation is the evaluation of one resource against one control. Control evaluation charges appear on your AWS Backup bill. For current control evaluation pricing, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

To use AWS Backup Audit Manager controls, you must enable AWS Config recording to track your backup activity. AWS Config charges for each configuration item recorded, and these charges appear on your AWS Config bill. For current configuration item recorded pricing, see [AWS Config pricing](https://aws.amazon.com/config/pricing/).

## Amazon Aurora pricing
<a name="aurora-billing"></a>

During the configured retention period for Aurora continuous backups (up to 35 days), snapshots do not incur a storage charge. Snapshots retained past this window are charged as full backups.

## Billing and cost FAQ
<a name="billing-cost-faq"></a>

Use the following questions and answers to understand AWS Backup billing behavior.

**Where do AWS Backup charges appear on my bill?**

For resources that AWS Backup fully manages, your backup activity is billed under AWS Backup. For resources that are not fully managed by AWS Backup, some charges, especially backup storage, appear under the protected service instead. For example, backup storage for some Amazon EC2 and Amazon RDS resources can appear under those services. Storage and data transfer for logically air-gapped vaults always appear under AWS Backup. To confirm how a resource is billed, check whether it has full AWS Backup management in the feature availability table. For more information about where charges appear, see [Feature availability](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html).

**How can I see my AWS Backup cost by vault, plan, or protected resource?**

Use cost allocation tags together with a Cost and Usage Report (CUR) that includes resource IDs. Add cost allocation tags to your recovery points where the resource supports them, activate those tags in the Billing console, enable resource IDs in your CUR, and then join the recovery point identifiers in the CUR with your AWS Backup metadata. Cross-account monitoring shows job activity, not cost. For more information about tracking cost by vault, plan, or resource, see [Tagging AWS Backup resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/tags-on-backups.html) and [Cost allocation for centralized backups](https://aws.amazon.com/blogs/storage/cost-allocation-and-tracking-for-aws-centralized-backups/).

**Which account pays for a cross-account or cross-Region backup copy?**

A same-Region copy has no cross-Region data transfer charge. For a cross-account, cross-Region copy, the account that is charged for data transfer depends on how the resource is managed. For resources with full AWS Backup management the source account is charged, and for resources without full AWS Backup management the destination account is charged. In all cases, the account that receives the copied recovery point pays to store it. Data transfer charges apply only when data leaves an AWS Region. To confirm which account was charged, check the data transfer line item in your bill. For more information about which account is charged, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**What determines how much backup storage I'm billed for?**

Your bill reflects all retained backup data, not just the data that changed today. Depending on the resource and backup type, the amount you are billed for can include the following:
+ The initial full backup
+ Unique changes retained by later recovery points
+ Older data that a recovery point still needs
+ Copies in other vaults, accounts, or Regions
+ Resource-specific minimum billable sizes
+ The requests and events the backup process uses
+ A retention period shorter than your backup interval, which can make each backup a full backup instead of an incremental backup

Not every recovery point is a full copy, and not every backup type is incremental. Check the storage model documented for your specific resource and backup type. For more information about backup storage billing, see [Incremental backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#incremental-backups) and [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**What happens to backup charges when I delete source data, a resource, or a backup plan?**

Deleting source data, removing a resource, or deleting a backup plan does not delete your existing recovery points. Those recovery points keep using storage until their retention period ends, until you delete them, or, for a copy, until the copy reaches the end of its own retention period. Check every relevant vault, Region, and account, including automatic service vaults and copy destinations. Before you delete a recovery point, confirm that you no longer need it and that it meets your retention, compliance, restore, and dependency requirements. For more information about deleting backup plans and recovery points, see [Deleting a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-a-backup-plan.html) and [Deleting recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html).

**What can change my AWS Backup costs if my backup plan stays the same?**

Cost can change without any plan change because your usage, selected resources, retention, copies, or restores can change. Common causes include the following:
+ More protected data or a higher change rate
+ New resources matching a tag-based assignment
+ More retained recovery points
+ New copies or destinations
+ A restore testing plan matching a new recovery point
+ More Amazon S3 requests from schedule frequency or object count

Start from the first date you saw the change and compare it against resource growth, jobs, copies, restores, selection tags, and retention. For more information about cost changes, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**How are recovery points in a vault locked in compliance mode billed?**

Existing recovery points continue to be billed until their retention periods end, and stopping new backups does not change that. With AWS Backup Vault Lock in compliance mode, you can still change or remove the lock during the grace time, which you set and which must be at least 3 days (72 hours). After the grace time expires, neither you nor AWS can change or delete the vault or its lock. AWS Backup denies any attempt to delete a backup or change its lifecycle, so recovery points remain billable until their lifecycle completes. Review your Vault Lock settings carefully during the grace time. For more information about Vault Lock billing, see [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html).

**Does switching from native Amazon RDS or Amazon Aurora backups to AWS Backup change the storage price?**

AWS Backup uses the native Amazon RDS and Amazon Aurora backup systems, so this storage is billed under Amazon RDS rather than at a separate AWS Backup storage rate. The models differ by engine. Standard Amazon RDS automated backups and manual snapshots share the applicable per-account, per-Region free allocation. Aurora automated backups are incremental, with a free amount based on your latest cluster volume size. Aurora manual snapshots, including periodic snapshots that AWS Backup creates, are full snapshots. Aurora snapshots, including those AWS Backup creates, are free within the Aurora automated backup retention period and are billed at full size after that period. Calculate standard Amazon RDS and Aurora costs separately. For more information about Amazon RDS and Aurora backup pricing, see [Amazon RDS backups with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/rds-backup.html) and [Aurora backup storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-storage-backup.html).

**Does Amazon EBS snapshot storage reset each month?**

No. Standard-tier Amazon EBS snapshots stay incremental across calendar months. A GB-month is a billing measurement, not a sign that AWS creates a new full snapshot each month. If many or all previously written blocks change, a later snapshot can add roughly that amount of new data while older snapshots keep the previous blocks. Snapshot Archive works differently: archiving converts the selected snapshot to a full archived snapshot, the archive tier has a minimum retention period, and you must restore the snapshot to the standard tier before you use it. For more information about Amazon EBS snapshot billing, see [How Amazon EBS snapshots work](https://docs.aws.amazon.com/ebs/latest/userguide/how_snapshots_work.html) and [Snapshot Archive pricing](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive-pricing.html).

**How are Amazon EFS backups billed after I delete files?**

Amazon EFS backup is incremental, and your existing recovery points keep deleted file data until those recovery points expire or you delete them. Removing a file from the live file system does not remove that file's data from recovery points that already exist. Check the recovery points for the file system, the reserved automatic Amazon EFS backup vault, any custom vaults, your copy destinations, and your retention and lifecycle settings. If the console looks empty, confirm you are viewing the correct Region and vault. For more information about Amazon EFS backup billing, see [Amazon EFS and AWS Backup](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html) and [Listing recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/listing-backups.html).

**What is included in Amazon S3 backup storage charges?**

Amazon S3 backup storage can include data that your current bucket size does not reflect. This storage can include the following:
+ Current and noncurrent object versions retained in recovery points
+ Delete markers
+ The documented 128 KiB minimum billable size for smaller objects and delete markers
+ Copies or snapshots that still reference older data

When continuous and periodic backups of the same bucket are in the same vault, AWS Backup takes periodic snapshots from the continuous recovery point, so it does not need to scan the bucket. For more information about Amazon S3 backup storage charges, see [Amazon S3 backups with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) and [AWS Backup pricing](https://aws.amazon.com/backup/pricing/). Periodic backups also incur Amazon S3 GET and LIST request charges and Amazon EventBridge event charges, which appear under those services.

**Will point-in-time recovery cost less if I run scheduled backups less often?**

No. Running periodic backups less often does not reduce the continuous capture that point-in-time recovery (PITR) performs. Changing periodic backups from daily to monthly can lower periodic jobs or requests, but PITR keeps capturing changes on its own schedule. PITR cost depends on the protected resource's billing model, its data size or change volume, and your retention period. For more information about point-in-time recovery cost, see [Point-in-time recovery](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html) and [Restore a continuous backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-restoring.html).

**What charges can restore testing create?**

Restore testing can create several kinds of charges:
+ An evaluation charge for each recovery point that AWS Backup successfully orchestrates for restore through a restore testing plan
+ Resource-specific restore or storage charges
+ Charges for any restored resource you keep after the restore completes (the amount depends on the resource type and how long you keep it)
+ Additional service requests such as Amazon S3 PUT requests where applicable

An existing restore testing plan can start charging when a new recovery point matches its vault, resource type, selection window, and schedule, without any edit to the plan. Evaluation prices vary by Region, so check current pricing. For more information about restore testing charges, see [Restore testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) and [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**What additional charges apply to logically air-gapped vaults?**

A logically air-gapped vault can create destination storage charges and, for cross-Region copies, data transfer charges. Logically air-gapped vault storage is billed at resource-specific and Region-specific rates, and the backup storage free tiers for Amazon EBS, Amazon DocumentDB, and Amazon Neptune do not apply to storage in a logically air-gapped vault. For a copy, the same cross-account and cross-Region rule applies: for a fully managed resource the source account is charged, and for a resource that is not fully managed the destination account is charged. The account that receives the copy pays to store it. Data transfer rates are the same for backup vaults and logically air-gapped vaults. For more information about logically air-gapped vault charges, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).

**How should I estimate my AWS Backup cost?**

Estimate cost separately for each protected resource, backup type, retention period, copy, and enabled feature. For each one, record your current protected-data size, expected change rate, backup frequency, retention period, storage tier and any minimum-retention requirements, copies and destination Regions, restore testing configuration, the service requests and events your backups generate, and any free backup-storage allowance available to you. Use the AWS Pricing Calculator to estimate costs, then compare the estimate with your actual usage. For more information about estimating cost, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/) and [AWS Pricing Calculator](https://calculator.aws/).
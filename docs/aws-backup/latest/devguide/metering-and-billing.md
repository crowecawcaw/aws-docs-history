# Metering, costs, and billing for AWS Backup

## AWS Backup pricing

Current AWS Backup prices are available at [AWS Backup
pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/").

###### Important

To avoid additional charges, configure your retention policy with a warm storage
duration of **at least one week**.

For example, assume you take daily backups and retain them for one day. Further,
assume that your protected resources are so large it takes the entire day to complete your
backup. AWS Backup implements your retention period of one day and removes your backup from
warm storage when your backup job completes. The next day, AWS Backup cannot create an
incremental backup because you have no backup in warm storage. Since this retention period
did not follow best practices, you run the risk and expense of creating a full backup
every day.

Contact AWS Support for further assistance.

## AWS Backup billing

When a resource type supports full AWS Backup management, charges for AWS Backup activity
(including storage, data transfers, restores, and early deletion) appear in the "Backup"
section of your Amazon Web Services bill. For a list of services that support full AWS Backup management,
see the Full AWS Backup management section in the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table.

When a resource type does not support full AWS Backup management, some of your AWS Backup
activity such as storage costs for your backups, have billing reflected by the respective
AWS service.

**Copy Jobs**

You will only be charged once a recovery point has been created in the destination vault.
There is no charge when a copy job fails and no recovery point is created.

When you configure cross account and cross Region copies, you will see the following
billing depending on which resources you copy. For fully managed resources, the source
account will see the data transfer charges, and for non fully managed resources, the
destination account will see the data transfer charges.

## Cost allocation tags

You can use cost allocation tags to track and optimize AWS Backup costs on a detailed level,
and view and filter those tags using AWS Cost Explorer.

To use cost allocation tags, see [Automating backups and optimizing backup costs for Amazon EFS using AWS Backup](https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/ "https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/") and [Using
Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").

## AWS Backup Audit Manager pricing

AWS Backup Audit Manager charges for usage based on the number of control evaluations. A
control evaluation is the evaluation of one resource against one control. Control evaluation
charges appear on your AWS Backup bill. For current control evaluation pricing, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/").

To use AWS Backup Audit Manager controls, you must enable AWS Config recording to track your backup
activity. AWS Config charges for each configuration item recorded, and these charges appear on
your AWS Config bill. For current configuration item recorded pricing, see [AWS Config pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

## Amazon Aurora pricing

During the configured retention period for Aurora continuous backups (up to
35 days), snapshots do not incur a storage charge.
Snapshots retained past this window are charged as full backups.

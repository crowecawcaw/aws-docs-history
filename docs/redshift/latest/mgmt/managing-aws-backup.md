Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AWS Backup integration with Amazon Redshift

AWS Backup is a fully managed service that helps you centralize and automate data
protection across AWS services, in the cloud, and on premises.

Using AWS Backup for Amazon Redshift, you can configure data protection policies and monitor
activity for different Amazon Redshift resources in one place. You can also create and store
snapshots on Amazon Redshift provisioned clusters and serverless namespaces. This lets you automate and consolidate backup
tasks that you had to do separately before, without any manual processes.

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

A backup, or _recovery point_, represents the content of
a resource, such as an Amazon Redshift cluster, at a specified time. AWS Backup saves backups in
backup vaults, which you can organize according to your business needs. The terms _recovery point_ and _backup_
are used interchangeably. For more information about AWS Backup, see [Backup creation, maintenance, and restore](../../../aws-backup/latest/devguide/recovery-points.md "../../../aws-backup/latest/devguide/recovery-points.md")
in the _AWS Backup Developer Guide_.

Amazon Redshift is natively integrated with AWS Backup. That lets you define your backup plans and
assign Amazon Redshift resources to the backup plans. AWS Backup automates the creation of Amazon Redshift
manual snapshots, and securely stores these snapshots in a backup vault that you
designate in your backup plan. For information about vaults, see [Backup vaults](../../../aws-backup/latest/devguide/vaults.md "../../../aws-backup/latest/devguide/vaults.md") in the _AWS Backup Developer Guide_.
In the backup plan,
you can define the backup frequency, backup window, lifecycle, or backup vault. For
information about backup plans, see [Backup plans](../../../aws-backup/latest/devguide/about-backup-plans.md "../../../aws-backup/latest/devguide/about-backup-plans.md") in the _AWS Backup Developer Guide_.

For information about creating and restoring Amazon Redshift Serverless snapshots without using
AWS Backup, see [Snapshots and recovery points](serverless-snapshots-recovery-points.md "serverless-snapshots-recovery-points.md").
For information about creating and restoring Amazon Redshift provisioned cluster snapshots without
using AWS Backup see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").

###### Topics

- [Considerations for using AWS Backup
  with Amazon Redshift](#managing-aws-backup-considerations "#managing-aws-backup-considerations")
- [Limitations for using AWS Backup with Amazon Redshift](#managing-aws-backup-limitations "#managing-aws-backup-limitations")
- [Managing AWS Backup with Amazon Redshift](#managing-aws-backup-overview "#managing-aws-backup-overview")

## Considerations for using AWS Backup

with Amazon Redshift

Following are considerations for using AWS Backup with Amazon Redshift:

- AWS Backup for Amazon Redshift is available where both AWS Backup and Amazon Redshift are
  available in the same AWS Regions. For information on where AWS Backup is
  available, see [Amazon Redshift endpoints and quotas](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md") in
  _AWS General Reference_.
- To get started using AWS Backup, verify that you have met all the
  prerequisites. For more information, see [Prerequisites](../../../aws-backup/latest/devguide/getting-started.md#gs-assumptions "../../../aws-backup/latest/devguide/getting-started.md#gs-assumptions") in the _AWS Backup Developer Guide_.
- Affirmatively opt in to AWS Backup service. Opt-in choices apply to the
  specific account and AWS Region. If you want to use backups in multiple Regions
  with a given account, you must opt in to each individual Region with that account.
  For more information, see [Opt in to managing services with AWS Backup](../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in "../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in") in the _AWS Backup Developer Guide_.
- AWS Backup integration for Amazon Redshift only supports manual snapshots
  for provisioned clusters and serverless namespaces.
- Once you use AWS Backup to manage snapshot settings, you can't continue to
  manage manual snapshot settings using Amazon Redshift. Instead, you can continue to
  manage the settings using an AWS Backup plan. For more information, see [Backup plans](../../../aws-backup/latest/devguide/about-backup-plans.md "../../../aws-backup/latest/devguide/about-backup-plans.md")
  in the _AWS Backup Developer Guide_.
- Restoring whole data warehouse snapshots to a serverless namespace is a destructive change.
  All previously existing data in the target namespace is lost when you restore a
  data warehouse snapshot to that namespace. This only applies to restoring data
  warehouse snapshots. Restoring single table snapshots to a namespace doesn’t
  delete existing data.
- To restore a snapshot to a provisioned cluster, you need to have an IAM policy
  with the `RestoreFromClusterSnapshot` permission. To restore a snapshot to a serverless
  namespace, you need to have an IAM policy with the `RestoreFromSnapshot` permission.
  These permissions apply to the target data warehouse type, not to source snapshot type.
  For example, to restore a cluster snapshot to a namespace, you would need the
  `RestoreFromSnapshot` permission, not `RestoreFromClusterSnapshot`. For more information
  on managing IAM policies, see [Identity and access management in
  Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

## Limitations for using AWS Backup with Amazon Redshift

Following are limitations for using AWS Backup with Amazon Redshift:

- You can't use AWS Backup to manage Amazon Redshift automated snapshots. To manage
  automated snapshots, use tags. For information about tagging resources, see
  [Tagging resources in
  Amazon Redshift](amazon-redshift-tagging.md "amazon-redshift-tagging.md").
- When restoring single tables from a snapshot, you can’t restore from a provisioned
  cluster snapshot to a serverless namespace or vice versa. You can restore entire
  snapshots in any configuration. For example, you can restore all of the databases
  in a provisioned cluster snapshot to a serverless namespace, but you can’t restore
  a single table from that same snapshot to the same namespace.

## Managing AWS Backup with Amazon Redshift

To protect resources on your Amazon Redshift data warehouses, you can use the AWS Backup
console, or programmatically use the AWS Backup API or AWS Command Line Interface (AWS CLI). When you need
to recover a resource, you can use either the AWS Backup console or the AWS CLI to find and
recover the resource you need. For more information, see [AWS Command Line Interface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html").

When using AWS Backup for Amazon Redshift, you can perform the following actions:

- Create periodic backups that automatically initiate Amazon Redshift snapshots.
  Periodic backups are useful to meet your long-term data retention needs. For
  more information, see [Amazon Redshift
  backups](../../../aws-backup/latest/devguide/redshift-backups.md "../../../aws-backup/latest/devguide/redshift-backups.md") in the _AWS Backup Developer Guide_.
- Automate backup scheduling and retention by centrally configuring backup
  plans.
- Restore a provisioned cluster or serverless namespace to the saved backup you choose.
  You can choose to restore all of the data in the snapshot or a single table from it.
  You set how often to back up
  your resources. For information about
  restoring provisioned cluster snapshots, see [Restore an Amazon Redshift
  cluster](../../../aws-backup/latest/devguide/redshift-restores.md "../../../aws-backup/latest/devguide/redshift-restores.md") in the _AWS Backup Developer Guide_.
  For information on restoring serverless namespace snapshots, see
  [Amazon Redshift Serverless restore](../../../aws-backup/latest/devguide/redshift-serverless-restore.md "../../../aws-backup/latest/devguide/redshift-serverless-restore.md") in the _AWS Backup Developer Guide_.

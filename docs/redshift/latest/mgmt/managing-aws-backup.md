

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# AWS Backup integration with Amazon Redshift
<a name="managing-aws-backup"></a>

AWS Backup is a fully managed service that helps you centralize and automate data protection across AWS services, in the cloud, and on premises. 

Using AWS Backup for Amazon Redshift, you can configure data protection policies and monitor activity for different Amazon Redshift resources in one place. You can also create and store snapshots on Amazon Redshift provisioned clusters and serverless namespaces. This lets you automate and consolidate backup tasks that you had to do separately before, without any manual processes.

**Note**  
No-backup tables aren't supported for RG or RA3 provisioned clusters and Amazon Redshift Serverless workgroups. A table marked as no-backup in an RG or RA3 cluster or serverless workgroup is treated as a permanent table that will always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables, truncate them before taking a snapshot.

A backup, or *recovery point*, represents the content of a resource, such as an Amazon Redshift cluster, at a specified time. AWS Backup saves backups in backup vaults, which you can organize according to your business needs. The terms *recovery point* and *backup* are used interchangeably. For more information about AWS Backup, see [Backup creation, maintenance, and restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html) in the *AWS Backup Developer Guide*.

Amazon Redshift is natively integrated with AWS Backup. That lets you define your backup plans and assign Amazon Redshift resources to the backup plans. AWS Backup automates the creation of Amazon Redshift manual snapshots, and securely stores these snapshots in a backup vault that you designate in your backup plan. For information about vaults, see [Backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html) in the *AWS Backup Developer Guide*. In the backup plan, you can define the backup frequency, backup window, lifecycle, or backup vault. For information about backup plans, see [Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) in the *AWS Backup Developer Guide*.

For information about creating and restoring Amazon Redshift Serverless snapshots without using AWS Backup, see [Snapshots and recovery points](serverless-snapshots-recovery-points.md). For information about creating and restoring Amazon Redshift provisioned cluster snapshots without using AWS Backup see [Amazon Redshift snapshots and backups](working-with-snapshots.md).

**Topics**
+ [Considerations for using AWS Backup with Amazon Redshift](#managing-aws-backup-considerations)
+ [Limitations for using AWS Backup with Amazon Redshift](#managing-aws-backup-limitations)
+ [Managing AWS Backup with Amazon Redshift](#managing-aws-backup-overview)

## Considerations for using AWS Backup with Amazon Redshift
<a name="managing-aws-backup-considerations"></a>

Following are considerations for using AWS Backup with Amazon Redshift:
+ AWS Backup for Amazon Redshift is available where both AWS Backup and Amazon Redshift are available in the same AWS Regions. For information on where AWS Backup is available, see [Amazon Redshift endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/redshift-service.html) in *AWS General Reference*.
+ To get started using AWS Backup, verify that you have met all the prerequisites. For more information, see [Prerequisites](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html#gs-assumptions) in the *AWS Backup Developer Guide*.
+ Affirmatively opt in to AWS Backup service. Opt-in choices apply to the specific account and AWS Region. If you want to use backups in multiple Regions with a given account, you must opt in to each individual Region with that account. For more information, see [Opt in to managing services with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-supported-services.html#opt-in) in the *AWS Backup Developer Guide*.
+ AWS Backup integration for Amazon Redshift only supports manual snapshots for provisioned clusters and serverless namespaces.
+ Once you use AWS Backup to manage snapshot settings, you can't continue to manage manual snapshot settings using Amazon Redshift. Instead, you can continue to manage the settings using an AWS Backup plan. For more information, see [Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) in the *AWS Backup Developer Guide*.
+  Restoring whole data warehouse snapshots to a serverless namespace is a destructive change. All previously existing data in the target namespace is lost when you restore a data warehouse snapshot to that namespace. This only applies to restoring data warehouse snapshots. Restoring single table snapshots to a namespace doesn’t delete existing data.
+ To restore a snapshot to a provisioned cluster, you need to have an IAM policy with the `RestoreFromClusterSnapshot` permission. To restore a snapshot to a serverless namespace, you need to have an IAM policy with the `RestoreFromSnapshot` permission. These permissions apply to the target data warehouse type, not to source snapshot type. For example, to restore a cluster snapshot to a namespace, you would need the `RestoreFromSnapshot` permission, not `RestoreFromClusterSnapshot`. For more information on managing IAM policies, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md).

## Limitations for using AWS Backup with Amazon Redshift
<a name="managing-aws-backup-limitations"></a>

Following are limitations for using AWS Backup with Amazon Redshift:
+ You can't use AWS Backup to manage Amazon Redshift automated snapshots. To manage automated snapshots, use tags. For information about tagging resources, see [Tagging resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html).
+ When restoring single tables from a snapshot, you can’t restore from a provisioned cluster snapshot to a serverless namespace or vice versa. You can restore entire snapshots in any configuration. For example, you can restore all of the databases in a provisioned cluster snapshot to a serverless namespace, but you can’t restore a single table from that same snapshot to the same namespace.

## Managing AWS Backup with Amazon Redshift
<a name="managing-aws-backup-overview"></a>

To protect resources on your Amazon Redshift data warehouses, you can use the AWS Backup console, or programmatically use the AWS Backup API or AWS Command Line Interface (AWS CLI). When you need to recover a resource, you can use either the AWS Backup console or the AWS CLI to find and recover the resource you need. For more information, see [AWS Command Line Interface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html).

When using AWS Backup for Amazon Redshift, you can perform the following actions:
+ Create periodic backups that automatically initiate Amazon Redshift snapshots. Periodic backups are useful to meet your long-term data retention needs. For more information, see [Amazon Redshift backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-backups.html) in the *AWS Backup Developer Guide*.
+ Automate backup scheduling and retention by centrally configuring backup plans.
+ Restore a provisioned cluster or serverless namespace to the saved backup you choose. You can choose to restore all of the data in the snapshot or a single table from it. You set how often to back up your resources. For information about restoring provisioned cluster snapshots, see [Restore an Amazon Redshift cluster](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html) in the *AWS Backup Developer Guide*. For information on restoring serverless namespace snapshots, see [ Amazon Redshift Serverless restore ](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-serverless-restore.html) in the *AWS Backup Developer Guide*.
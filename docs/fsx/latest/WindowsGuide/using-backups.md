# Protecting your data with backups

You can protect the data on your FSx for Windows File Server file system by taking regular file system backups. Amazon FSx provides you with multiple options for
backing up your file systems. You can use automatic daily backups to take a backup
everyday. You can take a user-initiated backup of your file system at any time. You can also use
AWS Backup as part of a centralized backup solution for your AWS resources. These backup solutions
can help you to meet your data retention, business, and compliance
needs.

We recommend using the automatic daily backups that are enabled by default
for your file system, and using AWS Backup for a centralized backup solution across
AWS services. AWS Backup enables you to configure additional backup plans with
different frequencies (for example, multiple times a day, daily, or weekly) and
retention periods.

With Amazon FSx, backups are file-system-consistent, highly durable, and incremental. Each backup contains all of the
information that is necessary to create a new file system, effectively restoring a point-in-time snapshot of the file system. To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows. To
ensure high durability, Amazon FSx stores backups in Amazon Simple Storage Service (Amazon S3).

Amazon FSx backups are incremental, whether they are generated using the automatic daily backup or
the user-initiated backup feature. This means that only the data on the file system that has changed after
your most recent backup is saved. This minimizes the time required to create the backup and saves
on storage costs by not duplicating data.

At some point during the backup process, storage I/O may be suspended briefly, typically for a few seconds. Because the VSS service needs
to flush any cached writes to disk before resuming I/O, the duration of the pause may be longer if your workload has a large amount of write operations per second (`DataWriteOperations`).
Most end users and applications will experience this I/O suspension as a brief I/O pause. Your applications may have different sensitivity to timeout settings depending on how they are configured.

Creating regular backups for your file system is a best practice that complements the
replication that Amazon FSx for Windows File Server performs for your file system. Amazon FSx backups help support your backup retention and compliance needs.
Working with Amazon FSx backups is easy, whether it's creating backups, copying a backup,
restoring a file system from a backup, or deleting a backup. Note that in order to view usage for a single file system backup,
you will need to enable tags for that specific backup and enable tag-based billing reporting.

###### Topics

- [Working with automatic daily backups](#automatic-backups "#automatic-backups")
- [Working with user-initiated backups](#user-initiated-backups "#user-initiated-backups")
- [Using AWS Backup with Amazon FSx](#aws-backup-and-fsx "#aws-backup-and-fsx")
- [Copying backups](#copy-backups "#copy-backups")
- [Restoring backups to new file system](#restoring-backups "#restoring-backups")
- [Creating user-initiated backups](creating-backups.md "creating-backups.md")
- [Deleting backups](delete-backups.md "delete-backups.md")
- [Size of backups](#backup-size "#backup-size")
- [Copying backups within the same account](copying-backups.md "copying-backups.md")
- [Restoring a backup to a new file system](how-to-restore-backups.md "how-to-restore-backups.md")

## Working with automatic daily backups

By default, Amazon FSx takes an automatic daily backup of your file system. These automatic daily backups occur
during the daily backup window that was established when you created the file system. When you choose your daily backup
window, we recommend that you choose a convenient time of the day that is outside of the normal operating
hours for the applications that use the file system. We also recommend choosing a backup window outside of the
maintenance window because automated backups may not occur if there is ongoing file system maintenance.

Automatic daily backups are kept for a certain period of time, known as a retention period. When you create a file system in the Amazon FSx console, the default automatic daily backup retention period
is 30 days. The default retention period is different in the Amazon FSx API and CLI.
You can set the retention period to be between 0–90 days. Setting the retention period to 0 (zero) days turns
off automatic daily backups. Automatic daily backups are deleted when the file system is deleted.

###### Note

Setting the retention period to 0 days means that your file system is never automatically
backed up. We highly recommend that you use automatic daily backups for file systems that have any
level of critical functionality associated with them.

You can use the AWS CLI or one of the AWS SDKs to change the backup window and backup
retention period for your file systems. Use the [`UpdateFileSystem`](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md")
API operation or the [`update-file-system`](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md")
CLI command. For more information, see [Update a file
system using the AWS CLI](walkthrough03-update-file-system.md "walkthrough03-update-file-system.md").

###### Important

Lowering the retention period for automatic daily backups will result in the permanent deletion
of backups outside of the new retention window. Ensure that you no longer need these older backups before proceeding.

## Working with user-initiated backups

With Amazon FSx, you can manually take backups of your file systems at any time. You can do so
using the Amazon FSx console, API, or the AWS Command Line Interface (AWS CLI). Your user-initiated backups of Amazon FSx file
systems never expire, and they are available for as long as you want to keep them. User-initiated
backups are retained even after you delete the file system that was backed up. You can delete
user-initiated backups only by using the Amazon FSx console, API, or CLI. They are never automatically
deleted by Amazon FSx. For more information, see [Deleting backups](delete-backups.md "delete-backups.md").

If a backup is initiated while the file system is being modified (such as during an update
to throughput capacity, or during file system maintenance), the backup request is queued and will
resume when the activity is complete.

To learn how to take user-initiated backups of your file systems, see
[Creating user-initiated backups](creating-backups.md "creating-backups.md").

## Using AWS Backup with Amazon FSx

AWS Backup is a simple and cost-effective way to protect your data by backing up your Amazon FSx file systems.
AWS Backup is a unified backup service designed to simplify the creation, copying, restoration, and deletion
of backups, while providing improved reporting and auditing. AWS Backup makes it easier to develop a centralized
backup strategy for legal, regulatory, and professional compliance. AWS Backup also makes protecting your
AWS storage volumes, databases, and file systems simpler by providing a central place where you can do the following:

- Configure and audit the AWS resources that you want to back up.
- Automate backup scheduling.
- Set retention policies.
- Copy backups across AWS Regions and across AWS accounts.
- Monitor all recent backup, copy, and restore activity.

AWS Backup uses the built-in backup functionality of Amazon FSx. Backups taken from the AWS Backup console
have the same level of file system consistency and performance, and the same restore options as
backups taken through the Amazon FSx console. Backups taken from AWS Backup are incremental relative to any other
Amazon FSx backups you take, either user-initiated or automatic.

If you use AWS Backup to manage these backups, you gain additional functionality, such as unlimited retention options and the ability to create scheduled
backups as frequently as every hour. In addition, AWS Backup retains your immutable backups even after
the source file system is deleted. This protects against accidental or malicious deletion.

Backups taken by AWS Backup are considered user-initiated backups, and they count toward the
user-initiated backup quota for Amazon FSx. You can see and restore backups taken by AWS Backup in the
Amazon FSx console, CLI, and API.
However, you can't delete backups taken by AWS Backup in the Amazon FSx console, CLI, or API. For more
information about how to use AWS Backup to back up your Amazon FSx file systems, see [Working with
Amazon FSx File Systems](../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx "../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx") in the _AWS Backup Developer Guide_.

## Copying backups

You can use Amazon FSx to manually copy backups within the same AWS account to another AWS
Region (cross-Region copies) or within the same AWS Region (in-Region copies). You can make cross-Region
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
account (cross-Region or in-Region) by using the Amazon FSx console, AWS CLI, or Amazon FSx API. You can also
use [AWS Backup](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md") to perform backup copies, either on-demand or policy-based.

_Cross-account backup copies_ are valuable for meeting
regulatory compliance requirements to copy backups to an isolated account. They also provide an
additional layer of data protection to help prevent accidental or malicious deletion of backups,
loss of credentials, or compromise of AWS KMS keys. Cross-account backups support _fan-in_ (copy backups from multiple primary accounts to one isolated
backup copy account) and _fan-out_ (copy backups from one
primary account to multiple isolated backup copy accounts).

You can make cross-account backup copies by using AWS Backup with AWS Organizations support. Account
boundaries for cross-account copies are defined by AWS Organizations policies. For more information about
using AWS Backup to make cross-account backup copies, see [Creating backup copies across AWS accounts](../../../aws-backup/latest/devguide/create-cross-account-backup.md "../../../aws-backup/latest/devguide/create-cross-account-backup.md") in the
_AWS Backup Developer Guide_.

### Backup copy limitations

The following are some limitations when you copy backups:

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

### Permissions for cross-Region backup copies

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

### Full and incremental copies

When you copy a backup to a different destination AWS Region or destination AWS account from the source backup,
the first copy is a full backup copy, even if you use the same KMS key to encrypt both source and destination copies of the backup.

After the first backup copy, all subsequent
backup copies to the same destination Region within the same AWS account are
incremental, provided that you haven't deleted all previously-copied backups in
that Region and have been using the same AWS KMS key. If either condition isn't
met, the copy operation results in a full (not incremental) backup copy.

To learn how to copy backups of your file systems, see
[Copying backups within the same account](copying-backups.md "copying-backups.md").

## Restoring backups to new file system

You can use an available backup to create a new file system, effectively restoring a
point-in-time snapshot of another file system. You can restore a backup using the console, AWS CLI,
or one of the AWS SDKs. Restoring a backup to a new file system takes the same amount of time as
creating a new file system. The data restored from the backup is lazy-loaded onto the file system,
during which time you will experience slightly higher latency.

To ensure that users can continue to access the restored file system, make sure that
the Active Directory domain associated with the restored file system is the same as that
of the original file system, or is trusted by the Active Directory domain of the original file system.
For more information about Active Directory,
see [Working with Microsoft Active Directory](aws-ad-integration-fsxW.md "aws-ad-integration-fsxW.md").

To learn how to restore a backup to a new FSx for Windows file system, see
[Restoring a backup to a new file system](how-to-restore-backups.md "how-to-restore-backups.md").

###### Note

You can only restore a file system backup to a new file system with the same deployment type and
storage capacity as the original. You can increase the new file system's storage capacity
after it becomes available. For more information,
see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity").

You can change any of the following file system settings when restoring a backup to a new file system:

- Storage type
- Throughput capacity
- VPC
- Availability Zone
- Subnet
- VPC security groups
- Active Directory Configuration
- AWS KMS encryption key
- Daily automatic backup start time
- Weekly maintenance window

## Size of backups

Backups size is determined using the used storage in the file system, rather than the total provisioned storage capacity.
The size of your backups will depend on the used storage capacity as well as the amount of data churn on your file system.
Depending on how your data is distributed across the file system’s storage volumes and how often it changes,
your total backup usage may be greater or less than your used storage capacity. When you delete a backup, only the
data unique to that backup is removed.

In order to provide backups that are file-system-consistent, durable, and incremental, Amazon FSx backs up data at the block level.
The data on the file system's storage volumes
may be stored across multiple blocks depending on the pattern that they were written or over-written in.
As a result, the total size of backup usage may not match the exact size of the files and directories on the file system.
Your overall backup usage and cost can be found in the AWS Billing Dashboard or AWS Cost Management Console.

Use tags to organize your AWS bill to reflect your own cost structure.
To do this, sign up to get your AWS account bill with tag key values included.
Then, to see the cost of combined resources, organize your billing information
according to resources with the same tag key values. For example, you can tag
several resources with a specific application name, and then organize your billing
information to see the total cost of that application across several services.
For more information, see
[Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

###### Note

When you [increase storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity"), the process of migrating data from the old set of storage disks to the new, larger set of
storage disks can result in a temporary increase in backup usage until backups associated with the old set of storage disks are
deleted. If your file system’s storage was only partially used before you increase storage capacity, the size of data that
needs to be migrated to the new disks may be larger than the size of data that exists on the original storage disks. This may
cause an increase in backup usage up to the new storage capacity level. You should consider the impact of increasing storage
capacity on your backup planning.

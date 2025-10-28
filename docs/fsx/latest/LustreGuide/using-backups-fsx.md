# Protecting your data with backups

With Amazon FSx for Lustre, you can take automatic daily backups and user-initiated backups of
persistent file systems that are not linked to an Amazon S3 durable data repository.
Amazon FSx backups are file-system-consistent, highly durable, and incremental. To
ensure high durability, Amazon FSx for Lustre stores backups in Amazon Simple Storage Service (Amazon S3) with 99.999999999% (11 9's) durability.

FSx for Lustre file system backups are block-based, incremental backups, whether they are generated using the automatic daily backup or
the user-initiated backup feature. This means that when you take a backup,
Amazon FSx compares the data on your file system to your previous backup at the block level. Then Amazon FSx stores a copy
of all block-level changes in the new backup. Block-level data that remains unchanged since the previous backup is not stored in the new backup.
The duration of the backup process depends on how much data has changed since the last backup was taken
and is independent of the storage capacity of the file system. The following list illustrates backup times under different circumstances:

- The initial backup of a brand new file system with very little data takes minutes to complete.
- The initial backup of a brand new file system taken after loading TBs of data takes hours to complete.
- A second backup taken of the file system with TBs of data with minimal changes to the block-level data (relatively few creates/modifications) takes seconds to complete.
- A third backup of the same file system after a large amount of data has been added and modified takes hours to complete.
  When you delete a backup, only the data unique to that
  backup is removed. Each FSx for Lustre backup contains all of the information that is needed to
  create a new file system from the backup, effectively restoring a point-in-time snapshot of the
  file system.

Creating regular backups for your file system is a best practice that complements the
replication that Amazon FSx for Lustre performs for your file system. Amazon FSx backups help support your backup retention and compliance needs.
Working with Amazon FSx for Lustre backups is easy, whether it's creating backups, copying a backup,
restoring a file system from a backup, or deleting a backup.

Backups are not supported on scratch file systems because these file systems are designed for
temporary storage and shorter-term processing of data. Backups are not supported on file systems
linked to an Amazon S3 bucket because the S3 bucket serves as the primary data repository, and the
Lustre file system does not necessarily contain the full dataset at any given time.

###### Topics

- [Backup support in FSx for Lustre](#fsxl-backup-support "#fsxl-backup-support")
- [Working with automatic daily backups](#automatic-backups "#automatic-backups")
- [Working with user-initiated backups](#user-initiated-backups "#user-initiated-backups")
- [Using AWS Backup with Amazon FSx](#aws-backup-and-fsx "#aws-backup-and-fsx")
- [Copying backups](copy-backups.md "copy-backups.md")
- [Copying backups within the same AWS account](copying-backups-same-account.md "copying-backups-same-account.md")
- [Restoring backups](restoring-backups.md "restoring-backups.md")
- [Deleting backups](delete-backups.md "delete-backups.md")

## Backup support in FSx for Lustre

Backups are supported only on FSx for Lustre persistent file systems that are
not linked to an Amazon S3 data repository.

Amazon FSx does not support backups on scratch file systems because scratch file systems are
designed for temporary storage and shorter-term processing of data. Amazon FSx does not support
backups on file systems linked to an Amazon S3 bucket because the S3 bucket serves as the primary
data repository and the file system does not necessarily contain the full dataset at any given
time. For more information, see [Deployment and storage class options](using-fsx-lustre.md "using-fsx-lustre.md") and [Using data repositories](fsx-data-repositories.md "fsx-data-repositories.md").

## Working with automatic daily backups

Amazon FSx for Lustre can take an automatic daily backup of your file system. These automatic daily backups
occur during the daily backup window that was established when you created the file system. At
some point during the daily backup window, storage I/O might be suspended briefly while the
backup process initializes (typically for less than a few seconds). When you choose your daily
backup window, we recommend that you choose a convenient time of the day. This time ideally is
outside of the normal operating hours for the applications that use the file system.

Automatic daily backups are kept for a certain period of time, known as a _retention period_. You can set the retention period to be between 0–90
days. Setting the retention period to 0 (zero) days turns off automatic daily backups. The
default retention period for automatic daily backups is 0 days. Automatic daily backups are
deleted when the file system is deleted.

###### Note

Setting the retention period to 0 days means that your file system is never automatically
backed up. We highly recommend that you use automatic daily backups for file systems that have any
level of critical functionality associated with them.

You can use the AWS CLI or one of the AWS SDKs to change the backup window and backup
retention period for your file systems. Use the [`UpdateFileSystem`](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md")
API operation or the [`update-file-system`](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md")
CLI command.

## Working with user-initiated backups

Amazon FSx for Lustre enables you to manually take backups of your file systems at any time. You can do so
using the Amazon FSx for Lustre console, API, or the AWS Command Line Interface (CLI). Your user-initiated backups of
Amazon FSx file systems never expire, and they are available for as long as you want to keep them.
User-initiated backups are retained even after you delete the file system that was backed up. You
can delete user-initiated backups only by using the Amazon FSx for Lustre console, API, or CLI, and they are
never automatically deleted by Amazon FSx. For more information, see [Deleting backups](delete-backups.md "delete-backups.md").

### Creating user-initiated backups

The following procedure guides you through how to create a user-initiated
backup in the Amazon FSx console for an existing file system.

###### To create a user-initiated file system backup

1. Open the Amazon FSx for Lustre console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose the name of the file system that you want to back
   up.
3. From **Actions**, choose **Create backup**.
4. In the **Create backup** dialog box that opens, provide a name for your
   backup. Backup names can be a maximum of 256 Unicode characters, including letters, white
   space, numbers, and the special characters . + - = \_ : /
5. Choose **Create backup**.

You have now created your file system backup. You can find a table of all your backups in
the Amazon FSx for Lustre console by choosing **Backups** in the left side navigation. You can
search for the name you gave your backup, and the table filters to only show matching
results.

When you create a user-initiated backup as this procedure described, it has the type
`USER_INITIATED`, and it has the **Creating** status while Amazon FSx creates the
backup. The status changes to **Transferring** while the backup is transferred
to Amazon S3, until it is fully available.

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
- Monitor all recent backup and restore activity.

AWS Backup uses the built-in backup functionality of Amazon FSx. Backups taken from the AWS Backup console
have the same level of file system consistency and performance, and the same restore options as
backups that are taken through the Amazon FSx console. If you use AWS Backup to manage these backups, you
gain additional functionality, such as unlimited retention options and the ability to create
scheduled backups as frequently as every hour. In addition, AWS Backup retains your immutable backups
even after the source file system is deleted. This helps protect against accidental or malicious
deletion.

Backups created by AWS Backup have backup type `AWS_BACKUP`
and are incremental relative to any other Amazon FSx backups you take of your file system.
Backups taken by AWS Backup are considered user-initiated backups, and they count toward the
user-initiated backup quota for Amazon FSx. You can see and restore backups taken by AWS Backup in the
Amazon FSx console, CLI, and API. However, you can't delete the backups taken by AWS Backup in the Amazon FSx
console, CLI, or API. For more information about how to use AWS Backup to back up your Amazon FSx file systems,
see [Working with
Amazon FSx File Systems](../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx "../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx") in the _AWS Backup Developer Guide_.

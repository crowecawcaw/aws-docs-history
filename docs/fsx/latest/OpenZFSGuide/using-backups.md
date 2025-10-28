# Protecting your data with backups

With FSx for OpenZFS, backups are file-system-consistent, highly durable, and incremental.
To ensure high durability, Amazon FSx stores backups in Amazon Simple Storage Service (Amazon S3).

Amazon FSx backups are incremental, whether they are generated using the automatic daily backup or
the user-initiated backup feature. This means that only the data on the file system that has changed after
your most recent backup is saved. This minimizes the time required to create the backup and saves
on storage costs by not duplicating data. When you delete a backup, only the data unique to that
backup is removed. Each FSx for OpenZFS backup contains all of the information that is needed to
create a new file system from the backup, effectively restoring a point-in-time snapshot of the
file system.

Creating regular backups for your file system is a best practice that complements the
replication that FSx for OpenZFS performs for your file system. Amazon FSx backups help support your
backup retention and compliance needs. Working with Amazon FSx backups is easy, whether it's
creating backups, copying a backup, restoring a file system from a backup, or deleting a backup.

###### Topics

- [Working with automatic daily backups](#automatic-backups "#automatic-backups")
- [Working with user-initiated backups](#user-initiated-backups "#user-initiated-backups")
- [Working with AWS Backup](#aws-backup-and-fsx "#aws-backup-and-fsx")
- [Copying backups](copy-backups.md "copy-backups.md")
- [Restoring backups](restoring-backups.md "restoring-backups.md")
- [Deleting backups](delete-backups.md "delete-backups.md")

## Working with automatic daily backups

By default, Amazon FSx takes an automatic daily backup of your file system. These automatic daily backups occur
during the daily backup window that was established when you created the file system. At
some point during the daily backup window, storage I/O might be suspended briefly while the
backup process initializes (typically for less than a few seconds). When you choose your daily backup
window, we recommend that you choose a convenient time of the day. This time ideally is outside of the normal operating
hours for the applications that use the file system.

Automatic daily backups are kept for a certain period of time, known as a retention period. When you create a file system in the Amazon FSx console, the default automatic daily backup retention period
is 30 days. The default retention period is different in the Amazon FSx API and CLI.
You can set the retention period to be between 1–90 days.
Automatic daily backups are deleted when the file system is deleted.

###### Note

While automatic daily backups have a maximum retention period of 90 days,
user-initiated backups are kept forever, unless you delete them. For more information
about user-initiated backups, see [Working with user-initiated backups](#user-initiated-backups "#user-initiated-backups").

You can use the AWS CLI or one of the AWS SDKs to change the backup window and backup
retention period for your file systems. Use the [`UpdateFileSystem`](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md")
API operation or the [`update-file-system`](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md")
CLI command.

## Working with user-initiated backups

With Amazon FSx, you can manually take backups of your file systems at any time. You can do so
using the Amazon FSx console, API, or the AWS Command Line Interface (AWS CLI). Your user-initiated backups of Amazon FSx file
systems never expire, and they are available for as long as you want to keep them. User-initiated
backups are retained even after you delete the file system that was backed up. You can delete
user-initiated backups only by using the Amazon FSx console, API, or CLI. They are never automatically
deleted by Amazon FSx. For more information, see [Deleting backups](delete-backups.md "delete-backups.md").

### Creating user-initiated backups

The following procedure guides you through how to create a user-initiated
backup in the Amazon FSx console for an existing file system.

###### To create a user-initiated file system backup

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose the name of the file system that you want to back
   up.
3. From **Actions**, choose **Create backup**.
4. In the **Create backup** dialog box that opens, provide a name for your
   backup. Backup names can be a maximum of 256 Unicode characters, including letters, white
   space, numbers, and the special characters . + - = \_ : /
5. Choose **Create backup**.

You have now created your file system backup. You can find a table of all your backups in
the Amazon FSx console by choosing **Backups** in the left side navigation. You can
search for the name you gave your backup, and the table filters to only show matching
results.

When you create a user-initiated backup as this procedure described, it has the type
`User-Initiated`, and it has the `Creating` status until it is fully
available.

## Working with AWS Backup

AWS Backup is a simple and cost-effective way to protect your data by backing up your
Amazon FSx for OpenZFS file systems. AWS Backup is a unified backup service designed to simplify the
creation, restoration, and deletion of backups, while providing improved reporting and auditing.
AWS Backup makes it easier to develop a centralized backup strategy for legal, regulatory, and
professional compliance. AWS Backup also makes protecting your AWS storage file systems, databases,
and file systems simpler by providing a central place where you can do the following:

- Configure and audit the AWS resources that you want to back up.
- Automate backup scheduling.
- Set retention policies.
- Copy backups across AWS Regions and AWS accounts
- Monitor all recent backup, copy, and restore activity.

AWS Backup uses the built-in backup functionality of Amazon FSx. Backups taken from the AWS Backup console
have the same level of file system consistency and performance, are incremental relative to any
other Amazon FSx backups you take of your file system (user-initiated or automatic), and offer
the same restore options as backups taken through the Amazon FSx console. If you use AWS Backup to manage
these backups, you gain additional functionality, such as unlimited retention options and the
ability to create scheduled backups as frequently as every hour. In addition, AWS Backup and Amazon FSx
retain your immutable backups even after the source file system is deleted. This protects against
accidental or malicious deletion.

Backups taken by AWS Backup are considered user-initiated backups, and they count toward the
user-initiated backup quota for Amazon FSx. You can view and restore backups taken by AWS Backup in the
Amazon FSx console, CLI, and API. However, you can't delete backups taken by AWS Backup in the Amazon FSx
console, CLI, or API. For more information about how to use AWS Backup to back up your Amazon FSx file
systems and how to delete backups, see [Working with
Amazon FSx file systems](../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx "../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-fsx") in the _AWS Backup Developer Guide_.

### Deleting backups

You can't delete backups taken by AWS Backup in the Amazon FSx console, CLI, or API. For information on deleting a backup taken by AWS Backup, see [Backup deletion](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md") in the _AWS Backup Developer Guide_. Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is
also deleted. Do not delete a backup unless you're sure you won't need that backup
again in the future.

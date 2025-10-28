# Backing up EFS file systems

Amazon EFS is natively integrated with AWS Backup, a fully managed, policy-based service that you can
use to create and manage backup policies to protect your data in Amazon EFS. File systems that you
create using the Amazon EFS console are automatically backed up by AWS Backup by default. When you use the
CLI or API to create a file system, automatic backups are enabled by default only for One Zone
file systems.

Using AWS Backup for Amazon EFS, you can perform the following actions:

- Manage automatic backup scheduling and retention by configuring backup plans.
  You specify the backup frequency,
  when to back up, how long to retain backups, and a lifecycle policy for backups.
- Restore backups of Amazon EFS data. You can restore file system data to either a new or
  existing file system. You also can choose whether to perform a full restore or an item-level
  restore.

For more information about using AWS Backup, see
[Getting started with AWS Backup](../../../aws-backup/latest/devguide/getting-started.md "../../../aws-backup/latest/devguide/getting-started.md")
in the _AWS Backup Developer Guide_.

###### Topics

- [How AWS Backup works with Amazon EFS](#how-backup-works "#how-backup-works")
- [Required IAM permissions](#backup-req-permissions "#backup-req-permissions")
- [Backup performance](#backup-performance "#backup-performance")
- [Managing automatic backups of EFS file
  systems](automatic-backups.md "automatic-backups.md")

## How AWS Backup works with Amazon EFS

File systems that you
create using the Amazon EFS console are automatically backed up by AWS Backup by default. When you use the CLI or API
to create a file system, automatic backups are enabled by default only for One Zone file systems.
You can turn on automatic backups after creating your EFS file system using the AWS CLI or API.
The default EFS backup plan uses the AWS Backup recommended settings for automatic
backups—daily backups with a 35-day retention period. The backups created using the
default EFS backup plan are stored in a default EFS backup vault, which is
also created by Amazon EFS on your behalf. The default backup plan and backup vault cannot be
deleted.

All data in an EFS file system is backed up, whatever storage class the data is in. You
don't incur data access charges when backing up an EFS file system that has lifecycle
management enabled and has data in the Infrequent Access (IA) or Archive
storage class. When you restore a recovery point, all files are restored to the
Standard storage class.

### Incremental backups

AWS Backup performs incremental backups of EFS file systems. During the initial
backup, a copy of the entire file system is made. During subsequent backups of that file
system, only files and directories that have been changed, added, or removed are copied.
With each incremental backup, AWS Backup retains the necessary reference data to allow a full restore.
This approach minimizes the time required to complete the backup and saves on storage
costs by not duplicating data.

### Backup consistency

Amazon EFS is designed to be highly available. You can access and modify your EFS file
systems while your backup is occurring in AWS Backup. However, inconsistencies, such as
duplicated, skewed, or excluded data, can occur if you make modifications to your file
system while the backup is occurring. These modifications include write, rename, move,
or delete operations. To ensure consistent backups, we recommend that you pause
applications or processes that are modifying the file system for the duration of the
backup process. Or, schedule your backups to occur during periods when the file system
is not being modified.

### Backup completion window

You can optionally specify a completion window for a backup. This window defines the
period of time in which a backup needs to be completed. If you specify a completion window, make
sure that you consider the expected performance and the size and makeup of your file system.
Doing this helps make sure that your backup can be completed during the window.

Backups that aren't completed during the specified window are flagged with an incomplete
status. During the next scheduled backup, AWS Backup resumes at the point that it left off. You can see
the status of all of your backups on the AWS Backup Management Console.

#### Best practices for backup completion windows

When configuring backup completion windows for your EFS file systems, consider the following best practices to ensure reliable backup operations:

- **Monitor backup duration** – If you notice that your backups are taking an extended period (for example, 20 days or more), consider shortening your completion window to 3 days. This approach allows AWS Backup to perform multiple shorter, partial backups rather than attempting to complete the entire backup in a single extended window.
- **Consider file system characteristics** – Large file systems with millions of files or significant data volumes may benefit from shorter completion windows. The 3-day window recommendation helps ensure that backup operations complete successfully and resume efficiently if needed.
- **Plan for incremental progress** – When using shorter completion windows, AWS Backup automatically resumes from where it left off during the next scheduled backup. This incremental approach can be more reliable for large file systems than attempting to complete everything in a single long window.
- **Test your backup strategy** – Before relying on your backup configuration in production, test it with your specific file system size and characteristics to determine the optimal completion window for your use case.

###### Note

Shorter completion windows don't indicate a limitation in AWS Backup's capability to handle large file systems. Instead, they provide a more predictable and manageable backup process that can adapt to varying file system sizes and network conditions.

### On-demand backups

With AWS Backup, you can save a single resource to a backup vault on-demand. Unlike with
scheduled backups, you don't need to create a backup plan to initiate an on-demand
backup. You can still assign a lifecycle to your backup, which automatically moves the
recovery point to the cold storage tier and notes when to delete it.

Additionally, AWS Backup automatically transitions data to cold storage only for data that no
longer exists in the most recent warm backup. For example, your file system has 100 files
when you create a backup and you delete two files the day after you created the backup (100
files - 2 files = 98 files on second day). When you transition the data to cold storage,
only the two deleted files move to cold storage and the remaining 98 files are billed as
warm storage.

### Concurrent backups

AWS Backup limits backups to one concurrent backup per resource. Therefore, scheduled or
on-demand backups might fail if a backup job is already in progress. For more information about
AWS Backup limits, see [AWS Backup quotas](../../../aws-backup/latest/devguide/aws-backup-limits.md "../../../aws-backup/latest/devguide/aws-backup-limits.md") in the _AWS Backup Developer Guide_.

### Backup deletions

The default EFS backup vault Access policy is set to deny deleting recovery
points. To delete existing backups of your EFS file systems, you must change the vault access
policy. If you attempt to delete an EFS recovery point without modifying the vault
access policy, you receive the following error message:

```
"Access Denied: Insufficient privileges to perform this action. Please consult with the account administrator for necessary permissions."
```

To edit the default backup vault access policy, you must have permissions to edit policies.
For more information, see [Allow all IAM actions (admin access)](../../../IAM/latest/UserGuide/id_credentials_delegate-permissions_examples.md#creds-policies-all-iam "../../../IAM/latest/UserGuide/id_credentials_delegate-permissions_examples.md#creds-policies-all-iam") in the
_IAM User Guide_.

## Required IAM permissions

AWS Backup creates a service-linked role on your behalf in your account. This role has the
permissions required to perform Amazon EFS backups.

You can use the `elasticfilesystem:backup` and
`elasticfilesystem:restore` actions to allow or deny an IAM entity (such as a
user, group, or role) the ability to create or restore backups of an EFS file system. You can
use these actions in a file system policy or in an identity-based IAM policy. For more
information, see [Identity and access management for Amazon EFS](security-iam.md "security-iam.md") and [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").

## Backup performance

In general, you can expect the following backup and restore rates with AWS Backup. The rates may
be less for some workloads, such as those containing a large file or directory.

- Backup rate of 2,000 files per second or 400 megabytes per second (MBps), whichever is
  slower.
- Restore rate of 1,500 files per second or 200 MBps, whichever is slower.

The maximum duration for a backup operation in AWS Backup is 30 days.

Using AWS Backup doesn't consume accumulated burst credits, and it doesn't count
against the General Purpose performance mode file operation limits. For more information, see
[Quotas for Amazon EFS file systems](limits.md#limits-fs-specific "limits.md#limits-fs-specific").

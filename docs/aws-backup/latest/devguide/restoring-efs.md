# Restore an Amazon EFS file system

If you are restoring an Amazon Elastic File System (Amazon EFS) instance, you can perform a full restore or an
item-level restore.

**Full Restore**

When you perform a full restore, the entire file system is restored.

AWS Backup does not support destructive restores with Amazon EFS. A destructive restore is when a
restored file system deletes or overwrites the source or existing file system. Instead,
AWS Backup restores your file system to a recovery directory off of the root directory.

**Item-Level Restore**

When you perform an item-level restore, AWS Backup restores a specific file or directory. You
must specify the path relative to the file system root. For example, if the file system is
mounted to `/user/home/myname/efs` and the file path is
`user/home/myname/efs/file1`, you enter `/file1`. Paths
are case sensitive. Wildcard characters and regex strings are not supported. Your path may
be different from what is in the host if the file system is mounted using an access
point.

You can select up to 10 items when you use the console to perform an EFS restore. There
is no item limit when you use CLI to restore; however, there is a 200 KB limit on the length
of the restore metadata that can be passed.

You can restore those items to either a new or existing file system. Either way, AWS Backup
creates a new Amazon EFS directory
(`aws-backup-restore_`datetime``) off of the
root directory to contain the items. The full hierarchy of the specified items is preserved
in the recovery directory. For example, if directory A contains subdirectories B, C, and D,
AWS Backup retains the hierarchical structure when A, B, C, and D are recovered. Regardless of
whether you perform an Amazon EFS item-level restore to an existing file system or to a new file
system, each restore attempt creates a new recovery directory off of the root directory to
contain the restored files. If you attempt multiple restores for the same path, several
directories containing the restored items might exist.

###### Note

If you only keep one weekly backup, you can only restore to the state of the file
system at the time you took that backup. You can't restore to prior incremental
backups.

## Use the AWS Backup console to restore an Amazon EFS recovery

point

###### To restore an Amazon EFS file system

1.  Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2.  Your EFS backup vault receives the access policy `Deny`
    `backup:StartRestoreJob` upon creation. If you are restoring your backup
    vault for the first time, you must change your access policy as follows.

        1. Choose **Backup vaults**.
        2. Choose the backup vault containing the recovery point you would like to
         restore.
        3. Scroll down to the vault **Access policy**
        4. If present, delete `backup:StartRestoreJob` from the
         `Statement`. Do this by choosing **Edit**, deleting
         `backup:StartRestoreJob`, then choosing **Save
         policy**.

3.  In the navigation pane, choose **Protected resources** and the
    EFS file system ID you want to restore.
4.  On the **Resource details** page, a list of recovery points for
    the selected file system ID is shown. To restore a file system, in the
    **Backups** pane, choose the radio button next to the recovery
    point ID of the file system. In the upper-right corner of the pane, choose
    **Restore**.
5.  Specify the restore parameters for your file system. The restore parameters you
    enter are specific to the resource type that you selected.

You can perform a **Full restore**, which restores the entire
file system. Or, you can restore specific files and directories using
**Item-level restore**.

    * Choose the **Full restore** option to restore the file system
     in its entirety including all root level folders and files.
    * Choose the **Item-level restore** option to restore a
     specific file or directory. You can select and restore up to five items within
     your Amazon EFS.


    To restore a specific file or directory, you must specify the relative path
     related to the mount point. For example, if the file system is mounted to
     `/user/home/myname/efs` and the file path is
     `user/home/myname/efs/file1`, enter `/file1`.
     Paths are case sensitive and cannot contain special characters, wildcard
     characters, and regex strings.




    	1. In the **Item path** text box, enter the path for your
    	 file or folder.
    	2. Choose **Add item** to add additional files or
    	 directories. You can select and restore up to five items within your EFS file
    	 system.

6.  For **Restore location**
    - Choose **Restore to directory in source file system** if you
      want to restore to the source file system.
    - Choose **Restore to a new file system** if you want to
      restore to a different file system.

7.  For **File system type**

        * (Recommended) Choose **Regional** if you want to restore your
         file system across multiple AWS Availability Zones.
        * Choose **One Zone** if you want to restore your file system
         to a single Availability Zone. Then, in the **Availability Zone**
         dropdown, choose the destination for your restore.

    For more information, see [Managing Amazon EFS storage classes](../../../efs/latest/ug/storage-classes.md "../../../efs/latest/ug/storage-classes.md") in
    the _Amazon EFS User Guide._

8.  For **Performance**
    - If you chose to perform a **Regional** restore, choose either
      **(Recommended) General purpose** or **Max
      I/O**.
    - If you chose to perform a **One Zone** restore, you must
      choose **(Recommended) General purpose**. One Zone restores do
      not support **Max I/O**.

9.  For **Enable encryption**
    - Choose **Enable encryption**, if you want to encrypt your
      file system. KMS key IDs and aliases appear in the list after they have been
      created using the AWS Key Management Service (AWS KMS) console.
    - In the **KMS key** text box, choose the key you want to use
      from the list.

10. For **Restore role**, choose the IAM role that AWS Backup will
    assume for this restore.

###### Note

If the AWS Backup default role is not present in your account, a **Default
role** is created for you with the correct permissions. You can delete
this default role or make it unusable. 11. Choose **Restore backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job.

###### Note

If you only keep one weekly backup, you can only restore to the state of the
file system at the time you took that backup. You can't restore to prior incremental
backups.

## Use the AWS Backup API, CLI, or SDK to restore Amazon EFS recovery

points

Use `StartRestoreJob`. When restoring an Amazon EFS instance, you can restore an
entire file system or specific files or directories. To restore Amazon EFS resources, you need
the following information:

- `file-system-id` — The ID of the Amazon EFS file system that is
  backed up by AWS Backup. Returned in `GetRecoveryPointRestoreMetadata`. This is
  not required when a **new** file system is restored (this value is
  ignored if parameter `newFileSystem` is `True`).
- `Encrypted` — A Boolean value that, if true, specifies that the
  file system is encrypted. If `KmsKeyId` is specified,
  `Encrypted` must be set to `true`.
- `KmsKeyId` — Specifies the AWS KMS key that is used to encrypt the
  restored file system.
- `PerformanceMode` — Specifies the throughput mode of the file
  system. Valid values are `generalPurpose` (default) and `maxIO`.
  The `generalPurpose` mode provides the lowest latency per operation and can achieve
  up to 7,000 file operations per second. The `maxIO` mode can scale to higher levels
  of aggregate throughput and operations per second with a slightly higher latency for file operations.
- `CreationToken` — A user-supplied value that ensures the
  uniqueness (idempotency) of the request.
- `newFileSystem` — A Boolean value that, if true, specifies that
  the recovery point is restored to a new Amazon EFS file system.
- `ItemsToRestore` — An array of up to five strings where each
  string is a file path. Use `ItemsToRestore` to restore specific files or
  directories rather than the entire file system. This parameter is optional.

You may also include `aws:backup:request-id`.

One Zone restores can be performed by including parameters:

```
"singleAzFilesystem": "true"
"availabilityZoneName": "`ap-northeast-3`"
```

For more information about Amazon EFS configuration values, see [create-file-system](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html").

## Disabling automatic backups in Amazon EFS

By default, [Amazon EFS creates backups of data
automatically](../../../efs/latest/ug/awsbackup.md#automatic-backups "../../../efs/latest/ug/awsbackup.md#automatic-backups"). These backups are represented as recovery points in AWS Backup.
Attempts to remove the recovery point will result in an error message that notes there are
insufficient privileges to perform the action.

It is best practice to keep this auto-backup active. Particularly in the case of
accidental data deletion, this backup allows restoration of file system content to the
date of the last recovery point created.

In the unlikely event you wish to turn these off, the access policy must be changed
from `"Effect": "Deny"` to `"Effect": "Allow"`. See the
_Amazon EFS User Guide_ for more information about turning [automatic
backups](../../../efs/latest/ug/awsbackup.md#automatic-backups "../../../efs/latest/ug/awsbackup.md#automatic-backups") on or off.

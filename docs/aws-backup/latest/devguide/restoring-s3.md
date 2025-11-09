# Restore S3 data using AWS Backup

You can restore the S3 data that you backed up using AWS Backup to the S3 Standard storage
class. You can restore all the objects in a bucket or specific objects. You can restore them
to an existing or new bucket.

## Amazon S3 restore permissions

Before you begin restoring resources, ensure the role you're using has sufficient
permissions.

For more information, see the following entries on policies:

1. [`AWSBackupServiceRolePolicyForS3Restore`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md")
2. [`AWSBackupServiceRolePolicyForRestores`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md")
3. [Managed policies for AWS Backup](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

## Amazon S3 restore considerations

- If ACLs were enabled during the backup, the destination bucket for the restore
  must have ACLs enabled; otherwise, the restore job fails.
- If Block Public Access is enabled on the destination bucket, the restore job
  completes successfully, but objects with public ACLs are not restored.
- Restores of objects are skipped if the destination bucket has an object with the same
  name or version ID.
- When you restore to the original S3 bucket,
  - AWS Backup does not perform a destructive restore, which means AWS Backup will not put
    an object into a bucket in place of an object that already exists, regardless of
    version.
  - A delete marker in the current version is treated as the object as
    nonexistent, so a restore can occur.
  - AWS Backup does not delete objects (without delete markers) from a bucket during a
    restore (example: keys currently in the bucket which were not present during the
    backup will remain).

- **Restoring cross-Region copies**
  - While S3 backups can be copied cross-Region, restore jobs only occur in the
    same Region in which the original backup or copy is located.

  **Example:** An S3 bucket created in US East (N. Virginia) Region can be
  copied to Canada (Central) Region. The restore job can be initiated using the original
  bucket in US East (N. Virginia) Region and restored to that Region, or the restore job can be
  initiated using the copy in Canada (Central) Region and restored to that
  Region.
  - The original encryption method cannot be used to restore a recovery point
    (backup) copied from another Region. Cross-Region copy AWS KMS encryption is not
    available for Amazon S3 resources; instead, use a different encryption type for a
    restore job.

## Restoring ACLs and object tags

When restoring Amazon S3 data, you choose whether ACLs are part of the restore.

If ACLs are available in the recovery point, you choose to restore or exclude ACLs
using the Restore ACLs setting; if ACLs were not in the backup, they cannot be restored
regardless of the setting. If you try to create a restore job with ACls enabled but
they were not part of the backup, you may see an error such as `Unable to 
 restore Access Control Lists (ACLs) for bucket because backup was created with the 
 'BackupACLs' option disabled. Please proceed with restoring without ACLs`.

Object tags are automatically restored if they were included in the original
backup

###### Note

Restoring recovery points without ACLs

If through AWS CLI you attempt to restore ACLs from a backup that excluded ACLs, the
restore operation will fail with an error message indicating invalid restore
parameters.

## Restore multiple versions

By default, AWS Backup restores only the latest version of your objects. You have the
choice to restore additional or all versions of the objects.

See step 6 in the following section for how to restore up the 10 latest versions or
all versions using the AWS Backup console.

See [Restore Amazon S3 recovery points through AWS CLI](#s3-restore-cli "#s3-restore-cli") later on this page for metadata details to
include when restoring programmatically.

## Restore through the AWS Backup console

###### To restore your Amazon S3 data using the AWS Backup console:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, and
   select the Amazon S3 resource ID that you want to restore.
3. On the **Resource details** page, you will see a list of recovery
   points for the selected resource ID. To restore a resource:
   1. In the **Backups** pane, choose the recovery point ID of the
      resource.
   2. In the upper-right corner of the pane, choose
      **Restore**.

   (Alternatively, you can go to the backup vault, find the recovery point, and
   then click **Actions** then click
   **Restore**.)

4. If you are restoring a continuous backup, in the **Restore time**
   pane, select either option:
   1. Accept the default to restore to the **Latest restorable
      time**.
   2. **Specify date and time** to restore.

5. In the **Settings** pane, specify whether to **Restore
   entire bucket** or perform **Item level restore**.
   1. If you choose **Item level restore**, you restore up to 5
      items (objects or folders in a bucket) per restore job by specifying each item's
      [S3 URI](../../../AmazonS3/latest/userguide/access-bucket-intro.md "../../../AmazonS3/latest/userguide/access-bucket-intro.md") that
      uniquely identifies that object.

   (For more information about S3 bucket URIs, see [Methods for accessing a
   bucket](../../../AmazonS3/latest/userguide/access-bucket-intro.md "../../../AmazonS3/latest/userguide/access-bucket-intro.md") in the _Amazon Simple Storage Service User
   Guide_.) 2. Choose **Add item** to specify another item to
   restore.

6. By default, only the latest version of an object is restored. You can restore up
   to the 10 latest versions or restore all versions of the objects. Select your
   preference from the drop-down menu.
7. Choose your **Restore destination**. You can either
   **Restore to source bucket**, **Use existing
   bucket**, or **Create new bucket**.

###### Note

Your restore destination bucket must have versioning turned on. AWS Backup notifies
you if the bucket you select does not meet this requirement.

    1. If you choose **Use existing bucket**, select the destination
     S3 bucket from the menu which shows all existing buckets within your current AWS
     Region.
    2. If you choose **Create new bucket**, type in the
     **new bucket name**. After the bucket is created, you can
     modify the BPA (Block Public Access) and S3 versioning default settings.

8. For the encryption of objects in your S3 bucket, you can choose your
   **Restored object encryption**. Use **original encryption
   keys** (default), **Amazon S3 key (SSE-S3)**, or
   **AWS Key Management Service key (SSE-KMS)**.

These settings only apply to encryption of the objects in the S3 bucket. This does
not affect the encryption for the bucket itself.

    1. **Use original encryption keys (default)** restores objects
     with the same encryption keys used by the source object. If a source object was
     unencrypted, this method restores the object without encryption.


    This restore option allows you to optionally choose a substitute encryption
     key to encrypt the restore object(s) if the original key is unavailable.
    2. If you choose **Amazon S3 key (SSE-S3)**, you do not need to
     specify any other options.
    3. If you choose **AWS Key Management Service key (SSE-KMS)**, you can make the
     following choices: **AWS managed key (aws/s3)**,
     **Choose from your AWS KMS keys**, or **Enter AWS KMS key
     ARN**.


    	1. If you choose **AWS managed key (aws/s3)**, you do not
    	 need to specify any other options.
    	2. If you **Choose from your AWS KMS keys**, select a AWS KMS
    	 key from the dropdown menu. Alternatively, choose **Create
    	 key**.
    	3. If you **Enter AWS KMS key ARN**, type in the ARN into the
    	 text box. Alternatively, choose **Create key**.

9. In the **Restore role** pane, choose the IAM role that AWS Backup
   will assume for this restore.
10. Choose **Restore backup**. The **Restore jobs**
    pane appears. A message at the top of the page provides information about the restore
    job.

## Restore Amazon S3 recovery points through AWS CLI

Use `StartRestoreJob`. You can specify the following metadata during Amazon S3
restores:

```
// Mandatory metadata:
DestinationBucketName // The destination bucket for your restore.

// Optional metadata:
RestoreACLs // Boolean. If ACLs were part of the backup, include and set to TRUE. If the backup
does not include ACLs and this parameter is included, set to FALSE.
EncryptionType // The type of encryption to encrypt your restored objects. Options are `original` (same encryption as the original object), `SSE-S3`, or `SSE-KMS`).
ItemsToRestore // A list of up to five paths of individual objects to restore. Only required for item-level restore.
KMSKey // Specifies the SSE-KMS key to use. Only needed if encryption is SSE-KMS.
RestoreLatestVersionsUpTo // Include this optional parameter to multiple versions.
RestoreTime // The restore time (only valid for continuous recovery points where it is required, in format 2021-11-27T03:30:27Z).

```

`RestoreLatestVersionsUpTo` is an optional metadata key-value pair. By
default, or if this is omitted, the latest version is restored. Include this metadata to
restore additional versions of your objects. Accepted values are:

- `1` (to restore the latest version)
- `*n*` , where _n_ is any positive
  integer greater than 1. The latest _n_ versions of your objects
  will be restored. If the actual version count of an object is less than
  _n_, that number of versions will be restored for that
  object.
- `all` (to restore all versions)

## Recovery point status

Recovery points will have a status indicating their state.

`EXPIRED` status indicates that the recovery point has exceeded its
retention period, but AWS Backup lacks permission or is otherwise unable to delete
it. To manually delete these recovery points, see [Step 3:
Delete the recovery points](gs-cleanup-resources.md#cleanup-backups "gs-cleanup-resources.md#cleanup-backups") in the _Clean up resources_
section of _Getting started_.

`STOPPED` status occurs on a continuous backup where a user has taken some
action that causes the continuous backup to be disabled. This can be caused by the removal
of permissions, turning off versioning, turning off events being sent to Amazon EventBridge, or
disabling the EventBridge rules that are put in place by AWS Backup.

To resolve `STOPPED` status, ensure that all requested permissions are in
place and that versioning is enabled on the S3 bucket. Once these conditions are met, the
next instance of a backup rule running will result in a new continuous recovery point
being created. The recovery points with STOPPED status do not need to be deleted.

## S3 restore messages

When a restore job completes or fails, you may see the following message. The
following table can help you determine the possible cause of the status message.

| Scenario                                                 | Job Status | Message                                                                                                                                                          | Example                                                                                                                                                                                                                    |
| -------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All objects failed to be restored.                       | `FAILED`   | "No objects were restored from<br>`*RecoveryPointARN*` to<br>`*bucket*`. To get notified of<br>these failures, enable SNS event notifications."                  | The role used to start the restore job does not have permission to put<br>objects in the destination bucket.<br>The restore role does not have permission to verify if object version exists<br>in the destination bucket. |
| One or more (but not all) objects failed to be restored. | COMPLETED  | "One or more objects failed to be restored from<br>`*RecoveryPointARN*` to<br>`*bucket*`. To get notified of<br>these failures, enable SNS event notifications." | The role used to start the restore job does not have access to the KMS key<br>used by one or more of the original objects.                                                                                                 |
| There are no objects to restore.                         | COMPLETED  | "There are no objects that match the restore request for<br>`*RecoveryPointARN*`."                                                                               | The recovery point (backup) of source bucket to be restored has no<br>objects.<br>The prefix used for the restore job does not correspond with any<br>object.                                                              |

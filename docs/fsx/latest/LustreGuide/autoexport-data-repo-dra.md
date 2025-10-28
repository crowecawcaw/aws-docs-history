# Automatically export updates to your S3

bucket

You can configure your FSx for Lustre file system to automatically update the contents of a
linked S3 bucket as files are added, changed, or deleted on the file system. FSx for Lustre creates,
updates, or deletes the object in S3, corresponding to the change in the file system.

###### Note

Automatic export isn't available on FSx for Lustre 2.10 file systems or `Scratch 1`
file systems.

You can export to a data repository that is in the same AWS Region as the file system
or in a different AWS Region.

You can configure automatic export when you create the data repository association and
update the automatic export settings at any time using the FSx management console, the AWS CLI,
and the AWS API.

###### Important

- If a file is modified in the file system with all automatic export policies
  enabled and automatic import disabled, the content of that file is always exported to a
  corresponding object in S3. If an object already exists in the target location, the object
  is overwritten.
- If a file is modified in both the file system and S3, with all automatic import
  and automatic export policies enabled, either the file in the file system or the object in S3
  could be overwritten by the other. It isn't guaranteed that a later edit in one location will
  overwrite an earlier edit in another location. If you modify the same file in both the file
  system and the S3 bucket, you should ensure application-level coordination to prevent such
  conflicts. FSx for Lustre doesn't prevent conflicting writes in multiple locations.
  The export policy specifies how you want FSx for Lustre to update your linked S3 bucket as the
  contents change in the file system. A data repository association can have one of the following automatic export policies:

- **New** – FSx for Lustre automatically updates the S3 data repository
  only when a new file, directory, or symlink is created on the file system.
- **Changed** – FSx for Lustre automatically updates the S3
  data repository only when an existing file in the file system is changed. For file
  content changes, the file must be closed before it's propagated to the S3 repository.
  Metadata changes (rename, ownership, permissions, and timestamps) are propagated when
  the operation is done. For renaming changes (including moves), the existing (pre-renamed)
  S3 object is deleted and a new S3 object is created with the new name.
- **Deleted** – FSx for Lustre automatically updates the S3
  data repository only when a file, directory, or symlink is deleted in the file system.
- **Any combination of New, Changed, and Deleted** – FSx for Lustre
  automatically updates the S3 data repository when any of the specified actions occur in
  file system. For example, you can specify that the S3 repository is updated when a file
  is added to (**New**) or removed from (**Deleted**) the
  file system, but not when a file is changed.
- **No policy configured** – FSx for Lustre doesn't automatically
  update the S3 data repository when files are added to, changed in, or deleted from the file
  system. If you don't configure an export policy, automatic export is disabled. You can
  still manually export changes by using an export data repository task, as described in
  [Using data repository tasks to export changes](export-data-repo-task-dra.md "export-data-repo-task-dra.md").
  For most use cases, we recommend that you configure an export policy of **New**,
  **Changed**, and **Deleted**. This policy ensures that
  all updates made on your file system are automatically exported to your linked S3 data repository.

We recommend that you [turn on logging](cw-event-logging.md#manage-logging "cw-event-logging.md#manage-logging") to CloudWatch Logs to
log information about any files or directories that couldn't be exported automatically.
Warnings and errors in the log contain information about the failure reason. For more
information, see [Data repository event logs](data-repo-event-logs.md "data-repo-event-logs.md").

###### Note

While access time (`atime`) and modification time (`mtime`) are
synchronized with S3 during export operations, changes to these timestamps alone do not
trigger automatic export. Only changes to file content or other metadata (such as ownership
or permissions) will trigger an automatic export to S3.

## Updating export settings

You can set a file system's export settings to a linked S3 bucket when you create the
data repository association. For more information, see [Creating a link to an S3 bucket](create-linked-dra.md "create-linked-dra.md").

You can also update the export settings at any time, including the export policy. For
more information, see [Updating data repository association settings](update-dra-settings.md "update-dra-settings.md").

## Monitoring automatic export

You can monitor automatic export enabled data repository associations using
a set of metrics published to Amazon CloudWatch. The `AgeOfOldestQueuedMessage`
metric represents the age of the oldest update made to the file system which has
not yet been exported to S3. If the `AgeOfOldestQueuedMessage` is greater
than zero for an extended period of time, we recommend temporarily reducing the number
of changes (directory renames in particular) that are actively being made to the
file system until the message queue has been reduced. For more information, see
[FSx for Lustre S3 repository metrics](fs-metrics.md#auto-import-export-metrics "fs-metrics.md#auto-import-export-metrics").

###### Important

When deleting a data repository association or file system with automatic export
enabled, you should first make sure that `AgeOfOldestQueuedMessage` is zero,
meaning that there are no changes that have not yet been exported. If
`AgeOfOldestQueuedMessage` is greater than zero when you delete your
data repository association or file system, the changes that had not yet been
exported will not reach your linked S3 bucket. To avoid this, wait for
`AgeOfOldestQueuedMessage` to reach zero before deleting your
data repository association or file system.

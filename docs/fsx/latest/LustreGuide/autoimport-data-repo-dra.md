# Automatically import updates from your S3

bucket

You can configure FSx for Lustre to automatically update metadata in the file system as
objects are added to, changed in, or deleted from your S3 bucket. FSx for Lustre creates,
updates, or deletes the file and directory listing, corresponding to the change in S3.
If the changed object in the S3 bucket no longer contains its metadata, FSx for Lustre
maintains the current metadata values of the file, including the current permissions.

###### Note

The FSx for Lustre file system and the linked S3 bucket must be located in the same
AWS Region to automatically import updates.

You can configure automatic import when you create the data repository association,
and you can update the automatic import settings at any time using the FSx management
console, the AWS CLI, or the AWS API.

###### Note

You can configure both automatic import and automatic export on the same data
repository association. This topic describes only the automatic import feature.

###### Important

- If an object is modified in S3 with all automatic import policies
  enabled and automatic export disabled, the content of that object is always imported
  to a corresponding file in the file system. If a file already exists in the target
  location, the file is overwritten.
- If a file is modified in both the file system and S3, with all automatic
  import and automatic export policies enabled, either the file in the file system or the
  object in S3 could be overwritten by the other. It isn't guaranteed that a later edit in
  one location will overwrite an earlier edit in another location. If you modify the same
  file in both the file system and the S3 bucket, you should ensure application-level
  coordination to prevent such conflicts. FSx for Lustre doesn't prevent conflicting writes
  in multiple locations.
  The import policy specifies how you want FSx for Lustre to update your file system
  as the contents change in the linked S3 bucket. A data repository association can have one of the following
  import policies:

- **New** – FSx for Lustre automatically updates file and directory
  metadata only when new objects are added to the linked S3 data repository.
- **Changed** – FSx for Lustre automatically updates file and directory
  metadata only when an existing object in the data repository is changed.
- **Deleted** – FSx for Lustre automatically updates file
  and directory metadata only when an object in the data repository is deleted.
- **Any combination of New, Changed, and Deleted** – FSx for Lustre
  automatically updates file and directory metadata when any of the specified actions
  occur in the S3 data repository. For example, you can specify that the file system
  is updated when an object is added to (**New**) or removed from
  (**Deleted**) the S3 repository, but not updated when an object
  is changed.
- **No policy configured** – FSx for Lustre doesn't update
  file and directory metadata on the file system when objects are added to, changed in,
  or deleted from the S3 data repository. If you don't configure an import policy,
  automatic import is disabled for the data repository association. You can still manually import metadata
  changes by using an import data repository task, as described in
  [Using data repository tasks to import changes](import-data-repo-task-dra.md "import-data-repo-task-dra.md").

###### Important

Automatic import will not synchronize the following S3 actions with
your linked FSx for Lustre file system:

- Deleting an object using S3 object lifecycle expirations
- Permanently deleting the current object version in a versioning-enabled bucket
- Undeleting an object in a versioning-enabled bucket
  For most use cases, we recommend that you configure an import policy of **New**,
  **Changed**, and **Deleted**. This policy ensures that
  all updates made in your linked S3 data repository are automatically imported to your file
  system.

When you set an import policy to update your file system file and directory metadata
based on changes in the linked S3 data repository, FSx for Lustre creates an event notification
configuration on the linked S3 bucket. The event notification configuration is named
`FSx`. Don't modify or delete the `FSx` event notification configuration
on the S3 bucket – doing so will prevent the automatic import of updated file and directory metadata
to your file system.

When FSx for Lustre updates a file listing that has changed on the linked S3 data repository, it
overwrites the local file with the updated version, even if the file is write-locked.

FSx for Lustre makes a best effort to update your file system. FSx for Lustre cannot update the
file system in the following situations:

- If FSx for Lustre doesn't have permission to open the changed or new S3 object. In this case,
  FSx for Lustre skips the object and continues. The DRA lifecycle state isn't affected.
- If FSx for Lustre doesn't have bucket-level permissions, such as for `GetBucketAcl`.
  This will cause the data repository lifecycle state to become **Misconfigured**.
  For more information, see [Data repository association lifecycle state](dra-lifecycles.md "dra-lifecycles.md").
- If the `FSx` event notification configuration on the linked S3 bucket is
  deleted or changed. This will cause the data repository lifecycle state to become
  **Misconfigured**. For more information, see [Data repository association lifecycle state](dra-lifecycles.md "dra-lifecycles.md").
  We recommend that you [turn on logging](cw-event-logging.md#manage-logging "cw-event-logging.md#manage-logging") to CloudWatch Logs to
  log information about any files or directories that couldn't be imported automatically.
  Warnings and errors in the log contain information about the failure reason. For more information,
  see [Data repository event logs](data-repo-event-logs.md "data-repo-event-logs.md").

## Prerequisites

The following conditions are required for FSx for Lustre to automatically import new,
changed, or deleted files from the linked S3 bucket:

- The file system and its linked S3 bucket are located in the same
  AWS Region.
- The S3 bucket doesn't have a misconfigured **Lifecycle state**.
  For more information, see
  [Data repository association lifecycle state](dra-lifecycles.md "dra-lifecycles.md").
- Your account has the permissions required to configure and receive event
  notifications on the linked S3 bucket.

## Types of file changes supported

FSx for Lustre supports importing the following changes to files and directories that
occur in the linked S3 bucket:

- Changes to file contents.
- Changes to file or directory metadata.
- Changes to symlink target or metadata.
- Deletions of files and directories. If you delete an object in the linked S3 bucket
  which corresponds to a directory in the file system (that is, an object with a key name
  that ends with a slash), FSx for Lustre deletes the corresponding directory on the file system
  only if it is empty.

## Updating import settings

You can set a file system's import settings for a linked S3 bucket when you create the
data repository association. For more information, see [Creating a link to an S3 bucket](create-linked-dra.md "create-linked-dra.md").

You can also update the import settings at any time, including the import policy. For
more information, see [Updating data repository association settings](update-dra-settings.md "update-dra-settings.md").

## Monitoring automatic import

If the rate of change in your S3 bucket exceeds the rate at which automatic import
can process these changes, the corresponding metadata changes being imported to
your FSx for Lustre file system are delayed. If this occurs, you can use the
`AgeOfOldestQueuedMessage` metric to monitor the age of the oldest change
waiting to be processed by automatic import. For more information on this metric,
see [FSx for Lustre S3 repository metrics](fs-metrics.md#auto-import-export-metrics "fs-metrics.md#auto-import-export-metrics").

If the delay in importing metadata changes exceeds 14 days (as measured using the
`AgeOfOldestQueuedMessage` metric), changes in your S3 bucket that haven't
been processed by automatic import aren't imported into your file system. Additionally,
your data repository association lifecycle is marked as **MISCONFIGURED**
and automatic import is stopped. If you have automatic export enabled, automatic export
continues monitoring your FSx for Lustre file system for changes. However, additional changes
aren't synchronized from your FSx for Lustre file system to S3.

To return your data repository association from the **MISCONFIGURED**
lifecycle state to the **AVAILABLE** lifecycle state, you must update
your data repository association. You can update your data repository association using
the [update-data-repository-association](../../../cli/latest/reference/fsx/update-data-repository-association.md "../../../cli/latest/reference/fsx/update-data-repository-association.md") CLI command (or the corresponding
[UpdateDataRepositoryAssociation](../APIReference/API_UpdateDataRepositoryAssociation.md "../APIReference/API_UpdateDataRepositoryAssociation.md") API operation). The only request parameter
that you need is the `AssociationID` of the data repository association
that you want to update.

After the data repository association lifecycle state changes to **AVAILABLE**,
automatic import (and automatic export if enabled) restarts. Upon restarting, automatic export resumes
synchronizing file system changes to S3. To synchronize the metadata of new and changed objects in
S3 with your FSx for Lustre file system that weren't imported or are from when the data repository
association was in a misconfigured state, run an
[import data repository task](import-data-repo-task-dra.md "import-data-repo-task-dra.md"). Import data repository
tasks don't synchronize deletes in your S3 bucket with your FSx for Lustre file system. If you want to
fully synchronize S3 with your file system (including deletes), you must re-create your file system.

To ensure that delays to importing metadata changes don't exceed 14 days, we recommend that
you set an alarm on the `AgeOfOldestQueuedMessage` metric and reduce activity
in your S3 bucket if the `AgeOfOldestQueuedMessage` metric grows beyond your alarm threshold.
For an FSx for Lustre file system connected to an S3 bucket with a single shard continuously sending
the maximum number of possible changes from S3, with only automatic import running on the FSx for Lustre
file system, automatic import can process a 7-hour backlog of S3 changes within 14 days.

Additionally, with a single S3 action, you can generate more changes than automatic import
will ever process in 14 days. Examples of these types of actions include, but are not limited to,
AWS Snowball uploads to S3 and large-scale deletions. If you make a large-scale change
to your S3 bucket that you want synchronized with your FSx for Lustre file system, to prevent
automatic import changes from exceeding 14 days, you should delete your file system and re-create
it once the S3 change has completed.

If your `AgeOfOldestQueuedMessage` metric is growing, review your S3 bucket
`GetRequests`, `PutRequests`, `PostRequests`, and `DeleteRequests`
metrics for activity changes that would cause an increase in the rate and/or number of changes being sent
to automatic import. For information about available S3 metrics, see
[Monitoring Amazon S3](../../../AmazonS3/latest/userguide/monitoring-overview.md "../../../AmazonS3/latest/userguide/monitoring-overview.md") in the _Amazon S3 User Guide_.

For a list of all available FSx for Lustre metrics, see
[Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

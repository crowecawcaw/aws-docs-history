# Resolving tag-sync errors in myApplications

This section describes common tag-sync errors and how to resolve them. After attempting to resolve the error,
you can retry the failed tag-sync task.

- **Insufficient permissions** — You do not have the required minimum
  permissions to start, update, or cancel the tag-sync. Review [Tag-sync required
  permissions](../../../servicecatalog/latest/arguide/app-tag-sync.md#tag-sync-role "../../../servicecatalog/latest/arguide/app-tag-sync.md#tag-sync-role") for more information. After ensuring the role you specify to perform the tag-sync has the
  minimum required permissions, retry the failed tag-sync task.
- **Already exists** — A task with this tag key-value pair
  already exists for this application. An application can support more than one tag-sync, but each tag-sync must
  have a different tag key-value pair. After you specify a different tag key-value pair, retry the failed
  tag-sync task.
- **Maximum limit reached** — You have reached the maximum of 100 tag-sync tasks per account,
  across all applications.

# Using data repository tasks to export changes

The export data repository task exports files that are new or changed in your file system.
It creates a new object in S3 for any new file on the file system. For any file that has been
modified on the file system, or whose metadata has been modified, the corresponding object in
S3 is replaced with a new object with the new data and metadata. No action is taken for files
that have been deleted from the file system.

###### Note

Keep the following in mind when using export data repository tasks:

- The use of wildcards to include or exclude files for export isn't supported.
- When performing `mv` operations, the target file after being moved
  will be exported to S3 even if there is no UID, GID, permission, or content change.
  Use the following procedures to export data and metadata changes on the file system to
  linked S3 buckets by using the Amazon FSx console and CLI. Note that you can use one data repository
  task for multiple DRAs.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. On the navigation pane, choose **File systems**, then choose
   your Lustre file system.
3. Choose the **Data repository** tab.
4. In the **Data repository associations** pane, choose the data
   repository association you want to create the export task for.
5. For **Actions**, choose **Export task**. This
   choice isn't available if the file system isn't linked to a data repository on S3. The
   **Create export data repository task** dialog appears.
6. (Optional) Specify up to 32 directories or files to export from your Amazon FSx file
   system by providing the paths to those directories or files in **File system
   paths to export**. The paths you provide need to be relative to the mount
   point of the file system. If the mount point is `/mnt/fsx` and
   `/mnt/fsx/path1` is a directory or file on the file system you want to
   export, then the path to provide is `path1`.

###### Note

If a path that you provide isn't valid, the task fails. 7. (Optional) Choose **Enable** under **Completion
report** to generate a task completion report after the task completes. A
_task completion report_ provides details about
the files processed by the task that meet the scope provided in **Report
scope**. To specify the location for Amazon FSx to deliver the report, enter a
relative path on the file system's linked S3 data repository for
**Report path**. 8. Choose **Create**.

A notification at the top of the **File systems** page shows
the task that you just created in progress.
To view the task status and details, scroll down to the **Data Repository
Tasks** pane in the **Data Repository** tab for the file
system. The default sort order shows the most recent task at the top of the list.

To view a task summary from this page, choose **Task ID** for the
task you just created. The **Summary** page for the task
appears.

- Use the [`create-data-repository-task`](../../../cli/latest/reference/fsx/create-data-repository-task.md "../../../cli/latest/reference/fsx/create-data-repository-task.md") CLI command to export data and
  metadata changes on your FSx for Lustre file system. The corresponding API operation is
  [`CreateDataRepositoryTask`](../APIReference/API_CreateDataRepositoryTask.md "../APIReference/API_CreateDataRepositoryTask.md").

```
`$` aws fsx create-data-repository-task \
    --file-system-id fs-0123456789abcdef0 \
    --type EXPORT_TO_REPOSITORY \
    --paths path1,path2/file1 \
    --report Enabled=true
```

After successfully creating the data repository task, Amazon FSx returns the task
description as JSON, as shown in the following example.

```
{
    "Task": {
        "TaskId": "task-123f8cd8e330c1321",
        "Type": "EXPORT_TO_REPOSITORY",
        "Lifecycle": "PENDING",
        "FileSystemId": "fs-0123456789abcdef0",
        "Paths": ["path1", "path2/file1"],
        "Report": {
            "Path":"s3://dataset-01/reports",
            "Format":"REPORT_CSV_20191124",
            "Enabled":true,
            "Scope":"FAILED_FILES_ONLY"
        },
        "CreationTime": "1545070680.120",
        "ClientRequestToken": "10192019-drt-12",
        "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:task:task-123f8cd8e330c1321"
    }
}
```

After creating the task to export data to the linked data repository, you can check the
status of the export data repository task. For more information about viewing data repository
tasks, see [Accessing data repository tasks](view-data-repo-tasks.md "view-data-repo-tasks.md").

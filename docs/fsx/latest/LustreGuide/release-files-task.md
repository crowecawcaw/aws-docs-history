# Using data repository tasks to release files

Use the following procedures to create tasks that release files from the
file system by using the Amazon FSx console and CLI. Releasing a file retains the file
listing and metadata, but removes the local copy of that file's contents.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**, then
   choose your Lustre file system.
3. Choose the **Data repository** tab.
4. In the **Data repository associations** pane, choose the data
   repository association that you want to create the release task for.
5. For **Actions**, choose **Create release
   task**. This choice is available only if the file system is
   linked to a data repository on S3. The **Create release data repository
   task** dialog appears.
6. In **File system paths to release**, specify up to 32 directories
   or files to release from your Amazon FSx file system by providing the paths to those
   directories or files. The paths that you provide must be relative to the mount point
   of the file system. For example, if the mount point is `/mnt/fsx` and
   `/mnt/fsx/path1` is a file on the file system that you want to release,
   then the path to provide is `path1`. To release all files in the file system,
   specify a forward slash (/) as the path.

###### Note

If a path that you provide isn't valid, the task fails. 7. For **Minimum duration since last access**, specify the
the duration, in days, such that any file not accessed in that duration should
be released. Last access time is calculated using the maximum value of
`atime`, `mtime`, and `ctime`. Files with
a last access duration period greater than minimum duration since last access
(relative to the task create time) will be released. Files with a last access
duration period less than this number of days won't be released, even if they
are in the **File system paths to release** field. Provide
a duration of `0` days to release files independent of duration
since last access. 8. (Optional) Under **Completion report**, choose
**Enable** to generate a task completion report that
provides details about the files that meet the scope provided in
**Report scope**. To specify a location for Amazon FSx
to deliver the report, enter a relative path on the file system's
linked S3 data repository for **Report path**. 9. Choose **Create data repository task**.

A notification at the top of the **File systems** page shows
the task that you just created in progress.
To view the task status and details, in the **Data Repository**
tab, scroll down to **Data Repository Tasks**. The default sort order
shows the most recent task at the top of the list.

To view a task summary from this page, choose **Task ID** for the
task you just created.

- Use the [`create-data-repository-task`](../../../cli/latest/reference/fsx/create-data-repository-task.md "../../../cli/latest/reference/fsx/create-data-repository-task.md") CLI command to create a task
  that releases files on your FSx for Lustre file system. The corresponding API operation is
  [`CreateDataRepositoryTask`](../APIReference/API_CreateDataRepositoryTask.md "../APIReference/API_CreateDataRepositoryTask.md").

Set the following parameters:

    + Set `--file-system-id` to the ID of the file system that you are
     releasing files from.
    + Set `--paths` to the paths on the file system from which the data
     will be released. If a directory is specified, files within the directory are
     released. If a file path is specified, only that file is released. To release all
     files in the file system that been exported to a linked S3 bucket, specify a forward
     slash (/) for the path.
    + Set `--type` to `RELEASE_DATA_FROM_FILESYSTEM`.
    + Set the `--release-configuration DurationSinceLastAccess` options
     as follows:




    	- `Unit` – Set to `DAYS`.
    	- `Value` – Specify an integer that represents the
    	 the duration, in days, such that any file not accessed in that duration should be released.
    	 Files that were accessed during a period less than this number of days won't be released,
    	 even if they are in the `--paths` parameter. Provide a duration of `0`
    	 days to release files independent of duration since last access.

This sample command specifies that files that been exported to a linked S3 bucket
and meet the `--release-configuration` criteria will be released from the
directories in the specified paths.

```
`$` aws fsx create-data-repository-task \
    --file-system-id fs-0123456789abcdef0 \
    --type RELEASE_DATA_FROM_FILESYSTEM \
    --paths path1,path2/file1 \
    --release-configuration '{"DurationSinceLastAccess":{"Unit":"DAYS","Value":10}}' \
    --report Enabled=false
```

After successfully creating the data repository task, Amazon FSx returns the task
description as JSON.
After creating the task to release files, you can check the
status of the task. For more information about viewing data repository tasks, see [Accessing data repository tasks](view-data-repo-tasks.md "view-data-repo-tasks.md").

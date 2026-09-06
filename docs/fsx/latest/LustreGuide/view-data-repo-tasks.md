

# Accessing data repository tasks
<a name="view-data-repo-tasks"></a>

After you create a data repository task, you can access the task, and all existing tasks in your account, using the Amazon FSx console, CLI, and API. Amazon FSx provides the following detailed task information: 
+ All existing tasks.
+ All tasks for a specific file system.
+ All tasks for a specific data repository association.
+ All tasks with a specific lifecycle status. For more information about task lifecycle status values, see [Understanding a task's status and details](data-repo-task-status.md).

You can access all existing data repository tasks in your account by using the Amazon FSx console, CLI, or API, as described following.

## To view data repository tasks and task details (console)
<a name="access-all-tasks-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. On the navigation pane, choose the file system that you want to view data repository tasks for. The file system details page appears.

1. On the file system details page, choose the **Data repository** tab. Any tasks for this file system appear on the **Data repository tasks** panel.

1. To see a task's details, choose **Task ID** or **Task name** in the **Data repository tasks** panel. The task detail page appears.  
![Data repository tasks page](http://docs.aws.amazon.com/fsx/latest/LustreGuide/images/task-details-rprt.png)

## To retrieve data repository tasks and task details (CLI)
<a name="task-details-cli"></a>

Using the Amazon FSx [`describe-data-repository-tasks`](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-data-repository-tasks.html) CLI command, you can view all the data repository tasks, and their details, in your account. [`DescribeDataRepositoryTasks`](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeDataRepositoryTasks.html) is the equivalent API command.
+ Use the following command to view all data repository task objects in your account.

  ```
  aws fsx describe-data-repository-tasks
  ```

  If the command is successful, Amazon FSx returns the response in JSON format.

  ```
  {
      "DataRepositoryTasks": [
          {
              "Lifecycle": "EXECUTING",
              "Paths": [],
              "Report": {
                  "Path":"s3://dataset-01/reports",
                  "Format":"REPORT_CSV_20191124",
                  "Enabled":true,
                  "Scope":"FAILED_FILES_ONLY"
              },
              "StartTime": 1591863862.288,
              "EndTime": ,
              "Type": "EXPORT_TO_REPOSITORY",
              "Tags": [],
              "TaskId": "task-0123456789abcdef3",
              "Status": {
                  "SucceededCount": 4255,
                  "TotalCount": 4200,
                  "FailedCount": 55,
                  "LastUpdatedTime": 1571863875.289
              },
              "FileSystemId": "fs-0123456789a7",
              "CreationTime": 1571863850.075,
              "ResourceARN": "arn:aws:fsx:us-east-1:1234567890:task/task-0123456789abcdef3"
          },
          {
              "Lifecycle": "FAILED",
              "Paths": [],
              "Report": {
                  "Enabled": false,
              },
              "StartTime": 1571863862.288,
              "EndTime": 1571863905.292,
              "Type": "EXPORT_TO_REPOSITORY",
              "Tags": [],
              "TaskId": "task-0123456789abcdef1",
              "Status": {
                  "SucceededCount": 1153,
                  "TotalCount": 1156,
                  "FailedCount": 3,
                  "LastUpdatedTime": 1571863875.289
              },
              "FileSystemId": "fs-0123456789abcdef0",
              "CreationTime": 1571863850.075,
              "ResourceARN": "arn:aws:fsx:us-east-1:1234567890:task/task-0123456789abcdef1"
          },
          {
              "Lifecycle": "SUCCEEDED",
              "Paths": [],
              "Report": {
                  "Path":"s3://dataset-04/reports",
                  "Format":"REPORT_CSV_20191124",
                  "Enabled":true,
                  "Scope":"FAILED_FILES_ONLY"
              },
              "StartTime": 1571863862.288,
              "EndTime": 1571863905.292,
              "Type": "EXPORT_TO_REPOSITORY",
              "Tags": [],
              "TaskId": "task-04299453935122318",
              "Status": {
                  "SucceededCount": 258,
                  "TotalCount": 258,
                  "FailedCount": 0,
                  "LastUpdatedTime": 1771848950.012,
              },
              "FileSystemId": "fs-0123456789abcdef0",
              "CreationTime": 1771848950.012,
              "ResourceARN": "arn:aws:fsx:us-east-1:1234567890:task/task-0123456789abcdef0"
          }
      ]
  }
  ```

## Viewing tasks by file system
<a name="view-tasks-by-fs"></a>

You can view all tasks for a specific file system using the Amazon FSx console, CLI, or API, as described following.

### To view tasks by file system (console)
<a name="tasks-by-fs-console"></a>

1. Choose **File systems** on the navigation pane. The **File systems** page appears.

1. Choose the file system that you want to view data repository tasks for. The file system details page appears.

1. On the file system details page, choose the **Data repository** tab. Any tasks for this file system appear on the **Data repository tasks** panel.

### To retrieve tasks by file system (CLI)
<a name="task-by-fs-cli"></a>
+ Use the following command to view all data repository tasks for file system `fs-0123456789abcdef0`.

  ```
  aws fsx describe-data-repository-tasks \
      --filters Name=file-system-id,Values=fs-0123456789abcdef0
  ```

  If the command is successful, Amazon FSx returns the response in JSON format.

  ```
  {
      "DataRepositoryTasks": [
          {
              "Lifecycle": "FAILED",
              "Paths": [],
              "Report": {
                  "Path":"s3://dataset-04/reports",
                  "Format":"REPORT_CSV_20191124",
                  "Enabled":true,
                  "Scope":"FAILED_FILES_ONLY"
              },
              "StartTime": 1571863862.288,
              "EndTime": 1571863905.292,
              "Type": "EXPORT_TO_REPOSITORY",
              "Tags": [],
              "TaskId": "task-0123456789abcdef1",
              "Status": {
                  "SucceededCount": 1153,
                  "TotalCount": 1156,
                  "FailedCount": 3,
                  "LastUpdatedTime": 1571863875.289
              },
              "FileSystemId": "fs-0123456789abcdef0",
              "CreationTime": 1571863850.075,
              "ResourceARN": "arn:aws:fsx:us-east-1:1234567890:task/task-0123456789abcdef1"
          },
          {
              "Lifecycle": "SUCCEEDED",
              "Paths": [],
              "Report": {
                  "Enabled": false,
              },
              "StartTime": 1571863862.288,
              "EndTime": 1571863905.292,
              "Type": "EXPORT_TO_REPOSITORY",
              "Tags": [],
              "TaskId": "task-0123456789abcdef0",
              "Status": {
                  "SucceededCount": 258,
                  "TotalCount": 258,
                  "FailedCount": 0,
                  "LastUpdatedTime": 1771848950.012,
              },
              "FileSystemId": "fs-0123456789abcdef0",
              "CreationTime": 1771848950.012,
              "ResourceARN": "arn:aws:fsx:us-east-1:1234567890:task/task-0123456789abcdef0"
          }
      ]
  }
  ```
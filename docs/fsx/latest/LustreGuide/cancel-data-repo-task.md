

# Canceling a data repository task
<a name="cancel-data-repo-task"></a>

You can cancel a data repository task while it's in either the PENDING or EXECUTING state. When you cancel a task, the following occurs:
+ Amazon FSx doesn't process any files that are in the queue to be processed.
+ Amazon FSx continues processing any files that are currently in process.
+ Amazon FSx doesn't revert any files that the task already processed.

## To cancel a data repository task (console)
<a name="w2aac13c33c17c13b7b1"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Click on the file system for which you want to cancel a data repository task.

1. Open the **Data Repository** tab and scroll down to view the **Data Repository Tasks** panel.

1. Choose **Task ID** or **Task name** for the task that you want to cancel.

1. Choose **Cancel task** to cancel the task.

1. Enter the task ID to confirm the cancellation request.

## To cancel a data repository task (CLI)
<a name="w2aac13c33c17c13b7b3"></a>

Use the Amazon FSx [`cancel-data-repository-task`](https://docs.aws.amazon.com/cli/latest/reference/fsx/cancel-data-repository-task.html) CLI command, to cancel a task. [`CancelDataRepositoryTask`](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CancelDataRepositoryTask.html) is the equivalent API command.
+ Use the following command to cancel a data repository task.

  ```
  aws fsx cancel-data-repository-task \
      --task-id task-0123456789abcdef0
  ```

  If the command is successful, Amazon FSx returns the response in JSON format.

  ```
  {
      "Status": "CANCELING",
      "TaskId": "task-0123456789abcdef0"
  }
  ```
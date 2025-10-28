# Canceling a data repository task

You can cancel a data repository task while it's in either the PENDING or EXECUTING state.
When you cancel a task, the following occurs:

- Amazon FSx doesn't process any files that are in the queue to be processed.
- Amazon FSx continues processing any files that are currently in process.
- Amazon FSx doesn't revert any files that the task already processed.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Click on the file system for which you want to cancel a data repository task.
3. Open the **Data Repository** tab and scroll down to view the
   **Data Repository Tasks** panel.
4. Choose **Task ID** or **Task name** for the task that you
   want to cancel.
5. Choose **Cancel task** to cancel the task.
6. Enter the task ID to confirm the cancellation request.
   Use the Amazon FSx [`cancel-data-repository-task`](../../../cli/latest/reference/fsx/cancel-data-repository-task.md "../../../cli/latest/reference/fsx/cancel-data-repository-task.md") CLI command,
   to cancel a task. [`CancelDataRepositoryTask`](../APIReference/API_CancelDataRepositoryTask.md "../APIReference/API_CancelDataRepositoryTask.md") is the equivalent API command.

- Use the following command to cancel a data repository task.

```
aws fsx cancel-data-repository-task \
    --task-id task-0123456789abcdef0
```

If the command is successful, Amazon FSx returns the response in JSON format.

```
`{
 "Status": "CANCELING",
 "TaskId": "task-0123456789abcdef0"
}`
```

# Setting bandwidth limits for your AWS DataSync

task

You can configure network bandwidth limits for your AWS DataSync task and each of its
executions.

###### Note

Not applicable to
[Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

## Limiting bandwidth for a task

Set a bandwidth limit when creating, editing, or starting a task.

The following instructions describe how to configure a bandwidth limit for
your task when you're creating it.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. For **Bandwidth limit**, choose one of the
following:

    * Select **Use available** to use all of
     the available network bandwidth for each task
     execution.
    * Select **Set bandwidth limit (MiB/s)**
     and enter the maximum bandwidth that you want DataSync to use
     for each task execution.

You can configure a task's bandwidth limit by using the
`BytesPerSecond` parameter with any of the following
operations:

- [CreateTask](API_CreateTask.md "API_CreateTask.md")
- [UpdateTask](API_UpdateTask.md "API_UpdateTask.md")
- [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md")

## Throttling bandwidth for a task

execution

You can modify the bandwidth limit for a running or queued task execution.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the navigation pane, expand **Data transfer**.
   then choose **Tasks**.
3. Choose the task and then select **History** to
   view the task's executions.
4. Choose the task execution that you want to modify and then choose
   **Edit**.
5. In the dialog box, choose one of the following:
   - Select **Use available** to use all of
     the available network bandwidth for the task
     execution.
   - Select **Set bandwidth limit (MiB/s)**
     and enter the maximum bandwidth that you want DataSync to use
     for the task execution.

6. Choose **Save changes**.

The new bandwidth limit takes effect within 60 seconds.
You can modify the bandwidth limit for a running or queued task execution
by using the `BytesPerSecond` parameter with the [UpdateTaskExecution](API_UpdateTaskExecution.md "API_UpdateTaskExecution.md") operation.

# Starting a task to transfer your data

Once you create your AWS DataSync transfer task, you can start moving data. Each run of a
task is called a _task execution_. For information about what happens
during a task execution, see [How DataSync transfers files, objects, and
directories](how-datasync-transfer-works.md#transferring-files "how-datasync-transfer-works.md#transferring-files").

###### Important

If you're planning to transfer data to or from an Amazon S3 location, review [how DataSync can affect your S3 request charges](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests") and the [DataSync pricing page](https://aws.amazon.com/datasync/pricing/ "https://aws.amazon.com/datasync/pricing/") before you
begin.

## Starting your task

Once you've created your task, you can begin moving data right away.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data
   transfer**, then choose
   **Tasks**.
3. Choose the task that you want to run.

Make sure that the task has an **Available**
status. You also can select multiple tasks. 4. Choose **Actions** and then choose one of the
following options:

    * **Start** – Runs the task (or
     tasks if you selected more than one).
    * **Start with overriding options**
     – Allows you to modify some of your task settings
     before you begin moving data. When you're ready, choose
     **Start**.

5. Choose **See execution details** to view details
   about the running task execution.
   To start your DataSync task, you just need to specify the Amazon Resource Name (ARN) of
   the task you want to run. Here's an example `start-task-execution`
   command:

```
aws datasync start-task-execution \
    --task-arn 'arn:aws:datasync:`region`:`account-id`:task/`task-id`'
```

The following example starts a task with a few settings that are different than the
task's default settings:

```
aws datasync start-task-execution \
    --override-options VerifyMode=NONE,OverwriteMode=NEVER,PosixPermissions=NONE
```

The command returns an ARN for your task execution similar to the following
example:

```
{
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:209870788375:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f"
}
```

###### Note

Each agent can run a single task at a time.

You can start your task by using the [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md") operation. Use the [DescribeTaskExecution](API_DescribeTaskExecution.md "API_DescribeTaskExecution.md") operation to get details about the
running task execution.

Once started, you can [check the
task execution's status](#understand-task-execution-statuses "#understand-task-execution-statuses") as DataSync copies your data. You also can [throttle the task execution's
bandwidth](configure-bandwidth.md#adjust-bandwidth-throttling "configure-bandwidth.md#adjust-bandwidth-throttling") if needed.

## Task execution statuses

When you start a DataSync task, you might see these statuses. ([Task statuses](create-task-how-to.md#understand-task-creation-statuses "create-task-how-to.md#understand-task-creation-statuses") are different
than task execution statuses.)

| Console status | API status     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Queueing       | `QUEUED`       | Another task execution is running and using the same DataSync<br>agent. For more information, see<br>[Knowing when your task is queued](#queue-task-execution "#queue-task-execution").                                                                                                                                                                                                                                                                                               |
| Launching      | `LAUNCHING`    | DataSync is initializing the task execution. This status usually<br>goes quickly but can take up to a few minutes.                                                                                                                                                                                                                                                                                                                                                                    |
| Launched       | `LAUNCHED`     | DataSync has launched the task execution.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Preparing      | `PREPARING`    | DataSync is determining what data to transfer.<br>Preparation can take just minutes, a few hours, or even longer<br>depending on the number of files, objects, or directories in both<br>locations and how you configure your task. How preparation works<br>also depends on your task mode. For more information, see<br>[How DataSync prepares your data<br>transfer](how-datasync-transfer-works.md#how-datasync-prepares "how-datasync-transfer-works.md#how-datasync-prepares"). |
| Transferring   | `TRANSFERRING` | DataSync is performing the actual data transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Verifying      | `VERIFYING`    | DataSync is verifying the integrity of your data at the end of<br>the transfer.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Success        | `SUCCESS`      | The task execution succeeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Cancelling     | `CANCELLING`   | The task execution is in the process of being cancelled.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Error          | `ERROR`        | The task execution failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Knowing when your task is queued

When running multiple tasks (for example, you're [transferring a large dataset](create-task-how-to.md#multiple-tasks-large-dataset "create-task-how-to.md#multiple-tasks-large-dataset")),
DataSync might queue the tasks to run in a series (first in, first out). Some examples
of when this happens include:

- You run different tasks that use the same DataSync agent. While you can use
  the same agent for multiple tasks, an agent can only run one task at a
  time.
- A task execution is in progress and you start additional executions of the
  same task using different [filters](filtering.md "filtering.md") or [manifests](transferring-with-manifest.md "transferring-with-manifest.md").

In each example, the queued tasks don't start until the task ahead of them
finishes.

## Cancelling your task execution

You can stop any running or queued DataSync task execution.

###### To cancel a task execution by using the console

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**,
   then choose **Tasks**.
3. Select the **Task ID** for the running task that you want
   to monitor.

The task status should be **Running**. 4. Choose **History** to view the task's executions. 5. Select the task execution that you want to stop, and then choose
**Stop**. 6. In the dialog box, choose **Stop**.

To cancel a running or queued task by using the DataSync API, see [CancelTaskExecution](API_CancelTaskExecution.md "API_CancelTaskExecution.md").

### Automated cancellation of stuck tasks

At times a running DataSync task execution can become stuck.

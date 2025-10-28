# Creating a task for transferring your data

A _task_ describes where and how AWS DataSync transfers
data. A task consists of the following:

- [Source
  location](working-with-locations.md "working-with-locations.md") – The storage system or service where
  DataSync transfers data from.
- [Destination
  location](working-with-locations.md "working-with-locations.md") – The storage system or service where
  DataSync transfers data to.
- [Task options](task-options.md "task-options.md")
  – Settings such as what files to transfer, how data gets verified, when the
  task runs, and more.
- [Task executions](run-task.md "run-task.md")
  – When you run a task, it's called a _task
  execution_.

## Creating your task

When you create a DataSync task, you specify your source and destination locations. You
also can customize your task by choosing which files to transfer, how metadata gets
handled, setting up a schedule, and more.

Before you create your task, make sure that you understand [how DataSync transfers work](how-datasync-transfer-works.md#transferring-files "how-datasync-transfer-works.md#transferring-files") and review the [task quotas](datasync-limits.md#task-hard-limits "datasync-limits.md#task-hard-limits").

###### Important

If you're planning to transfer data to or from an Amazon S3 location, review [how DataSync can affect your S3 request charges](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests") and the [DataSync pricing page](https://aws.amazon.com/datasync/pricing/ "https://aws.amazon.com/datasync/pricing/") before you
begin.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. Make sure you're in one of the AWS Regions where you plan to
   transfer data.
3. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
4. On the **Configure source location** page, [create](transferring-data-datasync.md "transferring-data-datasync.md") or choose a
   source location, then choose **Next**.
5. On the **Configure destination location** page, [create](transferring-data-datasync.md "transferring-data-datasync.md") or choose a
   destination location, then choose **Next**.
6. (Recommended) On the **Configure settings** page,
   give your task a name that you can remember.
7. While still on the **Configure settings** page,
   choose your task options or use the default settings.

You might be interested in some of the following options:

    * Specify the [task
     mode](choosing-task-mode.md "choosing-task-mode.md") that you want to use.
    * Specify what data to transfer by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or
     [filters](filtering.md "filtering.md").
    * Configure how to [handle
     file metadata](configure-metadata.md "configure-metadata.md") and [verify data
     integrity](configure-data-verification-options.md "configure-data-verification-options.md").
    * Monitor your transfer with [task
     reports](task-reports.md "task-reports.md") or [Amazon CloudWatch](monitor-datasync.md "monitor-datasync.md"). We recommend setting up some kind of
     monitoring for your task.

When you're done, choose **Next**. 8. Review your task configuration, then choose **Create
task**.
You're ready to [start your task](run-task.md "run-task.md").

Once you [create your DataSync source
and destination locations](transferring-data-datasync.md "transferring-data-datasync.md"), you can create your task.

1. In your AWS CLI settings, make sure that you're using one of the
   AWS Regions where you plan to transfer data.
2. Copy the following `create-task` command:

```
aws datasync create-task \
  --source-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --destination-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --name "`task-name`"
```

3. For `--source-location-arn`, specify the Amazon Resource
   Name (ARN) of your source location.
4. For `--destination-location-arn`, specify the ARN of your
   destination location.

If you're transferring across AWS Regions or accounts, make sure
that the ARN includes the other Region or account ID. 5. (Recommended) For `--name`, specify a name for your task
that you can remember. 6. Specify other task options as needed. You might be interested in some
of the following options:

    * Specify what data to transfer by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or
     [filters](filtering.md "filtering.md").
    * Configure how to [handle
     file metadata](configure-metadata.md "configure-metadata.md") and [verify data
     integrity](configure-data-verification-options.md "configure-data-verification-options.md").
    * Monitor your transfer with [task
     reports](task-reports.md "task-reports.md") or [Amazon CloudWatch](monitor-datasync.md "monitor-datasync.md"). We recommend setting up some kind of
     monitoring for your task.

For more options, see [create-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html"). Here's an example `create-task`
command that specifies several options:

```
aws datasync create-task \
  --source-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --destination-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --cloud-watch-log-group-arn "arn:aws:logs:`region`:`account-id`" \
  --name "`task-name`" \
  --options VerifyMode=NONE,OverwriteMode=NEVER,Atime=BEST_EFFORT,Mtime=PRESERVE,Uid=INT_VALUE,Gid=INT_VALUE,PreserveDevices=PRESERVE,PosixPermissions=PRESERVE,PreserveDeletedFiles=PRESERVE,TaskQueueing=ENABLED,LogLevel=TRANSFER
```

7. Run the `create-task` command.

If the command is successful, you get a response that shows you the
ARN of the task that you created. For example:

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:111222333444:task/task-08de6e6697796f026"
}
```

You're ready to [start your task](run-task.md "run-task.md").

## Task statuses

When you create a DataSync task, you can check its status to see if it's ready to
run.

| Console status | API status    | Description                                                                                                                                                                                                                                   |
| -------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available      | `AVAILABLE`   | The task is ready to start transferring data.                                                                                                                                                                                                 |
| Running        | `RUNNING`     | A task execution is in progress. For more information, see [Task execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").                                                        |
| Unavailable    | `UNAVAILABLE` | A DataSync agent used by the task is offline. For more information, see [What do I do if my agent is offline?](troubleshooting-datasync-agents.md#troubleshoot-agent-offline "troubleshooting-datasync-agents.md#troubleshoot-agent-offline") |
| Queued         | `QUEUED`      | Another task execution that uses the same DataSync agent is in progress. For more information, see [Knowing when your task is queued](run-task.md#queue-task-execution "run-task.md#queue-task-execution").                                   | ## Partitioning large datasets with multiple tasks If you're transferring a large dataset, such as [migrating](datasync-large-migration.md "datasync-large-migration.md") millions of files or objects, we recommend partitioning your dataset with multiple DataSync tasks. Partitioning your source data across multiple tasks (and possibly [agents](do-i-need-datasync-agent.md#multiple-agents "do-i-need-datasync-agent.md#multiple-agents"), depending on your locations) helps reduce the time it takes DataSync to prepare and transfer your data. Consider some of the ways that you can partition a large dataset across several DataSync tasks: <br>• Create tasks that transfer separate folders. For example, you might create two tasks that target `/FolderA` and `/FolderB`, respectively, in your source storage. <br>• Create tasks that transfer subsets of files, objects, and folders by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or [filters](filtering.md "filtering.md"). Be mindful that this approach can increase the I/O operations on your storage and affect your network bandwidth. For more information, see the blog on [How to accelerate your data transfers with DataSync scale out architectures](https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/ "https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/"). ## Segmenting transferred data with multiple tasks If you're transferring different sets of data to the same destination, you can create multiple tasks to help segment the data that you transfer. For example, if you're transferring to the same S3 bucket named `MyBucket`, you can create different prefixes in the bucket that correspond to each task. This approach prevents file name conflicts the datasets and allows you to set different permissions for each prefix. Here's how you might set this up: 1. Create three prefixes in the destination `MyBucket` named `task1`, `task2`, and `task3`: <br>• `s3://MyBucket/task1` <br>• `s3://MyBucket/task2` <br>• `s3://MyBucket/task3` 2. Create three DataSync tasks named `task1`, `task2`, and `task3` that transfer to the corresponding prefix in `MyBucket`. |

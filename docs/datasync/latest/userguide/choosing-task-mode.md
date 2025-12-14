# Choosing a task mode for your data transfer

Your AWS DataSync task can run in one of the following modes:

- **Enhanced mode** – Transfer virtually
  unlimited numbers of files or objects with higher performance than Basic mode.
  Enhanced mode tasks optimize the data transfer process by listing, preparing,
  transferring, and verifying data in parallel. Enhanced mode is currently
  available for transfers between Amazon S3 locations, transfers between Azure
  Blob and Amazon S3 without an agent, transfers between other clouds and
  Amazon S3 without an agent, and transfers between NFS or SMB file servers and Amazon S3
  using an Enhanced mode agent.
- **Basic mode** – Transfer files or
  objects between AWS storage and all other supported DataSync locations.
  Basic mode tasks are subject to [quotas](datasync-limits.md "datasync-limits.md")
  on the number of files, objects, and directories in a dataset. Basic mode
  sequentially prepares, transfers, and verifies data, making it slower than
  Enhanced mode for most workloads.

## Understanding task mode differences

The following information can help you determine which task mode to
use.

| Capability                                                                                                                                             | Enhanced mode behavior                                                                                                                                                                                                                                                              | Basic mode behavior                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Performance](how-datasync-transfer-works.md#transferring-files "how-datasync-transfer-works.md#transferring-files")                                   | DataSync lists, prepares, transfers, and verifies your data in parallel.<br>Provides higher performance than Basic mode for most workloads<br>(such as<br>transferring<br>large objects)                                                                                            | DataSync prepares, transfers, and verifies your data sequentially.<br>Performance is slower than Enhanced mode for most workloads                                                                                                                     |
| Number of items in a dataset that DataSync can work with per task<br>execution                                                                         | Virtually unlimited numbers of objects                                                                                                                                                                                                                                              | [Quotas](datasync-limits.md#task-hard-limits "datasync-limits.md#task-hard-limits") apply                                                                                                                                                             |
| Data transfer [counters](transfer-performance-counters.md "transfer-performance-counters.md") and [metrics](monitor-datasync.md "monitor-datasync.md") | More counters and metrics than Basic mode, such as the number<br>of objects that<br>DataSync<br>finds at your source location, how many objects are prepared<br>during each task execution, and folder counters similar to file and object counters                                 | Less counters and metrics than Enhanced mode                                                                                                                                                                                                          |
| [Logging](configure-logging.md "configure-logging.md")                                                                                                 | Structured logs (JSON format)                                                                                                                                                                                                                                                       | Unstructured logs                                                                                                                                                                                                                                     |
| [Supported<br>locations](working-with-locations.md "working-with-locations.md")                                                                        | Currently for transfers between Amazon S3 locations, transfers between<br>Azure Blob and Amazon S3 without an agent, transfers<br>between other clouds and Amazon S3 without an agent, and transfers between<br>NFS or SMB file servers and Amazon S3 using an Enhanced mode agent. | For transfers between all locations that DataSync supports                                                                                                                                                                                            |
| [Data<br>verification options](configure-data-verification-options.md "configure-data-verification-options.md")                                        | DataSync verifies only transferred data                                                                                                                                                                                                                                             | DataSync verifies all data by default                                                                                                                                                                                                                 |
| [Bandwidth limits](configure-bandwidth.md "configure-bandwidth.md")                                                                                    | Not applicable                                                                                                                                                                                                                                                                      | Supported                                                                                                                                                                                                                                             |
| Cost                                                                                                                                                   | For more information, see the [DataSync pricing](https://aws.amazon.com/datasync/pricing "https://aws.amazon.com/datasync/pricing") page                                                                                                                                            | For more information, see the [DataSync pricing](https://aws.amazon.com/datasync/pricing "https://aws.amazon.com/datasync/pricing") page                                                                                                              |
| Failure handling for unsupported object tags                                                                                                           | For cloud storage transfers to or from locations that don't support<br>object tagging, task execution will fail immediately if the<br>`ObjectTags` option is unspeficied or set to<br>`PRESERVE`.                                                                                   | For cloud storage transfers to or from locations that don't support<br>object tagging, task execution will run normally, but will report<br>per-object failures for tagged objects if the `ObjectTags`<br>option is unspecified or set to `PRESERVE`. |

## Choosing a task mode

You can choose Enhanced mode only for transfers between Amazon S3 locations, transfers
between Azure Blob and Amazon S3 without an agent, transfers between other
clouds and Amazon S3 without an agent, and transfers between NFS or SMB file servers and
Amazon S3 using an Enhanced mode agent. Otherwise, you must use Basic mode. For example,
a transfer from an on-premises [HDFS location](create-hdfs-location.md "create-hdfs-location.md")
to an S3 location requires Basic mode.

Your task options and performance might vary depending on the task mode you choose.
Once you create your task, you can't change the task mode.

**Required permissions**

To create an Enhanced mode task, the IAM role that you're using
DataSync with must have the `iam:CreateServiceLinkedRole`
permission.

For your DataSync user permissions, consider using [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess"). This is an AWS managed policy that
provides a user full access to DataSync and minimal access to its
dependencies.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. For
**Task
mode**, choose one of the following
options:

    * **Enhanced**
    * **Basic**

For more information, see [Understanding task mode differences](#task-mode-differences "#task-mode-differences"). 5. While still on the **Configure settings** page,
choose other task options or use the default settings.

You might be interested in some of the following options:

    * Specify what data to transfer by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or
     [filters](filtering.md "filtering.md").
    * Configure how to [handle
     file metadata](configure-metadata.md "configure-metadata.md") and [verify data
     integrity](configure-data-verification-options.md "configure-data-verification-options.md").
    * Monitor your transfer with [task
     reports](task-reports.md "task-reports.md") or [Amazon CloudWatch Logs](monitor-datasync.md "monitor-datasync.md").

When you're done, choose **Next**. 6. Review your task configuration, then choose **Create
task**.

1. In your AWS CLI settings, make sure that you're using one of the
   AWS Regions where you plan to transfer data.
2. Copy the following `create-task` command:

```
aws datasync create-task \
  --source-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --destination-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --task-mode "`ENHANCED-or-BASIC`"
```

3. For `--source-location-arn`, specify the Amazon Resource
   Name (ARN) of your source location.
4. For `--destination-location-arn`, specify the ARN of your
   destination location.

If you're transferring across AWS Regions or accounts, make sure
that the ARN includes the other Region or account ID. 5. For `--task-mode`, specify `ENHANCED` or
`BASIC`.

For more information, see [Understanding task mode differences](#task-mode-differences "#task-mode-differences"). 6. Specify other task options as needed. You might be interested in some
of the following options:

    * Specify what data to transfer by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or
     [filters](filtering.md "filtering.md").
    * Configure how to [handle
     file metadata](configure-metadata.md "configure-metadata.md") and [verify data
     integrity](configure-data-verification-options.md "configure-data-verification-options.md").
    * Monitor your transfer with [task
     reports](task-reports.md "task-reports.md") or [Amazon CloudWatch Logs](monitor-datasync.md "monitor-datasync.md").

For more options, see [create-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html"). Here's an example `create-task`
command that specifies Enhanced mode and several other
options:

```
aws datasync create-task \
  --source-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --destination-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --name "`task-name`" \
  --task-mode "ENHANCED" \
  --options TransferMode=CHANGED,VerifyMode=ONLY_FILES_TRANSFERRED,ObjectTags=PRESERVE,LogLevel=TRANSFER
```

7. Run the `create-task` command.

If the command is successful, you get a response that shows you the
ARN of the task that you created. For example:

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:111222333444:task/task-08de6e6697796f026"
}
```

You can specify the DataSync task mode by configuring the `TaskMode`
parameter in the [CreateTask](API_CreateTask.md "API_CreateTask.md")
operation.

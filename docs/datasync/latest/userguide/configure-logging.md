# Monitoring data transfers with Amazon CloudWatch Logs

You can monitor your AWS DataSync transfer by using CloudWatch Logs. We recommend that you configure
your task to at least log basic information (such as transfer
errors).

## Allowing DataSync to upload logs to a CloudWatch log

group

To [configure logging](#configure-logging-for-task "#configure-logging-for-task") for your DataSync
task, you need a CloudWatch log group that DataSync has permission to send logs to. You set up
this access through an AWS Identity and Access Management (IAM) role. How this specifically works depends on
your [task mode](choosing-task-mode.md "choosing-task-mode.md").

Enhanced mode
With Enhanced mode, DataSync automatically sends task logs to a log
group named `/aws/datasync`. If that log group doesn't exist in
your AWS Region, DataSync creates the log group on your behalf by using an
IAM [service-linked role](using-service-linked-roles-service-action-2.md "using-service-linked-roles-service-action-2.md") when you create your task.

Basic mode
There are a couple ways to set up a CloudWatch log group for a DataSync task using
Basic mode. In the console, you can automatically create an IAM role
that in most cases includes the permissions that DataSync requires to upload
logs. Keep in mind that this automatically generated role might not meet
your needs from a least-privilege standpoint.

If
you want to use an existing CloudWatch log group or are creating your tasks
programmatically, you must create the IAM role yourself.

The
following example is an IAM policy that grants these permissions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DataSyncLogsToCloudWatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogStream"
 ],
 "Principal": {
 "Service": "datasync.amazonaws.com"
 },
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:datasync:`us-east-1`:`444455556666`:task/*"
 ]
 },
 "StringEquals": {
 "aws:SourceAccount": "`444455556666`"
 }
 },
 "Resource": "arn:aws:logs:`us-east-1`:`444455556666`:log-group:*:*"
 }
 ]
}`

```

The policy uses
`Condition`
statements to help ensure that only DataSync tasks from the specified account
have access to the specified CloudWatch log group. We recommend using the
[aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context
keys in these `Condition` statements to protect against the
confused deputy problem. For more information, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

To specify the DataSync task or tasks, replace
`region` with the Region code
for the AWS Region where the tasks are located (for example,
`us-west-2`), and replace
`account-id` with the
AWS account ID of the account that contains the tasks. To specify the CloudWatch
log group, replace the same values. You can also modify the
`Resource` statement to target specific log groups. For more
information about using `SourceArn` and
`SourceAccount`, see [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") in the _IAM User Guide_.

To apply the policy, save this policy statement to a file on your local
computer. Then run the following AWS CLI command to apply the resource policy.
To use this example command, replace
`full-path-to-policy-file`
with the path to the file that contains your policy statement.

```
aws logs put-resource-policy --policy-name `trust-datasync` --policy-document file://`full-path-to-policy-file`
```

###### Note

Run this command by using the same AWS account and AWS Region
where you activated your DataSync agent.

For more information, see the [_Amazon CloudWatch Logs User Guide_](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

## Configuring logging for your DataSync

task

We recommend that you configure at least some level of logging for your DataSync
task.

###### Before you begin

DataSync needs permission to upload logs to a CloudWatch log group. For more information,
see [Allowing DataSync to upload logs to a CloudWatch log
group](#cloudwatchlogs "#cloudwatchlogs").

The following instructions describe how to configure CloudWatch logging when
creating a task. You also can configure logging when editing a task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. On the **Configure settings** page, choose a [task mode](choosing-task-mode.md "choosing-task-mode.md") and any other
options.

You might be interested in some of the following options:

    * Specify what data to transfer by using a [manifest](transferring-with-manifest.md "transferring-with-manifest.md") or
     [filters](filtering.md "filtering.md").
    * Configure how to [handle
     file metadata](configure-metadata.md "configure-metadata.md") and [verify data
     integrity](configure-data-verification-options.md "configure-data-verification-options.md").

5. For **Log level**, choose one of the following
   options:
   - **Log basic information such as transfer
     errors** – Publish logs with only basic
     information (such as transfer errors).
   - **Log all transferred objects and files**
     – Publish logs for all files or objects that DataSync
     transfers and performs data-integrity checks on.
   - **Don't generate logs**

6. Do one of the following depending on the task mode you're using to
   create or specify a CloudWatch log group:

Enhanced mode
When you choose **Create task**, DataSync
automatically uses (or creates) a log group named
`/aws/datasync`.

Basic mode
For **CloudWatch log group**, specify a log
group that DataSync has permission to upload logs to by doing
one of the following:

    * Choose **Autogenerate** to
     automatically create a log group that allows DataSync
     to upload logs to it.
    * Choose an existing log group in your current
     AWS Region.


    If you choose an existing log group, make sure
     that [DataSync has
     permission](#cloudwatchlogs "#cloudwatchlogs") to upload logs to that log
     group.

7. Choose **Create task**.
   You're ready to [start your task](run-task.md "run-task.md").

1. Copy the following `create-task` command:

```
aws datasync create-task \
  --source-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --destination-location-arn "arn:aws:datasync:`us-east-1`:`account-id`:location/`location-id`" \
  --task-mode "`ENHANCED-or-BASIC`" \
  --name "`task-name`" \
  --options '{"LogLevel": "`log-level`"}' \
  --cloudwatch-log-group-arn "arn:aws:logs:`us-east-1`:`account-id`:log-group:`log-group-name`:*"
```

2. For `--source-location-arn`, specify the Amazon Resource
   Name (ARN) of your source location.
3. For `--destination-location-arn`, specify the ARN of your
   destination location.

If you're transferring across AWS Regions or accounts, make sure
that the ARN includes the other Region or account ID. 4. For `--task-mode`, specify `ENHANCED` or
`BASIC`. 5. (Recommended) For `--name`, specify a name for your task
that you can remember. 6. For `LogLevel`, specify one of the following
options:

    * `BASIC` – Publish logs with only basic
     information (such as transfer errors).
    * `TRANSFER` – Publish logs for all files or
     objects that DataSync transfers and performs data-integrity checks
     on.
    * `NONE` – Don't generate logs.

7. For -`-cloudwatch-log-group-arn`, specify the ARN of a CloudWatch
   log group.

###### Important

If your `--task-mode` is `ENHANCED`, you
don't need to specify this option. For more information, see [Allowing DataSync to upload logs to a CloudWatch log
group](#cloudwatchlogs "#cloudwatchlogs"). 8. Run the `create-task` command.

If the command is successful, you get a response that shows you the
ARN of the task that you created. For example:

```
{
    "TaskArn": "arn:aws:datasync:us-east-1:111222333444:task/task-08de6e6697796f026"
}
```

You're ready to [start your task](run-task.md "run-task.md").

You can configure CloudWatch logging for your task by using the
`CloudWatchLogGroupArn` parameter with any of the following
operations:

- [CreateTask](API_CreateTask.md "API_CreateTask.md")
- [UpdateTask](API_UpdateTask.md "API_UpdateTask.md")

## Viewing DataSync task

logs

When you [start your task](run-task.md "run-task.md"), you can view the task
execution's logs by using the CloudWatch console or AWS CLI (among other options). For more
information, see the [_Amazon CloudWatch Logs User Guide_](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

DataSync provides JSON-structured logs for Enhanced mode tasks. Basic mode
tasks have unstructured logs. The following examples show how verification errors
display in Enhanced mode logs compared to Basic mode logs.

Enhanced mode log example

```
{
    "Action": "VERIFY",
    "Source": {
        "LocationId": "loc-abcdef01234567890",
        "RelativePath": "directory1/directory2/file1.txt"
    },
    "Destination": {
        "LocationId": "loc-05ab2fdc272204a5f",
        "RelativePath": "directory1/directory2/file1.txt",
        "Metadata": {
            "Type": "Object",
            "ContentSize": 66060288,
            "LastModified": "2024-10-03T20:46:58Z",
            "S3": {
                "SystemMetadata": {
                    "ContentType": "binary/octet-stream",
                    "ETag": "\"1234abcd5678efgh9012ijkl3456mnop\"",
                    "ServerSideEncryption": "AES256"
                },
                "UserMetadata": {
                    "file-mtime": "1602647222/222919600"
                },
                "Tags": {}
            }
        }
    },
    "ErrorCode": "FileNotAtSource",
    "ErrorDetail": "Verification failed due to file being present at the destination but not at the source"
}
```

Basic mode log example

```
[NOTICE] Verification failed > /directory1/directory2/file1.txt
[NOTICE] /directory1/directory2/file1.txt   dstMeta: type=R mode=0755 uid=65534 gid=65534 size=8972938 atime=1728657659/0 mtime=1728657659/0 extAttrsHash=0
[NOTICE]   dstHash: f9c2cca900301d38b0930367d8d587153154af467da0fdcf1bebc0848ec72c0d
```

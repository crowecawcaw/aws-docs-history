# UpdateTask

Updates the configuration of a _task_, which defines where and how
AWS DataSync transfers your data.

## Request Syntax

```
{
   "CloudWatchLogGroupArn": "`string`",
   "Excludes": [
      {
         "FilterType": "`string`",
         "Value": "`string`"
      }
   ],
   "Includes": [
      {
         "FilterType": "`string`",
         "Value": "`string`"
      }
   ],
   "ManifestConfig": {
      "Action": "`string`",
      "Format": "`string`",
      "Source": {
         "S3": {
            "BucketAccessRoleArn": "`string`",
            "ManifestObjectPath": "`string`",
            "ManifestObjectVersionId": "`string`",
            "S3BucketArn": "`string`"
         }
      }
   },
   "Name": "`string`",
   "Options": {
      "Atime": "`string`",
      "BytesPerSecond": `number`,
      "Gid": "`string`",
      "LogLevel": "`string`",
      "Mtime": "`string`",
      "ObjectTags": "`string`",
      "OverwriteMode": "`string`",
      "PosixPermissions": "`string`",
      "PreserveDeletedFiles": "`string`",
      "PreserveDevices": "`string`",
      "SecurityDescriptorCopyFlags": "`string`",
      "TaskQueueing": "`string`",
      "TransferMode": "`string`",
      "Uid": "`string`",
      "VerifyMode": "`string`"
   },
   "Schedule": {
      "ScheduleExpression": "`string`",
      "Status": "`string`"
   },
   "TaskArn": "`string`",
   "TaskReportConfig": {
      "Destination": {
         "S3": {
            "BucketAccessRoleArn": "`string`",
            "S3BucketArn": "`string`",
            "Subdirectory": "`string`"
         }
      },
      "ObjectVersionIds": "`string`",
      "OutputType": "`string`",
      "Overrides": {
         "Deleted": {
            "ReportLevel": "`string`"
         },
         "Skipped": {
            "ReportLevel": "`string`"
         },
         "Transferred": {
            "ReportLevel": "`string`"
         },
         "Verified": {
            "ReportLevel": "`string`"
         }
      },
      "ReportLevel": "`string`"
   }
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[CloudWatchLogGroupArn](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for
monitoring your task.

For Enhanced mode tasks, you must use `/aws/datasync` as your log group
name. For example:

`arn:aws:logs:us-east-1:111222333444:log-group:/aws/datasync:*`

For more information, see [Monitoring data transfers with
CloudWatch Logs](configure-logging.md "configure-logging.md").

Type: String

Length Constraints: Maximum length of 562.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`

Required: No

**[Excludes](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies exclude filters that define the files, objects, and folders in your source
location that you don't want DataSync to transfer. For more information and
examples, see [Specifying what DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[Includes](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies include filters define the files, objects, and folders in your source location
that you want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[ManifestConfig](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

When using this parameter, your caller identity (the IAM role that you're
using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

To remove a manifest configuration, specify this parameter as empty.

Type: [ManifestConfig](API_ManifestConfig.md "API_ManifestConfig.md") object

Required: No

**[Name](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies the name of your task.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

**[Options](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You
also can specify how to verify data integrity, set bandwidth limits for your task, among other
options.

Each option has a default value. Unless you need to, you don't have to configure any
option before calling [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md").

You also can override your task options for each task execution. For example, you might
want to adjust the `LogLevel` for an individual execution.

Type: [Options](API_Options.md "API_Options.md") object

Required: No

**[Schedule](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies a schedule for when you want your task to run. For more information, see [Scheduling your
task](task-scheduling.md "task-scheduling.md").

Type: [TaskSchedule](API_TaskSchedule.md "API_TaskSchedule.md") object

Required: No

**[TaskArn](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies the ARN of the task that you want to update.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`

Required: Yes

**[TaskReportConfig](#API_UpdateTask_RequestSyntax "#API_UpdateTask_RequestSyntax")**

Specifies how you want to configure a task report, which provides detailed information
about your DataSync transfer. For more information, see [Monitoring your DataSync
transfers with task reports](task-reports.md "task-reports.md").

When using this parameter, your caller identity (the IAM role that you're
using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

To remove a task report configuration, specify this parameter as empty.

Type: [TaskReportConfig](API_TaskReportConfig.md "API_TaskReportConfig.md") object

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateTask.md "../../../goto/cli2/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateTask.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateTask.md "../../../goto/boto3/datasync-2018-11-09/UpdateTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateTask.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateTask.md")

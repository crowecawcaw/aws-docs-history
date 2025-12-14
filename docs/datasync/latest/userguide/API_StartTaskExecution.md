# StartTaskExecution

Starts an AWS DataSync transfer task. For each task, you can only run one task
execution at a time.

There are several steps to a task execution. For more information, see [Task execution statuses](working-with-task-executions.md#understand-task-execution-statuses "working-with-task-executions.md#understand-task-execution-statuses").

###### Important

If you're planning to transfer data to or from an Amazon S3 location, review
[how
DataSync can affect your S3 request charges](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests") and the [DataSync pricing page](http://aws.amazon.com/datasync/pricing/ "http://aws.amazon.com/datasync/pricing/") before
you begin.

## Request Syntax

```
{
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
   "OverrideOptions": {
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
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
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

**[Excludes](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Specifies a list of filter rules that determines which files to exclude from a task. The
list contains a single filter string that consists of the patterns to exclude. The patterns
are delimited by "|" (that is, a pipe), for example, `"/folder1|/folder2"`.

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[Includes](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Specifies a list of filter rules that determines which files to include when running a
task. The pattern should contain a single filter string that consists of the patterns to
include. The patterns are delimited by "|" (that is, a pipe), for example,
`"/folder1|/folder2"`.

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[ManifestConfig](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

To remove a manifest configuration, specify this parameter with an empty value.

Type: [ManifestConfig](API_ManifestConfig.md "API_ManifestConfig.md") object

Required: No

**[OverrideOptions](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You
also can specify how to verify data integrity, set bandwidth limits for your task, among other
options.

Each option has a default value. Unless you need to, you don't have to configure any
option before calling [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md").

You also can override your task options for each task execution. For example, you might
want to adjust the `LogLevel` for an individual execution.

Type: [Options](API_Options.md "API_Options.md") object

Required: No

**[Tags](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Specifies the tags that you want to apply to the Amazon Resource Name (ARN) representing
the task execution.

_Tags_ are key-value pairs that help you manage, filter, and search for
your DataSync resources.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

**[TaskArn](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the task that you want to start.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`

Required: Yes

**[TaskReportConfig](#API_StartTaskExecution_RequestSyntax "#API_StartTaskExecution_RequestSyntax")**

Specifies how you want to configure a task report, which provides detailed information
about your DataSync transfer. For more information, see [Monitoring your DataSync
transfers with task reports](task-reports.md "task-reports.md").

When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

To remove a task report configuration, specify this parameter as empty.

Type: [TaskReportConfig](API_TaskReportConfig.md "API_TaskReportConfig.md") object

Required: No

## Response Syntax

```
{
   "TaskExecutionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TaskExecutionArn](#API_StartTaskExecution_ResponseSyntax "#API_StartTaskExecution_ResponseSyntax")**

The ARN of the running task execution.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Sample Request

The following example starts a task execution using the default options for the
specified task.

```
{
    "OverrideOptions": {
        "Atime": "BEST_EFFORT",
        "BytesPerSecond": 1000,
        "Gid": "NONE",
        "Mtime": "PRESERVE",
        "PosixPermissions": "PRESERVE",
        "PreserveDevices": "NONE",
        "PreserveDeletedFiles": "PRESERVE",
        "Uid": "NONE",
        "VerifyMode": "POINT_IN_TIME_CONSISTENT"
    },
    "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026"
}
```

### Sample Response

This example illustrates one usage of StartTaskExecution.

```
{
  "TaskExecutionArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/StartTaskExecution.md "../../../goto/cli2/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/StartTaskExecution.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForCpp/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForGoV2/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForKotlin/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/StartTaskExecution.md "../../../goto/boto3/datasync-2018-11-09/StartTaskExecution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/StartTaskExecution.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/StartTaskExecution.md")

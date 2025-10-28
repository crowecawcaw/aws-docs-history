# DescribeTask

Provides information about a _task_, which defines where and how
AWS DataSync transfers your data.

## Request Syntax

```
{
   "TaskArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[TaskArn](#API_DescribeTask_RequestSyntax "#API_DescribeTask_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the transfer task that you want information
about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}$`

Required: Yes

## Response Syntax

```
{
   "CloudWatchLogGroupArn": "***string***",
   "CreationTime": ***number***,
   "CurrentTaskExecutionArn": "***string***",
   "DestinationLocationArn": "***string***",
   "DestinationNetworkInterfaceArns": [ "***string***" ],
   "ErrorCode": "***string***",
   "ErrorDetail": "***string***",
   "Excludes": [
      {
         "FilterType": "***string***",
         "Value": "***string***"
      }
   ],
   "Includes": [
      {
         "FilterType": "***string***",
         "Value": "***string***"
      }
   ],
   "ManifestConfig": {
      "Action": "***string***",
      "Format": "***string***",
      "Source": {
         "S3": {
            "BucketAccessRoleArn": "***string***",
            "ManifestObjectPath": "***string***",
            "ManifestObjectVersionId": "***string***",
            "S3BucketArn": "***string***"
         }
      }
   },
   "Name": "***string***",
   "Options": {
      "Atime": "***string***",
      "BytesPerSecond": ***number***,
      "Gid": "***string***",
      "LogLevel": "***string***",
      "Mtime": "***string***",
      "ObjectTags": "***string***",
      "OverwriteMode": "***string***",
      "PosixPermissions": "***string***",
      "PreserveDeletedFiles": "***string***",
      "PreserveDevices": "***string***",
      "SecurityDescriptorCopyFlags": "***string***",
      "TaskQueueing": "***string***",
      "TransferMode": "***string***",
      "Uid": "***string***",
      "VerifyMode": "***string***"
   },
   "Schedule": {
      "ScheduleExpression": "***string***",
      "Status": "***string***"
   },
   "ScheduleDetails": {
      "DisabledBy": "***string***",
      "DisabledReason": "***string***",
      "StatusUpdateTime": ***number***
   },
   "SourceLocationArn": "***string***",
   "SourceNetworkInterfaceArns": [ "***string***" ],
   "Status": "***string***",
   "TaskArn": "***string***",
   "TaskMode": "***string***",
   "TaskReportConfig": {
      "Destination": {
         "S3": {
            "BucketAccessRoleArn": "***string***",
            "S3BucketArn": "***string***",
            "Subdirectory": "***string***"
         }
      },
      "ObjectVersionIds": "***string***",
      "OutputType": "***string***",
      "Overrides": {
         "Deleted": {
            "ReportLevel": "***string***"
         },
         "Skipped": {
            "ReportLevel": "***string***"
         },
         "Transferred": {
            "ReportLevel": "***string***"
         },
         "Verified": {
            "ReportLevel": "***string***"
         }
      },
      "ReportLevel": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CloudWatchLogGroupArn](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your
task.

For more information, see [Monitoring data transfers with
CloudWatch Logs](configure-logging.md "configure-logging.md").

Type: String

Length Constraints: Maximum length of 562.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`

**[CreationTime](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The time that the task was created.

Type: Timestamp

**[CurrentTaskExecutionArn](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARN of the most recent task execution.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

**[DestinationLocationArn](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARN of your transfer's destination location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[DestinationNetworkInterfaceArns](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARNs of the [network
interfaces](datasync-network.md#required-network-interfaces "datasync-network.md#required-network-interfaces") that DataSync created for your destination location.

Type: Array of strings

Length Constraints: Maximum length of 128.

Pattern: `^arn:aws[\-a-z]{0,}:ec2:[a-z\-0-9]*:[0-9]{12}:network-interface/eni-[0-9a-f]+$`

**[ErrorCode](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

If there's an issue with your task, you can use the error code to help you troubleshoot
the problem. For more information, see [Troubleshooting issues with DataSync transfers](troubleshooting-datasync-locations-tasks.md "troubleshooting-datasync-locations-tasks.md").

Type: String

**[ErrorDetail](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

If there's an issue with your task, you can use the error details to help you
troubleshoot the problem. For more information, see [Troubleshooting issues with DataSync transfers](troubleshooting-datasync-locations-tasks.md "troubleshooting-datasync-locations-tasks.md").

Type: String

**[Excludes](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The exclude filters that define the files, objects, and folders in your source location
that you don't want DataSync to transfer. For more information and examples, see
[Specifying what
DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

**[Includes](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The include filters that define the files, objects, and folders in your source location
that you want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

**[ManifestConfig](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

Type: [ManifestConfig](API_ManifestConfig.md "API_ManifestConfig.md") object

**[Name](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The name of your task.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

**[Options](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The task's settings. For example, what file metadata gets preserved, how data integrity
gets verified at the end of your transfer, bandwidth limits, among other options.

Type: [Options](API_Options.md "API_Options.md") object

**[Schedule](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The schedule for when you want your task to run. For more information, see [Scheduling your
task](task-scheduling.md "task-scheduling.md").

Type: [TaskSchedule](API_TaskSchedule.md "API_TaskSchedule.md") object

**[ScheduleDetails](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The details about your [task schedule](task-scheduling.md "task-scheduling.md").

Type: [TaskScheduleDetails](API_TaskScheduleDetails.md "API_TaskScheduleDetails.md") object

**[SourceLocationArn](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARN of your transfer's source location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[SourceNetworkInterfaceArns](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARNs of the [network
interfaces](datasync-network.md#required-network-interfaces "datasync-network.md#required-network-interfaces") that DataSync created for your source location.

Type: Array of strings

Length Constraints: Maximum length of 128.

Pattern: `^arn:aws[\-a-z]{0,}:ec2:[a-z\-0-9]*:[0-9]{12}:network-interface/eni-[0-9a-f]+$`

**[Status](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The status of your task. For information about what each status means, see [Task statuses](create-task-how-to.md#understand-task-creation-statuses "create-task-how-to.md#understand-task-creation-statuses").

Type: String

Valid Values: `AVAILABLE | CREATING | QUEUED | RUNNING | UNAVAILABLE`

**[TaskArn](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The ARN of your task.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]*:[0-9]{12}:task/task-[0-9a-f]{17}$`

**[TaskMode](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The task mode that you're using. For more information, see [Choosing a task mode for your data
transfer](choosing-task-mode.md "choosing-task-mode.md").

Type: String

Valid Values: `BASIC | ENHANCED`

**[TaskReportConfig](#API_DescribeTask_ResponseSyntax "#API_DescribeTask_ResponseSyntax")**

The configuration of your task report, which provides detailed information about your
DataSync transfer. For more information, see [Monitoring your DataSync
transfers with task reports](task-reports.md "task-reports.md").

Type: [TaskReportConfig](API_TaskReportConfig.md "API_TaskReportConfig.md") object

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

The following example specifies the ARN of a DataSync task to get
information about.

```
{
  "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026"
}
```

### Sample Response

The following example shows a `DescribeTask` response.

```
{
  "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026",
  "Name": "MyTask",
  "TaskMode": "BASIC",
  "Status": "RUNNING",
  "SourceLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3",
  "DestinationLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2",
  "CurrentTaskExecutionArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026/execution/exec-04ce9d516d69bd52f",
  "CreationTime": 1532660733.39,
  "Options": {
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
  "CloudWatchLogGroupArn": "arn:aws:logs:us-east-2:111222333444:log-group:/log-group-name:*"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeTask.md "../../../goto/cli2/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeTask.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeTask.md "../../../goto/boto3/datasync-2018-11-09/DescribeTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeTask.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeTask.md")

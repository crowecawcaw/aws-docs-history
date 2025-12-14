# CreateTask

Configures a _task_, which defines where and how AWS DataSync
transfers your data.

A task includes a source location, destination location, and transfer options (such as
bandwidth limits, scheduling, and more).

###### Important

If you're planning to transfer data to or from an Amazon S3 location, review
[how
DataSync can affect your S3 request charges](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests") and the [DataSync pricing page](http://aws.amazon.com/datasync/pricing/ "http://aws.amazon.com/datasync/pricing/") before
you begin.

## Request Syntax

```
{
   "CloudWatchLogGroupArn": "`string`",
   "DestinationLocationArn": "`string`",
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
   "SourceLocationArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TaskMode": "`string`",
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

**[CloudWatchLogGroupArn](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for
monitoring your task.

For Enhanced mode tasks, you don't need to specify anything. DataSync
automatically sends logs to a CloudWatch log group named
`/aws/datasync`.

For more information, see [Monitoring data transfers with
CloudWatch Logs](configure-logging.md "configure-logging.md").

Type: String

Length Constraints: Maximum length of 562.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):logs:[a-z\-0-9]+:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`

Required: No

**[DestinationLocationArn](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies the ARN of your transfer's destination location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Excludes](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies exclude filters that define the files, objects, and folders in your source
location that you don't want DataSync to transfer. For more information and
examples, see [Specifying what DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[Includes](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies include filters that define the files, objects, and folders in your source
location that you want DataSync to transfer. For more information and examples, see
[Specifying what
DataSync transfers by using filters](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: No

**[ManifestConfig](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Configures a manifest, which is a list of files or objects that you want DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

Type: [ManifestConfig](API_ManifestConfig.md "API_ManifestConfig.md") object

Required: No

**[Name](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies the name of your task.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

**[Options](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies your task's settings, such as preserving file metadata, verifying data
integrity, among other options.

Type: [Options](API_Options.md "API_Options.md") object

Required: No

**[Schedule](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies a schedule for when you want your task to run. For more information, see [Scheduling your
task](task-scheduling.md "task-scheduling.md").

Type: [TaskSchedule](API_TaskSchedule.md "API_TaskSchedule.md") object

Required: No

**[SourceLocationArn](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies the ARN of your transfer's source location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Tags](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies the tags that you want to apply to your task.

_Tags_ are key-value pairs that help you manage, filter, and search
for your DataSync resources.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

**[TaskMode](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies one of the following task modes for your data transfer:

- `ENHANCED` - Transfer virtually unlimited numbers of objects with higher
  performance than Basic mode. Enhanced mode tasks optimize the data transfer process by
  listing, preparing, transferring, and verifying data in parallel. Enhanced mode is
  currently available for transfers between Amazon S3 locations, transfers between
  Azure Blob and Amazon S3 without an agent, and transfers between other clouds and
  Amazon S3 without an agent.

###### Note

To create an Enhanced mode task, the IAM role that you use to call
the `CreateTask` operation must have the
`iam:CreateServiceLinkedRole` permission.

- `BASIC` (default) - Transfer files or objects between AWS
  storage and all other supported DataSync locations. Basic mode tasks are subject
  to [quotas](datasync-limits.md "datasync-limits.md") on the number of files, objects, and directories in a dataset. Basic
  mode sequentially prepares, transfers, and verifies data, making it slower than Enhanced
  mode for most workloads.

For more information, see [Understanding
task mode differences](choosing-task-mode.md#task-mode-differences "choosing-task-mode.md#task-mode-differences").

Type: String

Valid Values: `BASIC | ENHANCED`

Required: No

**[TaskReportConfig](#API_CreateTask_RequestSyntax "#API_CreateTask_RequestSyntax")**

Specifies how you want to configure a task report, which provides detailed information
about your DataSync transfer. For more information, see [Monitoring your DataSync
transfers with task reports](task-reports.md "task-reports.md").

When using this parameter, your caller identity (the role that you're using DataSync with) must have the `iam:PassRole` permission. The [AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess") policy includes this permission.

Type: [TaskReportConfig](API_TaskReportConfig.md "API_TaskReportConfig.md") object

Required: No

## Response Syntax

```
{
   "TaskArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TaskArn](#API_CreateTask_ResponseSyntax "#API_CreateTask_ResponseSyntax")**

The Amazon Resource Name (ARN) of the task.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`

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

### Sample Request for an Enhanced mode task

The following example creates a DataSync task that uses Enhanced
mode.

Unlike when creating Basic mode tasks, you don't have to specify an Amazon CloudWatch log group. With Enhanced mode tasks, DataSync automatically
sends task logs to a log group named `/aws/datasync`. If that log group doesn't
exist in your AWS Region, DataSync creates the log group on your
behalf when you create the task.

```
{
  "SourceLocationArn": "arn:aws:datasync:us-east-1:111222333444:location/1111aaaa2222bbbb3",
  "DestinationLocationArn": "arn:aws:datasync:us-east-1:111222333444:location/0000zzzz1111yyyy2",
  "Name": "My Enhanced mode task",
  "TaskMode": "ENHANCED",
  "Options": {
    "TransferMode": "CHANGED",
    "VerifyMode": "ONLY_FILES_TRANSFERRED",
    "ObjectTags": "PRESERVE",
    "LogLevel": "TRANSFER"
  }
}
```

### Sample Request for a Basic mode task

The following example creates a DataSync task that uses Basic mode.

```
{
    "SourceLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3",
    "DestinationLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2",
    "Name": "My Basic mode task",
    "TaskMode": "BASIC",
    "Options": {
        "Atime": "BEST_EFFORT",
        "Gid": "NONE",
        "Mtime": "PRESERVE",
        "PosixPermissions": "PRESERVE",
        "PreserveDevices": "NONE",
        "PreserveDeletedFiles": "PRESERVE",
        "Uid": "NONE",
        "VerifyMode": "ONLY_FILES_TRANSFERRED"
    },
    "Schedule": {
        "ScheduleExpression": "0 12 ? * SUN,WED *"
    },
    "CloudWatchLogGroupArn": "arn:aws:logs:us-east-2:111222333444:log-group:/log-group-name:*",
    "Tags": [
        {
            "Key": "Name",
            "Value": "Migration-wave-1"
        }
    ]
}
```

### Sample Response

The following response includes the ARN of a created task.

```
{
  "TaskArn": "arn:aws:datasync:us-east-2:111222333444:task/task-08de6e6697796f026"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateTask.md "../../../goto/cli2/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateTask.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateTask.md "../../../goto/boto3/datasync-2018-11-09/CreateTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateTask.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateTask.md")

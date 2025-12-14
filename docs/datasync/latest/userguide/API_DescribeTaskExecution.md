# DescribeTaskExecution

Provides information about an execution of your AWS DataSync task. You can
use this operation to help monitor the progress of an ongoing data transfer or check the
results of the transfer.

###### Note

Some `DescribeTaskExecution` response elements are only relevant to a
specific task mode. For information, see [Understanding task mode differences](choosing-task-mode.md#task-mode-differences "choosing-task-mode.md#task-mode-differences") and [Understanding data
transfer performance counters](transfer-performance-counters.md "transfer-performance-counters.md").

## Request Syntax

```
{
   "TaskExecutionArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[TaskExecutionArn](#API_DescribeTaskExecution_RequestSyntax "#API_DescribeTaskExecution_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the task execution that you want
information about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

Required: Yes

## Response Syntax

```
{
   "BytesCompressed": ***number***,
   "BytesTransferred": ***number***,
   "BytesWritten": ***number***,
   "EndTime": ***number***,
   "EstimatedBytesToTransfer": ***number***,
   "EstimatedFilesToDelete": ***number***,
   "EstimatedFilesToTransfer": ***number***,
   "EstimatedFoldersToDelete": ***number***,
   "EstimatedFoldersToTransfer": ***number***,
   "Excludes": [
      {
         "FilterType": "***string***",
         "Value": "***string***"
      }
   ],
   "FilesDeleted": ***number***,
   "FilesFailed": {
      "Delete": ***number***,
      "Prepare": ***number***,
      "Transfer": ***number***,
      "Verify": ***number***
   },
   "FilesListed": {
      "AtDestinationForDelete": ***number***,
      "AtSource": ***number***
   },
   "FilesPrepared": ***number***,
   "FilesSkipped": ***number***,
   "FilesTransferred": ***number***,
   "FilesVerified": ***number***,
   "FoldersDeleted": ***number***,
   "FoldersFailed": {
      "Delete": ***number***,
      "List": ***number***,
      "Prepare": ***number***,
      "Transfer": ***number***,
      "Verify": ***number***
   },
   "FoldersListed": {
      "AtDestinationForDelete": ***number***,
      "AtSource": ***number***
   },
   "FoldersPrepared": ***number***,
   "FoldersSkipped": ***number***,
   "FoldersTransferred": ***number***,
   "FoldersVerified": ***number***,
   "Includes": [
      {
         "FilterType": "***string***",
         "Value": "***string***"
      }
   ],
   "LaunchTime": ***number***,
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
   "ReportResult": {
      "ErrorCode": "***string***",
      "ErrorDetail": "***string***",
      "Status": "***string***"
   },
   "Result": {
      "ErrorCode": "***string***",
      "ErrorDetail": "***string***",
      "PrepareDuration": ***number***,
      "PrepareStatus": "***string***",
      "TotalDuration": ***number***,
      "TransferDuration": ***number***,
      "TransferStatus": "***string***",
      "VerifyDuration": ***number***,
      "VerifyStatus": "***string***"
   },
   "StartTime": ***number***,
   "Status": "***string***",
   "TaskExecutionArn": "***string***",
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

**[BytesCompressed](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of physical bytes that DataSync transfers over the network after
compression (if compression is possible). This number is typically less than [BytesTransferred](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-BytesTransferred "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-BytesTransferred") unless the data isn't compressible.

Type: Long

**[BytesTransferred](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of bytes that DataSync sends to the network before compression (if
compression is possible). For the number of bytes transferred over the network, see [BytesCompressed](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-BytesCompressed "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-BytesCompressed").

Type: Long

**[BytesWritten](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of logical bytes that DataSync actually writes to the destination
location.

Type: Long

**[EndTime](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The time that the transfer task ends.

Type: Timestamp

**[EstimatedBytesToTransfer](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of logical bytes that DataSync expects to write to the destination
location.

Type: Long

**[EstimatedFilesToDelete](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync expects to delete in
your destination location. If you don't configure your task to [delete data in the destination that
isn't in the source](configure-metadata.md "configure-metadata.md"), the value is always `0`.

###### Note

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[EstimatedFoldersToDelete](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-EstimatedFoldersToDelete "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-EstimatedFoldersToDelete").

Type: Long

**[EstimatedFilesToTransfer](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync expects to
transfer over the network. This value is calculated while DataSync
[prepares](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses") the transfer.

How this gets calculated depends primarily on your task’s [transfer
mode](API_Options.md#DataSync-Type-Options-TransferMode "API_Options.md#DataSync-Type-Options-TransferMode") configuration:

- If `TranserMode` is set to `CHANGED` - The calculation is based
  on comparing the content of the source and destination locations and determining the
  difference that needs to be transferred. The difference can include:
  - Anything that's added or modified at the source location.
  - Anything that's in both locations and modified at the destination after an initial
    transfer (unless [OverwriteMode](API_Options.md#DataSync-Type-Options-OverwriteMode "API_Options.md#DataSync-Type-Options-OverwriteMode") is set to `NEVER`).
  - **(Basic task mode only)** The number of items that
    DataSync expects to delete (if [PreserveDeletedFiles](API_Options.md#DataSync-Type-Options-PreserveDeletedFiles "API_Options.md#DataSync-Type-Options-PreserveDeletedFiles") is set to
    `REMOVE`).

- If `TranserMode` is set to `ALL` - The calculation is based only
  on the items that DataSync finds at the source location.

###### Note

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[EstimatedFoldersToTransfer](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-EstimatedFoldersToTransfer "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-EstimatedFoldersToTransfer").

Type: Long

**[EstimatedFoldersToDelete](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync expects to delete in
your destination location. If you don't configure your task to [delete data in the destination that
isn't in the source](configure-metadata.md "configure-metadata.md"), the value is always `0`.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[EstimatedFoldersToTransfer](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync expects to
transfer over the network. This value is calculated as DataSync
[prepares](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses") directories to transfer.

How this gets calculated depends primarily on your task’s [transfer
mode](API_Options.md#DataSync-Type-Options-TransferMode "API_Options.md#DataSync-Type-Options-TransferMode") configuration:

- If `TranserMode` is set to `CHANGED` - The calculation is based
  on comparing the content of the source and destination locations and determining the
  difference that needs to be transferred. The difference can include:
  - Anything that's added or modified at the source location.
  - Anything that's in both locations and modified at the destination after an initial
    transfer (unless [OverwriteMode](API_Options.md#DataSync-Type-Options-OverwriteMode "API_Options.md#DataSync-Type-Options-OverwriteMode") is set to `NEVER`).

- If `TranserMode` is set to `ALL` - The calculation is based only
  on the items that DataSync finds at the source location.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[Excludes](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

A list of filter rules that exclude specific data during your transfer. For more
information and examples, see [Filtering data transferred by DataSync](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

**[FilesDeleted](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync actually deletes in
your destination location. If you don't configure your task to [delete data in the destination that
isn't in the source](configure-metadata.md "configure-metadata.md"), the value is always `0`.

###### Note

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[FoldersDeleted](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersDeleted "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersDeleted").

Type: Long

**[FilesFailed](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files or objects that DataSync fails to prepare, transfer, verify, and
delete during your task execution.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: [TaskExecutionFilesFailedDetail](API_TaskExecutionFilesFailedDetail.md "API_TaskExecutionFilesFailedDetail.md") object

**[FilesListed](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files or objects that DataSync finds at your locations.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: [TaskExecutionFilesListedDetail](API_TaskExecutionFilesListedDetail.md "API_TaskExecutionFilesListedDetail.md") object

**[FilesPrepared](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files or objects that DataSync will attempt to transfer after comparing
your source and destination locations.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

This counter isn't applicable if you configure your task to [transfer
all data](configure-metadata.md#task-option-transfer-mode "configure-metadata.md#task-option-transfer-mode"). In that scenario, DataSync copies everything from the source to
the destination without comparing differences between the locations.

Type: Long

**[FilesSkipped](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync skips during your
transfer.

###### Note

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[FoldersSkipped](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersSkipped "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersSkipped").

Type: Long

**[FilesTransferred](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync actually
transfers over the network. This value is updated periodically during your task execution when
something is read from the source and sent over the network.

If DataSync fails to transfer something, this value can be less than
`EstimatedFilesToTransfer`. In some cases, this value can also be greater than
`EstimatedFilesToTransfer`. This element is implementation-specific for some
location types, so don't use it as an exact indication of what's transferring or to monitor
your task execution.

###### Note

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[FoldersTransferred](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersTransferred "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersTransferred").

Type: Long

**[FilesVerified](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of files, objects, and directories that DataSync verifies during your
transfer.

###### Note

When you configure your task to [verify only the
data that's transferred](configure-data-verification-options.md "configure-data-verification-options.md"), DataSync doesn't verify directories in some
situations or files that fail to transfer.

For [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md"), this counter only includes files or objects. Directories are counted in
[FoldersVerified](API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersVerified "API_DescribeTaskExecution.md#DataSync-DescribeTaskExecution-response-FoldersVerified").

Type: Long

**[FoldersDeleted](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync actually deletes in
your destination location. If you don't configure your task to [delete data in the destination that
isn't in the source](configure-metadata.md "configure-metadata.md"), the value is always `0`.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[FoldersFailed](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync fails to list, prepare, transfer, verify, and
delete during your task execution.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: [TaskExecutionFoldersFailedDetail](API_TaskExecutionFoldersFailedDetail.md "API_TaskExecutionFoldersFailedDetail.md") object

**[FoldersListed](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync finds at your locations.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: [TaskExecutionFoldersListedDetail](API_TaskExecutionFoldersListedDetail.md "API_TaskExecutionFoldersListedDetail.md") object

**[FoldersPrepared](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync will attempt to transfer after comparing
your source and destination locations.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

This counter isn't applicable if you configure your task to [transfer
all data](configure-metadata.md#task-option-transfer-mode "configure-metadata.md#task-option-transfer-mode"). In that scenario, DataSync copies everything from the source to
the destination without comparing differences between the locations.

Type: Long

**[FoldersSkipped](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync skips during your
transfer.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[FoldersTransferred](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync actually
transfers over the network. This value is updated periodically during your task execution when
something is read from the source and sent over the network.

If DataSync fails to transfer something, this value can be less than
`EstimatedFoldersToTransfer`. In some cases, this value can also be greater than
`EstimatedFoldersToTransfer`.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[FoldersVerified](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The number of directories that DataSync verifies during your transfer.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

Type: Long

**[Includes](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

A list of filter rules that include specific data during your transfer. For more
information and examples, see [Filtering data transferred by DataSync](filtering.md "filtering.md").

Type: Array of [FilterRule](API_FilterRule.md "API_FilterRule.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

**[LaunchTime](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The time that the task execution actually begins. For non-queued tasks,
`LaunchTime` and `StartTime` are typically the same. For queued tasks,
`LaunchTime` is typically later than `StartTime` because previously
queued tasks must finish running before newer tasks can begin.

Type: Timestamp

**[ManifestConfig](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The configuration of the manifest that lists the files or objects to transfer. For more
information, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

Type: [ManifestConfig](API_ManifestConfig.md "API_ManifestConfig.md") object

**[Options](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You
also can specify how to verify data integrity, set bandwidth limits for your task, among other
options.

Each option has a default value. Unless you need to, you don't have to configure any
option before calling [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md").

You also can override your task options for each task execution. For example, you might
want to adjust the `LogLevel` for an individual execution.

Type: [Options](API_Options.md "API_Options.md") object

**[ReportResult](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

Indicates whether DataSync generated a complete [task report](task-reports.md "task-reports.md") for your
transfer.

Type: [ReportResult](API_ReportResult.md "API_ReportResult.md") object

**[Result](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The result of the task execution.

Type: [TaskExecutionResultDetail](API_TaskExecutionResultDetail.md "API_TaskExecutionResultDetail.md") object

**[StartTime](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The time that DataSync sends the request to start the task execution. For
non-queued tasks, `LaunchTime` and `StartTime` are typically the same.
For queued tasks, `LaunchTime` is typically later than `StartTime`
because previously queued tasks must finish running before newer tasks can begin.

Type: Timestamp

**[Status](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The status of the task execution.

For detailed information about task execution statuses, see [Task execution statuses](run-task.md#understand-task-execution-statuses "run-task.md#understand-task-execution-statuses").

Type: String

Valid Values: `QUEUED | CANCELLING | LAUNCHING | PREPARING | TRANSFERRING | VERIFYING | SUCCESS | ERROR`

**[TaskExecutionArn](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The ARN of the task execution that you wanted information about.
`TaskExecutionArn` is hierarchical and includes `TaskArn` for the task
that was executed.

For example, a `TaskExecution` value with the ARN
`arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b`
executed the task with the ARN
`arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2`.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

**[TaskMode](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The task mode that you're using. For more information, see [Choosing a task mode for your data
transfer](choosing-task-mode.md "choosing-task-mode.md").

Type: String

Valid Values: `BASIC | ENHANCED`

**[TaskReportConfig](#API_DescribeTaskExecution_ResponseSyntax "#API_DescribeTaskExecution_ResponseSyntax")**

The configuration of your task report, which provides detailed information about for your
DataSync transfer. For more information, see [Creating a task report](task-reports.md "task-reports.md").

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

This example illustrates a `DescribeTaskExecution` request.

```
{
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:111222333444:task/task-aaaabbbbccccddddf/execution/exec-1234abcd1234abcd1"
}
```

### Sample Response 1 for an Enhanced mode task execution

The following example describes a DataSync task execution that uses Enhanced
mode. The execution is also transferring specific data by using exclude and include
filters.

```
{
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:111222333444:task/task-aaaabbbbccccddddf/execution/exec-1234abcd1234abcd1",
    "Status": "SUCCESS",
    "Options": {
        "VerifyMode": "ONLY_FILES_TRANSFERRED",
        "OverwriteMode": "ALWAYS",
        "Atime": "BEST_EFFORT",
        "Mtime": "PRESERVE",
        "Uid": "NONE",
        "Gid": "NONE",
        "PreserveDeletedFiles": "PRESERVE",
        "PreserveDevices": "NONE",
        "PosixPermissions": "NONE",
        "BytesPerSecond": -1,
        "TaskQueueing": "ENABLED",
        "LogLevel": "BASIC",
        "TransferMode": "CHANGED",
        "SecurityDescriptorCopyFlags": "NONE",
        "ObjectTags": "PRESERVE"
    },
    "Excludes": [{
        "FilterType": "SIMPLE_PATTERN",
        "Value": "/archive-files"
    }],
    "Includes": [{
        "FilterType": "SIMPLE_PATTERN",
        "Value": "/files"
    }],
    "StartTime": "2024-10-16T11:19:56.844000-04:00",
    "EstimatedFilesToTransfer": 7,
    "EstimatedFoldersToTransfer": 2,
    "EstimatedBytesToTransfer": 30,
    "FilesTransferred": 7,
    "FoldersTransferred": 2,
    "BytesWritten": 30,
    "BytesTransferred": 30,
    "BytesCompressed": 30,
    "Result": {
        "PrepareDuration": 0,
        "PrepareStatus": "SUCCESS",
        "TotalDuration": 3310,
        "TransferDuration": 0,
        "TransferStatus": "SUCCESS",
        "VerifyDuration": 0,
        "VerifyStatus": "SUCCESS"
    },
    "FilesDeleted": 0,
    "FilesSkipped": 0,
    "FilesVerified": 7,
    "EstimatedFilesToDelete": 0,
    "TaskMode": "ENHANCED",
    "FilesPrepared": 7,
    "FilesListed": {
        "AtSource": 7,
        "AtDestinationForDelete": 0
    },
    "FilesFailed": {
        "Prepare": 0,
        "Transfer": 0,
        "Verify": 0,
        "Delete": 0
    },
    "FoldersDeleted": 0,
    "FoldersSkipped": 0,
    "FoldersVerified": 2,
    "FoldersPrepared": 2,
    "FoldersListed": {
        "AtSource": 2,
        "AtDestinationForDelete": 0
    },
    "FoldersFailed": {
        "List": 0,
        "Prepare": 0,
        "Transfer": 0,
        "Verify": 0,
        "Delete": 0
    }
}
```

### Sample Response 2 for an Enhanced mode task execution

The following example describes another DataSync task execution that uses
Enhanced mode. In this situation, the execution is transferring specific data by using a
manifest instead of filters.

```
{
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:111222333444:task/task-aaaabbbbccccddddf/execution/exec-1234abcd1234abcd1",
    "Status": "SUCCESS",
    "Options": {
        "VerifyMode": "ONLY_FILES_TRANSFERRED",
        "OverwriteMode": "ALWAYS",
        "Atime": "BEST_EFFORT",
        "Mtime": "PRESERVE",
        "Uid": "NONE",
        "Gid": "NONE",
        "PreserveDeletedFiles": "PRESERVE",
        "PreserveDevices": "NONE",
        "PosixPermissions": "NONE",
        "BytesPerSecond": -1,
        "TaskQueueing": "ENABLED",
        "LogLevel": "TRANSFER",
        "TransferMode": "CHANGED",
        "SecurityDescriptorCopyFlags": "NONE",
        "ObjectTags": "PRESERVE"
    },
    "Excludes": [],
    "Includes": [],
    "ManifestConfig": {
        "Action": "TRANSFER",
        "Format": "CSV",
        "S3AccessRoleArn": "arn:aws:iam::111222333444:role/service-role/DataSyncS3ManifestAccess",
        "S3Bucket": "arn:aws:s3:::manifests-datasync",
        "VersionId": "Ixs7NQzEOj8BkL9r4ywX2FtDh_cPf3mG",
        "Source": {
            "S3": {
                "ManifestObjectPath": "manifest-folder/manifest-versioned-files",
                "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/my-manifest-role/DataSyncS3ManifestAccess",
                "S3BucketArn": "arn:aws:s3:::manifests-datasync",
                "ManifestObjectVersionId": "Ixs7NQzEOj8BkL9r4ywX2FtDh_cPf3mG"
            }
        }
    },
    "StartTime": "2024-10-16T09:29:56.757000-04:00",
    "EstimatedFilesToTransfer": 1,
    "EstimatedFoldersToTransfer": 0,
    "EstimatedBytesToTransfer": 6,
    "FilesTransferred": 1,
    "FoldersTransferred": 1,
    "BytesWritten": 6,
    "BytesTransferred": 6,
    "BytesCompressed": 6,
    "Result": {
        "PrepareDuration": 0,
        "PrepareStatus": "SUCCESS",
        "TotalDuration": 3089,
        "TransferDuration": 0,
        "TransferStatus": "SUCCESS",
        "VerifyDuration": 0,
        "VerifyStatus": "SUCCESS"
    },
    "TaskReportConfig": {
        "Destination": {
            "S3": {
                "Subdirectory": "reports/",
                "S3BucketArn": "arn:aws:s3:::my-task-report",
                "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/my-task-report-role/DataSyncTaskReportS3BucketAccess"
            }
        },
        "OutputType": "STANDARD",
        "ReportLevel": "SUCCESSES_AND_ERRORS",
        "ObjectVersionIds": "INCLUDE"
    },
    "FilesDeleted": 0,
    "FilesSkipped": 0,
    "FilesVerified": 1,
    "ReportResult": {
        "Status": "SUCCESS"
    },
    "EstimatedFilesToDelete": 0,
    "TaskMode": "ENHANCED",
    "FilesPrepared": 1,
    "FilesListed": {
        "AtSource": 1,
        "AtDestinationForDelete": 0
    },
    "FilesFailed": {
        "Prepare": 0,
        "Transfer": 0,
        "Verify": 0,
        "Delete": 0
    },
    "FoldersDeleted": 0,
    "FoldersSkipped": 0,
    "FoldersVerified": 0,
    "FoldersPrepared": 0,
    "FoldersListed": {
        "AtSource": 0,
        "AtDestinationForDelete": 0
    },
    "FoldersFailed": {
        "List": 0,
        "Prepare": 0,
        "Transfer": 0,
        "Verify": 0,
        "Delete": 0
    }
  }
```

### Sample Response for a Basic mode task execution

The following example describes a DataSync task execution that uses Basic
mode.

```
{
    "TaskExecutionArn": "arn:aws:datasync:us-east-1:111222333444:task/task-aaaabbbbccccddddf/execution/exec-1234abcd1234abcd1",
    "BytesCompressed": 3500,
    "BytesTransferred": 5000,
    "BytesWritten": 5000,
    "EstimatedBytesToTransfer": 5000,
    "EstimatedFilesToDelete": 10,
    "EstimatedFilesToTransfer": 100,
    "FilesDeleted": 10,
    "FilesSkipped": 0,
    "FilesTransferred": 100,
    "FilesVerified": 100,
    "Result": {
        "PrepareDuration": 100,
        "PrepareStatus": "SUCCESS",
        "TransferDuration": 60,
        "TransferStatus": "SUCCESS",
        "VerifyDuration": 30,
        "VerifyStatus": "SUCCESS"
    },
    "StartTime": "2024-10-16T11:19:56.844000-04:00",
    "Status": "SUCCESS",
    "OverrideOptions": {
        "Atime": "BEST_EFFORT",
        "BytesPerSecond": "1000",
        "Gid": "NONE",
        "Mtime": "PRESERVE",
        "PosixPermissions": "PRESERVE",
        "PreserveDeletedFiles": "PRESERVE",
        "Uid": "NONE",
        "VerifyMode": "POINT_IN_TIME_CONSISTENT"
    },
    "TaskReportConfig": {
        "Destination": {
            "S3": {
                "BucketAccessRoleArn": "arn:aws:iam::111222333444:role/my-datasync-role",
                "S3BucketArn": "arn:aws:s3:::my-task-reports-bucket/*",
                "Subdirectory": "reports"
            }
        },
        "ObjectVersionIds": "INCLUDE",
        "OutputType": "STANDARD",
        "Overrides": {
            "Deleted": {
                "ReportLevel": "ERRORS_ONLY"
            },
            "Skipped": {
                "ReportLevel": "SUCCESSES_AND_ERRORS"
            },
            "Transferred": {
                "ReportLevel": "ERRORS_ONLY"
            },
            "Verified": {
                "ReportLevel": "ERRORS_ONLY"
            }
        },
        "ReportLevel": "ERRORS_ONLY"
    }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/cli2/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/boto3/datasync-2018-11-09/DescribeTaskExecution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeTaskExecution.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeTaskExecution.md")

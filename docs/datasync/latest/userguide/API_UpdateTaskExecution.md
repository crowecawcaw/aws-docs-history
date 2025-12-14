# UpdateTaskExecution

Updates the configuration of a running AWS DataSync task execution.

###### Note

Currently, the only `Option` that you can modify with
`UpdateTaskExecution` is `BytesPerSecond`, which throttles bandwidth for a running or queued task
execution.

## Request Syntax

```
{
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
   "TaskExecutionArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Options](#API_UpdateTaskExecution_RequestSyntax "#API_UpdateTaskExecution_RequestSyntax")**

Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You
also can specify how to verify data integrity, set bandwidth limits for your task, among other
options.

Each option has a default value. Unless you need to, you don't have to configure any
option before calling [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md").

You also can override your task options for each task execution. For example, you might
want to adjust the `LogLevel` for an individual execution.

Type: [Options](API_Options.md "API_Options.md") object

Required: Yes

**[TaskExecutionArn](#API_UpdateTaskExecution_RequestSyntax "#API_UpdateTaskExecution_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the task execution that you're
updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/cli2/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/boto3/datasync-2018-11-09/UpdateTaskExecution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateTaskExecution.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateTaskExecution.md")

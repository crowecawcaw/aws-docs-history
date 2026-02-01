# CancelTaskExecution

Stops an AWS DataSync task execution that's in progress. The transfer of some
files are abruptly interrupted. File contents that're transferred to the destination might be
incomplete or inconsistent with the source files.

However, if you start a new task execution using the same task and allow it to finish,
file content on the destination will be complete and consistent. This applies to other
unexpected failures that interrupt a task execution. In all of these cases, DataSync
successfully completes the transfer when you start the next task execution.

## Request Syntax

```
{
   "TaskExecutionArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[TaskExecutionArn](#API_CancelTaskExecution_RequestSyntax "#API_CancelTaskExecution_RequestSyntax")**

The Amazon Resource Name (ARN) of the task execution to stop.

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/cli2/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForCpp/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/boto3/datasync-2018-11-09/CancelTaskExecution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CancelTaskExecution.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CancelTaskExecution.md")

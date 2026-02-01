# ListTaskExecutions

Returns a list of executions for an AWS DataSync transfer task.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "TaskArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_ListTaskExecutions_RequestSyntax "#API_ListTaskExecutions_RequestSyntax")**

Specifies how many results you want in the response.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[NextToken](#API_ListTaskExecutions_RequestSyntax "#API_ListTaskExecutions_RequestSyntax")**

Specifies an opaque string that indicates the position at which to begin the next list
of results in the response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

Required: No

**[TaskArn](#API_ListTaskExecutions_RequestSyntax "#API_ListTaskExecutions_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the task that you want execution
information about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "TaskExecutions": [
      {
         "Status": "***string***",
         "TaskExecutionArn": "***string***",
         "TaskMode": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTaskExecutions_ResponseSyntax "#API_ListTaskExecutions_ResponseSyntax")**

The opaque string that indicates the position to begin the next list of results in the
response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

**[TaskExecutions](#API_ListTaskExecutions_ResponseSyntax "#API_ListTaskExecutions_ResponseSyntax")**

A list of the task's executions.

Type: Array of [TaskExecutionListEntry](API_TaskExecutionListEntry.md "API_TaskExecutionListEntry.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/cli2/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForCpp/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForGoV2/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForKotlin/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/boto3/datasync-2018-11-09/ListTaskExecutions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTaskExecutions.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTaskExecutions.md")

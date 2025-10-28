# ListTasks

Returns a list of the AWS DataSync tasks you created.

## Request Syntax

```
{
   "Filters": [
      {
         "Name": "`string`",
         "Operator": "`string`",
         "Values": [ "`string`" ]
      }
   ],
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Filters](#API_ListTasks_RequestSyntax "#API_ListTasks_RequestSyntax")**

You can use API filters to narrow down the list of resources returned by
`ListTasks`. For example, to retrieve all tasks on a specific source location,
you can use `ListTasks` with filter name `LocationId` and `Operator
 Equals` with the ARN for the location.

Type: Array of [TaskFilter](API_TaskFilter.md "API_TaskFilter.md") objects

Required: No

**[MaxResults](#API_ListTasks_RequestSyntax "#API_ListTasks_RequestSyntax")**

The maximum number of tasks to return.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[NextToken](#API_ListTasks_RequestSyntax "#API_ListTasks_RequestSyntax")**

An opaque string that indicates the position at which to begin the next list of
tasks.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "Tasks": [
      {
         "Name": "***string***",
         "Status": "***string***",
         "TaskArn": "***string***",
         "TaskMode": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTasks_ResponseSyntax "#API_ListTasks_ResponseSyntax")**

An opaque string that indicates the position at which to begin returning the next list
of tasks.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

**[Tasks](#API_ListTasks_ResponseSyntax "#API_ListTasks_ResponseSyntax")**

A list of all the tasks that are returned.

Type: Array of [TaskListEntry](API_TaskListEntry.md "API_TaskListEntry.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/ListTasks.md "../../../goto/cli2/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/ListTasks.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForCpp/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForGoV2/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForKotlin/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/ListTasks.md "../../../goto/boto3/datasync-2018-11-09/ListTasks.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTasks.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTasks.md")

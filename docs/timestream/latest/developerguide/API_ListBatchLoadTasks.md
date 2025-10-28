For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ListBatchLoadTasks

Provides a list of batch load tasks, along with the name, status, when the task is resumable until, and other
details. See [code sample](code-samples.md "code-samples.md") for
details.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "TaskStatus": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_ListBatchLoadTasks_RequestSyntax "#API_ListBatchLoadTasks_RequestSyntax")**

The total number of items to return in the output. If the total number of items available is more than the value
specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a
subsequent API invocation.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListBatchLoadTasks_RequestSyntax "#API_ListBatchLoadTasks_RequestSyntax")**

A token to specify where to start paginating. This is the NextToken from a previously truncated response.

Type: String

Required: No

**[TaskStatus](#API_ListBatchLoadTasks_RequestSyntax "#API_ListBatchLoadTasks_RequestSyntax")**

Status of the batch load task.

Type: String

Valid Values: `CREATED | IN_PROGRESS | FAILED | SUCCEEDED | PROGRESS_STOPPED | PENDING_RESUME`

Required: No

## Response Syntax

```
{
   "BatchLoadTasks": [
      {
         "CreationTime": ***number***,
         "DatabaseName": "***string***",
         "LastUpdatedTime": ***number***,
         "ResumableUntil": ***number***,
         "TableName": "***string***",
         "TaskId": "***string***",
         "TaskStatus": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BatchLoadTasks](#API_ListBatchLoadTasks_ResponseSyntax "#API_ListBatchLoadTasks_ResponseSyntax")**

A list of batch load task details.

Type: Array of [BatchLoadTask](API_BatchLoadTask.md "API_BatchLoadTask.md") objects

**[NextToken](#API_ListBatchLoadTasks_ResponseSyntax "#API_ListBatchLoadTasks_ResponseSyntax")**

A token to specify where to start paginating. Provide the next ListBatchLoadTasksRequest.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You are not authorized to perform this action.

HTTP Status Code: 400

**InternalServerException**

Timestream was unable to fully process this request because of an internal server error.

HTTP Status Code: 500

**InvalidEndpointException**

The requested endpoint was not valid.

HTTP Status Code: 400

**ThrottlingException**

Too many requests were made by a user and they exceeded the service quotas. The request was throttled.

HTTP Status Code: 400

**ValidationException**

An invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/cli2/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/DotNetSDKV3/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForGoV2/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForJavaScriptV3/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForKotlin/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForPHPV3/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/boto3/timestream-write-2018-11-01/ListBatchLoadTasks.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/ListBatchLoadTasks.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/ListBatchLoadTasks.md")

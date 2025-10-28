For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DeleteScheduledQuery

Deletes a given scheduled query. This is an irreversible operation.

## Request Syntax

```
{
   "ScheduledQueryArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ScheduledQueryArn](#API_query_DeleteScheduledQuery_RequestSyntax "#API_query_DeleteScheduledQuery_RequestSyntax")**

The ARN of the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have the necessary permissions to access the account settings.

HTTP Status Code: 400

**InternalServerException**

An internal server error occurred while processing the request.

HTTP Status Code: 400

**InvalidEndpointException**

The requested endpoint is invalid.

HTTP Status Code: 400

**ResourceNotFoundException**

The requested resource could not be found.

**ScheduledQueryArn**

The ARN of the scheduled query.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/cli2/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/boto3/timestream-query-2018-11-01/DeleteScheduledQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DeleteScheduledQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DeleteScheduledQuery.md")

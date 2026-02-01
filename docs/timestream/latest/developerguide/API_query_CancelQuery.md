For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CancelQuery

Cancels a query that has been issued. Cancellation is provided only if the query has
not completed running before the cancellation request was issued. Because cancellation
is an idempotent operation, subsequent cancellation requests will return a
`CancellationMessage`, indicating that the query has already been
canceled. See [code
sample](code-samples.md "code-samples.md") for details.

## Request Syntax

```
{
   "QueryId": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[QueryId](#API_query_CancelQuery_RequestSyntax "#API_query_CancelQuery_RequestSyntax")**

The ID of the query that needs to be cancelled. `QueryID` is returned as
part of the query result.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: Yes

## Response Syntax

```
{
   "CancellationMessage": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CancellationMessage](#API_query_CancelQuery_ResponseSyntax "#API_query_CancelQuery_ResponseSyntax")**

A `CancellationMessage` is returned when a `CancelQuery`
request for the query specified by `QueryId` has already been issued.

Type: String

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

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/CancelQuery.md "../../../goto/cli2/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-query-2018-11-01/CancelQuery.md "../../../goto/DotNetSDKV4/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/CancelQuery.md "../../../goto/boto3/timestream-query-2018-11-01/CancelQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/CancelQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/CancelQuery.md")

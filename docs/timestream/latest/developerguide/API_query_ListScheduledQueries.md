For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ListScheduledQueries

Gets a list of all scheduled queries in the caller's Amazon account and Region.
`ListScheduledQueries` is eventually consistent.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_query_ListScheduledQueries_RequestSyntax "#API_query_ListScheduledQueries_RequestSyntax")**

The maximum number of items to return in the output. If the total number of items
available is more than the value specified, a `NextToken` is provided in the
output. To resume pagination, provide the `NextToken` value as the argument
to the subsequent call to `ListScheduledQueriesRequest`.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 1000.

Required: No

**[NextToken](#API_query_ListScheduledQueries_RequestSyntax "#API_query_ListScheduledQueries_RequestSyntax")**

A pagination token to resume pagination.

Type: String

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "ScheduledQueries": [
      {
         "Arn": "***string***",
         "CreationTime": ***number***,
         "ErrorReportConfiguration": {
            "S3Configuration": {
               "BucketName": "***string***",
               "EncryptionOption": "***string***",
               "ObjectKeyPrefix": "***string***"
            }
         },
         "LastRunStatus": "***string***",
         "Name": "***string***",
         "NextInvocationTime": ***number***,
         "PreviousInvocationTime": ***number***,
         "State": "***string***",
         "TargetDestination": {
            "TimestreamDestination": {
               "DatabaseName": "***string***",
               "TableName": "***string***"
            }
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_query_ListScheduledQueries_ResponseSyntax "#API_query_ListScheduledQueries_ResponseSyntax")**

A token to specify where to start paginating. This is the NextToken from a previously
truncated response.

Type: String

**[ScheduledQueries](#API_query_ListScheduledQueries_ResponseSyntax "#API_query_ListScheduledQueries_ResponseSyntax")**

A list of scheduled queries.

Type: Array of [ScheduledQuery](API_query_ScheduledQuery.md "API_query_ScheduledQuery.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/cli2/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/boto3/timestream-query-2018-11-01/ListScheduledQueries.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ListScheduledQueries.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ListScheduledQueries.md")

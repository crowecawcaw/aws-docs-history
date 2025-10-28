For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Query

`Query` is a synchronous operation that enables you to run a query against
your Amazon Timestream data.

If you enabled `QueryInsights`, this API also returns insights and metrics related to the query that you executed. `QueryInsights` helps with performance tuning of your query. For more information about `QueryInsights`, see [Using query insights to optimize queries in Amazon Timestream](using-query-insights.md "using-query-insights.md").

###### Note

The maximum number of `Query` API requests you're allowed to make with `QueryInsights` enabled is 1 query per second (QPS). If you exceed this query rate, it might result in throttling.

`Query` will time out after 60 seconds.
You must update the default timeout in the SDK to support a timeout of 60 seconds. See
the [code
sample](code-samples.md "code-samples.md") for details.

Your query request will fail in the following cases:

- If you submit a `Query` request with the same client token outside
  of the 5-minute idempotency window.
- If you submit a `Query` request with the same client token, but
  change other parameters, within the 5-minute idempotency window.
- If the size of the row (including the query metadata) exceeds 1 MB, then the
  query will fail with the following error message:

`Query aborted as max page response size has been exceeded by the output
 result row`

- If the IAM principal of the query initiator and the result reader are not the
  same and/or the query initiator and the result reader do not have the same query
  string in the query requests, the query will fail with an `Invalid
pagination token` error.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "MaxRows": `number`,
   "NextToken": "`string`",
   "QueryInsights": {
      "Mode": "`string`"
   },
   "QueryString": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ClientToken](#API_query_Query_RequestSyntax "#API_query_Query_RequestSyntax")**

Unique, case-sensitive string of up to 64 ASCII characters specified when a
`Query` request is made. Providing a `ClientToken` makes the
call to `Query`
_idempotent_. This means that running the same query repeatedly will
produce the same result. In other words, making multiple identical `Query`
requests has the same effect as making a single request. When using
`ClientToken` in a query, note the following:

- If the Query API is instantiated without a `ClientToken`, the
  Query SDK generates a `ClientToken` on your behalf.
- If the `Query` invocation only contains the
  `ClientToken` but does not include a `NextToken`, that
  invocation of `Query` is assumed to be a new query run.
- If the invocation contains `NextToken`, that particular invocation
  is assumed to be a subsequent invocation of a prior call to the Query API, and a
  result set is returned.
- After 4 hours, any request with the same `ClientToken` is treated
  as a new request.

Type: String

Length Constraints: Minimum length of 32. Maximum length of 128.

Required: No

**[MaxRows](#API_query_Query_RequestSyntax "#API_query_Query_RequestSyntax")**

The total number of rows to be returned in the `Query` output. The initial
run of `Query` with a `MaxRows` value specified will return the
result set of the query in two cases:

- The size of the result is less than `1MB`.
- The number of rows in the result set is less than the value of
  `maxRows`.

Otherwise, the initial invocation of `Query` only returns a
`NextToken`, which can then be used in subsequent calls to fetch the
result set. To resume pagination, provide the `NextToken` value in the
subsequent command.

If the row size is large (e.g. a row has many columns), Timestream may return
fewer rows to keep the response size from exceeding the 1 MB limit. If
`MaxRows` is not provided, Timestream will send the necessary
number of rows to meet the 1 MB limit.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 1000.

Required: No

**[NextToken](#API_query_Query_RequestSyntax "#API_query_Query_RequestSyntax")**

A pagination token used to return a set of results. When the `Query` API
is invoked using `NextToken`, that particular invocation is assumed to be a
subsequent invocation of a prior call to `Query`, and a result set is
returned. However, if the `Query` invocation only contains the
`ClientToken`, that invocation of `Query` is assumed to be a
new query run.

Note the following when using NextToken in a query:

- A pagination token can be used for up to five `Query` invocations,
  OR for a duration of up to 1 hour – whichever comes first.
- Using the same `NextToken` will return the same set of records. To
  keep paginating through the result set, you must to use the most recent
  `nextToken`.
- Suppose a `Query` invocation returns two `NextToken`
  values, `TokenA` and `TokenB`. If `TokenB` is
  used in a subsequent `Query` invocation, then `TokenA` is
  invalidated and cannot be reused.
- To request a previous result set from a query after pagination has begun, you
  must re-invoke the Query API.
- The latest `NextToken` should be used to paginate until
  `null` is returned, at which point a new `NextToken`
  should be used.
- If the IAM principal of the query initiator and the result reader are not the
  same and/or the query initiator and the result reader do not have the same query
  string in the query requests, the query will fail with an `Invalid
pagination token` error.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**[QueryInsights](#API_query_Query_RequestSyntax "#API_query_Query_RequestSyntax")**

Encapsulates settings for enabling `QueryInsights`.

Enabling `QueryInsights` returns insights and metrics in addition to query results for the query that you executed. You can use `QueryInsights` to tune your query performance.

Type: [QueryInsights](API_query_QueryInsights.md "API_query_QueryInsights.md") object

Required: No

**[QueryString](#API_query_Query_RequestSyntax "#API_query_Query_RequestSyntax")**

The query to be run by Timestream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 262144.

Required: Yes

## Response Syntax

```
{
   "ColumnInfo": [
      {
         "Name": "***string***",
         "Type": {
            "ArrayColumnInfo": "ColumnInfo",
            "RowColumnInfo": [
               "ColumnInfo"
            ],
            "ScalarType": "***string***",
            "TimeSeriesMeasureValueColumnInfo": "ColumnInfo"
         }
      }
   ],
   "NextToken": "***string***",
   "QueryId": "***string***",
   "QueryInsightsResponse": {
      "OutputBytes": ***number***,
      "OutputRows": ***number***,
      "QuerySpatialCoverage": {
         "Max": {
            "PartitionKey": [ "***string***" ],
            "TableArn": "***string***",
            "Value": ***number***
         }
      },
      "QueryTableCount": ***number***,
      "QueryTemporalRange": {
         "Max": {
            "TableArn": "***string***",
            "Value": ***number***
         }
      },
      "UnloadPartitionCount": ***number***,
      "UnloadWrittenBytes": ***number***,
      "UnloadWrittenRows": ***number***
   },
   "QueryStatus": {
      "CumulativeBytesMetered": ***number***,
      "CumulativeBytesScanned": ***number***,
      "ProgressPercentage": ***number***
   },
   "Rows": [
      {
         "Data": [
            {
               "ArrayValue": [
                  "Datum"
               ],
               "NullValue": ***boolean***,
               "RowValue": "Row",
               "ScalarValue": "***string***",
               "TimeSeriesValue": [
                  {
                     "Time": "***string***",
                     "Value": "Datum"
                  }
               ]
            }
         ]
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ColumnInfo](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

The column data types of the returned result set.

Type: Array of [ColumnInfo](API_query_ColumnInfo.md "API_query_ColumnInfo.md") objects

**[NextToken](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

A pagination token that can be used again on a `Query` call to get the
next set of results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

**[QueryId](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

A unique ID for the given query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

**[QueryInsightsResponse](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

Encapsulates `QueryInsights` containing insights and metrics related to the query that you executed.

Type: [QueryInsightsResponse](API_query_QueryInsightsResponse.md "API_query_QueryInsightsResponse.md") object

**[QueryStatus](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

Information about the status of the query, including progress and bytes
scanned.

Type: [QueryStatus](API_query_QueryStatus.md "API_query_QueryStatus.md") object

**[Rows](#API_query_Query_ResponseSyntax "#API_query_Query_ResponseSyntax")**

The result set rows returned by the query.

Type: Array of [Row](API_query_Row.md "API_query_Row.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have the necessary permissions to access the account settings.

HTTP Status Code: 400

**ConflictException**

Unable to poll results for a cancelled query.

HTTP Status Code: 400

**InternalServerException**

An internal server error occurred while processing the request.

HTTP Status Code: 400

**InvalidEndpointException**

The requested endpoint is invalid.

HTTP Status Code: 400

**QueryExecutionException**

Timestream was unable to run the query successfully.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/Query.md "../../../goto/cli2/timestream-query-2018-11-01/Query.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/Query.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/Query.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/Query.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/Query.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/Query.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/Query.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Query.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Query.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/Query.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/Query.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/Query.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/Query.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/Query.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/Query.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/Query.md "../../../goto/boto3/timestream-query-2018-11-01/Query.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Query.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Query.md")

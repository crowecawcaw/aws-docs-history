For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# PrepareQuery

A synchronous operation that allows you to submit a query with parameters to be stored
by Timestream for later running. Timestream only supports using this operation with
`ValidateOnly` set to `true`.

## Request Syntax

```
{
   "QueryString": "`string`",
   "ValidateOnly": `boolean`
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[QueryString](#API_query_PrepareQuery_RequestSyntax "#API_query_PrepareQuery_RequestSyntax")**

The Timestream query string that you want to use as a prepared statement. Parameter
names can be specified in the query string `@` character followed by an
identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 262144.

Required: Yes

**[ValidateOnly](#API_query_PrepareQuery_RequestSyntax "#API_query_PrepareQuery_RequestSyntax")**

By setting this value to `true`, Timestream will only validate that the
query string is a valid Timestream query, and not store the prepared query for later
use.

Type: Boolean

Required: No

## Response Syntax

```
{
   "Columns": [
      {
         "Aliased": ***boolean***,
         "DatabaseName": "***string***",
         "Name": "***string***",
         "TableName": "***string***",
         "Type": {
            "ArrayColumnInfo": {
               "Name": "***string***",
               "Type": "Type"
            },
            "RowColumnInfo": [
               {
                  "Name": "***string***",
                  "Type": "Type"
               }
            ],
            "ScalarType": "***string***",
            "TimeSeriesMeasureValueColumnInfo": {
               "Name": "***string***",
               "Type": "Type"
            }
         }
      }
   ],
   "Parameters": [
      {
         "Name": "***string***",
         "Type": {
            "ArrayColumnInfo": {
               "Name": "***string***",
               "Type": "Type"
            },
            "RowColumnInfo": [
               {
                  "Name": "***string***",
                  "Type": "Type"
               }
            ],
            "ScalarType": "***string***",
            "TimeSeriesMeasureValueColumnInfo": {
               "Name": "***string***",
               "Type": "Type"
            }
         }
      }
   ],
   "QueryString": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Columns](#API_query_PrepareQuery_ResponseSyntax "#API_query_PrepareQuery_ResponseSyntax")**

A list of SELECT clause columns of the submitted query string.

Type: Array of [SelectColumn](API_query_SelectColumn.md "API_query_SelectColumn.md") objects

**[Parameters](#API_query_PrepareQuery_ResponseSyntax "#API_query_PrepareQuery_ResponseSyntax")**

A list of parameters used in the submitted query string.

Type: Array of [ParameterMapping](API_query_ParameterMapping.md "API_query_ParameterMapping.md") objects

**[QueryString](#API_query_PrepareQuery_ResponseSyntax "#API_query_PrepareQuery_ResponseSyntax")**

The query string that you want prepare.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 262144.

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

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/cli2/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/boto3/timestream-query-2018-11-01/PrepareQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/PrepareQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/PrepareQuery.md")

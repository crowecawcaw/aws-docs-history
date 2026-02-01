For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DescribeEndpoints

DescribeEndpoints returns a list of available endpoints to make Timestream
API calls against. This API is available through both Write and Query.

Because the Timestream SDKs are designed to transparently work with the
service’s architecture, including the management and mapping of the service endpoints,
_it is not recommended that you use this API unless_:

- You are using [VPC endpoints (AWS PrivateLink) with Timestream](VPCEndpoints.md "VPCEndpoints.md")
- Your application uses a programming language that does not yet have SDK
  support
- You require better control over the client-side implementation
  For detailed information on how and when to use and implement DescribeEndpoints, see
  [The Endpoint Discovery Pattern](Using.md#Using-API.endpoint-discovery "Using.md#Using-API.endpoint-discovery").

## Response Syntax

```
{
   "Endpoints": [
      {
         "Address": "***string***",
         "CachePeriodInMinutes": ***number***
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Endpoints](#API_query_DescribeEndpoints_ResponseSyntax "#API_query_DescribeEndpoints_ResponseSyntax")**

An `Endpoints` object is returned when a `DescribeEndpoints`
request is made.

Type: Array of [Endpoint](API_query_Endpoint.md "API_query_Endpoint.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalServerException**

An internal server error occurred while processing the request.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/cli2/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/boto3/timestream-query-2018-11-01/DescribeEndpoints.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeEndpoints.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeEndpoints.md")

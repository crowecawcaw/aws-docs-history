For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DescribeAccountSettings

Describes the settings for your account that include the query pricing model and the configured maximum TCUs the service can use for your query workload.

You're charged only for the duration of compute units used for your workloads.

## Response Syntax

```
{
   "MaxQueryTCU": ***number***,
   "QueryCompute": {
      "ComputeMode": "***string***",
      "ProvisionedCapacity": {
         "ActiveQueryTCU": ***number***,
         "LastUpdate": {
            "Status": "***string***",
            "StatusMessage": "***string***",
            "TargetQueryTCU": ***number***
         },
         "NotificationConfiguration": {
            "RoleArn": "***string***",
            "SnsConfiguration": {
               "TopicArn": "***string***"
            }
         }
      }
   },
   "QueryPricingModel": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[MaxQueryTCU](#API_query_DescribeAccountSettings_ResponseSyntax "#API_query_DescribeAccountSettings_ResponseSyntax")**

The maximum number of [Timestream compute units](tcu.md "tcu.md") (TCUs) the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. This configuration is applicable only for on-demand usage of (TCUs).

Type: Integer

**[QueryCompute](#API_query_DescribeAccountSettings_ResponseSyntax "#API_query_DescribeAccountSettings_ResponseSyntax")**

An object that contains the usage settings for Timestream Compute Units (TCUs) in your account for the query workload. QueryCompute is available only in the Asia Pacific (Mumbai) region.

Type: [QueryComputeResponse](API_query_QueryComputeResponse.md "API_query_QueryComputeResponse.md") object

**[QueryPricingModel](#API_query_DescribeAccountSettings_ResponseSyntax "#API_query_DescribeAccountSettings_ResponseSyntax")**

The pricing model for queries in your account.

###### Note

The `QueryPricingModel` parameter is used by several Timestream operations; however, the `UpdateAccountSettings` API operation doesn't recognize any values other than `COMPUTE_UNITS`.

Type: String

Valid Values: `BYTES_SCANNED | COMPUTE_UNITS`

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/cli2/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/DotNetSDKV3/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/boto3/timestream-query-2018-11-01/DescribeAccountSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeAccountSettings.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeAccountSettings.md")

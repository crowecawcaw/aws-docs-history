# ListMetricAttributionMetrics

Lists the metrics for the metric attribution.

## Request Syntax

```
{
   "maxResults": `number`,
   "metricAttributionArn": "`string`",
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[maxResults](#API_ListMetricAttributionMetrics_RequestSyntax "#API_ListMetricAttributionMetrics_RequestSyntax")**

The maximum number of metrics to return in one page of results.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[metricAttributionArn](#API_ListMetricAttributionMetrics_RequestSyntax "#API_ListMetricAttributionMetrics_RequestSyntax")**

The Amazon Resource Name (ARN) of the metric attribution to retrieve attributes for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[nextToken](#API_ListMetricAttributionMetrics_RequestSyntax "#API_ListMetricAttributionMetrics_RequestSyntax")**

Specify the pagination token from a previous request to retrieve the next page of results.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "metrics": [
      {
         "eventType": "***string***",
         "expression": "***string***",
         "metricName": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metrics](#API_ListMetricAttributionMetrics_ResponseSyntax "#API_ListMetricAttributionMetrics_ResponseSyntax")**

The metrics for the specified metric attribution.

Type: Array of [MetricAttribute](API_MetricAttribute.md "API_MetricAttribute.md") objects

Array Members: Maximum number of 10 items.

**[nextToken](#API_ListMetricAttributionMetrics_ResponseSyntax "#API_ListMetricAttributionMetrics_ResponseSyntax")**

Specify the pagination token from a previous `ListMetricAttributionMetricsResponse` request to retrieve the next page of results.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/cli2/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/boto3/personalize-2018-05-22/ListMetricAttributionMetrics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListMetricAttributionMetrics.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListMetricAttributionMetrics.md")

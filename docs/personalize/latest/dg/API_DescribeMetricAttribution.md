# DescribeMetricAttribution

Describes a metric attribution.

## Request Syntax

```
{
   "metricAttributionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[metricAttributionArn](#API_DescribeMetricAttribution_RequestSyntax "#API_DescribeMetricAttribution_RequestSyntax")**

The metric attribution's Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "metricAttribution": {
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "failureReason": "***string***",
      "lastUpdatedDateTime": ***number***,
      "metricAttributionArn": "***string***",
      "metricsOutputConfig": {
         "roleArn": "***string***",
         "s3DataDestination": {
            "kmsKeyArn": "***string***",
            "path": "***string***"
         }
      },
      "name": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metricAttribution](#API_DescribeMetricAttribution_ResponseSyntax "#API_DescribeMetricAttribution_ResponseSyntax")**

The details of the metric attribution.

Type: [MetricAttribution](API_MetricAttribution.md "API_MetricAttribution.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/cli2/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/boto3/personalize-2018-05-22/DescribeMetricAttribution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeMetricAttribution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeMetricAttribution.md")

# CreateMetricAttribution

Creates a metric attribution.
A metric attribution creates reports on the data that you import into Amazon Personalize. Depending on how you imported the data, you can view reports in Amazon CloudWatch or Amazon S3.
For more information, see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "metrics": [
      {
         "eventType": "`string`",
         "expression": "`string`",
         "metricName": "`string`"
      }
   ],
   "metricsOutputConfig": {
      "roleArn": "`string`",
      "s3DataDestination": {
         "kmsKeyArn": "`string`",
         "path": "`string`"
      }
   },
   "name": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateMetricAttribution_RequestSyntax "#API_CreateMetricAttribution_RequestSyntax")**

The Amazon Resource Name (ARN) of the destination dataset group for the metric attribution.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[metrics](#API_CreateMetricAttribution_RequestSyntax "#API_CreateMetricAttribution_RequestSyntax")**

A list of metric attributes for the metric attribution. Each metric attribute specifies an event type to track and a function.
Available functions are `SUM()` or `SAMPLECOUNT()`. For SUM() functions, provide the
dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).

Type: Array of [MetricAttribute](API_MetricAttribute.md "API_MetricAttribute.md") objects

Array Members: Maximum number of 10 items.

Required: Yes

**[metricsOutputConfig](#API_CreateMetricAttribution_RequestSyntax "#API_CreateMetricAttribution_RequestSyntax")**

The output configuration details for the metric attribution.

Type: [MetricAttributionOutput](API_MetricAttributionOutput.md "API_MetricAttributionOutput.md") object

Required: Yes

**[name](#API_CreateMetricAttribution_RequestSyntax "#API_CreateMetricAttribution_RequestSyntax")**

A name for the metric attribution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

## Response Syntax

```
{
   "metricAttributionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metricAttributionArn](#API_CreateMetricAttribution_ResponseSyntax "#API_CreateMetricAttribution_ResponseSyntax")**

The Amazon Resource Name (ARN) for the new metric attribution.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/cli2/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/boto3/personalize-2018-05-22/CreateMetricAttribution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateMetricAttribution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateMetricAttribution.md")

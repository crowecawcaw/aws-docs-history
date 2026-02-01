# UpdateMetricAttribution

Updates a metric attribution.

## Request Syntax

```
{
   "addMetrics": [
      {
         "eventType": "`string`",
         "expression": "`string`",
         "metricName": "`string`"
      }
   ],
   "metricAttributionArn": "`string`",
   "metricsOutputConfig": {
      "roleArn": "`string`",
      "s3DataDestination": {
         "kmsKeyArn": "`string`",
         "path": "`string`"
      }
   },
   "removeMetrics": [ "`string`" ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[addMetrics](#API_UpdateMetricAttribution_RequestSyntax "#API_UpdateMetricAttribution_RequestSyntax")**

Add new metric attributes to the metric attribution.

Type: Array of [MetricAttribute](API_MetricAttribute.md "API_MetricAttribute.md") objects

Array Members: Maximum number of 10 items.

Required: No

**[metricAttributionArn](#API_UpdateMetricAttribution_RequestSyntax "#API_UpdateMetricAttribution_RequestSyntax")**

The Amazon Resource Name (ARN) for the metric attribution to update.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[metricsOutputConfig](#API_UpdateMetricAttribution_RequestSyntax "#API_UpdateMetricAttribution_RequestSyntax")**

An output config for the metric attribution.

Type: [MetricAttributionOutput](API_MetricAttributionOutput.md "API_MetricAttributionOutput.md") object

Required: No

**[removeMetrics](#API_UpdateMetricAttribution_RequestSyntax "#API_UpdateMetricAttribution_RequestSyntax")**

Remove metric attributes from the metric attribution.

Type: Array of strings

Array Members: Maximum number of 10 items.

Length Constraints: Maximum length of 256.

Required: No

## Response Syntax

```
{
   "metricAttributionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metricAttributionArn](#API_UpdateMetricAttribution_ResponseSyntax "#API_UpdateMetricAttribution_ResponseSyntax")**

The Amazon Resource Name (ARN) for the metric attribution that you updated.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/cli2/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForCpp/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/boto3/personalize-2018-05-22/UpdateMetricAttribution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateMetricAttribution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateMetricAttribution.md")

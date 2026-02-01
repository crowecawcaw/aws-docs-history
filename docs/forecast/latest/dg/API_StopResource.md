Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# StopResource

Stops a resource.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

The resource undergoes the following states: `CREATE_STOPPING` and
`CREATE_STOPPED`. You cannot resume a resource once it has been
stopped.

This operation can be applied to the following resources (and their corresponding child
resources):

- Dataset Import Job
- Predictor Job
- Forecast Job
- Forecast Export Job
- Predictor Backtest Export Job
- Explainability Job
- Explainability Export Job

## Request Syntax

```
{
   "ResourceArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceArn](#API_StopResource_RequestSyntax "#API_StopResource_RequestSyntax")**

The Amazon Resource Name (ARN) that identifies the resource to stop. The supported ARNs
are `DatasetImportJobArn`, `PredictorArn`,
`PredictorBacktestExportJobArn`, `ForecastArn`,
`ForecastExportJobArn`, `ExplainabilityArn`, and
`ExplainabilityExportArn`.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of resources per account has been exceeded.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/StopResource.md "../../../goto/cli2/forecast-2018-06-26/StopResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/StopResource.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/StopResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/StopResource.md "../../../goto/SdkForCpp/forecast-2018-06-26/StopResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/StopResource.md "../../../goto/SdkForGoV2/forecast-2018-06-26/StopResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/StopResource.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/StopResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/StopResource.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/StopResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/StopResource.md "../../../goto/SdkForKotlin/forecast-2018-06-26/StopResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/StopResource.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/StopResource.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/StopResource.md "../../../goto/boto3/forecast-2018-06-26/StopResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/StopResource.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/StopResource.md")

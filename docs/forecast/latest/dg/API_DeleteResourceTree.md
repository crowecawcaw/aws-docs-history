Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DeleteResourceTree

Deletes an entire resource tree. This operation will delete the parent resource and
its child resources.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

Child resources are resources that were created from another resource. For example,
when a forecast is generated from a predictor, the forecast is the child resource and
the predictor is the parent resource.

Amazon Forecast resources possess the following parent-child resource hierarchies:

- **Dataset**: dataset import jobs
- **Dataset Group**: predictors, predictor backtest
  export jobs, forecasts, forecast export jobs
- **Predictor**: predictor backtest export jobs,
  forecasts, forecast export jobs
- **Forecast**: forecast export jobs

###### Note

`DeleteResourceTree` will only delete Amazon Forecast resources, and will not
delete datasets or exported files stored in Amazon S3.

## Request Syntax

```
{
   "ResourceArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceArn](#API_DeleteResourceTree_RequestSyntax "#API_DeleteResourceTree_RequestSyntax")**

The Amazon Resource Name (ARN) of the parent resource to delete. All child resources
of the parent resource will also be deleted.

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

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/cli2/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForCpp/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/boto3/forecast-2018-06-26/DeleteResourceTree.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteResourceTree.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteResourceTree.md")

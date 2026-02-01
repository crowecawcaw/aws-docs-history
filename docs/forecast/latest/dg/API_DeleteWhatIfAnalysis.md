Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DeleteWhatIfAnalysis

Deletes a what-if analysis created using the [CreateWhatIfAnalysis](API_CreateWhatIfAnalysis.md "API_CreateWhatIfAnalysis.md")
operation. You can delete only what-if analyses that have a status of `ACTIVE` or `CREATE_FAILED`. To get the status, use the [DescribeWhatIfAnalysis](API_DescribeWhatIfAnalysis.md "API_DescribeWhatIfAnalysis.md") operation.

You can't delete a what-if analysis while any of its forecasts are being exported.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "WhatIfAnalysisArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[WhatIfAnalysisArn](#API_DeleteWhatIfAnalysis_RequestSyntax "#API_DeleteWhatIfAnalysis_RequestSyntax")**

The Amazon Resource Name (ARN) of the what-if analysis that you want to delete.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/cli2/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForCpp/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/boto3/forecast-2018-06-26/DeleteWhatIfAnalysis.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteWhatIfAnalysis.md")

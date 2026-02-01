Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DeleteWhatIfForecastExport

Deletes a what-if forecast export created using the [CreateWhatIfForecastExport](API_CreateWhatIfForecastExport.md "API_CreateWhatIfForecastExport.md")
operation. You can delete only what-if forecast exports that have a status of `ACTIVE` or `CREATE_FAILED`. To get the status, use the [DescribeWhatIfForecastExport](API_DescribeWhatIfForecastExport.md "API_DescribeWhatIfForecastExport.md") operation.

## Request Syntax

```
{
   "WhatIfForecastExportArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[WhatIfForecastExportArn](#API_DeleteWhatIfForecastExport_RequestSyntax "#API_DeleteWhatIfForecastExport_RequestSyntax")**

The Amazon Resource Name (ARN) of the what-if forecast export that you want to delete.

Type: String

Length Constraints: Maximum length of 300.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/cli2/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForCpp/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/boto3/forecast-2018-06-26/DeleteWhatIfForecastExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteWhatIfForecastExport.md")

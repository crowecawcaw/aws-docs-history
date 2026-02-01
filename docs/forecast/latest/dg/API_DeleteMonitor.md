Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DeleteMonitor

Deletes a monitor resource. You can only delete a monitor resource with a status of `ACTIVE`, `ACTIVE_STOPPED`, `CREATE_FAILED`, or `CREATE_STOPPED`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "MonitorArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MonitorArn](#API_DeleteMonitor_RequestSyntax "#API_DeleteMonitor_RequestSyntax")**

The Amazon Resource Name (ARN) of the monitor resource to delete.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DeleteMonitor.md "../../../goto/cli2/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteMonitor.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForCpp/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DeleteMonitor.md "../../../goto/boto3/forecast-2018-06-26/DeleteMonitor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteMonitor.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DeleteMonitor.md")



 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DeleteWhatIfForecast
<a name="API_DeleteWhatIfForecast"></a>

Deletes a what-if forecast created using the [CreateWhatIfForecast](API_CreateWhatIfForecast.md) operation. You can delete only what-if forecasts that have a status of `ACTIVE` or `CREATE_FAILED`. To get the status, use the [DescribeWhatIfForecast](API_DescribeWhatIfForecast.md) operation. 

You can't delete a what-if forecast while it is being exported. After a what-if forecast is deleted, you can no longer query the what-if analysis.

## Request Syntax
<a name="API_DeleteWhatIfForecast_RequestSyntax"></a>

```
{
   "WhatIfForecastArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWhatIfForecast_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [WhatIfForecastArn](#API_DeleteWhatIfForecast_RequestSyntax) **   <a name="forecast-DeleteWhatIfForecast-request-WhatIfForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast that you want to delete.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Elements
<a name="API_DeleteWhatIfForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWhatIfForecast_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteWhatIfForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DeleteWhatIfForecast) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DeleteWhatIfForecast) 
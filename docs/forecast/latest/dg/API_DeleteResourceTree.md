

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DeleteResourceTree
<a name="API_DeleteResourceTree"></a>

Deletes an entire resource tree. This operation will delete the parent resource and its child resources.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

Child resources are resources that were created from another resource. For example, when a forecast is generated from a predictor, the forecast is the child resource and the predictor is the parent resource.

Amazon Forecast resources possess the following parent-child resource hierarchies:
+  **Dataset**: dataset import jobs
+  **Dataset Group**: predictors, predictor backtest export jobs, forecasts, forecast export jobs
+  **Predictor**: predictor backtest export jobs, forecasts, forecast export jobs
+  **Forecast**: forecast export jobs

**Note**  
 `DeleteResourceTree` will only delete Amazon Forecast resources, and will not delete datasets or exported files stored in Amazon S3. 

## Request Syntax
<a name="API_DeleteResourceTree_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourceTree_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DeleteResourceTree_RequestSyntax) **   <a name="forecast-DeleteResourceTree-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the parent resource to delete. All child resources of the parent resource will also be deleted.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Elements
<a name="API_DeleteResourceTree_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourceTree_Errors"></a>

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
<a name="API_DeleteResourceTree_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DeleteResourceTree) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DeleteResourceTree) 
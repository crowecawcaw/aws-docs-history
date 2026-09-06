

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# UpdateDatasetGroup
<a name="API_UpdateDatasetGroup"></a>

Replaces the datasets in a dataset group with the specified datasets.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

**Note**  
The `Status` of the dataset group must be `ACTIVE` before you can use the dataset group to create a predictor. Use the [DescribeDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html) operation to get the status.

## Request Syntax
<a name="API_UpdateDatasetGroup_RequestSyntax"></a>

```
{
   "DatasetArns": [ "{{string}}" ],
   "DatasetGroupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDatasetGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetArns](#API_UpdateDatasetGroup_RequestSyntax) **   <a name="forecast-UpdateDatasetGroup-request-DatasetArns"></a>
An array of the Amazon Resource Names (ARNs) of the datasets to add to the dataset group.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

 ** [DatasetGroupArn](#API_UpdateDatasetGroup_RequestSyntax) **   <a name="forecast-UpdateDatasetGroup-request-DatasetGroupArn"></a>
The ARN of the dataset group.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Elements
<a name="API_UpdateDatasetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDatasetGroup_Errors"></a>

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
<a name="API_UpdateDatasetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/UpdateDatasetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/UpdateDatasetGroup) 
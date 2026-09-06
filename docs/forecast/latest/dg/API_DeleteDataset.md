

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DeleteDataset
<a name="API_DeleteDataset"></a>

Deletes an Amazon Forecast dataset that was created using the [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html) operation. You can only delete datasets that have a status of `ACTIVE` or `CREATE_FAILED`. To get the status use the [DescribeDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

**Note**  
Forecast does not automatically update any dataset groups that contain the deleted dataset. In order to update the dataset group, use the [UpdateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html) operation, omitting the deleted dataset's ARN.

## Request Syntax
<a name="API_DeleteDataset_RequestSyntax"></a>

```
{
   "DatasetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDataset_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetArn](#API_DeleteDataset_RequestSyntax) **   <a name="forecast-DeleteDataset-request-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset to delete.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Elements
<a name="API_DeleteDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDataset_Errors"></a>

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
<a name="API_DeleteDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DeleteDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DeleteDataset) 
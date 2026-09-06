

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DeleteDatasetImportJob
<a name="API_DeleteDatasetImportJob"></a>

Deletes a dataset import job created using the [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html) operation. You can delete only dataset import jobs that have a status of `ACTIVE` or `CREATE_FAILED`. To get the status, use the [DescribeDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_DeleteDatasetImportJob_RequestSyntax"></a>

```
{
   "DatasetImportJobArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDatasetImportJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DatasetImportJobArn](#API_DeleteDatasetImportJob_RequestSyntax) **   <a name="forecast-DeleteDatasetImportJob-request-DatasetImportJobArn"></a>
The Amazon Resource Name (ARN) of the dataset import job to delete.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Elements
<a name="API_DeleteDatasetImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDatasetImportJob_Errors"></a>

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
<a name="API_DeleteDatasetImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DeleteDatasetImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DeleteDatasetImportJob) 
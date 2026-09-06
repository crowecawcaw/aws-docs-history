

# UpdateDataset
<a name="API_UpdateDataset"></a>

Update a dataset to replace its schema with a new or existing one. For more information, see [Replacing a dataset's schema](https://docs.aws.amazon.com/personalize/latest/dg/updating-dataset-schema.html). 

## Request Syntax
<a name="API_UpdateDataset_RequestSyntax"></a>

```
{
   "datasetArn": "{{string}}",
   "schemaArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDataset_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [datasetArn](#API_UpdateDataset_RequestSyntax) **   <a name="personalize-UpdateDataset-request-datasetArn"></a>
The Amazon Resource Name (ARN) of the dataset that you want to update.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [schemaArn](#API_UpdateDataset_RequestSyntax) **   <a name="personalize-UpdateDataset-request-schemaArn"></a>
The Amazon Resource Name (ARN) of the new schema you want use.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_UpdateDataset_ResponseSyntax"></a>

```
{
   "datasetArn": "string"
}
```

## Response Elements
<a name="API_UpdateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_UpdateDataset_ResponseSyntax) **   <a name="personalize-UpdateDataset-response-datasetArn"></a>
The Amazon Resource Name (ARN) of the dataset you updated.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_UpdateDataset_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/UpdateDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/UpdateDataset) 
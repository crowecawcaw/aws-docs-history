

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# UpdateModel
<a name="API_UpdateModel"></a>

Updates a model in the account.

## Request Syntax
<a name="API_UpdateModel_RequestSyntax"></a>

```
{
   "LabelsInputConfiguration": { 
      "LabelGroupName": "{{string}}",
      "S3InputConfiguration": { 
         "Bucket": "{{string}}",
         "Prefix": "{{string}}"
      }
   },
   "ModelDiagnosticsOutputConfiguration": { 
      "KmsKeyId": "{{string}}",
      "S3OutputConfiguration": { 
         "Bucket": "{{string}}",
         "Prefix": "{{string}}"
      }
   },
   "ModelName": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateModel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [LabelsInputConfiguration](#API_UpdateModel_RequestSyntax) **   <a name="LookoutForEquipment-UpdateModel-request-LabelsInputConfiguration"></a>
Contains the configuration information for the S3 location being used to hold label data.   
Type: [LabelsInputConfiguration](API_LabelsInputConfiguration.md) object  
Required: No

 ** [ModelDiagnosticsOutputConfiguration](#API_UpdateModel_RequestSyntax) **   <a name="LookoutForEquipment-UpdateModel-request-ModelDiagnosticsOutputConfiguration"></a>
The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics for the model. You must also specify the `RoleArn` request parameter.  
Type: [ModelDiagnosticsOutputConfiguration](API_ModelDiagnosticsOutputConfiguration.md) object  
Required: No

 ** [ModelName](#API_UpdateModel_RequestSyntax) **   <a name="LookoutForEquipment-UpdateModel-request-ModelName"></a>
The name of the model to update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [RoleArn](#API_UpdateModel_RequestSyntax) **   <a name="LookoutForEquipment-UpdateModel-request-RoleArn"></a>
The ARN of the model to update.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

## Response Elements
<a name="API_UpdateModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateModel_Errors"></a>

 ** AccessDeniedException **   
The request could not be completed because you do not have access to the resource.   
HTTP Status Code: 400

 ** ConflictException **   
 The request could not be completed due to a conflict with the current state of the target resource.   
HTTP Status Code: 400

 ** InternalServerException **   
 Processing of the request has failed because of an unknown error, exception or failure.   
HTTP Status Code: 500

 ** ResourceNotFoundException **   
 The resource requested could not be found. Verify the resource ID and retry your request.   
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling.  
HTTP Status Code: 400

 ** ValidationException **   
 The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS service that's being utilized.   
HTTP Status Code: 400

## See Also
<a name="API_UpdateModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/UpdateModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateModel) 
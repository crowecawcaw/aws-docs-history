

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# StopRetrainingScheduler
<a name="API_StopRetrainingScheduler"></a>

Stops a retraining scheduler. 

## Request Syntax
<a name="API_StopRetrainingScheduler_RequestSyntax"></a>

```
{
   "ModelName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopRetrainingScheduler_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ModelName](#API_StopRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-StopRetrainingScheduler-request-ModelName"></a>
The name of the model whose retraining scheduler you want to stop.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

## Response Syntax
<a name="API_StopRetrainingScheduler_ResponseSyntax"></a>

```
{
   "ModelArn": "string",
   "ModelName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_StopRetrainingScheduler_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelArn](#API_StopRetrainingScheduler_ResponseSyntax) **   <a name="LookoutForEquipment-StopRetrainingScheduler-response-ModelArn"></a>
The ARN of the model whose retraining scheduler is being stopped.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+` 

 ** [ModelName](#API_StopRetrainingScheduler_ResponseSyntax) **   <a name="LookoutForEquipment-StopRetrainingScheduler-response-ModelName"></a>
The name of the model whose retraining scheduler is being stopped.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$` 

 ** [Status](#API_StopRetrainingScheduler_ResponseSyntax) **   <a name="LookoutForEquipment-StopRetrainingScheduler-response-Status"></a>
The status of the retraining scheduler.   
Type: String  
Valid Values: `PENDING | RUNNING | STOPPING | STOPPED` 

## Errors
<a name="API_StopRetrainingScheduler_Errors"></a>

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
<a name="API_StopRetrainingScheduler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/StopRetrainingScheduler) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/StopRetrainingScheduler) 


 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# UpdateRetrainingScheduler
<a name="API_UpdateRetrainingScheduler"></a>

Updates a retraining scheduler. 

## Request Syntax
<a name="API_UpdateRetrainingScheduler_RequestSyntax"></a>

```
{
   "LookbackWindow": "{{string}}",
   "ModelName": "{{string}}",
   "PromoteMode": "{{string}}",
   "RetrainingFrequency": "{{string}}",
   "RetrainingStartDate": {{number}}
}
```

## Request Parameters
<a name="API_UpdateRetrainingScheduler_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [LookbackWindow](#API_UpdateRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-UpdateRetrainingScheduler-request-LookbackWindow"></a>
The number of past days of data that will be used for retraining.  
Type: String  
Pattern: `^P180D$|^P360D$|^P540D$|^P720D$`   
Required: No

 ** [ModelName](#API_UpdateRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-UpdateRetrainingScheduler-request-ModelName"></a>
The name of the model whose retraining scheduler you want to update.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [PromoteMode](#API_UpdateRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-UpdateRetrainingScheduler-request-PromoteMode"></a>
Indicates how the service will use new models. In `MANAGED` mode, new models will automatically be used for inference if they have better performance than the current model. In `MANUAL` mode, the new models will not be used [until they are manually activated](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation).  
Type: String  
Valid Values: `MANAGED | MANUAL`   
Required: No

 ** [RetrainingFrequency](#API_UpdateRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-UpdateRetrainingScheduler-request-RetrainingFrequency"></a>
This parameter uses the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:  
+ P3M15D – Every 3 months and 15 days
+ P2M – Every 2 months
+ P150D – Every 150 days
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `^P(\dY)?(\d{1,2}M)?(\d{1,3}D)?$`   
Required: No

 ** [RetrainingStartDate](#API_UpdateRetrainingScheduler_RequestSyntax) **   <a name="LookoutForEquipment-UpdateRetrainingScheduler-request-RetrainingStartDate"></a>
The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.  
Type: Timestamp  
Required: No

## Response Elements
<a name="API_UpdateRetrainingScheduler_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRetrainingScheduler_Errors"></a>

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
<a name="API_UpdateRetrainingScheduler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler) 
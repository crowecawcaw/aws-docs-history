

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# CreateLabel
<a name="API_CreateLabel"></a>

 Creates a label for an event. 

## Request Syntax
<a name="API_CreateLabel_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "EndTime": {{number}},
   "Equipment": "{{string}}",
   "FaultCode": "{{string}}",
   "LabelGroupName": "{{string}}",
   "Notes": "{{string}}",
   "Rating": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_CreateLabel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-ClientToken"></a>
 A unique identifier for the request to create a label. If you do not set the client request token, Lookout for Equipment generates one.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `\p{ASCII}{1,256}`   
Required: Yes

 ** [EndTime](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-EndTime"></a>
 The end time of the labeled event.   
Type: Timestamp  
Required: Yes

 ** [Equipment](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-Equipment"></a>
 Indicates that a label pertains to a particular piece of equipment.   
Data in this field will be retained for service usage. Follow best practices for the security of your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[\P{M}\p{M}]{1,200}`   
Required: No

 ** [FaultCode](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-FaultCode"></a>
 Provides additional information about the label. The fault code must be defined in the FaultCodes attribute of the label group.  
Data in this field will be retained for service usage. Follow best practices for the security of your data.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[\P{M}\p{M}]{1,100}`   
Required: No

 ** [LabelGroupName](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-LabelGroupName"></a>
 The name of a group of labels.   
Data in this field will be retained for service usage. Follow best practices for the security of your data.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [Notes](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-Notes"></a>
 Metadata providing additional information about the label.   
Data in this field will be retained for service usage. Follow best practices for the security of your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2560.  
Pattern: `[\P{M}\p{M}]{1,2560}`   
Required: No

 ** [Rating](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-Rating"></a>
 Indicates whether a labeled event represents an anomaly.   
Type: String  
Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL`   
Required: Yes

 ** [StartTime](#API_CreateLabel_RequestSyntax) **   <a name="LookoutForEquipment-CreateLabel-request-StartTime"></a>
 The start time of the labeled event.   
Type: Timestamp  
Required: Yes

## Response Syntax
<a name="API_CreateLabel_ResponseSyntax"></a>

```
{
   "LabelId": "string"
}
```

## Response Elements
<a name="API_CreateLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LabelId](#API_CreateLabel_ResponseSyntax) **   <a name="LookoutForEquipment-CreateLabel-response-LabelId"></a>
 The ID of the label that you have created.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}` 

## Errors
<a name="API_CreateLabel_Errors"></a>

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

 ** ServiceQuotaExceededException **   
 Resource limitations have been exceeded.   
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling.  
HTTP Status Code: 400

 ** ValidationException **   
 The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS service that's being utilized.   
HTTP Status Code: 400

## See Also
<a name="API_CreateLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/CreateLabel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateLabel) 
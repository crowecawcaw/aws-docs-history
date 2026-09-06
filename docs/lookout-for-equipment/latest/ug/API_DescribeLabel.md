

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DescribeLabel
<a name="API_DescribeLabel"></a>

 Returns the name of the label. 

## Request Syntax
<a name="API_DescribeLabel_RequestSyntax"></a>

```
{
   "LabelGroupName": "{{string}}",
   "LabelId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLabel_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [LabelGroupName](#API_DescribeLabel_RequestSyntax) **   <a name="LookoutForEquipment-DescribeLabel-request-LabelGroupName"></a>
 Returns the name of the group containing the label.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: Yes

 ** [LabelId](#API_DescribeLabel_RequestSyntax) **   <a name="LookoutForEquipment-DescribeLabel-request-LabelId"></a>
 Returns the ID of the label.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}`   
Required: Yes

## Response Syntax
<a name="API_DescribeLabel_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "EndTime": number,
   "Equipment": "string",
   "FaultCode": "string",
   "LabelGroupArn": "string",
   "LabelGroupName": "string",
   "LabelId": "string",
   "Notes": "string",
   "Rating": "string",
   "StartTime": number
}
```

## Response Elements
<a name="API_DescribeLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-CreatedAt"></a>
 The time at which the label was created.   
Type: Timestamp

 ** [EndTime](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-EndTime"></a>
 The end time of the requested label.   
Type: Timestamp

 ** [Equipment](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-Equipment"></a>
 Indicates that a label pertains to a particular piece of equipment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[\P{M}\p{M}]{1,200}` 

 ** [FaultCode](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-FaultCode"></a>
 Indicates the type of anomaly associated with the label.   
Data in this field will be retained for service usage. Follow best practices for the security of your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[\P{M}\p{M}]{1,100}` 

 ** [LabelGroupArn](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-LabelGroupArn"></a>
 The Amazon Resource Name (ARN) of the requested label group.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+` 

 ** [LabelGroupName](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-LabelGroupName"></a>
 The name of the requested label group.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$` 

 ** [LabelId](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-LabelId"></a>
 The ID of the requested label.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}` 

 ** [Notes](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-Notes"></a>
Metadata providing additional information about the label.  
Data in this field will be retained for service usage. Follow best practices for the security of your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2560.  
Pattern: `[\P{M}\p{M}]{1,2560}` 

 ** [Rating](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-Rating"></a>
 Indicates whether a labeled event represents an anomaly.   
Type: String  
Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL` 

 ** [StartTime](#API_DescribeLabel_ResponseSyntax) **   <a name="LookoutForEquipment-DescribeLabel-response-StartTime"></a>
 The start time of the requested label.   
Type: Timestamp

## Errors
<a name="API_DescribeLabel_Errors"></a>

 ** AccessDeniedException **   
The request could not be completed because you do not have access to the resource.   
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
<a name="API_DescribeLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/DescribeLabel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeLabel) 
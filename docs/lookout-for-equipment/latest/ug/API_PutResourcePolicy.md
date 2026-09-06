

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Creates a resource control policy for a given resource.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "PolicyRevisionId": "{{string}}",
   "ResourceArn": "{{string}}",
   "ResourcePolicy": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_PutResourcePolicy_RequestSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-request-ClientToken"></a>
A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `\p{ASCII}{1,256}`   
Required: Yes

 ** [PolicyRevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-request-PolicyRevisionId"></a>
A unique identifier for a revision of the resource policy.  
Type: String  
Length Constraints: Maximum length of 50.  
Pattern: `[0-9A-Fa-f]+`   
Required: No

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which the policy is being created.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:.+`   
Required: Yes

 ** [ResourcePolicy](#API_PutResourcePolicy_RequestSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-request-ResourcePolicy"></a>
The JSON-formatted resource policy to create.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`   
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "PolicyRevisionId": "string",
   "ResourceArn": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyRevisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-response-PolicyRevisionId"></a>
A unique identifier for a revision of the resource policy.  
Type: String  
Length Constraints: Maximum length of 50.  
Pattern: `[0-9A-Fa-f]+` 

 ** [ResourceArn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="LookoutForEquipment-PutResourcePolicy-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which the policy was created.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:.+` 

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

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
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lookoutequipment-2020-12-15/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/PutResourcePolicy) 
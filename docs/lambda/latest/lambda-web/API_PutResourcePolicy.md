

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Adds or updates a resource-based policy on a web function. A resource-based policy grants permissions to other AWS accounts or services to perform actions on the web function.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /2025-03-07/resource-policy/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}",
   "RevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambdaweb-PutResourcePolicy-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `arn:[^:]+:lambda:[^:]+:\d{12}:web-function/[^/]+`   
Required: Yes

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambdaweb-PutResourcePolicy-request-Policy"></a>
The JSON-formatted resource-based policy to attach to the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20480.  
Required: Yes

 ** [RevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="lambdaweb-PutResourcePolicy-request-RevisionId"></a>
The revision ID of the existing policy. Use this to prevent conflicts when updating a policy concurrently. If you don't specify a value, the update proceeds without checking the current revision.  
Type: String  
Pattern: `[0-9a-f-]{36}`   
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "RevisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="lambdaweb-PutResourcePolicy-response-Policy"></a>
The JSON-formatted resource-based policy attached to the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20480.

 ** [RevisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="lambdaweb-PutResourcePolicy-response-RevisionId"></a>
The revision ID of the policy. Use this value in subsequent `PutResourcePolicy` or `DeleteResourcePolicy` requests to prevent conflicts.  
Type: String  
Pattern: `[0-9a-f-]{36}` 

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.    
 ** message **   
A message describing the access denied error.
HTTP Status Code: 403

 ** ConflictException **   
The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.    
 ** message **   
A message describing the conflict.  
 ** resourceId **   
The identifier of the resource in conflict.  
 ** resourceType **   
The type of the resource in conflict.
HTTP Status Code: 409

 ** InternalServerException **   
The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.    
 ** message **   
A message describing the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.    
 ** message **   
A message describing the resource not found error.  
 ** resourceId **   
The identifier of the resource that was not found.  
 ** resourceType **   
The type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.    
 ** message **   
A message describing the quota that was exceeded.  
 ** quotaCode **   
The quota code of the exceeded quota.  
 ** resourceId **   
The identifier of the resource that exceeded the quota.  
 ** resourceType **   
The type of resource that exceeded the quota.  
 ** serviceCode **   
The service code of the service that owns the quota.
HTTP Status Code: 402

 ** ThrottlingException **   
The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.    
 ** message **   
A message describing the throttling error.  
 ** quotaCode **   
The quota code that was exceeded, if applicable.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.  
 ** serviceCode **   
The service code of the throttled service.
HTTP Status Code: 429

 ** ValidationException **   
The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.    
 ** message **   
A message describing the validation error.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/PutResourcePolicy) 
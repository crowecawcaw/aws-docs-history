

# DeleteWebFunction
<a name="API_DeleteWebFunction"></a>

Deletes a web function and all of its associated revisions and endpoints.

To use this operation, you must have the `DeleteWebFunction` permission on the web function. You don't need the `DeleteWebFunctionRevision` or `DeleteWebFunctionEndpoint` permission.

## Request Syntax
<a name="API_DeleteWebFunction_RequestSyntax"></a>

```
DELETE /2025-03-07/web-functions/{{functionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWebFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [functionName](#API_DeleteWebFunction_RequestSyntax) **   <a name="lambdaweb-DeleteWebFunction-request-uri-functionName"></a>
The web function to delete.  
You can specify either of the following:  
+ The function name, for example `my-function`.
+ The function ARN.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_DeleteWebFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWebFunction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteWebFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteWebFunction_Errors"></a>

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
<a name="API_DeleteWebFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/DeleteWebFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/DeleteWebFunction) 
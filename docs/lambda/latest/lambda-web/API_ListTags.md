

# ListTags
<a name="API_ListTags"></a>

Returns a list of tags applied to a web function.

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
GET /2025-03-07/tags/{{resource}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTags_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resource](#API_ListTags_RequestSyntax) **   <a name="lambdaweb-ListTags-request-uri-resource"></a>
The Amazon Resource Name (ARN) of the web function.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `arn:[^:]+:lambda:[^:]+:\d{12}:web-function/[^/]+`   
Required: Yes

## Request Body
<a name="API_ListTags_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTags_ResponseSyntax) **   <a name="lambdaweb-ListTags-response-Tags"></a>
A map of tag keys and values associated with the web function.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9 _\.:/=+\-@]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9 _\.:/=+\-@]*` 

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.    
 ** message **   
A message describing the access denied error.
HTTP Status Code: 403

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
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/ListTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ListTags) 
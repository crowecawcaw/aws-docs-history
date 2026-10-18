

# ListWebFunctions
<a name="API_ListWebFunctions"></a>

Lists web functions in your account. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListWebFunctions_RequestSyntax"></a>

```
POST /2025-03-07/web-functions HTTP/1.1
Content-type: application/json

{
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWebFunctions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWebFunctions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListWebFunctions_RequestSyntax) **   <a name="lambdaweb-ListWebFunctions-request-filters"></a>
A list of filters to apply to the results. The only supported filter name is `state`. If you don't specify a filter, the operation returns all web functions.  
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [maxResults](#API_ListWebFunctions_RequestSyntax) **   <a name="lambdaweb-ListWebFunctions-request-maxResults"></a>
The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [nextToken](#API_ListWebFunctions_RequestSyntax) **   <a name="lambdaweb-ListWebFunctions-request-nextToken"></a>
The pagination token that's returned by a previous request to retrieve the next page of results.  
Type: String  
Pattern: `[a-f0-9-]{36}`   
Required: No

## Response Syntax
<a name="API_ListWebFunctions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "functions": [ 
      { 
         "createdAt": "string",
         "functionArn": "string",
         "functionName": "string",
         "state": "string",
         "stateReason": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWebFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [functions](#API_ListWebFunctions_ResponseSyntax) **   <a name="lambdaweb-ListWebFunctions-response-functions"></a>
A list of web function summaries.  
Type: Array of [FunctionSummary](API_FunctionSummary.md) objects

 ** [nextToken](#API_ListWebFunctions_ResponseSyntax) **   <a name="lambdaweb-ListWebFunctions-response-nextToken"></a>
The pagination token that's included if more results are available. Use this value as the `nextToken` request parameter in a subsequent call to retrieve the next page of results.  
Type: String  
Pattern: `[a-f0-9-]{36}` 

## Errors
<a name="API_ListWebFunctions_Errors"></a>

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
<a name="API_ListWebFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/ListWebFunctions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ListWebFunctions) 
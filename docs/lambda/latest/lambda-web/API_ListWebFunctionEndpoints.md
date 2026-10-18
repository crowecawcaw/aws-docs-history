

# ListWebFunctionEndpoints
<a name="API_ListWebFunctionEndpoints"></a>

Lists endpoints for a web function. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListWebFunctionEndpoints_RequestSyntax"></a>

```
POST /2025-03-07/web-functions/{{functionName}}/list-endpoints HTTP/1.1
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
<a name="API_ListWebFunctionEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [functionName](#API_ListWebFunctionEndpoints_RequestSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-request-uri-functionName"></a>
The web function.  
You can specify either of the following:  
+ The function name, for example `my-function`.
+ The function ARN.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_ListWebFunctionEndpoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListWebFunctionEndpoints_RequestSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-request-filters"></a>
A list of filters to apply to the results. Supported filter names: `authType`, `autoDeploymentMode`, `endpointType`, `state`, and `updateStatus`. If you don't specify a filter, the operation returns all endpoints for the web function.  
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [maxResults](#API_ListWebFunctionEndpoints_RequestSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-request-maxResults"></a>
The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [nextToken](#API_ListWebFunctionEndpoints_RequestSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-request-nextToken"></a>
The pagination token that's returned by a previous request to retrieve the next page of results.  
Type: String  
Pattern: `[a-f0-9-]{36}`   
Required: No

## Response Syntax
<a name="API_ListWebFunctionEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoints": [ 
      { 
         "authType": "string",
         "autoDeploymentMode": "string",
         "createdAt": "string",
         "description": "string",
         "domainName": "string",
         "endpointArn": "string",
         "endpointName": "string",
         "endpointType": "string",
         "regions": [ "string" ],
         "revisionWeights": [ 
            { 
               "revisionId": "string",
               "weight": number
            }
         ],
         "scalingConfig": { 
            "maxEnvironments": number
         },
         "state": "string",
         "stateReason": "string",
         "throttleConfig": { 
            "rateLimit": number
         },
         "updatedAt": "string",
         "updateStatus": "string",
         "updateStatusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWebFunctionEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoints](#API_ListWebFunctionEndpoints_ResponseSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-response-endpoints"></a>
A list of endpoint summaries for the web function.  
Type: Array of [FunctionEndpointSummary](API_FunctionEndpointSummary.md) objects

 ** [nextToken](#API_ListWebFunctionEndpoints_ResponseSyntax) **   <a name="lambdaweb-ListWebFunctionEndpoints-response-nextToken"></a>
The pagination token that's included if more results are available. Use this value as the `nextToken` request parameter in a subsequent call to retrieve the next page of results.  
Type: String  
Pattern: `[a-f0-9-]{36}` 

## Errors
<a name="API_ListWebFunctionEndpoints_Errors"></a>

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
<a name="API_ListWebFunctionEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/ListWebFunctionEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ListWebFunctionEndpoints) 


# CreateWebFunction
<a name="API_CreateWebFunction"></a>

Creates a web function with an initial revision and endpoint. To create a web function, you provide the function name, revision configuration (code and service settings), and endpoint configuration.

To use this operation, you must have the `CreateWebFunction` permission on the web function. You don't need separate permissions for the initial revision or endpoint.

## Request Syntax
<a name="API_CreateWebFunction_RequestSyntax"></a>

```
PUT /2025-03-07/web-functions HTTP/1.1
Content-type: application/json

{
   "endpointConfig": { 
      "authType": "{{string}}",
      "autoDeploymentMode": "{{string}}",
      "description": "{{string}}",
      "endpointName": "{{string}}",
      "endpointType": "{{string}}",
      "regions": [ "{{string}}" ],
      "scalingConfig": { 
         "maxEnvironments": {{number}}
      },
      "throttleConfig": { 
         "rateLimit": {{number}}
      }
   },
   "functionName": "{{string}}",
   "revisionConfig": { 
      "buildConfig": { 
         "codeConfig": { 
            "s3Object": { 
               "bucket": "{{string}}",
               "key": "{{string}}",
               "versionId": "{{string}}"
            }
         },
         "runtimeConfig": { 
            "runtime": "{{string}}"
         }
      },
      "description": "{{string}}",
      "kmsKeyArn": "{{string}}",
      "serviceConfig": { 
         "egressNetworkConnectorArn": "{{string}}",
         "environmentVariables": { 
            "{{string}}" : "{{string}}" 
         },
         "executionRoleArn": "{{string}}",
         "maxConcurrencyPerEnvironment": {{number}},
         "telemetryConfig": { 
            "loggingConfig": { 
               "applicationLogLevel": "{{string}}",
               "logGroup": "{{string}}",
               "systemLogLevel": "{{string}}"
            }
         },
         "timeoutSeconds": {{number}}
      }
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateWebFunction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWebFunction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endpointConfig](#API_CreateWebFunction_RequestSyntax) **   <a name="lambdaweb-CreateWebFunction-request-endpointConfig"></a>
The configuration for the initial endpoint of the web function.  
Type: [EndpointConfig](API_EndpointConfig.md) object  
Required: No

 ** [functionName](#API_CreateWebFunction_RequestSyntax) **   <a name="lambdaweb-CreateWebFunction-request-functionName"></a>
The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (\_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [revisionConfig](#API_CreateWebFunction_RequestSyntax) **   <a name="lambdaweb-CreateWebFunction-request-revisionConfig"></a>
The configuration for the initial revision of the web function, including code and service settings.  
Type: [RevisionConfig](API_RevisionConfig.md) object  
Required: No

 ** [tags](#API_CreateWebFunction_RequestSyntax) **   <a name="lambdaweb-CreateWebFunction-request-tags"></a>
A map of tag keys and values to apply to the web function.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9 _\.:/=+\-@]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9 _\.:/=+\-@]*`   
Required: No

## Response Syntax
<a name="API_CreateWebFunction_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "endpoint": { 
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
   },
   "functionArn": "string",
   "functionName": "string",
   "revision": { 
      "createdAt": "string",
      "description": "string",
      "revisionArn": "string",
      "revisionId": "string",
      "state": "string",
      "stateReason": "string"
   },
   "state": "string",
   "stateReason": "string",
   "tags": { 
      "string" : "string" 
   },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_CreateWebFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-createdAt"></a>
The date and time the web function was created.  
Type: Timestamp

 ** [endpoint](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-endpoint"></a>
A summary of the initial endpoint created with the web function.  
Type: [FunctionEndpointSummary](API_FunctionEndpointSummary.md) object

 ** [functionArn](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-functionArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [functionName](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-functionName"></a>
The name of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [revision](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-revision"></a>
A summary of the initial revision created with the web function.  
Type: [FunctionRevisionSummary](API_FunctionRevisionSummary.md) object

 ** [state](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-state"></a>
The current state of the web function.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting` 

 ** [stateReason](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-stateReason"></a>
The reason for the current state of the web function.  
Type: String

 ** [tags](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-tags"></a>
A map of tag keys and values associated with the web function.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9 _\.:/=+\-@]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9 _\.:/=+\-@]*` 

 ** [updatedAt](#API_CreateWebFunction_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunction-response-updatedAt"></a>
The date and time the web function was last updated.  
Type: Timestamp

## Errors
<a name="API_CreateWebFunction_Errors"></a>

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
<a name="API_CreateWebFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/CreateWebFunction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/CreateWebFunction) 
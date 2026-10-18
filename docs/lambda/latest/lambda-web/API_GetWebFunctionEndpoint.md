

# GetWebFunctionEndpoint
<a name="API_GetWebFunctionEndpoint"></a>

Retrieves details about a web function endpoint, including its current state, configuration, and domain name.

## Request Syntax
<a name="API_GetWebFunctionEndpoint_RequestSyntax"></a>

```
GET /2025-03-07/web-functions/{{functionName}}/endpoints/{{endpointName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWebFunctionEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointName](#API_GetWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-request-uri-endpointName"></a>
The endpoint to retrieve.  
You can specify either of the following:  
+ The endpoint name, for example `my-endpoint`.
+ The endpoint ARN.
The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [functionName](#API_GetWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-request-uri-functionName"></a>
The web function.  
You can specify either of the following:  
+ The function name, for example `my-function`.
+ The function ARN.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_GetWebFunctionEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWebFunctionEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authType": "string",
   "autoDeploymentMode": "string",
   "createdAt": "string",
   "description": "string",
   "domainName": "string",
   "endpointArn": "string",
   "endpointName": "string",
   "endpointType": "string",
   "functionArn": "string",
   "regionalEndpoints": { 
      "string" : { 
         "authType": "string",
         "domainName": "string",
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
         "updateStatus": "string",
         "updateStatusReason": "string"
      }
   },
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
```

## Response Elements
<a name="API_GetWebFunctionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authType](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-authType"></a>
The authorization type for a web function endpoint.  
Valid values:  
+  `ApplicationManaged` – Your application handles authorization.
+  `IamAuth` – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).
Type: String  
Valid Values: `ApplicationManaged | IamAuth` 

 ** [autoDeploymentMode](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-autoDeploymentMode"></a>
The auto-deployment mode for a web function endpoint.  
Valid values:  
+  `LatestRevision` – The endpoint automatically serves the newest revision.
+  `Disabled` – Revision routing stays fixed until you change it.
Type: String  
Valid Values: `LatestRevision | Disabled` 

 ** [createdAt](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-createdAt"></a>
The date and time the endpoint was created.  
Type: Timestamp

 ** [description](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-description"></a>
The description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [domainName](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-domainName"></a>
The domain name assigned to the endpoint.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 256.  
Pattern: `([a-z0-9-]+\.)+[a-z]+` 

 ** [endpointArn](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [endpointName](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-endpointName"></a>
The name of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [endpointType](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-endpointType"></a>
The type of a web function endpoint.  
Valid values:  
+  `HomeRegion` – Serves traffic from the Region where you created the web function.
+  `MultiRegion` – Replicates across the Regions that you choose and routes each request to the nearest one.
+  `PerRegion` – Creates a separate endpoint in each Region that you choose.
Type: String  
Valid Values: `HomeRegion | MultiRegion | PerRegion` 

 ** [functionArn](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-functionArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [regionalEndpoints](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-regionalEndpoints"></a>
The list of regional endpoint configurations.  
Type: String to [RegionalEndpoint](API_RegionalEndpoint.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Key Pattern: `([a-z]{2,}-){2,}[0-9]` 

 ** [regions](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-regions"></a>
The Regions configured for the endpoint.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([a-z]{2,}-){2,}[0-9]` 

 ** [revisionWeights](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-revisionWeights"></a>
The traffic distribution across revisions for the endpoint. Each entry maps a revision to a weight from 1 to 100.  
Type: Array of [RevisionWeight](API_RevisionWeight.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [scalingConfig](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-scalingConfig"></a>
The scaling configuration for a web function endpoint.  
Type: [ScalingConfig](API_ScalingConfig.md) object

 ** [state](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-state"></a>
The current state of the endpoint.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting` 

 ** [stateReason](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-stateReason"></a>
The reason for the current state of the endpoint.  
Type: String

 ** [throttleConfig](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-throttleConfig"></a>
The throttling configuration for a web function endpoint.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object

 ** [updatedAt](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-updatedAt"></a>
The date and time the endpoint was last updated.  
Type: Timestamp

 ** [updateStatus](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-updateStatus"></a>
The status of the most recent update to an endpoint. Possible values:  
+  `InProgress` – The update is in progress.
+  `Successful` – The update completed successfully.
+  `Failed` – The update failed.
Type: String  
Valid Values: `InProgress | Successful | Failed` 

 ** [updateStatusReason](#API_GetWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-GetWebFunctionEndpoint-response-updateStatusReason"></a>
The reason for the endpoint's most recent update status.  
Type: String

## Errors
<a name="API_GetWebFunctionEndpoint_Errors"></a>

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
<a name="API_GetWebFunctionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/GetWebFunctionEndpoint) 
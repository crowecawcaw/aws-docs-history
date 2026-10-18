

# CreateWebFunctionEndpoint
<a name="API_CreateWebFunctionEndpoint"></a>

Creates an endpoint for a web function. An endpoint exposes the web function over HTTPS and routes traffic to one or more revisions.

To use this operation, you must have the `CreateWebFunctionEndpoint` permission on the web function, not on the endpoint being created.

## Request Syntax
<a name="API_CreateWebFunctionEndpoint_RequestSyntax"></a>

```
PUT /2025-03-07/web-functions/{{functionName}}/endpoints HTTP/1.1
Content-type: application/json

{
   "authType": "{{string}}",
   "autoDeploymentMode": "{{string}}",
   "description": "{{string}}",
   "endpointName": "{{string}}",
   "endpointType": "{{string}}",
   "regions": [ "{{string}}" ],
   "revisionWeights": [ 
      { 
         "revisionId": "{{string}}",
         "weight": {{number}}
      }
   ],
   "scalingConfig": { 
      "maxEnvironments": {{number}}
   },
   "throttleConfig": { 
      "rateLimit": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateWebFunctionEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [functionName](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-uri-functionName"></a>
The web function to create the endpoint for.  
You can specify either of the following:  
+ The function name, for example `my-function`.
+ The function ARN.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_CreateWebFunctionEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authType](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-authType"></a>
The authorization type for the endpoint.  
Valid values:  
+  `ApplicationManaged` – Your application handles authorization.
+  `IamAuth` – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).
Type: String  
Valid Values: `ApplicationManaged | IamAuth`   
Required: Yes

 ** [autoDeploymentMode](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-autoDeploymentMode"></a>
The auto-deployment mode for the endpoint. Controls whether the endpoint automatically serves the newest revision. If you don't specify a value, the default is `Disabled`, and this default is returned in the response.  
Valid values:  
+  `LatestRevision` – The endpoint automatically serves the newest revision.
+  `Disabled` – Revision routing stays fixed until you change it.
Type: String  
Valid Values: `LatestRevision | Disabled`   
Required: No

 ** [description](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-description"></a>
A description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** [endpointName](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-endpointName"></a>
The name of the endpoint to create. The name can contain letters, numbers, hyphens (-), and underscores (\_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [endpointType](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-endpointType"></a>
The type of endpoint to create. Determines how traffic is served and routed across Regions.  
Valid values:  
+  `HomeRegion` – Serves traffic from the Region where you created the web function.
+  `MultiRegion` – Replicates across the Regions that you choose and routes each request to the nearest one.
+  `PerRegion` – Creates a separate endpoint in each Region that you choose.
Type: String  
Valid Values: `HomeRegion | MultiRegion | PerRegion`   
Required: Yes

 ** [regions](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-regions"></a>
The list of Regions for the endpoint. Required when the endpoint type is `MultiRegion` or `PerRegion`: specify at least one Region other than the Region where you create the endpoint (the home Region). The home Region is added automatically if you don't include it; specifying only the home Region isn't allowed. When the endpoint type is `HomeRegion`, omit this field or specify only the home Region.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([a-z]{2,}-){2,}[0-9]`   
Required: No

 ** [revisionWeights](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-revisionWeights"></a>
A list of revision weights that determine how traffic is distributed across revisions. You can specify up to two revisions for canary or blue-green deployments.  
Type: Array of [RevisionWeight](API_RevisionWeight.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: No

 ** [scalingConfig](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-scalingConfig"></a>
The scaling configuration for the endpoint. There is no default value. If you don't specify a scaling configuration, it is absent from the response.  
Type: [ScalingConfig](API_ScalingConfig.md) object  
Required: No

 ** [throttleConfig](#API_CreateWebFunctionEndpoint_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-request-throttleConfig"></a>
The throttling configuration for the endpoint. There is no default value. If you don't specify a throttling configuration, it is absent from the response.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateWebFunctionEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_CreateWebFunctionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authType](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-authType"></a>
The authorization type for a web function endpoint.  
Valid values:  
+  `ApplicationManaged` – Your application handles authorization.
+  `IamAuth` – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).
Type: String  
Valid Values: `ApplicationManaged | IamAuth` 

 ** [autoDeploymentMode](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-autoDeploymentMode"></a>
The auto-deployment mode for a web function endpoint.  
Valid values:  
+  `LatestRevision` – The endpoint automatically serves the newest revision.
+  `Disabled` – Revision routing stays fixed until you change it.
Type: String  
Valid Values: `LatestRevision | Disabled` 

 ** [createdAt](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-createdAt"></a>
The date and time the endpoint was created.  
Type: Timestamp

 ** [description](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-description"></a>
The description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [domainName](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-domainName"></a>
The domain name assigned to the endpoint.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 256.  
Pattern: `([a-z0-9-]+\.)+[a-z]+` 

 ** [endpointArn](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [endpointName](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-endpointName"></a>
The name of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [endpointType](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-endpointType"></a>
The type of a web function endpoint.  
Valid values:  
+  `HomeRegion` – Serves traffic from the Region where you created the web function.
+  `MultiRegion` – Replicates across the Regions that you choose and routes each request to the nearest one.
+  `PerRegion` – Creates a separate endpoint in each Region that you choose.
Type: String  
Valid Values: `HomeRegion | MultiRegion | PerRegion` 

 ** [functionArn](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-functionArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [regionalEndpoints](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-regionalEndpoints"></a>
The list of regional endpoint configurations.  
Type: String to [RegionalEndpoint](API_RegionalEndpoint.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 50.  
Key Pattern: `([a-z]{2,}-){2,}[0-9]` 

 ** [regions](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-regions"></a>
The Regions configured for the endpoint.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([a-z]{2,}-){2,}[0-9]` 

 ** [revisionWeights](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-revisionWeights"></a>
The traffic distribution across revisions for the endpoint. Each entry maps a revision to a weight from 1 to 100.  
Type: Array of [RevisionWeight](API_RevisionWeight.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [scalingConfig](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-scalingConfig"></a>
The scaling configuration for a web function endpoint.  
Type: [ScalingConfig](API_ScalingConfig.md) object

 ** [state](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-state"></a>
The current state of the endpoint.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting` 

 ** [stateReason](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-stateReason"></a>
The reason for the current state of the endpoint.  
Type: String

 ** [throttleConfig](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-throttleConfig"></a>
The throttling configuration for a web function endpoint.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object

 ** [updatedAt](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-updatedAt"></a>
The date and time the endpoint was last updated.  
Type: Timestamp

 ** [updateStatus](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-updateStatus"></a>
The status of the most recent update to an endpoint. Possible values:  
+  `InProgress` – The update is in progress.
+  `Successful` – The update completed successfully.
+  `Failed` – The update failed.
Type: String  
Valid Values: `InProgress | Successful | Failed` 

 ** [updateStatusReason](#API_CreateWebFunctionEndpoint_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionEndpoint-response-updateStatusReason"></a>
The reason for the endpoint's most recent update status.  
Type: String

## Errors
<a name="API_CreateWebFunctionEndpoint_Errors"></a>

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
<a name="API_CreateWebFunctionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/CreateWebFunctionEndpoint) 
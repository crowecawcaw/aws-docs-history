

# CreateWebFunctionRevision
<a name="API_CreateWebFunctionRevision"></a>

Creates an immutable revision for a web function. A revision represents a specific version of the function code and configuration.

To use this operation, you must have the `CreateWebFunctionRevision` permission on the web function, not on the revision being created.

## Request Syntax
<a name="API_CreateWebFunctionRevision_RequestSyntax"></a>

```
POST /2025-03-07/web-functions/{{functionName}}/revisions HTTP/1.1
Content-type: application/json

{
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
}
```

## URI Request Parameters
<a name="API_CreateWebFunctionRevision_RequestParameters"></a>

The request uses the following URI parameters.

 ** [functionName](#API_CreateWebFunctionRevision_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-request-uri-functionName"></a>
The web function.  
You can specify either of the following:  
+ The function name, for example `my-function`.
+ The function ARN.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_CreateWebFunctionRevision_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [buildConfig](#API_CreateWebFunctionRevision_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-request-buildConfig"></a>
The build configuration for the revision, including code location and runtime settings.  
Type: [BuildConfig](API_BuildConfig.md) object  
Required: Yes

 ** [description](#API_CreateWebFunctionRevision_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-request-description"></a>
A description of the revision.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** [kmsKeyArn](#API_CreateWebFunctionRevision_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the revision's code and environment variables.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:(aws[a-z-]*):kms:[a-z0-9-]+:[0-9]{12}:key/[a-z0-9-]+`   
Required: No

 ** [serviceConfig](#API_CreateWebFunctionRevision_RequestSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-request-serviceConfig"></a>
The service configuration for the revision, including execution role, timeout, and concurrency settings.  
Type: [ServiceConfig](API_ServiceConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateWebFunctionRevision_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "buildConfig": { 
      "codeConfig": { 
         "s3Object": { 
            "bucket": "string",
            "key": "string",
            "versionId": "string"
         }
      },
      "runtimeConfig": { 
         "runtime": "string"
      }
   },
   "createdAt": "string",
   "description": "string",
   "errors": [ 
      { 
         "attribute": "string",
         "errorCode": "string",
         "errorMessage": "string"
      }
   ],
   "functionArn": "string",
   "kmsKeyArn": "string",
   "revisionArn": "string",
   "revisionId": "string",
   "serviceConfig": { 
      "egressNetworkConnectorArn": "string",
      "environmentVariables": { 
         "string" : "string" 
      },
      "executionRoleArn": "string",
      "maxConcurrencyPerEnvironment": number,
      "telemetryConfig": { 
         "loggingConfig": { 
            "applicationLogLevel": "string",
            "logGroup": "string",
            "systemLogLevel": "string"
         }
      },
      "timeoutSeconds": number
   },
   "state": "string",
   "stateReason": "string"
}
```

## Response Elements
<a name="API_CreateWebFunctionRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [buildConfig](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-buildConfig"></a>
The build configuration for a web function revision, including code location and runtime settings.  
Type: [BuildConfig](API_BuildConfig.md) object

 ** [createdAt](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-createdAt"></a>
The date and time the revision was created.  
Type: Timestamp

 ** [description](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-description"></a>
The description of the revision.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [errors](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-errors"></a>
A list of errors encountered during revision creation. This field is absent when the revision has no errors.  
Type: Array of [RevisionError](API_RevisionError.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [functionArn](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-functionArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [kmsKeyArn](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the revision's code and environment variables.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:(aws[a-z-]*):kms:[a-z0-9-]+:[0-9]{12}:key/[a-z0-9-]+` 

 ** [revisionArn](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-revisionArn"></a>
The Amazon Resource Name (ARN) of the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [revisionId](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-revisionId"></a>
The identifier of the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [serviceConfig](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-serviceConfig"></a>
The service configuration for a web function revision, including execution role, timeout, VPC network access, concurrency, and telemetry settings.  
Type: [ServiceConfig](API_ServiceConfig.md) object

 ** [state](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-state"></a>
The current state of the revision.  
Type: String  
Valid Values: `Pending | Active | Failed` 

 ** [stateReason](#API_CreateWebFunctionRevision_ResponseSyntax) **   <a name="lambdaweb-CreateWebFunctionRevision-response-stateReason"></a>
The reason for the current state of the revision.  
Type: String

## Errors
<a name="API_CreateWebFunctionRevision_Errors"></a>

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
<a name="API_CreateWebFunctionRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-web-2025-03-07/CreateWebFunctionRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/CreateWebFunctionRevision) 


# CreateRuntimeVersion

Creates a new runtime version. A runtime version defines the function execution environment by referencing a container image. Runtime versions are immutable. To update the runtime, create a new runtime version and migrate functions by updating the runtime aliases to point to the new runtime version.

## Request Syntax
<a name="API_CreateRuntimeVersion_RequestSyntax"></a>

```
POST /2026-10-01/runtimes/{{RuntimeName}}/versions HTTP/1.1
Content-type: application/json

{
   "DryRun": {{boolean}},
   "ImageUri": "{{string}}",
   "Name": "{{string}}",
   "ReleaseNotes": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRuntimeVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuntimeName](#API_CreateRuntimeVersion_RequestSyntax) **   <a name="lambdacore-CreateRuntimeVersion-request-uri-RuntimeName"></a>
The name or ARN of the runtime to create a version for.  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

## Request Body
<a name="API_CreateRuntimeVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_CreateRuntimeVersion_RequestSyntax) **   <a name="lambdacore-CreateRuntimeVersion-request-DryRun"></a>
When set to true, the request is validated without creating a new runtime version. Use this to check that the request would succeed. No runtime version is created and no changes are made.  
Type: Boolean  
Required: No

 ** [ImageUri](#API_CreateRuntimeVersion_RequestSyntax) **   <a name="lambdacore-CreateRuntimeVersion-request-ImageUri"></a>
The URI of the container image used to define the function execution environment for this runtime version.  
Type: String  
Required: Yes

 ** [Name](#API_CreateRuntimeVersion_RequestSyntax) **   <a name="lambdacore-CreateRuntimeVersion-request-Name"></a>
The name to assign to the new runtime version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

 ** [ReleaseNotes](#API_CreateRuntimeVersion_RequestSyntax) **   <a name="lambdacore-CreateRuntimeVersion-request-ReleaseNotes"></a>
The release notes to associate with the runtime version.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreateRuntimeVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Compatibility": { 
      "Architectures": [ "string" ],
      "IntegrationModels": [ "string" ],
      "ManagedInstances": "string"
   },
   "Created": "string",
   "LastModified": "string",
   "Name": "string",
   "Platforms": [ 
      { 
         "Architecture": "string",
         "Digest": "string",
         "Os": "string"
      }
   ],
   "ReleaseNotes": "string",
   "ResolvedUri": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_CreateRuntimeVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-Arn"></a>
The Amazon Resource Name (ARN) of the runtime version.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [Compatibility](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-Compatibility"></a>
The compatibility matrix of the runtime version.  
Type: [Compatibility](API_Compatibility.md) object

 ** [Created](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-Created"></a>
The date and time when the runtime version was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [LastModified](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-LastModified"></a>
The date and time when the runtime version was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Name](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-Name"></a>
The name of the runtime version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [Platforms](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-Platforms"></a>
The platforms (architecture and OS combinations) available for the runtime version.  
Type: Array of [Platform](API_Platform.md) objects

 ** [ReleaseNotes](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-ReleaseNotes"></a>
The release notes associated with the runtime version.  
Type: String

 ** [ResolvedUri](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-ResolvedUri"></a>
The resolved image URI of the runtime version.  
Type: String

 ** [State](#API_CreateRuntimeVersion_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeVersion-response-State"></a>
The current state of the runtime version.  
Type: String  
Valid Values: `CREATING | ACTIVE | FAILED | DELETING | PENDING_DELETION` 

## Errors
<a name="API_CreateRuntimeVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **   
One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.    
 ** message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **   
The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.    
 ** message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
The specified resource does not exist. Verify the identifier and Region.    
 ** Message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 404

 ** ServiceException **   
An internal service error occurred. Retry the request with exponential backoff.    
 ** Message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The request would exceed a service quota for your account. Request a quota increase or reduce the number of resources in use, then retry the request.    
 ** Message **   
The error message that describes the exception.  
 ** Type **   
The exception type.
HTTP Status Code: 402

 ** TooManyRequestsException **   
The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.    
 ** message **   
The error message that describes the exception.  
 ** Reason **   
The reason for the throttling.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.  
 ** Type **   
The exception type.
HTTP Status Code: 429

## See Also
<a name="API_CreateRuntimeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/CreateRuntimeVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/CreateRuntimeVersion) 
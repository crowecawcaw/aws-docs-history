

# CreateRuntime

Creates a customer-managed runtime, a resource providing a centrally managed execution environment for your Lambda functions. The runtime resource is the parent of the runtime version and runtime alias child resources.

## Request Syntax
<a name="API_CreateRuntime_RequestSyntax"></a>

```
POST /2026-10-01/runtimes HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "LicenseInfo": "{{string}}",
   "Name": "{{string}}",
   "ReleaseLifecycle": { 
      "DeprecationDate": "{{string}}",
      "FunctionCreateBlockDate": "{{string}}",
      "FunctionUpdateBlockDate": "{{string}}",
      "ReleaseState": "{{string}}"
   },
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateRuntime_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRuntime_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateRuntime_RequestSyntax) **   <a name="lambdacore-CreateRuntime-request-Description"></a>
A description of the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** [LicenseInfo](#API_CreateRuntime_RequestSyntax) **   <a name="lambdacore-CreateRuntime-request-LicenseInfo"></a>
The license information for the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** [Name](#API_CreateRuntime_RequestSyntax) **   <a name="lambdacore-CreateRuntime-request-Name"></a>
The name of the runtime to create.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 128.  
Pattern: `[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

 ** [ReleaseLifecycle](#API_CreateRuntime_RequestSyntax) **   <a name="lambdacore-CreateRuntime-request-ReleaseLifecycle"></a>
The runtime lifecycle for the runtime (optional). Use this to schedule runtime deprecation.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object  
Required: No

 ** [Tags](#API_CreateRuntime_RequestSyntax) **   <a name="lambdacore-CreateRuntime-request-Tags"></a>
A map of tag keys and values to associate with the runtime.  
Type: String to string map  
Required: No

## Response Syntax
<a name="API_CreateRuntime_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Arn": "string",
   "Created": "string",
   "Description": "string",
   "LastModified": "string",
   "LicenseInfo": "string",
   "Name": "string",
   "ReleaseLifecycle": { 
      "DeprecationDate": "string",
      "FunctionCreateBlockDate": "string",
      "FunctionUpdateBlockDate": "string",
      "ReleaseState": "string"
   }
}
```

## Response Elements
<a name="API_CreateRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-Arn"></a>
The Amazon Resource Name (ARN) of the runtime.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [Created](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-Created"></a>
The date and time when the runtime was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Description](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-Description"></a>
The description of the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModified](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-LastModified"></a>
The date and time when the runtime was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [LicenseInfo](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-LicenseInfo"></a>
The license information for the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Name](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-Name"></a>
The name of the runtime.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 128.  
Pattern: `[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]` 

 ** [ReleaseLifecycle](#API_CreateRuntime_ResponseSyntax) **   <a name="lambdacore-CreateRuntime-response-ReleaseLifecycle"></a>
The runtime lifecycle for the runtime. Used to schedule runtime deprecation.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object

## Errors
<a name="API_CreateRuntime_Errors"></a>

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
<a name="API_CreateRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/CreateRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/CreateRuntime) 
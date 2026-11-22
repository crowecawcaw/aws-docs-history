

# UpdateRuntime

Updates the properties of an existing customer-managed runtime, such as its description, license information, or lifecycle information.

## Request Syntax
<a name="API_UpdateRuntime_RequestSyntax"></a>

```
PUT /2026-10-01/runtimes/{{RuntimeName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "LicenseInfo": "{{string}}",
   "ReleaseLifecycle": { 
      "DeprecationDate": "{{string}}",
      "FunctionCreateBlockDate": "{{string}}",
      "FunctionUpdateBlockDate": "{{string}}",
      "ReleaseState": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuntimeName](#API_UpdateRuntime_RequestSyntax) **   <a name="lambdacore-UpdateRuntime-request-uri-RuntimeName"></a>
The name or ARN of the runtime to update.  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

## Request Body
<a name="API_UpdateRuntime_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRuntime_RequestSyntax) **   <a name="lambdacore-UpdateRuntime-request-Description"></a>
The updated description of the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** [LicenseInfo](#API_UpdateRuntime_RequestSyntax) **   <a name="lambdacore-UpdateRuntime-request-LicenseInfo"></a>
The updated license information for the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** [ReleaseLifecycle](#API_UpdateRuntime_RequestSyntax) **   <a name="lambdacore-UpdateRuntime-request-ReleaseLifecycle"></a>
The runtime lifecycle for the runtime. Optional. Used to schedule runtime deprecation. Omitting or providing an empty object removes the existing lifecycle.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object  
Required: No

## Response Syntax
<a name="API_UpdateRuntime_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-Arn"></a>
The Amazon Resource Name (ARN) of the runtime.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [Created](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-Created"></a>
The date and time when the runtime was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Description](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-Description"></a>
The description of the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModified](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-LastModified"></a>
The date and time when the runtime was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [LicenseInfo](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-LicenseInfo"></a>
The license information for the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Name](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-Name"></a>
The name of the runtime.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 128.  
Pattern: `[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]` 

 ** [ReleaseLifecycle](#API_UpdateRuntime_ResponseSyntax) **   <a name="lambdacore-UpdateRuntime-response-ReleaseLifecycle"></a>
The runtime lifecycle for the runtime. Used to schedule runtime deprecation.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object

## Errors
<a name="API_UpdateRuntime_Errors"></a>

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
<a name="API_UpdateRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/UpdateRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/UpdateRuntime) 
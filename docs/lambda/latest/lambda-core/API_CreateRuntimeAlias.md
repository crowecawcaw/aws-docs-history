

# CreateRuntimeAlias

Creates a new customer-managed runtime alias. The alias is a named pointer to a runtime version. Functions consume the customer-managed runtime through the runtime alias.

## Request Syntax
<a name="API_CreateRuntimeAlias_RequestSyntax"></a>

```
POST /2026-10-01/runtimes/{{RuntimeName}}/aliases HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "ReleaseLifecycle": { 
      "DeprecationDate": "{{string}}",
      "FunctionCreateBlockDate": "{{string}}",
      "FunctionUpdateBlockDate": "{{string}}",
      "ReleaseState": "{{string}}"
   },
   "RuntimeVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRuntimeAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuntimeName](#API_CreateRuntimeAlias_RequestSyntax) **   <a name="lambdacore-CreateRuntimeAlias-request-uri-RuntimeName"></a>
The name or ARN of the runtime to create an alias for.  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

## Request Body
<a name="API_CreateRuntimeAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateRuntimeAlias_RequestSyntax) **   <a name="lambdacore-CreateRuntimeAlias-request-Description"></a>
A description of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[^\p{C}]*`   
Required: No

 ** [Name](#API_CreateRuntimeAlias_RequestSyntax) **   <a name="lambdacore-CreateRuntimeAlias-request-Name"></a>
The name to assign to the new runtime alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

 ** [ReleaseLifecycle](#API_CreateRuntimeAlias_RequestSyntax) **   <a name="lambdacore-CreateRuntimeAlias-request-ReleaseLifecycle"></a>
The runtime lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object  
Required: No

 ** [RuntimeVersion](#API_CreateRuntimeAlias_RequestSyntax) **   <a name="lambdacore-CreateRuntimeAlias-request-RuntimeVersion"></a>
The name of the runtime version the alias points to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

## Response Syntax
<a name="API_CreateRuntimeAlias_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Created": "string",
   "Description": "string",
   "LastModified": "string",
   "Name": "string",
   "ReleaseLifecycle": { 
      "DeprecationDate": "string",
      "FunctionCreateBlockDate": "string",
      "FunctionUpdateBlockDate": "string",
      "ReleaseState": "string"
   },
   "RuntimeVersion": "string",
   "RuntimeVersionArn": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_CreateRuntimeAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-Arn"></a>
The Amazon Resource Name (ARN) of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [Created](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-Created"></a>
The date and time when the runtime alias was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Description](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-Description"></a>
A description of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[^\p{C}]*` 

 ** [LastModified](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-LastModified"></a>
The date and time when the runtime alias was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Name](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-Name"></a>
The name of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [ReleaseLifecycle](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-ReleaseLifecycle"></a>
The runtime lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object

 ** [RuntimeVersion](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-RuntimeVersion"></a>
The name of the runtime version the alias points to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [RuntimeVersionArn](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-RuntimeVersionArn"></a>
The Amazon Resource Name (ARN) of the runtime version the alias points to.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [State](#API_CreateRuntimeAlias_ResponseSyntax) **   <a name="lambdacore-CreateRuntimeAlias-response-State"></a>
The current state of the runtime alias.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | PENDING_DELETION` 

## Errors
<a name="API_CreateRuntimeAlias_Errors"></a>

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
<a name="API_CreateRuntimeAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/CreateRuntimeAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/CreateRuntimeAlias) 
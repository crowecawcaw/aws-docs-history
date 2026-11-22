

# RestoreRuntime

Cancels a pending scheduled deletion, returning the resource to the ACTIVE state. Scope is determined by the RuntimeName path parameter plus an optional, mutually exclusive RuntimeVersion or RuntimeAlias query parameter: with neither, the runtime itself is restored; with RuntimeVersion, the named runtime version; with RuntimeAlias, the named runtime alias. Restoring a resource that is already ACTIVE is a no-op success. Restore only works while the target is PENDING\_DELETION; once the scheduled deletion has begun executing (DELETING) or has completed, the call fails.

## Request Syntax
<a name="API_RestoreRuntime_RequestSyntax"></a>

```
POST /2026-10-01/runtimes/{{RuntimeName}}/restore?RuntimeAlias={{RuntimeAlias}}&RuntimeVersion={{RuntimeVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RestoreRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuntimeAlias](#API_RestoreRuntime_RequestSyntax) **   <a name="lambdacore-RestoreRuntime-request-uri-RuntimeAlias"></a>
Optional. Restores the named RuntimeAlias under RuntimeName. Mutually exclusive with RuntimeVersion; supplying both is rejected with InvalidParameterValueException.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [RuntimeName](#API_RestoreRuntime_RequestSyntax) **   <a name="lambdacore-RestoreRuntime-request-uri-RuntimeName"></a>
The name or ARN of the runtime to restore. When RuntimeVersion or RuntimeAlias is specified, the runtime that owns the runtime version or runtime alias to restore.  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

 ** [RuntimeVersion](#API_RestoreRuntime_RequestSyntax) **   <a name="lambdacore-RestoreRuntime-request-uri-RuntimeVersion"></a>
Optional. Restores the named RuntimeVersion under RuntimeName. Mutually exclusive with RuntimeAlias; supplying both is rejected with InvalidParameterValueException.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

## Request Body
<a name="API_RestoreRuntime_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RestoreRuntime_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "LastModified": "string",
   "RuntimeAlias": "string",
   "RuntimeName": "string",
   "RuntimeVersion": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_RestoreRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-Arn"></a>
The fully qualified ARN of the resource that was restored (runtime, version, or alias).  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?` 

 ** [LastModified](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-LastModified"></a>
The date and time when the restored resource was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [RuntimeAlias](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-RuntimeAlias"></a>
Echoed back only when the request supplied a RuntimeAlias qualifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [RuntimeName](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-RuntimeName"></a>
The name or ARN of the runtime.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]` 

 ** [RuntimeVersion](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-RuntimeVersion"></a>
Echoed back only when the request supplied a RuntimeVersion qualifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?` 

 ** [State](#API_RestoreRuntime_ResponseSyntax) **   <a name="lambdacore-RestoreRuntime-response-State"></a>
The state of the restored resource, ACTIVE on success.  
Type: String  
Valid Values: `ACTIVE | PENDING_DELETION | DELETING | FAILED` 

## Errors
<a name="API_RestoreRuntime_Errors"></a>

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
<a name="API_RestoreRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/RestoreRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/RestoreRuntime) 
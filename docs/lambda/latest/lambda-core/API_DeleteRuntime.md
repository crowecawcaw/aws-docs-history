

# DeleteRuntime

Schedules a customer-managed runtime to be deleted. Runtimes scheduled for deletion enter the PENDING\_DELETION state and can be restored during the scheduled deletion window. Runtime versions and aliases must be deleted or scheduled for deletion before deleting the runtime. Function invokes fail for functions using runtime versions or aliases that are deleted or pending deletion.

## Request Syntax
<a name="API_DeleteRuntime_RequestSyntax"></a>

```
DELETE /2026-10-01/runtimes/{{RuntimeName}} HTTP/1.1
x-amzn-runtime-recovery-window-in-days: {{RecoveryWindowInDays}}
```

## URI Request Parameters
<a name="API_DeleteRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RecoveryWindowInDays](#API_DeleteRuntime_RequestSyntax) **   <a name="lambdacore-DeleteRuntime-request-RecoveryWindowInDays"></a>
Optional. The waiting period, in days (7-30), before the runtime is permanently deleted.  
Valid Range: Minimum value of 7. Maximum value of 30.

 ** [RuntimeName](#API_DeleteRuntime_RequestSyntax) **   <a name="lambdacore-DeleteRuntime-request-uri-RuntimeName"></a>
The name or ARN of the runtime to delete.  
Length Constraints: Minimum length of 2. Maximum length of 2048.  
Pattern: `(arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/)?[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

## Request Body
<a name="API_DeleteRuntime_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRuntime_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteRuntime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteRuntime_Errors"></a>

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
<a name="API_DeleteRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-core-2026-04-30/DeleteRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/DeleteRuntime) 


# StopPipe
<a name="API_StopPipe"></a>

Stop an existing pipe.

## Request Syntax
<a name="API_StopPipe_RequestSyntax"></a>

```
POST /v1/pipes/{{Name}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_StopPipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_StopPipe_RequestSyntax) **   <a name="eventbridge-StopPipe-request-uri-Name"></a>
The name of the pipe.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+`   
Required: Yes

## Request Body
<a name="API_StopPipe_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopPipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": number,
   "CurrentState": "string",
   "DesiredState": "string",
   "LastModifiedTime": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_StopPipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-Arn"></a>
The ARN of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)` 

 ** [CreationTime](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-CreationTime"></a>
The time the pipe was created.  
Type: Timestamp

 ** [CurrentState](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-CurrentState"></a>
The state the pipe is in.  
Type: String  
Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED` 

 ** [DesiredState](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-DesiredState"></a>
The state the pipe should be in.  
Type: String  
Valid Values: `RUNNING | STOPPED` 

 ** [LastModifiedTime](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-LastModifiedTime"></a>
When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).  
Type: Timestamp

 ** [Name](#API_StopPipe_ResponseSyntax) **   <a name="eventbridge-StopPipe-response-Name"></a>
The name of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+` 

## Errors
<a name="API_StopPipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
An action you attempted resulted in an exception.    
 ** resourceId **   
The ID of the resource that caused the exception.  
 ** resourceType **   
The type of resource that caused the exception.
HTTP Status Code: 409

 ** InternalException **   
This exception occurs due to unexpected causes.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.
HTTP Status Code: 500

 ** NotFoundException **   
An entity that you specified does not exist.  
HTTP Status Code: 404

 ** ThrottlingException **   
An action was throttled.    
 ** quotaCode **   
The identifier of the quota that caused the exception.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.  
 ** serviceCode **   
The identifier of the service that caused the exception.
HTTP Status Code: 429

 ** ValidationException **   
Indicates that an error has occurred while performing a validate operation.    
 ** fieldList **   
The list of fields for which validation failed and the corresponding failure messages.
HTTP Status Code: 400

## See Also
<a name="API_StopPipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pipes-2015-10-07/StopPipe) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/StopPipe) 
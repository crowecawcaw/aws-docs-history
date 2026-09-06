

# ListPipes
<a name="API_ListPipes"></a>

Get the pipes associated with this account. For more information about pipes, see [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) in the Amazon EventBridge User Guide.

## Request Syntax
<a name="API_ListPipes_RequestSyntax"></a>

```
GET /v1/pipes?CurrentState={{CurrentState}}&DesiredState={{DesiredState}}&Limit={{Limit}}&NamePrefix={{NamePrefix}}&NextToken={{NextToken}}&SourcePrefix={{SourcePrefix}}&TargetPrefix={{TargetPrefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPipes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CurrentState](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-CurrentState"></a>
The state the pipe is in.  
Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED` 

 ** [DesiredState](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-DesiredState"></a>
The state the pipe should be in.  
Valid Values: `RUNNING | STOPPED` 

 ** [Limit](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-Limit"></a>
The maximum number of pipes to include in the response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NamePrefix](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-NamePrefix"></a>
A value that will return a subset of the pipes associated with this account. For example, `"NamePrefix": "ABC"` will return all endpoints with "ABC" in the name.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+` 

 ** [NextToken](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SourcePrefix](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-SourcePrefix"></a>
The prefix matching the pipe source.  
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [TargetPrefix](#API_ListPipes_RequestSyntax) **   <a name="eventbridge-ListPipes-request-uri-TargetPrefix"></a>
The prefix matching the pipe target.  
Length Constraints: Minimum length of 1. Maximum length of 1600.

## Request Body
<a name="API_ListPipes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPipes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Pipes": [ 
      { 
         "Arn": "string",
         "CreationTime": number,
         "CurrentState": "string",
         "DesiredState": "string",
         "Enrichment": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Source": "string",
         "StateReason": "string",
         "Target": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipes_ResponseSyntax) **   <a name="eventbridge-ListPipes-response-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Pipes](#API_ListPipes_ResponseSyntax) **   <a name="eventbridge-ListPipes-response-Pipes"></a>
The pipes returned by the call.  
Type: Array of [Pipe](API_Pipe.md) objects

## Errors
<a name="API_ListPipes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **   
This exception occurs due to unexpected causes.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.
HTTP Status Code: 500

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
<a name="API_ListPipes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pipes-2015-10-07/ListPipes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/ListPipes) 
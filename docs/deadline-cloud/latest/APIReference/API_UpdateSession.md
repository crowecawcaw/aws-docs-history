# UpdateSession

Updates a session.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId`/sessions/`sessionId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "targetLifecycleStatus": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The farm ID to update in the session.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The job ID to update in the session.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The queue ID to update in the session.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[sessionId](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The session ID to update.


Pattern: `session-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[targetLifecycleStatus](#API_UpdateSession_RequestSyntax "#API_UpdateSession_RequestSyntax")**


The life cycle status to update in the session.


Type: String


Valid Values: `ENDED`



Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




**ConflictException** 


Your request has conflicting operations. This can occur if you're trying to perform more
 than one operation on the same resource at the same time.





**context** 


Information about the resources in use when the exception was thrown.




**reason** 


A description of the error.




**resourceId** 


The identifier of the resource in use.




**resourceType** 


The type of the resource in use.




HTTP Status Code: 409




**InternalServerErrorException** 


Deadline Cloud can't process your request right now. Try again later.





**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




HTTP Status Code: 500




**ResourceNotFoundException** 


The requested resource can't be found.





**context** 


Information about the resources in use when the exception was thrown.




**resourceId** 


The identifier of the resource that couldn't be found.




**resourceType** 


The type of the resource that couldn't be found.




HTTP Status Code: 404




**ThrottlingException** 


Your request exceeded a request rate quota.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that is being throttled.




**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




**serviceCode** 


Identifies the service that is being throttled.




HTTP Status Code: 429




**ValidationException** 


The request isn't valid. This can occur if your request contains malformed JSON or
 unsupported characters.





**context** 


Information about the resources in use when the exception was thrown.




**fieldList** 


A list of fields that failed validation.




**reason** 


The reason that the request failed validation.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateSession")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateSession")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateSession")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateSession")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateSession")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateSession")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateSession")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateSession")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateSession")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateSession "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateSession")

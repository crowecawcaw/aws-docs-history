# GetSessionAction

Gets a session action for the job.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId`/session-actions/`sessionActionId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetSessionAction_RequestSyntax "#API_GetSessionAction_RequestSyntax")**


The farm ID for the session action.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_GetSessionAction_RequestSyntax "#API_GetSessionAction_RequestSyntax")**


The job ID for the session.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetSessionAction_RequestSyntax "#API_GetSessionAction_RequestSyntax")**


The queue ID for the session action.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[sessionActionId](#API_GetSessionAction_RequestSyntax "#API_GetSessionAction_RequestSyntax")**


The session action ID for the session.


Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "acquiredLimits": [ 
      { 
         "count": ***number***,
         "limitId": "***string***"
      }
   ],
   "definition": { ... },
   "endedAt": "***string***",
   "manifests": [ 
      { 
         "outputManifestHash": "***string***",
         "outputManifestPath": "***string***"
      }
   ],
   "processExitCode": ***number***,
   "progressMessage": "***string***",
   "progressPercent": ***number***,
   "sessionActionId": "***string***",
   "sessionId": "***string***",
   "startedAt": "***string***",
   "status": "***string***",
   "workerUpdatedAt": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[acquiredLimits](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The limits and their amounts acquired during a session action. If no limits were
 acquired during the session, this field isn't returned.


Type: Array of [AcquiredLimit](API_AcquiredLimit.md "API_AcquiredLimit.md") objects




**[definition](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The session action definition.


Type: [SessionActionDefinition](API_SessionActionDefinition.md "API_SessionActionDefinition.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.




**[endedAt](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The date and time the resource ended running.


Type: Timestamp




**[manifests](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The list of manifest properties that describe file attachments for the task run.


Type: Array of [TaskRunManifestPropertiesResponse](API_TaskRunManifestPropertiesResponse.md "API_TaskRunManifestPropertiesResponse.md") objects




**[processExitCode](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The process exit code. The default Deadline Cloud worker agent converts unsigned
 32-bit exit codes to signed 32-bit exit codes.


Type: Integer


Valid Range: Minimum value of -2147483648. Maximum value of 2147483647.




**[progressMessage](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The message that communicates the progress of the session action.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 4096.




**[progressPercent](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The percentage completed for a session action.


Type: Float


Valid Range: Minimum value of 0. Maximum value of 100.




**[sessionActionId](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The session action ID.


Type: String


Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`





**[sessionId](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The session ID for the session action.


Type: String


Pattern: `session-[0-9a-f]{32}`





**[startedAt](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The date and time the resource started running.


Type: Timestamp




**[status](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The status of the session action.


Type: String


Valid Values: `ASSIGNED | RUNNING | CANCELING | SUCCEEDED | FAILED | INTERRUPTED | CANCELED | NEVER_ATTEMPTED | SCHEDULED | RECLAIMING | RECLAIMED`





**[workerUpdatedAt](#API_GetSessionAction_ResponseSyntax "#API_GetSessionAction_ResponseSyntax")**


The Linux timestamp of the date and time the session action was last updated.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetSessionAction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetSessionAction "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetSessionAction")

# UpdateWorkerSchedule

Updates the schedule for a worker.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers/`workerId`/schedule HTTP/1.1
Content-type: application/json

{
   "[updatedSessionActions](#deadlinecloud-UpdateWorkerSchedule-request-updatedSessionActions "#deadlinecloud-UpdateWorkerSchedule-request-updatedSessionActions")": { 
      "`string`" : { 
         "[completedStatus](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-completedStatus "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-completedStatus")": "`string`",
         "[endedAt](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-endedAt "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-endedAt")": "`string`",
         "[manifests](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-manifests "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-manifests")": [ 
            { 
               "[outputManifestHash](API_TaskRunManifestPropertiesRequest.md#deadlinecloud-Type-TaskRunManifestPropertiesRequest-outputManifestHash "API_TaskRunManifestPropertiesRequest.md#deadlinecloud-Type-TaskRunManifestPropertiesRequest-outputManifestHash")": "`string`",
               "[outputManifestPath](API_TaskRunManifestPropertiesRequest.md#deadlinecloud-Type-TaskRunManifestPropertiesRequest-outputManifestPath "API_TaskRunManifestPropertiesRequest.md#deadlinecloud-Type-TaskRunManifestPropertiesRequest-outputManifestPath")": "`string`"
            }
         ],
         "[processExitCode](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-processExitCode "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-processExitCode")": `number`,
         "[progressMessage](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-progressMessage "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-progressMessage")": "`string`",
         "[progressPercent](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-progressPercent "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-progressPercent")": `number`,
         "[startedAt](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-startedAt "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-startedAt")": "`string`",
         "[updatedAt](API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-updatedAt "API_UpdatedSessionActionInfo.md#deadlinecloud-Type-UpdatedSessionActionInfo-updatedAt")": "`string`"
      }
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_UpdateWorkerSchedule_RequestSyntax "#API_UpdateWorkerSchedule_RequestSyntax")**


The farm ID to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_UpdateWorkerSchedule_RequestSyntax "#API_UpdateWorkerSchedule_RequestSyntax")**


The fleet ID to update.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[workerId](#API_UpdateWorkerSchedule_RequestSyntax "#API_UpdateWorkerSchedule_RequestSyntax")**


The worker ID to update.


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[updatedSessionActions](#API_UpdateWorkerSchedule_RequestSyntax "#API_UpdateWorkerSchedule_RequestSyntax")**


The session actions associated with the worker schedule to update.


Type: String to [UpdatedSessionActionInfo](API_UpdatedSessionActionInfo.md "API_UpdatedSessionActionInfo.md") object map


Key Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[assignedSessions](#deadlinecloud-UpdateWorkerSchedule-response-assignedSessions "#deadlinecloud-UpdateWorkerSchedule-response-assignedSessions")": { 
      "***string***" : { 
         "[jobId](API_AssignedSession.md#deadlinecloud-Type-AssignedSession-jobId "API_AssignedSession.md#deadlinecloud-Type-AssignedSession-jobId")": "***string***",
         "[logConfiguration](API_AssignedSession.md#deadlinecloud-Type-AssignedSession-logConfiguration "API_AssignedSession.md#deadlinecloud-Type-AssignedSession-logConfiguration")": { 
            "[error](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error")": "***string***",
            "[logDriver](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver")": "***string***",
            "[options](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options")": { 
               "***string***" : "***string***" 
            },
            "[parameters](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters")": { 
               "***string***" : "***string***" 
            }
         },
         "[queueId](API_AssignedSession.md#deadlinecloud-Type-AssignedSession-queueId "API_AssignedSession.md#deadlinecloud-Type-AssignedSession-queueId")": "***string***",
         "[sessionActions](API_AssignedSession.md#deadlinecloud-Type-AssignedSession-sessionActions "API_AssignedSession.md#deadlinecloud-Type-AssignedSession-sessionActions")": [ 
            { 
               "[definition](API_AssignedSessionAction.md#deadlinecloud-Type-AssignedSessionAction-definition "API_AssignedSessionAction.md#deadlinecloud-Type-AssignedSessionAction-definition")": { ... },
               "[sessionActionId](API_AssignedSessionAction.md#deadlinecloud-Type-AssignedSessionAction-sessionActionId "API_AssignedSessionAction.md#deadlinecloud-Type-AssignedSessionAction-sessionActionId")": "***string***"
            }
         ]
      }
   },
   "[cancelSessionActions](#deadlinecloud-UpdateWorkerSchedule-response-cancelSessionActions "#deadlinecloud-UpdateWorkerSchedule-response-cancelSessionActions")": { 
      "***string***" : [ "***string***" ]
   },
   "[desiredWorkerStatus](#deadlinecloud-UpdateWorkerSchedule-response-desiredWorkerStatus "#deadlinecloud-UpdateWorkerSchedule-response-desiredWorkerStatus")": "***string***",
   "[updateIntervalSeconds](#deadlinecloud-UpdateWorkerSchedule-response-updateIntervalSeconds "#deadlinecloud-UpdateWorkerSchedule-response-updateIntervalSeconds")": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[assignedSessions](#API_UpdateWorkerSchedule_ResponseSyntax "#API_UpdateWorkerSchedule_ResponseSyntax")**


The assigned sessions to update.


Type: String to [AssignedSession](API_AssignedSession.md "API_AssignedSession.md") object map


Key Pattern: `session-[0-9a-f]{32}`





**[cancelSessionActions](#API_UpdateWorkerSchedule_ResponseSyntax "#API_UpdateWorkerSchedule_ResponseSyntax")**


The session actions associated with the worker schedule to cancel.


Type: String to array of strings map


Key Pattern: `session-[0-9a-f]{32}`



Array Members: Minimum number of 0 items. Maximum number of 100 items.


Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`





**[desiredWorkerStatus](#API_UpdateWorkerSchedule_ResponseSyntax "#API_UpdateWorkerSchedule_ResponseSyntax")**


The status to update the worker to.


Type: String


Valid Values: `STOPPED`





**[updateIntervalSeconds](#API_UpdateWorkerSchedule_ResponseSyntax "#API_UpdateWorkerSchedule_ResponseSyntax")**


Updates the time interval (in seconds) for the schedule.


Type: Integer


Valid Range: Minimum value of 0.




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateWorkerSchedule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateWorkerSchedule "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateWorkerSchedule")

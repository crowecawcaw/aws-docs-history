# GetStep

Gets a step.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId`/steps/`stepId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetStep_RequestSyntax "#API_GetStep_RequestSyntax")**


The farm ID for the step.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_GetStep_RequestSyntax "#API_GetStep_RequestSyntax")**


The job ID for the step.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetStep_RequestSyntax "#API_GetStep_RequestSyntax")**


The queue ID for the step.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[stepId](#API_GetStep_RequestSyntax "#API_GetStep_RequestSyntax")**


The step ID.


Pattern: `step-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "***string***",
   "createdBy": "***string***",
   "dependencyCounts": { 
      "consumersResolved": ***number***,
      "consumersUnresolved": ***number***,
      "dependenciesResolved": ***number***,
      "dependenciesUnresolved": ***number***
   },
   "description": "***string***",
   "endedAt": "***string***",
   "lifecycleStatus": "***string***",
   "lifecycleStatusMessage": "***string***",
   "name": "***string***",
   "parameterSpace": { 
      "combination": "***string***",
      "parameters": [ 
         { 
            "name": "***string***",
            "type": "***string***"
         }
      ]
   },
   "requiredCapabilities": { 
      "amounts": [ 
         { 
            "max": ***number***,
            "min": ***number***,
            "name": "***string***",
            "value": ***number***
         }
      ],
      "attributes": [ 
         { 
            "allOf": [ "***string***" ],
            "anyOf": [ "***string***" ],
            "name": "***string***"
         }
      ]
   },
   "startedAt": "***string***",
   "stepId": "***string***",
   "targetTaskRunStatus": "***string***",
   "taskFailureRetryCount": ***number***,
   "taskRunStatus": "***string***",
   "taskRunStatusCounts": { 
      "***string***" : ***number*** 
   },
   "updatedAt": "***string***",
   "updatedBy": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[createdAt](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[dependencyCounts](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The number of dependencies in the step.


Type: [DependencyCounts](API_DependencyCounts.md "API_DependencyCounts.md") object




**[description](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The description of the step.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[endedAt](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The date and time the resource ended running.


Type: Timestamp




**[lifecycleStatus](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The life cycle status of the step.


Type: String


Valid Values: `CREATE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED`





**[lifecycleStatusMessage](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


A message that describes the lifecycle status of the step.


Type: String




**[name](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The name of the step.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.




**[parameterSpace](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


A list of step parameters and the combination expression for the step.


Type: [ParameterSpace](API_ParameterSpace.md "API_ParameterSpace.md") object




**[requiredCapabilities](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The required capabilities of the step.


Type: [StepRequiredCapabilities](API_StepRequiredCapabilities.md "API_StepRequiredCapabilities.md") object




**[startedAt](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The date and time the resource started running.


Type: Timestamp




**[stepId](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The step ID.


Type: String


Pattern: `step-[0-9a-f]{32}`





**[targetTaskRunStatus](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The task status with which the job started.


Type: String


Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`





**[taskFailureRetryCount](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The total number of times tasks from the step failed and were retried.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[taskRunStatus](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The task run status for the job.


Type: String


Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`





**[taskRunStatusCounts](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The number of tasks running on the job.


Type: String to integer map


Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`





**[updatedAt](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetStep_ResponseSyntax "#API_GetStep_ResponseSyntax")**


The user or system that updated this resource.


Type: String




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetStep")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetStep")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetStep")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetStep")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetStep")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetStep")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetStep")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetStep")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetStep")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetStep "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetStep")

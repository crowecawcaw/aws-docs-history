# GetJob

Gets a Deadline Cloud job.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetJob_RequestSyntax "#API_GetJob_RequestSyntax")**


The farm ID of the farm in the job.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_GetJob_RequestSyntax "#API_GetJob_RequestSyntax")**


The job ID.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetJob_RequestSyntax "#API_GetJob_RequestSyntax")**


The queue ID associated with the job.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "attachments": { 
      "fileSystem": "***string***",
      "manifests": [ 
         { 
            "fileSystemLocationName": "***string***",
            "inputManifestHash": "***string***",
            "inputManifestPath": "***string***",
            "outputRelativeDirectories": [ "***string***" ],
            "rootPath": "***string***",
            "rootPathFormat": "***string***"
         }
      ]
   },
   "createdAt": "***string***",
   "createdBy": "***string***",
   "description": "***string***",
   "endedAt": "***string***",
   "jobId": "***string***",
   "lifecycleStatus": "***string***",
   "lifecycleStatusMessage": "***string***",
   "maxFailedTasksCount": ***number***,
   "maxRetriesPerTask": ***number***,
   "maxWorkerCount": ***number***,
   "name": "***string***",
   "parameters": { 
      "***string***" : { ... }
   },
   "priority": ***number***,
   "sourceJobId": "***string***",
   "startedAt": "***string***",
   "storageProfileId": "***string***",
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





**[attachments](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The attachments for the job.


Type: [Attachments](API_Attachments.md "API_Attachments.md") object




**[createdAt](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[description](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The description of the job.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[endedAt](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The date and time the resource ended running.


Type: Timestamp




**[jobId](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`





**[lifecycleStatus](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The life cycle status for the job. 


Type: String


Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE | UPLOAD_IN_PROGRESS | UPLOAD_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED | ARCHIVED`





**[lifecycleStatusMessage](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


A message that communicates the status of the life cycle for the job.


Type: String




**[maxFailedTasksCount](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The number of task failures before the job stops running and is marked as `FAILED`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[maxRetriesPerTask](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The maximum number of retries per failed tasks.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[maxWorkerCount](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The maximum number of worker hosts that can concurrently process a job. When the
 `maxWorkerCount` is reached, no more workers will be assigned to process the
 job, even if the fleets assigned to the job's queue has available workers.


If you don't set the `maxWorkerCount` when you create a job, this value is
 not returned in the response.


Type: Integer


Valid Range: Minimum value of -1. Maximum value of 2147483647.




**[name](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The name of the job.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.




**[parameters](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The parameters for the job.


Type: String to [JobParameter](API_JobParameter.md "API_JobParameter.md") object map


Key Length Constraints: Minimum length of 1. Maximum length of 1024.




**[priority](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The job priority.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 100.




**[sourceJobId](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The job ID for the source job.


Type: String


Pattern: `job-[0-9a-f]{32}`





**[startedAt](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The date and time the resource started running.


Type: Timestamp




**[storageProfileId](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The storage profile ID associated with the job.


Type: String


Pattern: `sp-[0-9a-f]{32}`





**[targetTaskRunStatus](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The task status with which the job started.


Type: String


Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`





**[taskFailureRetryCount](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The total number of times tasks from the job failed and were retried.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[taskRunStatus](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The task run status for the job.


Type: String


Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`





**[taskRunStatusCounts](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The number of tasks running on the job.


Type: String to integer map


Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`





**[updatedAt](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetJob_ResponseSyntax "#API_GetJob_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetJob")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetJob")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetJob")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetJob")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetJob")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetJob")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetJob")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetJob")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetJob")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetJob "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetJob")

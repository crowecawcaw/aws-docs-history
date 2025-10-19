# CreateJob

Creates a job. A job is a set of instructions that Deadline Cloud uses to schedule
 and run work on available workers. For more information, see [Deadline Cloud
 jobs](../userguide/deadline-cloud-jobs.md "../userguide/deadline-cloud-jobs.md").


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/queues/`queueId`/jobs HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "attachments": { 
      "fileSystem": "`string`",
      "manifests": [ 
         { 
            "fileSystemLocationName": "`string`",
            "inputManifestHash": "`string`",
            "inputManifestPath": "`string`",
            "outputRelativeDirectories": [ "`string`" ],
            "rootPath": "`string`",
            "rootPathFormat": "`string`"
         }
      ]
   },
   "maxFailedTasksCount": `number`,
   "maxRetriesPerTask": `number`,
   "maxWorkerCount": `number`,
   "parameters": { 
      "`string`" : { ... }
   },
   "priority": `number`,
   "sourceJobId": "`string`",
   "storageProfileId": "`string`",
   "targetTaskRunStatus": "`string`",
   "template": "`string`",
   "templateType": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The farm ID of the farm to connect to the job.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The ID of the queue that the job is submitted to.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[attachments](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The attachments for the job. Attach files required for the job to run to a render
 job.


Type: [Attachments](API_Attachments.md "API_Attachments.md") object


Required: No




**[maxFailedTasksCount](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The number of task failures before the job stops running and is marked as `FAILED`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[maxRetriesPerTask](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The maximum number of retries for each task.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[maxWorkerCount](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The maximum number of worker hosts that can concurrently process a job. When the
 `maxWorkerCount` is reached, no more workers will be assigned to process the
 job, even if the fleets assigned to the job's queue has available workers.


You can't set the `maxWorkerCount` to 0. If you set it to -1, there is no
 maximum number of workers.


If you don't specify the `maxWorkerCount`, Deadline Cloud won't throttle
 the number of workers used to process the job.


Type: Integer


Valid Range: Minimum value of -1. Maximum value of 2147483647.


Required: No




**[parameters](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The parameters for the job.


Type: String to [JobParameter](API_JobParameter.md "API_JobParameter.md") object map


Key Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**[priority](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The priority of the job. The highest priority (first scheduled) is 100. When two jobs
 have the same priority, the oldest job is scheduled first.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 100.


Required: Yes




**[sourceJobId](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The job ID for the source job.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: No




**[storageProfileId](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The storage profile ID for the storage profile to connect to the job.


Type: String


Pattern: `sp-[0-9a-f]{32}`



Required: No




**[targetTaskRunStatus](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The initial job status when it is created. Jobs that are created with a
 `SUSPENDED` status will not run until manually requeued.


Type: String


Valid Values: `READY | SUSPENDED`



Required: No




**[template](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The job template to use for this job.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1000000.


Required: No




**[templateType](#API_CreateJob_RequestSyntax "#API_CreateJob_RequestSyntax")**


The file type for the job template.


Type: String


Valid Values: `JSON | YAML`



Required: No




## Response Syntax



```
HTTP/1.1 201
Content-type: application/json

{
   "jobId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in JSON format by the service.





**[jobId](#API_CreateJob_ResponseSyntax "#API_CreateJob_ResponseSyntax")**


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`





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




**ServiceQuotaExceededException** 


You exceeded your service quota. Service quotas, also referred to as limits, are the
 maximum number of service resources or operations for your AWS account.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that has been exceeded.




**reason** 


A string that describes the reason the quota was exceeded.




**resourceId** 


The identifier of the affected resource.




**resourceType** 


The type of the affected resource




**serviceCode** 


Identifies the service that exceeded the quota.




HTTP Status Code: 402




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateJob")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateJob")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateJob")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateJob")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateJob")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateJob")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateJob")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateJob")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateJob")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateJob "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateJob")

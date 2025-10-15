# UpdateJob

Updates a job. 

When you change the status of the job to `ARCHIVED`, the job can't be
 scheduled or archived.

###### Important

An archived jobs and its steps and tasks are deleted after 120 days. The job can't be
 recovered.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[lifecycleStatus](#deadlinecloud-UpdateJob-request-lifecycleStatus "#deadlinecloud-UpdateJob-request-lifecycleStatus")": "`string`",
   "[maxFailedTasksCount](#deadlinecloud-UpdateJob-request-maxFailedTasksCount "#deadlinecloud-UpdateJob-request-maxFailedTasksCount")": `number`,
   "[maxRetriesPerTask](#deadlinecloud-UpdateJob-request-maxRetriesPerTask "#deadlinecloud-UpdateJob-request-maxRetriesPerTask")": `number`,
   "[maxWorkerCount](#deadlinecloud-UpdateJob-request-maxWorkerCount "#deadlinecloud-UpdateJob-request-maxWorkerCount")": `number`,
   "[priority](#deadlinecloud-UpdateJob-request-priority "#deadlinecloud-UpdateJob-request-priority")": `number`,
   "[targetTaskRunStatus](#deadlinecloud-UpdateJob-request-targetTaskRunStatus "#deadlinecloud-UpdateJob-request-targetTaskRunStatus")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The farm ID of the job to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The job ID to update.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The queue ID of the job to update.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[lifecycleStatus](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The status of a job in its lifecycle. When you change the status of the job to
 `ARCHIVED`, the job can't be scheduled or archived.


###### Important

An archived jobs and its steps and tasks are deleted after 120 days. The job can't be
 recovered.


Type: String


Valid Values: `ARCHIVED`



Required: No




**[maxFailedTasksCount](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The number of task failures before the job stops running and is marked as `FAILED`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[maxRetriesPerTask](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The maximum number of retries for a job.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[maxWorkerCount](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The maximum number of worker hosts that can concurrently process a job. When the
 `maxWorkerCount` is reached, no more workers will be assigned to process the
 job, even if the fleets assigned to the job's queue has available workers.


You can't set the `maxWorkerCount` to 0. If you set it to -1, there is no
 maximum number of workers.


If you don't specify the `maxWorkerCount`, the default is -1.


The maximum number of workers that can process tasks in the job.


Type: Integer


Valid Range: Minimum value of -1. Maximum value of 2147483647.


Required: No




**[priority](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The job priority to update.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 100.


Required: No




**[targetTaskRunStatus](#API_UpdateJob_RequestSyntax "#API_UpdateJob_RequestSyntax")**


The task status to update the job's tasks to.


Type: String


Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`



Required: No




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateJob")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateJob")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateJob")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateJob")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateJob")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateJob")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateJob")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateJob")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateJob")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateJob "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateJob")

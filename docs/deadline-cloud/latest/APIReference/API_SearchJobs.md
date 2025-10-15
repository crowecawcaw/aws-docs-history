# SearchJobs

Searches for jobs.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/search/jobs HTTP/1.1
Content-type: application/json

{
   "[filterExpressions](#deadlinecloud-SearchJobs-request-filterExpressions "#deadlinecloud-SearchJobs-request-filterExpressions")": { 
      "[filters](API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-filters "API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-filters")": [ 
         { ... }
      ],
      "[operator](API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-operator "API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-operator")": "`string`"
   },
   "[itemOffset](#deadlinecloud-SearchJobs-request-itemOffset "#deadlinecloud-SearchJobs-request-itemOffset")": `number`,
   "[pageSize](#deadlinecloud-SearchJobs-request-pageSize "#deadlinecloud-SearchJobs-request-pageSize")": `number`,
   "[queueIds](#deadlinecloud-SearchJobs-request-queueIds "#deadlinecloud-SearchJobs-request-queueIds")": [ "`string`" ],
   "[sortExpressions](#deadlinecloud-SearchJobs-request-sortExpressions "#deadlinecloud-SearchJobs-request-sortExpressions")": [ 
      { ... }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


The farm ID of the job.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[filterExpressions](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


The filter expression, `AND` or `OR`, to use
when searching among a group of search strings in a resource.

You can use two groupings per search each within parenthesis `()`.


Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md "API_SearchGroupedFilterExpressions.md") object


Required: No




**[itemOffset](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


Defines how far into the scrollable list to start the return of results.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.


Required: Yes




**[pageSize](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


Specifies the number of items per page for the resource.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**[queueIds](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


The queue ID to use in the job search.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[sortExpressions](#API_SearchJobs_RequestSyntax "#API_SearchJobs_RequestSyntax")**


The search terms for a resource.


Type: Array of [SearchSortExpression](API_SearchSortExpression.md "API_SearchSortExpression.md") objects


Array Members: Minimum number of 1 item. Maximum number of 5 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[jobs](#deadlinecloud-SearchJobs-response-jobs "#deadlinecloud-SearchJobs-response-jobs")": [ 
      { 
         "[createdAt](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-createdAt "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-createdAt")": "***string***",
         "[createdBy](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-createdBy "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-createdBy")": "***string***",
         "[endedAt](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-endedAt "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-endedAt")": "***string***",
         "[jobId](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-jobId "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-jobId")": "***string***",
         "[jobParameters](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-jobParameters "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-jobParameters")": { 
            "***string***" : { ... }
         },
         "[lifecycleStatus](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-lifecycleStatus "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-lifecycleStatus")": "***string***",
         "[lifecycleStatusMessage](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-lifecycleStatusMessage "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-lifecycleStatusMessage")": "***string***",
         "[maxFailedTasksCount](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxFailedTasksCount "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxFailedTasksCount")": ***number***,
         "[maxRetriesPerTask](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxRetriesPerTask "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxRetriesPerTask")": ***number***,
         "[maxWorkerCount](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxWorkerCount "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-maxWorkerCount")": ***number***,
         "[name](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-name "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-name")": "***string***",
         "[priority](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-priority "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-priority")": ***number***,
         "[queueId](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-queueId "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-queueId")": "***string***",
         "[sourceJobId](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-sourceJobId "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-sourceJobId")": "***string***",
         "[startedAt](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-startedAt "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-startedAt")": "***string***",
         "[targetTaskRunStatus](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-targetTaskRunStatus "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-targetTaskRunStatus")": "***string***",
         "[taskFailureRetryCount](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskFailureRetryCount "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskFailureRetryCount")": ***number***,
         "[taskRunStatus](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskRunStatus "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskRunStatus")": "***string***",
         "[taskRunStatusCounts](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskRunStatusCounts "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-taskRunStatusCounts")": { 
            "***string***" : ***number*** 
         },
         "[updatedAt](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-updatedAt "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-updatedAt")": "***string***",
         "[updatedBy](API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-updatedBy "API_JobSearchSummary.md#deadlinecloud-Type-JobSearchSummary-updatedBy")": "***string***"
      }
   ],
   "[nextItemOffset](#deadlinecloud-SearchJobs-response-nextItemOffset "#deadlinecloud-SearchJobs-response-nextItemOffset")": ***number***,
   "[totalResults](#deadlinecloud-SearchJobs-response-totalResults "#deadlinecloud-SearchJobs-response-totalResults")": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[jobs](#API_SearchJobs_ResponseSyntax "#API_SearchJobs_ResponseSyntax")**


The jobs in the search.


Type: Array of [JobSearchSummary](API_JobSearchSummary.md "API_JobSearchSummary.md") objects




**[nextItemOffset](#API_SearchJobs_ResponseSyntax "#API_SearchJobs_ResponseSyntax")**


The next incremental starting point after the defined `itemOffset`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




**[totalResults](#API_SearchJobs_ResponseSyntax "#API_SearchJobs_ResponseSyntax")**


The total number of results in the search.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchJobs")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchJobs")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchJobs")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchJobs")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchJobs")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchJobs")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchJobs")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchJobs")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchJobs")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchJobs "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchJobs")

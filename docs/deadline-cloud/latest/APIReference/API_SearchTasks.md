# SearchTasks

Searches for tasks.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/search/tasks HTTP/1.1
Content-type: application/json

{
   "filterExpressions": { 
      "filters": [ 
         { ... }
      ],
      "operator": "`string`"
   },
   "itemOffset": `number`,
   "jobId": "`string`",
   "pageSize": `number`,
   "queueIds": [ "`string`" ],
   "sortExpressions": [ 
      { ... }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


The farm ID of the task.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[filterExpressions](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


The filter expression, `AND` or `OR`, to use
when searching among a group of search strings in a resource.

You can use two groupings per search each within parenthesis `()`.


Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md "API_SearchGroupedFilterExpressions.md") object


Required: No




**[itemOffset](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


Defines how far into the scrollable list to start the return of results.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.


Required: Yes




**[jobId](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


The job ID for the task search.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: No




**[pageSize](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


Specifies the number of items per page for the resource.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**[queueIds](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


The queue IDs to include in the search.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[sortExpressions](#API_SearchTasks_RequestSyntax "#API_SearchTasks_RequestSyntax")**


The search terms for a resource.


Type: Array of [SearchSortExpression](API_SearchSortExpression.md "API_SearchSortExpression.md") objects


Array Members: Minimum number of 1 item. Maximum number of 5 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "nextItemOffset": ***number***,
   "tasks": [ 
      { 
         "endedAt": "***string***",
         "failureRetryCount": ***number***,
         "jobId": "***string***",
         "parameters": { 
            "***string***" : { ... }
         },
         "queueId": "***string***",
         "runStatus": "***string***",
         "startedAt": "***string***",
         "stepId": "***string***",
         "targetRunStatus": "***string***",
         "taskId": "***string***",
         "updatedAt": "***string***",
         "updatedBy": "***string***"
      }
   ],
   "totalResults": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[nextItemOffset](#API_SearchTasks_ResponseSyntax "#API_SearchTasks_ResponseSyntax")**


The next incremental starting point after the defined `itemOffset`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




**[tasks](#API_SearchTasks_ResponseSyntax "#API_SearchTasks_ResponseSyntax")**


Tasks in the search.


Type: Array of [TaskSearchSummary](API_TaskSearchSummary.md "API_TaskSearchSummary.md") objects




**[totalResults](#API_SearchTasks_ResponseSyntax "#API_SearchTasks_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchTasks")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchTasks")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchTasks")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchTasks")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchTasks")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchTasks")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchTasks")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchTasks")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchTasks")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchTasks "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchTasks")

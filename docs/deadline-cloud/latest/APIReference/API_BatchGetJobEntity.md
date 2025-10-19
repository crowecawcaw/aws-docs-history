# BatchGetJobEntity

Get batched job details for a worker.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers/`workerId`/batchGetJobEntity HTTP/1.1
Content-type: application/json

{
   "identifiers": [ 
      { ... }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_BatchGetJobEntity_RequestSyntax "#API_BatchGetJobEntity_RequestSyntax")**


The farm ID of the worker that's fetching job details. The worker must have an
 assignment on a job to fetch job details.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_BatchGetJobEntity_RequestSyntax "#API_BatchGetJobEntity_RequestSyntax")**


The fleet ID of the worker that's fetching job details. The worker must have an
 assignment on a job to fetch job details.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[workerId](#API_BatchGetJobEntity_RequestSyntax "#API_BatchGetJobEntity_RequestSyntax")**


The worker ID of the worker containing the job details to get.


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[identifiers](#API_BatchGetJobEntity_RequestSyntax "#API_BatchGetJobEntity_RequestSyntax")**


The job identifiers to include within the job entity batch details.


Type: Array of [JobEntityIdentifiersUnion](API_JobEntityIdentifiersUnion.md "API_JobEntityIdentifiersUnion.md") objects


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "entities": [ 
      { ... }
   ],
   "errors": [ 
      { ... }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[entities](#API_BatchGetJobEntity_ResponseSyntax "#API_BatchGetJobEntity_ResponseSyntax")**


A list of the job entities, or details, in the batch.


Type: Array of [JobEntity](API_JobEntity.md "API_JobEntity.md") objects


Array Members: Minimum number of 0 items. Maximum number of 25 items.




**[errors](#API_BatchGetJobEntity_ResponseSyntax "#API_BatchGetJobEntity_ResponseSyntax")**


A list of errors from the job error logs for the batch.


Type: Array of [GetJobEntityError](API_GetJobEntityError.md "API_GetJobEntityError.md") objects




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchGetJobEntity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetJobEntity "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetJobEntity")

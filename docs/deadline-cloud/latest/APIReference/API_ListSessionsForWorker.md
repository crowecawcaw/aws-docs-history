# ListSessionsForWorker

Lists sessions for a worker.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers/`workerId`/sessions?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_ListSessionsForWorker_RequestSyntax "#API_ListSessionsForWorker_RequestSyntax")**


The farm ID for the session.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_ListSessionsForWorker_RequestSyntax "#API_ListSessionsForWorker_RequestSyntax")**


The fleet ID for the session.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[maxResults](#API_ListSessionsForWorker_RequestSyntax "#API_ListSessionsForWorker_RequestSyntax")**


The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.


Valid Range: Minimum value of 1. Maximum value of 100.




**[nextToken](#API_ListSessionsForWorker_RequestSyntax "#API_ListSessionsForWorker_RequestSyntax")**


The token for the next set of results, or `null` to start from the beginning.




**[workerId](#API_ListSessionsForWorker_RequestSyntax "#API_ListSessionsForWorker_RequestSyntax")**


The worker ID for the session.


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "***string***",
   "sessions": [ 
      { 
         "endedAt": "***string***",
         "jobId": "***string***",
         "lifecycleStatus": "***string***",
         "queueId": "***string***",
         "sessionId": "***string***",
         "startedAt": "***string***",
         "targetLifecycleStatus": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[nextToken](#API_ListSessionsForWorker_ResponseSyntax "#API_ListSessionsForWorker_ResponseSyntax")**


The token for the next set of results, or `null` to start from the beginning.


Type: String




**[sessions](#API_ListSessionsForWorker_ResponseSyntax "#API_ListSessionsForWorker_ResponseSyntax")**


The sessions in the response.


Type: Array of [WorkerSessionSummary](API_WorkerSessionSummary.md "API_WorkerSessionSummary.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListSessionsForWorker")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListSessionsForWorker "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListSessionsForWorker")

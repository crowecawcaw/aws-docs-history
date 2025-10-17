# UpdateQueueLimitAssociation

Updates the status of the queue. If you set the status to one of the
 `STOP_LIMIT_USAGE*` values, there will be a delay before the status
 transitions to the `STOPPED` state. 


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/queue-limit-associations/`queueId`/`limitId` HTTP/1.1
Content-type: application/json

{
   "status": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_UpdateQueueLimitAssociation_RequestSyntax "#API_UpdateQueueLimitAssociation_RequestSyntax")**


The unique identifier of the farm that contains the associated queues and limits.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[limitId](#API_UpdateQueueLimitAssociation_RequestSyntax "#API_UpdateQueueLimitAssociation_RequestSyntax")**


The unique identifier of the limit associated to the queue.


Pattern: `limit-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_UpdateQueueLimitAssociation_RequestSyntax "#API_UpdateQueueLimitAssociation_RequestSyntax")**


The unique identifier of the queue associated to the limit.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[status](#API_UpdateQueueLimitAssociation_RequestSyntax "#API_UpdateQueueLimitAssociation_RequestSyntax")**


Sets the status of the limit. You can mark the limit active, or you can stop usage of
 the limit and either complete existing tasks or cancel any existing tasks immediately.
 


Type: String


Valid Values: `ACTIVE | STOP_LIMIT_USAGE_AND_COMPLETE_TASKS | STOP_LIMIT_USAGE_AND_CANCEL_TASKS`



Required: Yes




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueueLimitAssociation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueueLimitAssociation")

# GetQueueLimitAssociation

Gets information about a specific association between a queue and a limit.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queue-limit-associations/`queueId`/`limitId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetQueueLimitAssociation_RequestSyntax "#API_GetQueueLimitAssociation_RequestSyntax")**


The unique identifier of the farm that contains the associated queue and limit.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[limitId](#API_GetQueueLimitAssociation_RequestSyntax "#API_GetQueueLimitAssociation_RequestSyntax")**


The unique identifier of the limit associated with the queue.


Pattern: `limit-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetQueueLimitAssociation_RequestSyntax "#API_GetQueueLimitAssociation_RequestSyntax")**


The unique identifier of the queue associated with the limit.


Pattern: `queue-[0-9a-f]{32}`



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
   "limitId": "***string***",
   "queueId": "***string***",
   "status": "***string***",
   "updatedAt": "***string***",
   "updatedBy": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[createdAt](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The Unix timestamp of the date and time that the association was created.


Type: Timestamp




**[createdBy](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The user identifier of the person that created the association.


Type: String




**[limitId](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The unique identifier of the limit associated with the queue.


Type: String


Pattern: `limit-[0-9a-f]{32}`





**[queueId](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The unique identifier of the queue associated with the limit.


Type: String


Pattern: `queue-[0-9a-f]{32}`





**[status](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The current status of the limit.


Type: String


Valid Values: `ACTIVE | STOP_LIMIT_USAGE_AND_COMPLETE_TASKS | STOP_LIMIT_USAGE_AND_CANCEL_TASKS | STOPPED`





**[updatedAt](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The Unix timestamp of the date and time that the association was last updated.


Type: Timestamp




**[updatedBy](#API_GetQueueLimitAssociation_ResponseSyntax "#API_GetQueueLimitAssociation_ResponseSyntax")**


The user identifier of the person that last updated the association.


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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueueLimitAssociation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueueLimitAssociation "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueueLimitAssociation")

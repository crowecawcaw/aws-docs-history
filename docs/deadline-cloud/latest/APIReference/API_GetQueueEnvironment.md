# GetQueueEnvironment

Gets a queue environment.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/environments/`queueEnvironmentId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetQueueEnvironment_RequestSyntax "#API_GetQueueEnvironment_RequestSyntax")**


The farm ID for the queue environment.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueEnvironmentId](#API_GetQueueEnvironment_RequestSyntax "#API_GetQueueEnvironment_RequestSyntax")**


The queue environment ID.


Pattern: `queueenv-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetQueueEnvironment_RequestSyntax "#API_GetQueueEnvironment_RequestSyntax")**


The queue ID for the queue environment.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[createdAt](#deadlinecloud-GetQueueEnvironment-response-createdAt "#deadlinecloud-GetQueueEnvironment-response-createdAt")": "***string***",
   "[createdBy](#deadlinecloud-GetQueueEnvironment-response-createdBy "#deadlinecloud-GetQueueEnvironment-response-createdBy")": "***string***",
   "[name](#deadlinecloud-GetQueueEnvironment-response-name "#deadlinecloud-GetQueueEnvironment-response-name")": "***string***",
   "[priority](#deadlinecloud-GetQueueEnvironment-response-priority "#deadlinecloud-GetQueueEnvironment-response-priority")": ***number***,
   "[queueEnvironmentId](#deadlinecloud-GetQueueEnvironment-response-queueEnvironmentId "#deadlinecloud-GetQueueEnvironment-response-queueEnvironmentId")": "***string***",
   "[template](#deadlinecloud-GetQueueEnvironment-response-template "#deadlinecloud-GetQueueEnvironment-response-template")": "***string***",
   "[templateType](#deadlinecloud-GetQueueEnvironment-response-templateType "#deadlinecloud-GetQueueEnvironment-response-templateType")": "***string***",
   "[updatedAt](#deadlinecloud-GetQueueEnvironment-response-updatedAt "#deadlinecloud-GetQueueEnvironment-response-updatedAt")": "***string***",
   "[updatedBy](#deadlinecloud-GetQueueEnvironment-response-updatedBy "#deadlinecloud-GetQueueEnvironment-response-updatedBy")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[createdAt](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The user or system that created this resource.>


Type: String




**[name](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The name of the queue environment.


Type: String




**[priority](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The priority of the queue environment.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




**[queueEnvironmentId](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The queue environment ID.


Type: String


Pattern: `queueenv-[0-9a-f]{32}`





**[template](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The template for the queue environment.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 15000.




**[templateType](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The type of template for the queue environment.


Type: String


Valid Values: `JSON | YAML`





**[updatedAt](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetQueueEnvironment_ResponseSyntax "#API_GetQueueEnvironment_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueueEnvironment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueueEnvironment")

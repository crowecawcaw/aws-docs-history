# CreateQueueEnvironment

Creates an environment for a queue that defines how jobs in the queue run.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/queues/`queueId`/environments HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[priority](#deadlinecloud-CreateQueueEnvironment-request-priority "#deadlinecloud-CreateQueueEnvironment-request-priority")": `number`,
   "[template](#deadlinecloud-CreateQueueEnvironment-request-template "#deadlinecloud-CreateQueueEnvironment-request-template")": "`string`",
   "[templateType](#deadlinecloud-CreateQueueEnvironment-request-templateType "#deadlinecloud-CreateQueueEnvironment-request-templateType")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


The farm ID of the farm to connect to the environment.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


The queue ID to connect the queue and environment.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[priority](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


Sets the priority of the environments in the queue from 0 to 10,000, where 0 is the
 highest priority (activated first and deactivated last). If two environments share the same
 priority value, the environment created first takes higher priority.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.


Required: Yes




**[template](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


The environment template to use in the queue.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 15000.


Required: Yes




**[templateType](#API_CreateQueueEnvironment_RequestSyntax "#API_CreateQueueEnvironment_RequestSyntax")**


The template's file type, `JSON` or `YAML`.


Type: String


Valid Values: `JSON | YAML`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[queueEnvironmentId](#deadlinecloud-CreateQueueEnvironment-response-queueEnvironmentId "#deadlinecloud-CreateQueueEnvironment-response-queueEnvironmentId")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[queueEnvironmentId](#API_CreateQueueEnvironment_ResponseSyntax "#API_CreateQueueEnvironment_ResponseSyntax")**


The queue environment ID.


Type: String


Pattern: `queueenv-[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateQueueEnvironment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateQueueEnvironment")

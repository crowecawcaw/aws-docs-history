# UpdateQueueEnvironment

Updates the queue environment.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/queues/`queueId`/environments/`queueEnvironmentId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[priority](#deadlinecloud-UpdateQueueEnvironment-request-priority "#deadlinecloud-UpdateQueueEnvironment-request-priority")": `number`,
   "[template](#deadlinecloud-UpdateQueueEnvironment-request-template "#deadlinecloud-UpdateQueueEnvironment-request-template")": "`string`",
   "[templateType](#deadlinecloud-UpdateQueueEnvironment-request-templateType "#deadlinecloud-UpdateQueueEnvironment-request-templateType")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The farm ID of the queue environment to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueEnvironmentId](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The queue environment ID to update.


Pattern: `queueenv-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The queue ID of the queue environment to update.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[priority](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The priority to update.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.


Required: No




**[template](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The template to update.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 15000.


Required: No




**[templateType](#API_UpdateQueueEnvironment_RequestSyntax "#API_UpdateQueueEnvironment_RequestSyntax")**


The template type to update.


Type: String


Valid Values: `JSON | YAML`



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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueueEnvironment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueueEnvironment "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueueEnvironment")

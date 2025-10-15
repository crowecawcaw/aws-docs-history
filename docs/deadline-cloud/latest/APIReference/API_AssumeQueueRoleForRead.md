# AssumeQueueRoleForRead

Gets AWS credentials from the queue role. The IAM permissions of the credentials are
 scoped down to have read-only access.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/read-roles HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_AssumeQueueRoleForRead_RequestSyntax "#API_AssumeQueueRoleForRead_RequestSyntax")**


The farm ID of the farm containing the queue.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_AssumeQueueRoleForRead_RequestSyntax "#API_AssumeQueueRoleForRead_RequestSyntax")**


The queue ID.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[credentials](#deadlinecloud-AssumeQueueRoleForRead-response-credentials "#deadlinecloud-AssumeQueueRoleForRead-response-credentials")": { 
      "[accessKeyId](API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-accessKeyId "API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-accessKeyId")": "***string***",
      "[expiration](API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-expiration "API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-expiration")": "***string***",
      "[secretAccessKey](API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-secretAccessKey "API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-secretAccessKey")": "***string***",
      "[sessionToken](API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-sessionToken "API_AwsCredentials.md#deadlinecloud-Type-AwsCredentials-sessionToken")": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[credentials](#API_AssumeQueueRoleForRead_ResponseSyntax "#API_AssumeQueueRoleForRead_ResponseSyntax")**


The credentials for the queue role.


Type: [AwsCredentials](API_AwsCredentials.md "API_AwsCredentials.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssumeQueueRoleForRead")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssumeQueueRoleForRead "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssumeQueueRoleForRead")

# CreateLimit

Creates a limit that manages the distribution of shared resources, such as floating
 licenses. A limit can throttle work assignments, help manage workloads, and track current
 usage. Before you use a limit, you must associate the limit with one or more queues. 

You must add the `amountRequirementName` to a step in a job template to
 declare the limit requirement.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/limits HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "amountRequirementName": "`string`",
   "description": "`string`",
   "displayName": "`string`",
   "maxCount": `number`
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


The farm ID of the farm that contains the limit.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[amountRequirementName](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


The value that you specify as the `name` in the `amounts` field of
 the `hostRequirements` in a step of a job template to declare the limit
 requirement.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: Yes




**[description](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


A description of the limit. A description helps you identify the purpose of the
 limit.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


The display name of the limit.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**[maxCount](#API_CreateLimit_RequestSyntax "#API_CreateLimit_RequestSyntax")**


The maximum number of resources constrained by this limit. When all of the resources are
 in use, steps that require the limit won't be scheduled until the resource is
 available.


The `maxCount` must not be 0. If the value is -1, there is no restriction on
 the number of resources that can be acquired for this limit.


Type: Integer


Valid Range: Minimum value of -1. Maximum value of 2147483647.


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "limitId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[limitId](#API_CreateLimit_ResponseSyntax "#API_CreateLimit_ResponseSyntax")**


A unique identifier for the limit. Use this identifier in other operations, such as
 `CreateQueueLimitAssociation` and `DeleteLimit`.


Type: String


Pattern: `limit-[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateLimit")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateLimit")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateLimit")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateLimit")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateLimit")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateLimit")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateLimit")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateLimit")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateLimit")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateLimit "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateLimit")

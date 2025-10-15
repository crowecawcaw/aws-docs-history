# GetLimit

Gets information about a specific limit.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/limits/`limitId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetLimit_RequestSyntax "#API_GetLimit_RequestSyntax")**


The unique identifier of the farm that contains the limit.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[limitId](#API_GetLimit_RequestSyntax "#API_GetLimit_RequestSyntax")**


The unique identifier of the limit to return.


Pattern: `limit-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[amountRequirementName](#deadlinecloud-GetLimit-response-amountRequirementName "#deadlinecloud-GetLimit-response-amountRequirementName")": "***string***",
   "[createdAt](#deadlinecloud-GetLimit-response-createdAt "#deadlinecloud-GetLimit-response-createdAt")": "***string***",
   "[createdBy](#deadlinecloud-GetLimit-response-createdBy "#deadlinecloud-GetLimit-response-createdBy")": "***string***",
   "[currentCount](#deadlinecloud-GetLimit-response-currentCount "#deadlinecloud-GetLimit-response-currentCount")": ***number***,
   "[description](#deadlinecloud-GetLimit-response-description "#deadlinecloud-GetLimit-response-description")": "***string***",
   "[displayName](#deadlinecloud-GetLimit-response-displayName "#deadlinecloud-GetLimit-response-displayName")": "***string***",
   "[farmId](#deadlinecloud-GetLimit-response-farmId "#deadlinecloud-GetLimit-response-farmId")": "***string***",
   "[limitId](#deadlinecloud-GetLimit-response-limitId "#deadlinecloud-GetLimit-response-limitId")": "***string***",
   "[maxCount](#deadlinecloud-GetLimit-response-maxCount "#deadlinecloud-GetLimit-response-maxCount")": ***number***,
   "[updatedAt](#deadlinecloud-GetLimit-response-updatedAt "#deadlinecloud-GetLimit-response-updatedAt")": "***string***",
   "[updatedBy](#deadlinecloud-GetLimit-response-updatedBy "#deadlinecloud-GetLimit-response-updatedBy")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[amountRequirementName](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The value that you specify as the `name` in the `amounts` field of
 the `hostRequirements` in a step of a job template to declare the limit
 requirement.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.




**[createdAt](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The Unix timestamp of the date and time that the limit was created.


Type: Timestamp




**[createdBy](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The user identifier of the person that created the limit.


Type: String




**[currentCount](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The number of resources from the limit that are being used by jobs. The result is
 delayed and may not be the count at the time that you called the operation.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[description](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The description of the limit that helps identify what the limit is used for.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.




**[displayName](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The display name of the limit.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.




**[farmId](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The unique identifier of the farm that contains the limit.


Type: String


Pattern: `farm-[0-9a-f]{32}`





**[limitId](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The unique identifier of the limit.


Type: String


Pattern: `limit-[0-9a-f]{32}`





**[maxCount](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The maximum number of resources constrained by this limit. When all of the resources are
 in use, steps that require the limit won't be scheduled until the resource is
 available.


The `maxValue` must not be 0. If the value is -1, there is no restriction on
 the number of resources that can be acquired for this limit.


Type: Integer


Valid Range: Minimum value of -1. Maximum value of 2147483647.




**[updatedAt](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The Unix timestamp of the date and time that the limit was last updated.


Type: Timestamp




**[updatedBy](#API_GetLimit_ResponseSyntax "#API_GetLimit_ResponseSyntax")**


The user identifier of the person that last updated the limit.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetLimit")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetLimit")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetLimit")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetLimit")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetLimit")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetLimit")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetLimit")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetLimit")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetLimit")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetLimit "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetLimit")

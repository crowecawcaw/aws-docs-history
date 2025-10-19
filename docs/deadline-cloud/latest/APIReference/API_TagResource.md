# TagResource

Tags a resource using the resource's ARN and desired tags.


## Request Syntax



```
POST /2023-10-12/tags/`resourceArn` HTTP/1.1
Content-type: application/json

{
   "tags": { 
      "`string`" : "`string`" 
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[resourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**


The ARN of the resource to apply tags to.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**


Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.


Type: String to string map


Required: No




## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




**ConflictException** 


Your request has conflicting operations. This can occur if you're trying to perform more
 than one operation on the same resource at the same time.





**context** 


Information about the resources in use when the exception was thrown.




**reason** 


A description of the error.




**resourceId** 


The identifier of the resource in use.




**resourceType** 


The type of the resource in use.




HTTP Status Code: 409




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/TagResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/TagResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TagResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/TagResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TagResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/TagResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/TagResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/TagResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/TagResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TagResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TagResource")

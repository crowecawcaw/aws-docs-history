# GetResourcePolicy

Returns information about a resource policy.


## Request Syntax



```
GET /resource-policy/`resourceArn` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[resourceArn](#API_GetResourcePolicy_RequestSyntax "#API_GetResourcePolicy_RequestSyntax")**


The ARN of the resource.


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyDocument": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[PolicyDocument](#API_GetResourcePolicy_ResponseSyntax "#API_GetResourcePolicy_ResponseSyntax")**


The resource policy document.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**InternalServerException** 


The request has failed due to an internal error.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 500




**ThrottlingException** 


The request was denied due to request throttling.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 429




**ValidationException** 


The input fails to satisfy the constraints.





**Fields** 


The fields that caused the error, if applicable.




**Reason** 


The reason for the error.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetResourcePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetResourcePolicy")

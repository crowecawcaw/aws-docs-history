# GetFunction

Gets the code of a CloudFront function. To get configuration information and metadata about
 a function, use `DescribeFunction`.

To get a function's code, you must provide the function's name and stage. To get these
 values, you can use `ListFunctions`.


## Request Syntax



```
GET /2020-05-31/function/`Name`?Stage=`Stage` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Name](#API_GetFunction_RequestSyntax "#API_GetFunction_RequestSyntax")**


The name of the function whose code you are getting.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`



Required: Yes




**[Stage](#API_GetFunction_RequestSyntax "#API_GetFunction_RequestSyntax")**


The function's stage, either `DEVELOPMENT` or `LIVE`.


Valid Values: `DEVELOPMENT | LIVE`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**NoSuchFunctionExists** 


The function does not exist.


HTTP Status Code: 404




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFunction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFunction "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFunction")

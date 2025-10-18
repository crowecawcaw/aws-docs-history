# DeleteKeyValueStore

Specifies the key value store to delete.


## Request Syntax



```
DELETE /2020-05-31/key-value-store/`Name` HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[If-Match](#API_DeleteKeyValueStore_RequestSyntax "#API_DeleteKeyValueStore_RequestSyntax")**


The key value store to delete, if a match occurs.


Required: Yes




**[Name](#API_DeleteKeyValueStore_RequestSyntax "#API_DeleteKeyValueStore_RequestSyntax")**


The name of the key value store.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9-_]{1,64}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**CannotDeleteEntityWhileInUse** 


The entity cannot be deleted while it is in use.


HTTP Status Code: 409




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




**UnsupportedOperation** 


This operation is not supported in this AWS Region.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteKeyValueStore")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteKeyValueStore "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteKeyValueStore")

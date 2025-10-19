# DeleteConnectionGroup

Deletes a connection group.


## Request Syntax



```
DELETE /2020-05-31/connection-group/`Id` HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_DeleteConnectionGroup_RequestSyntax "#API_DeleteConnectionGroup_RequestSyntax")**


The ID of the connection group to delete.


Required: Yes




**[If-Match](#API_DeleteConnectionGroup_RequestSyntax "#API_DeleteConnectionGroup_RequestSyntax")**


The value of the `ETag` header that you received when retrieving the connection group to delete.


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




**ResourceNotDisabled** 


The specified CloudFront resource hasn't been disabled yet.


HTTP Status Code: 409




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteConnectionGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteConnectionGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteConnectionGroup")

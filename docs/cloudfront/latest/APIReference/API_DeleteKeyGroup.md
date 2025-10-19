# DeleteKeyGroup

Deletes a key group.

You cannot delete a key group that is referenced in a cache behavior. First update
 your distributions to remove the key group from all cache behaviors, then delete the key
 group.

To delete a key group, you must provide the key group's identifier and version. To get
 these values, use `ListKeyGroups` followed by `GetKeyGroup` or
 `GetKeyGroupConfig`.


## Request Syntax



```
DELETE /2020-05-31/key-group/`Id` HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_DeleteKeyGroup_RequestSyntax "#API_DeleteKeyGroup_RequestSyntax")**


The identifier of the key group that you are deleting. To get the identifier, use
 `ListKeyGroups`.


Required: Yes




**[If-Match](#API_DeleteKeyGroup_RequestSyntax "#API_DeleteKeyGroup_RequestSyntax")**


The version of the key group that you are deleting. The version is the key group's
 `ETag` value. To get the `ETag`, use `GetKeyGroup`
 or `GetKeyGroupConfig`.




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





**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**NoSuchResource** 


A resource that was specified is not valid.


HTTP Status Code: 404




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




**ResourceInUse** 


Cannot delete this resource because it is in use.


HTTP Status Code: 409




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteKeyGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteKeyGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteKeyGroup")

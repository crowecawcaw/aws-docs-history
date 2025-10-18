# PutKey

Creates a new key-value pair or replaces the value of an existing key.


## Request Syntax



```
PUT /key-value-stores/`KvsARN`/keys/`Key` HTTP/1.1
If-Match: `IfMatch`
Content-type: application/json

{
   "Value": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[IfMatch](#API_kvs_PutKey_RequestSyntax "#API_kvs_PutKey_RequestSyntax")**


The current version (`ETag`) of the key value store that you are putting
 keys into, which you can get by using the `DescribeKeyValueStore` API
 operation.


Required: Yes




**[Key](#API_kvs_PutKey_RequestSyntax "#API_kvs_PutKey_RequestSyntax")**


The key to put.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**[KvsARN](#API_kvs_PutKey_RequestSyntax "#API_kvs_PutKey_RequestSyntax")**


The Amazon Resource Name (ARN) of the key value store.


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Value](#API_kvs_PutKey_RequestSyntax "#API_kvs_PutKey_RequestSyntax")**


The value to put.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
ETag: `ETag`
Content-type: application/json

{
   "ItemCount": ***number***,
   "TotalSizeInBytes": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[ETag](#API_kvs_PutKey_ResponseSyntax "#API_kvs_PutKey_ResponseSyntax")**


The current version identifier of the key value store after the successful
 put.




The following data is returned in JSON format by the service.





**[ItemCount](#API_kvs_PutKey_ResponseSyntax "#API_kvs_PutKey_ResponseSyntax")**


Number of key-value pairs in the key value store after the successful put.


Type: Integer




**[TotalSizeInBytes](#API_kvs_PutKey_ResponseSyntax "#API_kvs_PutKey_ResponseSyntax")**


Total size of the key value store after the successful put, in bytes.


Type: Long




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied.


HTTP Status Code: 403




**ConflictException** 


Resource is not in expected state.


HTTP Status Code: 409




**InternalServerException** 


Internal server error.


HTTP Status Code: 500




**ResourceNotFoundException** 


Resource was not found.


HTTP Status Code: 404




**ServiceQuotaExceededException** 


Limit exceeded.


HTTP Status Code: 402




**ValidationException** 


Validation failed.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/PutKey")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/PutKey "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/PutKey")

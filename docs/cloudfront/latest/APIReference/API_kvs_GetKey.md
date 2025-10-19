# GetKey

Returns a key-value pair.


## Request Syntax



```
GET /key-value-stores/`KvsARN`/keys/`Key` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Key](#API_kvs_GetKey_RequestSyntax "#API_kvs_GetKey_RequestSyntax")**


The key to get.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**[KvsARN](#API_kvs_GetKey_RequestSyntax "#API_kvs_GetKey_RequestSyntax")**


The Amazon Resource Name (ARN) of the key value store.


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "ItemCount": ***number***,
   "Key": "***string***",
   "TotalSizeInBytes": ***number***,
   "Value": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ItemCount](#API_kvs_GetKey_ResponseSyntax "#API_kvs_GetKey_ResponseSyntax")**


Number of key-value pairs in the key value store.


Type: Integer




**[Key](#API_kvs_GetKey_ResponseSyntax "#API_kvs_GetKey_ResponseSyntax")**


The key of the key-value pair.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**[TotalSizeInBytes](#API_kvs_GetKey_ResponseSyntax "#API_kvs_GetKey_ResponseSyntax")**


Total size of the key value store in bytes.


Type: Long




**[Value](#API_kvs_GetKey_ResponseSyntax "#API_kvs_GetKey_ResponseSyntax")**


The value of the key-value pair.


Type: String




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




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/GetKey")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/GetKey "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/GetKey")

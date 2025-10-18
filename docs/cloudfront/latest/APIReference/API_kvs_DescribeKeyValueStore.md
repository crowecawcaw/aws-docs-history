# DescribeKeyValueStore

Returns metadata information about the key value store.


## Request Syntax



```
GET /key-value-stores/`KvsARN` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[KvsARN](#API_kvs_DescribeKeyValueStore_RequestSyntax "#API_kvs_DescribeKeyValueStore_RequestSyntax")**


The Amazon Resource Name (ARN) of the key value store.


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
ETag: `ETag`
Content-type: application/json

{
   "Created": ***number***,
   "FailureReason": "***string***",
   "ItemCount": ***number***,
   "KvsARN": "***string***",
   "LastModified": ***number***,
   "Status": "***string***",
   "TotalSizeInBytes": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[ETag](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


The version identifier for the current version of the key value store.




The following data is returned in JSON format by the service.





**[Created](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


Date and time when the key value store was created.


Type: Timestamp




**[FailureReason](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


The reason why the key value store wasn't created.


Type: String




**[ItemCount](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


Number of key-value pairs in the key value store.


Type: Integer




**[KvsARN](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


The Amazon Resource Name (ARN) of the key value store.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[LastModified](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


Date and time when the key-value pairs in the key value store was last
 modified.


Type: Timestamp




**[Status](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


The current status of the key value store.


Type: String




**[TotalSizeInBytes](#API_kvs_DescribeKeyValueStore_ResponseSyntax "#API_kvs_DescribeKeyValueStore_ResponseSyntax")**


Total size of the key value store in bytes.


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




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/cli2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/boto3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-keyvaluestore-2022-07-26/DescribeKeyValueStore")

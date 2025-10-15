# ListTableBuckets

Lists table buckets for your account. For more information, see [S3 Table buckets](../userguide/s3-tables-buckets.md "../userguide/s3-tables-buckets.md") in the *Amazon Simple Storage Service User Guide*.



Permissions

You must have the `s3tables:ListTableBuckets` permission to use this operation. 




## Request Syntax



```
GET /buckets?continuationToken=`continuationToken`&maxBuckets=`maxBuckets`&prefix=`prefix`&type=`type` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[continuationToken](#API_s3Buckets_ListTableBuckets_RequestSyntax "#API_s3Buckets_ListTableBuckets_RequestSyntax")**



`ContinuationToken` indicates to Amazon S3 that the list is being continued on
 this bucket with a token. `ContinuationToken` is obfuscated and is not a real key.
 You can use this `ContinuationToken` for pagination of the list results.


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[maxBuckets](#API_s3Buckets_ListTableBuckets_RequestSyntax "#API_s3Buckets_ListTableBuckets_RequestSyntax")**


The maximum number of table buckets to return in the list.


Valid Range: Minimum value of 1. Maximum value of 1000.




**[prefix](#API_s3Buckets_ListTableBuckets_RequestSyntax "#API_s3Buckets_ListTableBuckets_RequestSyntax")**


The prefix of the table buckets.


Length Constraints: Minimum length of 1. Maximum length of 63.




**[type](#API_s3Buckets_ListTableBuckets_RequestSyntax "#API_s3Buckets_ListTableBuckets_RequestSyntax")**


The type of table buckets to filter by in the list.


Valid Values: `customer | aws`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[continuationToken](#AmazonS3-s3Buckets_ListTableBuckets-response-continuationToken "#AmazonS3-s3Buckets_ListTableBuckets-response-continuationToken")": "***string***",
   "[tableBuckets](#AmazonS3-s3Buckets_ListTableBuckets-response-tableBuckets "#AmazonS3-s3Buckets_ListTableBuckets-response-tableBuckets")": [ 
      { 
         "[arn](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-arn "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-arn")": "***string***",
         "[createdAt](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-createdAt "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-createdAt")": "***string***",
         "[name](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-name "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-name")": "***string***",
         "[ownerAccountId](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-ownerAccountId "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-ownerAccountId")": "***string***",
         "[tableBucketId](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-tableBucketId "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-tableBucketId")": "***string***",
         "[type](API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-type "API_s3Buckets_TableBucketSummary.md#AmazonS3-Type-s3Buckets_TableBucketSummary-type")": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[continuationToken](#API_s3Buckets_ListTableBuckets_ResponseSyntax "#API_s3Buckets_ListTableBuckets_ResponseSyntax")**


You can use this `ContinuationToken` for pagination of the list results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[tableBuckets](#API_s3Buckets_ListTableBuckets_ResponseSyntax "#API_s3Buckets_ListTableBuckets_ResponseSyntax")**


A list of table buckets.


Type: Array of [TableBucketSummary](API_s3Buckets_TableBucketSummary.md "API_s3Buckets_TableBucketSummary.md") objects




## Errors





**AccessDeniedException** 


The action cannot be performed because you do not have the required permission.


HTTP Status Code: 403




**BadRequestException** 


The request is invalid or malformed.


HTTP Status Code: 400




**ConflictException** 


The request failed because there is a conflict with a previous write. You can retry the
 request.


HTTP Status Code: 409




**ForbiddenException** 


The caller isn't authorized to make the request.


HTTP Status Code: 403




**InternalServerErrorException** 


The request failed due to an internal server error.


HTTP Status Code: 500




**NotFoundException** 


The request was rejected because the specified resource could not be found.


HTTP Status Code: 404




**TooManyRequestsException** 


The limit on the number of requests per second was exceeded.


HTTP Status Code: 429




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListTableBuckets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListTableBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListTableBuckets")

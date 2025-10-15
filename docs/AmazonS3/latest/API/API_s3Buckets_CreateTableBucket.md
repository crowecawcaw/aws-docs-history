# CreateTableBucket

Creates a table bucket. For more information, see [Creating a table bucket](../userguide/s3-tables-buckets-create.md "../userguide/s3-tables-buckets-create.md") in the *Amazon Simple Storage Service User Guide*.



Permissions


* You must have the `s3tables:CreateTableBucket` permission to use this operation.
* If you use this operation with the optional `encryptionConfiguration` parameter you must have the `s3tables:PutTableBucketEncryption` permission.



## Request Syntax



```
PUT /buckets HTTP/1.1
Content-type: application/json

{
   "[encryptionConfiguration](#AmazonS3-s3Buckets_CreateTableBucket-request-encryptionConfiguration "#AmazonS3-s3Buckets_CreateTableBucket-request-encryptionConfiguration")": { 
      "[kmsKeyArn](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn")": "`string`",
      "[sseAlgorithm](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm")": "`string`"
   },
   "[name](#AmazonS3-s3Buckets_CreateTableBucket-request-name "#AmazonS3-s3Buckets_CreateTableBucket-request-name")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[encryptionConfiguration](#API_s3Buckets_CreateTableBucket_RequestSyntax "#API_s3Buckets_CreateTableBucket_RequestSyntax")**


The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.


Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md "API_s3Buckets_EncryptionConfiguration.md") object


Required: No




**[name](#API_s3Buckets_CreateTableBucket_RequestSyntax "#API_s3Buckets_CreateTableBucket_RequestSyntax")**


The name for the table bucket.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Pattern: `[0-9a-z-]*`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[arn](#AmazonS3-s3Buckets_CreateTableBucket-response-arn "#AmazonS3-s3Buckets_CreateTableBucket-response-arn")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[arn](#API_s3Buckets_CreateTableBucket_ResponseSyntax "#API_s3Buckets_CreateTableBucket_ResponseSyntax")**


The Amazon Resource Name (ARN) of the table bucket.


Type: String


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`





## Errors





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateTableBucket")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateTableBucket "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateTableBucket")

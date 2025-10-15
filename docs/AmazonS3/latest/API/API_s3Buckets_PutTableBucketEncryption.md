# PutTableBucketEncryption

Sets the encryption configuration for a table bucket.



Permissions

You must have the `s3tables:PutTableBucketEncryption` permission to use this operation.


###### Note

If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](../userguide/s3-tables-kms-permissions.md "../userguide/s3-tables-kms-permissions.md") in the *Amazon Simple Storage Service User Guide*.




## Request Syntax



```
PUT /buckets/`tableBucketARN`/encryption HTTP/1.1
Content-type: application/json

{
   "[encryptionConfiguration](#AmazonS3-s3Buckets_PutTableBucketEncryption-request-encryptionConfiguration "#AmazonS3-s3Buckets_PutTableBucketEncryption-request-encryptionConfiguration")": { 
      "[kmsKeyArn](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn")": "`string`",
      "[sseAlgorithm](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm")": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[tableBucketARN](#API_s3Buckets_PutTableBucketEncryption_RequestSyntax "#API_s3Buckets_PutTableBucketEncryption_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[encryptionConfiguration](#API_s3Buckets_PutTableBucketEncryption_RequestSyntax "#API_s3Buckets_PutTableBucketEncryption_RequestSyntax")**


The encryption configuration to apply to the table bucket.


Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md "API_s3Buckets_EncryptionConfiguration.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketEncryption")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketEncryption "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketEncryption")

# GetTableEncryption

Gets the encryption configuration for a table.



Permissions

You must have the `s3tables:GetTableEncryption` permission to use this operation.




## Request Syntax



```
GET /tables/`tableBucketARN`/`namespace`/`name`/encryption HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_s3Buckets_GetTableEncryption_RequestSyntax "#API_s3Buckets_GetTableEncryption_RequestSyntax")**


The name of the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[namespace](#API_s3Buckets_GetTableEncryption_RequestSyntax "#API_s3Buckets_GetTableEncryption_RequestSyntax")**


The namespace associated with the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_GetTableEncryption_RequestSyntax "#API_s3Buckets_GetTableEncryption_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket containing the table.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[encryptionConfiguration](#AmazonS3-s3Buckets_GetTableEncryption-response-encryptionConfiguration "#AmazonS3-s3Buckets_GetTableEncryption-response-encryptionConfiguration")": { 
      "[kmsKeyArn](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn")": "***string***",
      "[sseAlgorithm](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm")": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[encryptionConfiguration](#API_s3Buckets_GetTableEncryption_ResponseSyntax "#API_s3Buckets_GetTableEncryption_ResponseSyntax")**


The encryption configuration for the table.


Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md "API_s3Buckets_EncryptionConfiguration.md") object




## Errors





**AccessDeniedException** 


The action cannot be performed because you do not have the required permission.


HTTP Status Code: 403




**BadRequestException** 


The request is invalid or malformed.


HTTP Status Code: 400




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableEncryption")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableEncryption "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableEncryption")

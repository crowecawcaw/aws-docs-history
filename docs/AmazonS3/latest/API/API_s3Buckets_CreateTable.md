# CreateTable

Creates a new table associated with the given namespace in a table bucket. For more information, see [Creating an Amazon S3 table](../userguide/s3-tables-create.md "../userguide/s3-tables-create.md") in the *Amazon Simple Storage Service User Guide*.



Permissions


* You must have the `s3tables:CreateTable` permission to use this operation.
* If you use this operation with the optional `metadata` request parameter you must have the `s3tables:PutTableData` permission.
* If you use this operation with the optional `encryptionConfiguration` request parameter you must have the `s3tables:PutTableEncryption` permission.

###### Note

Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](../userguide/s3-tables-kms-permissions.md "../userguide/s3-tables-kms-permissions.md"). 




## Request Syntax



```
PUT /tables/`tableBucketARN`/`namespace` HTTP/1.1
Content-type: application/json

{
   "[encryptionConfiguration](#AmazonS3-s3Buckets_CreateTable-request-encryptionConfiguration "#AmazonS3-s3Buckets_CreateTable-request-encryptionConfiguration")": { 
      "[kmsKeyArn](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-kmsKeyArn")": "`string`",
      "[sseAlgorithm](API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm "API_s3Buckets_EncryptionConfiguration.md#AmazonS3-Type-s3Buckets_EncryptionConfiguration-sseAlgorithm")": "`string`"
   },
   "[format](#AmazonS3-s3Buckets_CreateTable-request-format "#AmazonS3-s3Buckets_CreateTable-request-format")": "`string`",
   "[metadata](#AmazonS3-s3Buckets_CreateTable-request-metadata "#AmazonS3-s3Buckets_CreateTable-request-metadata")": { ... },
   "[name](#AmazonS3-s3Buckets_CreateTable-request-name "#AmazonS3-s3Buckets_CreateTable-request-name")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[namespace](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The namespace to associated with the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket to create the table in.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[encryptionConfiguration](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. 


###### Note

If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](../userguide/s3-tables-kms-permissions.md "../userguide/s3-tables-kms-permissions.md").


Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md "API_s3Buckets_EncryptionConfiguration.md") object


Required: No




**[format](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The format for the table.


Type: String


Valid Values: `ICEBERG`



Required: Yes




**[metadata](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The metadata for the table.


Type: [TableMetadata](API_s3Buckets_TableMetadata.md "API_s3Buckets_TableMetadata.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**[name](#API_s3Buckets_CreateTable_RequestSyntax "#API_s3Buckets_CreateTable_RequestSyntax")**


The name for the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[tableARN](#AmazonS3-s3Buckets_CreateTable-response-tableARN "#AmazonS3-s3Buckets_CreateTable-response-tableARN")": "***string***",
   "[versionToken](#AmazonS3-s3Buckets_CreateTable-response-versionToken "#AmazonS3-s3Buckets_CreateTable-response-versionToken")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[tableARN](#API_s3Buckets_CreateTable_ResponseSyntax "#API_s3Buckets_CreateTable_ResponseSyntax")**


The Amazon Resource Name (ARN) of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`





**[versionToken](#API_s3Buckets_CreateTable_ResponseSyntax "#API_s3Buckets_CreateTable_ResponseSyntax")**


The version token of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateTable")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/CreateTable")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateTable")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateTable")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateTable")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateTable")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateTable")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateTable")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateTable")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateTable "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateTable")

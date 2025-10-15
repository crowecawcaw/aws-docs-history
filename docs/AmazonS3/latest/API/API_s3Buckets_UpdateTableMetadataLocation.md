# UpdateTableMetadataLocation

Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with `.metadata.json`, or if the metadata file is Gzip-compressed, `.metadata.json.gz`.



Permissions

You must have the `s3tables:UpdateTableMetadataLocation` permission to use this operation. 




## Request Syntax



```
PUT /tables/`tableBucketARN`/`namespace`/`name`/metadata-location HTTP/1.1
Content-type: application/json

{
   "[metadataLocation](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-request-metadataLocation "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-request-metadataLocation")": "`string`",
   "[versionToken](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-request-versionToken "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-request-versionToken")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax "#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax")**


The name of the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[namespace](#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax "#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax")**


The namespace of the table.


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`



Required: Yes




**[tableBucketARN](#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax "#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax")**


The Amazon Resource Name (ARN) of the table bucket. 


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[metadataLocation](#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax "#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax")**


The new metadata location for the table. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




**[versionToken](#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax "#API_s3Buckets_UpdateTableMetadataLocation_RequestSyntax")**


The version token of the table. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[metadataLocation](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-metadataLocation "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-metadataLocation")": "***string***",
   "[name](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-name "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-name")": "***string***",
   "[namespace](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-namespace "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-namespace")": [ "***string***" ],
   "[tableARN](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-tableARN "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-tableARN")": "***string***",
   "[versionToken](#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-versionToken "#AmazonS3-s3Buckets_UpdateTableMetadataLocation-response-versionToken")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[metadataLocation](#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax "#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax")**


The metadata location of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.




**[name](#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax "#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax")**


The name of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`





**[namespace](#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax "#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax")**


The namespace the table is associated with.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[0-9a-z_]*`





**[tableARN](#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax "#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax")**


The Amazon Resource Name (ARN) of the table.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`





**[versionToken](#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax "#API_s3Buckets_UpdateTableMetadataLocation_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/UpdateTableMetadataLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/UpdateTableMetadataLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/UpdateTableMetadataLocation")

# GetVectors

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

Returns vector attributes. To specify the vector index, you can either use both the
 vector bucket name and the vector index name, or use the vector index Amazon Resource Name
 (ARN). 



Permissions

You must have the `s3vectors:GetVectors` permission to use this
 operation. 




## Request Syntax



```
POST /GetVectors HTTP/1.1
Content-type: application/json

{
   "[indexArn](#AmazonS3-S3VectorBuckets_GetVectors-request-indexArn "#AmazonS3-S3VectorBuckets_GetVectors-request-indexArn")": "`string`",
   "[indexName](#AmazonS3-S3VectorBuckets_GetVectors-request-indexName "#AmazonS3-S3VectorBuckets_GetVectors-request-indexName")": "`string`",
   "[keys](#AmazonS3-S3VectorBuckets_GetVectors-request-keys "#AmazonS3-S3VectorBuckets_GetVectors-request-keys")": [ "`string`" ],
   "[returnData](#AmazonS3-S3VectorBuckets_GetVectors-request-returnData "#AmazonS3-S3VectorBuckets_GetVectors-request-returnData")": `boolean`,
   "[returnMetadata](#AmazonS3-S3VectorBuckets_GetVectors-request-returnMetadata "#AmazonS3-S3VectorBuckets_GetVectors-request-returnMetadata")": `boolean`,
   "[vectorBucketName](#AmazonS3-S3VectorBuckets_GetVectors-request-vectorBucketName "#AmazonS3-S3VectorBuckets_GetVectors-request-vectorBucketName")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[indexArn](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


The ARN of the vector index.


Type: String


Required: No




**[indexName](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


The name of the vector index.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




**[keys](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


The names of the vectors you want to return attributes for. 


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 100 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**[returnData](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


Indicates whether to include the vector data in the response. The default value is
 `false`.


Type: Boolean


Required: No




**[returnMetadata](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


Indicates whether to include metadata in the response. The default value is
 `false`.


Type: Boolean


Required: No




**[vectorBucketName](#API_S3VectorBuckets_GetVectors_RequestSyntax "#API_S3VectorBuckets_GetVectors_RequestSyntax")**


The name of the vector bucket that contains the vector index. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[vectors](#AmazonS3-S3VectorBuckets_GetVectors-response-vectors "#AmazonS3-S3VectorBuckets_GetVectors-response-vectors")": [ 
      { 
         "[data](API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-data "API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-data")": { ... },
         "[key](API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-key "API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-key")": "***string***",
         "[metadata](API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-metadata "API_S3VectorBuckets_GetOutputVector.md#AmazonS3-Type-S3VectorBuckets_GetOutputVector-metadata")": ***JSON value***
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[vectors](#API_S3VectorBuckets_GetVectors_ResponseSyntax "#API_S3VectorBuckets_GetVectors_ResponseSyntax")**


The attributes of the vectors.


Type: Array of [GetOutputVector](API_S3VectorBuckets_GetOutputVector.md "API_S3VectorBuckets_GetOutputVector.md") objects




## Errors





**AccessDeniedException** 


Access denied.


HTTP Status Code: 403




**InternalServerException** 


The request failed due to an internal server error.


HTTP Status Code: 500




**KmsDisabledException** 


The specified AWS KMS key isn't enabled.


HTTP Status Code: 400




**KmsInvalidKeyUsageException** 


The request was rejected for one of the following reasons: 



* The `KeyUsage` value of the KMS key is incompatible with the API
 operation.
* The encryption algorithm or signing algorithm specified for the operation is
 incompatible with the type of key material in the KMS key
 (`KeySpec`).

For more information, see [InvalidKeyUsageException](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors "https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors") in the *AWS Key Management Service API
 Reference*.


HTTP Status Code: 400




**KmsInvalidStateException** 


The key state of the KMS key isn't compatible with the operation.


For more information, see [KMSInvalidStateException](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors "https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html#API_Encrypt_Errors") in the *AWS Key Management Service API
 Reference*.


HTTP Status Code: 400




**KmsNotFoundException** 


The KMS key can't be found.


HTTP Status Code: 400




**NotFoundException** 


The request was rejected because the specified resource can't be found.


HTTP Status Code: 404




**ServiceQuotaExceededException** 


Your request exceeds a service quota. 


HTTP Status Code: 402




**ServiceUnavailableException** 


The service is unavailable. Wait briefly and retry your request. If it continues to
 fail, increase your waiting time between retries.


HTTP Status Code: 503




**TooManyRequestsException** 


The request was denied due to request throttling.


HTTP Status Code: 429




**ValidationException** 


The requested action isn't valid.





**fieldList** 


A list of specific validation failures that are encountered during input processing. Each entry
 in the list contains a path to the field that failed validation and a detailed message that 
 explains why the validation failed. To satisfy multiple constraints, a field can appear multiple times in this list if it
 failed. You can use the information to identify and fix
 the specific validation issues in your request.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/GetVectors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/GetVectors "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/GetVectors")

# QueryVectors

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

Performs an approximate nearest neighbor search query in a vector index using a query
 vector. By default, it returns the keys of approximate nearest neighbors. You can
 optionally include the computed distance (between the query vector and each vector in the
 response), the vector data, and metadata of each vector in the response. 

To specify the vector index, you can either use both the vector bucket name and the
 vector index name, or use the vector index Amazon Resource Name (ARN). 



Permissions

You must have the `s3vectors:QueryVectors` permission to use this
 operation. Additional permissions are required based on the request parameters you
 specify:



* With only `s3vectors:QueryVectors` permission, you can
 retrieve vector keys of approximate nearest neighbors and computed distances
 between these vectors. This permission is sufficient only when you don't set
 any metadata filters and don't request vector data or metadata (by keeping the 
 `returnMetadata` parameter set to
 `false` or not specified).
* If you specify a metadata filter or set 
 `returnMetadata` to true, you must have both
 `s3vectors:QueryVectors` and `s3vectors:GetVectors`
 permissions. The request fails with a `403 Forbidden error` if
 you request metadata filtering, vector data, or metadata without the
 `s3vectors:GetVectors` permission.



## Request Syntax



```
POST /QueryVectors HTTP/1.1
Content-type: application/json

{
   "[filter](#AmazonS3-S3VectorBuckets_QueryVectors-request-filter "#AmazonS3-S3VectorBuckets_QueryVectors-request-filter")": `JSON value`,
   "[indexArn](#AmazonS3-S3VectorBuckets_QueryVectors-request-indexArn "#AmazonS3-S3VectorBuckets_QueryVectors-request-indexArn")": "`string`",
   "[indexName](#AmazonS3-S3VectorBuckets_QueryVectors-request-indexName "#AmazonS3-S3VectorBuckets_QueryVectors-request-indexName")": "`string`",
   "[queryVector](#AmazonS3-S3VectorBuckets_QueryVectors-request-queryVector "#AmazonS3-S3VectorBuckets_QueryVectors-request-queryVector")": { ... },
   "[returnDistance](#AmazonS3-S3VectorBuckets_QueryVectors-request-returnDistance "#AmazonS3-S3VectorBuckets_QueryVectors-request-returnDistance")": `boolean`,
   "[returnMetadata](#AmazonS3-S3VectorBuckets_QueryVectors-request-returnMetadata "#AmazonS3-S3VectorBuckets_QueryVectors-request-returnMetadata")": `boolean`,
   "[topK](#AmazonS3-S3VectorBuckets_QueryVectors-request-topK "#AmazonS3-S3VectorBuckets_QueryVectors-request-topK")": `number`,
   "[vectorBucketName](#AmazonS3-S3VectorBuckets_QueryVectors-request-vectorBucketName "#AmazonS3-S3VectorBuckets_QueryVectors-request-vectorBucketName")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[filter](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


Metadata filter to apply during the query. For more information about metadata keys, see
 [Metadata
 filtering](../userguide/s3-vectors-metadata-filtering.md "../userguide/s3-vectors-metadata-filtering.md") in the *Amazon S3 User Guide*. 


Type: JSON value


Required: No




**[indexArn](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


The ARN of the vector index that you want to query.


Type: String


Required: No




**[indexName](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


The name of the vector index that you want to query. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




**[queryVector](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


The query vector. Ensure that the query vector has the same dimension as the dimension
 of the vector index that's being queried. For example, if your vector index contains
 vectors with 384 dimensions, your query vector must also have 384 dimensions.
 


Type: [VectorData](API_S3VectorBuckets_VectorData.md "API_S3VectorBuckets_VectorData.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**[returnDistance](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


Indicates whether to include the computed distance in the response. The default value is
 `false`.


Type: Boolean


Required: No




**[returnMetadata](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


Indicates whether to include metadata in the response. The default value is
 `false`.


Type: Boolean


Required: No




**[topK](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


The number of results to return for each query.


Type: Integer


Valid Range: Minimum value of 1.


Required: Yes




**[vectorBucketName](#API_S3VectorBuckets_QueryVectors_RequestSyntax "#API_S3VectorBuckets_QueryVectors_RequestSyntax")**


The name of the vector bucket that contains the vector index. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[vectors](#AmazonS3-S3VectorBuckets_QueryVectors-response-vectors "#AmazonS3-S3VectorBuckets_QueryVectors-response-vectors")": [ 
      { 
         "[data](API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-data "API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-data")": { ... },
         "[distance](API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-distance "API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-distance")": ***number***,
         "[key](API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-key "API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-key")": "***string***",
         "[metadata](API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-metadata "API_S3VectorBuckets_QueryOutputVector.md#AmazonS3-Type-S3VectorBuckets_QueryOutputVector-metadata")": ***JSON value***
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[vectors](#API_S3VectorBuckets_QueryVectors_ResponseSyntax "#API_S3VectorBuckets_QueryVectors_ResponseSyntax")**


The vectors in the approximate nearest neighbor search.


Type: Array of [QueryOutputVector](API_S3VectorBuckets_QueryOutputVector.md "API_S3VectorBuckets_QueryOutputVector.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/QueryVectors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryVectors "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryVectors")

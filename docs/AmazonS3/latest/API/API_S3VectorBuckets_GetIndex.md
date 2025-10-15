# GetIndex

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

Returns vector index attributes. To specify the vector index, you can either use both
 the vector bucket name and the vector index name, or use the vector index Amazon Resource
 Name (ARN). 



Permissions

You must have the `s3vectors:GetIndex` permission to use this
 operation. 




## Request Syntax



```
POST /GetIndex HTTP/1.1
Content-type: application/json

{
   "[indexArn](#AmazonS3-S3VectorBuckets_GetIndex-request-indexArn "#AmazonS3-S3VectorBuckets_GetIndex-request-indexArn")": "`string`",
   "[indexName](#AmazonS3-S3VectorBuckets_GetIndex-request-indexName "#AmazonS3-S3VectorBuckets_GetIndex-request-indexName")": "`string`",
   "[vectorBucketName](#AmazonS3-S3VectorBuckets_GetIndex-request-vectorBucketName "#AmazonS3-S3VectorBuckets_GetIndex-request-vectorBucketName")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[indexArn](#API_S3VectorBuckets_GetIndex_RequestSyntax "#API_S3VectorBuckets_GetIndex_RequestSyntax")**


The ARN of the vector index.


Type: String


Required: No




**[indexName](#API_S3VectorBuckets_GetIndex_RequestSyntax "#API_S3VectorBuckets_GetIndex_RequestSyntax")**


The name of the vector index.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




**[vectorBucketName](#API_S3VectorBuckets_GetIndex_RequestSyntax "#API_S3VectorBuckets_GetIndex_RequestSyntax")**


The name of the vector bucket that contains the vector index. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[index](#AmazonS3-S3VectorBuckets_GetIndex-response-index "#AmazonS3-S3VectorBuckets_GetIndex-response-index")": { 
      "[creationTime](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-creationTime "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-creationTime")": ***number***,
      "[dataType](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-dataType "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-dataType")": "***string***",
      "[dimension](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-dimension "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-dimension")": ***number***,
      "[distanceMetric](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-distanceMetric "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-distanceMetric")": "***string***",
      "[indexArn](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-indexArn "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-indexArn")": "***string***",
      "[indexName](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-indexName "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-indexName")": "***string***",
      "[metadataConfiguration](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-metadataConfiguration "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-metadataConfiguration")": { 
         "[nonFilterableMetadataKeys](API_S3VectorBuckets_MetadataConfiguration.md#AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-nonFilterableMetadataKeys "API_S3VectorBuckets_MetadataConfiguration.md#AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-nonFilterableMetadataKeys")": [ "***string***" ]
      },
      "[vectorBucketName](API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-vectorBucketName "API_S3VectorBuckets_Index.md#AmazonS3-Type-S3VectorBuckets_Index-vectorBucketName")": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[index](#API_S3VectorBuckets_GetIndex_ResponseSyntax "#API_S3VectorBuckets_GetIndex_ResponseSyntax")**


The attributes of the vector index.


Type: [Index](API_S3VectorBuckets_Index.md "API_S3VectorBuckets_Index.md") object




## Errors





**AccessDeniedException** 


Access denied.


HTTP Status Code: 403




**InternalServerException** 


The request failed due to an internal server error.


HTTP Status Code: 500




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/GetIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/GetIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/GetIndex")

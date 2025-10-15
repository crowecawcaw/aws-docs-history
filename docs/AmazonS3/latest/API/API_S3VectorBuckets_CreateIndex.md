# CreateIndex

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

Creates a vector index within a vector bucket. To specify the vector bucket, you must
 use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).



Permissions

You must have the `s3vectors:CreateIndex` permission to use this
 operation. 




## Request Syntax



```
POST /CreateIndex HTTP/1.1
Content-type: application/json

{
   "[dataType](#AmazonS3-S3VectorBuckets_CreateIndex-request-dataType "#AmazonS3-S3VectorBuckets_CreateIndex-request-dataType")": "`string`",
   "[dimension](#AmazonS3-S3VectorBuckets_CreateIndex-request-dimension "#AmazonS3-S3VectorBuckets_CreateIndex-request-dimension")": `number`,
   "[distanceMetric](#AmazonS3-S3VectorBuckets_CreateIndex-request-distanceMetric "#AmazonS3-S3VectorBuckets_CreateIndex-request-distanceMetric")": "`string`",
   "[indexName](#AmazonS3-S3VectorBuckets_CreateIndex-request-indexName "#AmazonS3-S3VectorBuckets_CreateIndex-request-indexName")": "`string`",
   "[metadataConfiguration](#AmazonS3-S3VectorBuckets_CreateIndex-request-metadataConfiguration "#AmazonS3-S3VectorBuckets_CreateIndex-request-metadataConfiguration")": { 
      "[nonFilterableMetadataKeys](API_S3VectorBuckets_MetadataConfiguration.md#AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-nonFilterableMetadataKeys "API_S3VectorBuckets_MetadataConfiguration.md#AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-nonFilterableMetadataKeys")": [ "`string`" ]
   },
   "[vectorBucketArn](#AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketArn "#AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketArn")": "`string`",
   "[vectorBucketName](#AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketName "#AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketName")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[dataType](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The data type of the vectors to be inserted into the vector index. 


Type: String


Valid Values: `float32`



Required: Yes




**[dimension](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The dimensions of the vectors to be inserted into the vector index. 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 4096.


Required: Yes




**[distanceMetric](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The distance metric to be used for similarity search. 


Type: String


Valid Values: `euclidean | cosine`



Required: Yes




**[indexName](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The name of the vector index to create. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: Yes




**[metadataConfiguration](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The metadata configuration for the vector index. 


Type: [MetadataConfiguration](API_S3VectorBuckets_MetadataConfiguration.md "API_S3VectorBuckets_MetadataConfiguration.md") object


Required: No




**[vectorBucketArn](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The Amazon Resource Name (ARN) of the vector bucket to create the vector index
 in.


Type: String


Required: No




**[vectorBucketName](#API_S3VectorBuckets_CreateIndex_RequestSyntax "#API_S3VectorBuckets_CreateIndex_RequestSyntax")**


The name of the vector bucket to create the vector index in. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors





**AccessDeniedException** 


Access denied.


HTTP Status Code: 403




**ConflictException** 


The request failed because a vector bucket name or a vector index name already exists.
 Vector bucket names must be unique within your AWS account for each AWS Region. Vector
 index names must be unique within your vector bucket. Choose a different vector bucket name
 or vector index name, and try again.


HTTP Status Code: 409




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/CreateIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/CreateIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/CreateIndex")

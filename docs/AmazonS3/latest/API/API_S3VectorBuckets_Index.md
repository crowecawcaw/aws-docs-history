# Index

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

The attributes of a vector index.


## Contents





**creationTime** 


Date and time when the vector index was created. 


Type: Timestamp


Required: Yes




**dataType** 


The data type of the vectors inserted into the vector index. 


Type: String


Valid Values: `float32`



Required: Yes




**dimension** 


The number of values in the vectors that are inserted into the vector index. 


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 4096.


Required: Yes




**distanceMetric** 


The distance metric to be used for similarity search. 


Type: String


Valid Values: `euclidean | cosine`



Required: Yes




**indexArn** 


The Amazon Resource Name (ARN) of the vector index.


Type: String


Required: Yes




**indexName** 


The name of the vector index.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: Yes




**vectorBucketName** 


The name of the vector bucket that contains the vector index. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 63.


Required: Yes




**metadataConfiguration** 


The metadata configuration for the vector index. 


Type: [MetadataConfiguration](API_S3VectorBuckets_MetadataConfiguration.md "API_S3VectorBuckets_MetadataConfiguration.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/Index "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/Index")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/Index "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/Index")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/Index "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/Index")

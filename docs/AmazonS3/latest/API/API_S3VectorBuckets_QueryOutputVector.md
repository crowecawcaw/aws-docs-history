# QueryOutputVector

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

The attributes of a vector in the approximate nearest neighbor search.


## Contents





**key** 


The key of the vector in the approximate nearest neighbor search.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**data** 


The vector data associated with the vector, if requested. 


Type: [VectorData](API_S3VectorBuckets_VectorData.md "API_S3VectorBuckets_VectorData.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**distance** 


The measure of similarity between the vector in the response and the query
 vector.


Type: Float


Required: No




**metadata** 


The metadata associated with the vector, if requested.


Type: JSON value


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryOutputVector "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryOutputVector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryOutputVector "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryOutputVector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryOutputVector "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryOutputVector")

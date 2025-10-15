# ListOutputVector

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

The attributes of a vector returned by the `ListVectors` operation.


## Contents





**key** 


The name of the vector. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**data** 


The vector data of the vector. 


Type: [VectorData](API_S3VectorBuckets_VectorData.md "API_S3VectorBuckets_VectorData.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**metadata** 


Metadata about the vector. 


Type: JSON value


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/ListOutputVector "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/ListOutputVector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/ListOutputVector "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/ListOutputVector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/ListOutputVector "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/ListOutputVector")

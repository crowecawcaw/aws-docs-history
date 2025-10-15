# MetadataConfiguration

###### Note

Amazon S3 Vectors is in preview release for Amazon S3 and is subject to change.

The metadata configuration for a vector index.


## Contents





**nonFilterableMetadataKeys** 


Non-filterable metadata keys allow you to enrich vectors with additional context during
 storage and retrieval. Unlike default metadata keys, these keys can’t be used as query
 filters. Non-filterable metadata keys can be retrieved but can’t be searched, queried, or
 filtered. You can access non-filterable metadata keys of your vectors after finding the
 vectors. For more information about non-filterable metadata keys, see [Vectors](../userguide/s3-vectors-vectors.md "../userguide/s3-vectors-vectors.md") and [Limitations and
 restrictions](../userguide/s3-vectors-limitations.md "../userguide/s3-vectors-limitations.md") in the *Amazon S3 User Guide*. 


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Length Constraints: Minimum length of 1. Maximum length of 63.


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/MetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/MetadataConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/MetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/MetadataConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/MetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/MetadataConfiguration")

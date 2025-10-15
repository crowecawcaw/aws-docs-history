# BucketInfo

Specifies the information about the bucket that will be created. For more information about
 directory buckets, see [Directory buckets](../userguide/directory-buckets-overview.md "../userguide/directory-buckets-overview.md") in the
 *Amazon S3 User Guide*.

###### Note

This functionality is only supported by directory buckets.


## Contents





**DataRedundancy** 


The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.


Type: String


Valid Values: `SingleAvailabilityZone | SingleLocalZone`



Required: No




**Type** 


The type of bucket.


Type: String


Valid Values: `Directory`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/BucketInfo "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/BucketInfo")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/BucketInfo "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/BucketInfo")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/BucketInfo "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/BucketInfo")

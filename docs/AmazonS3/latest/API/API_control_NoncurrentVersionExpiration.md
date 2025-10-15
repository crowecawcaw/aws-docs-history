# NoncurrentVersionExpiration

The container of the noncurrent version expiration.


## Contents





**NewerNoncurrentVersions** 


Specifies how many noncurrent versions S3 on Outposts will retain. If there are this many
 more recent noncurrent versions, S3 on Outposts will take the associated action. For more
 information about noncurrent versions, see [Lifecycle configuration
 elements](../userguide/intro-lifecycle-rules.md "../userguide/intro-lifecycle-rules.md") in the *Amazon S3 User Guide*.


Type: Integer


Required: No




**NoncurrentDays** 


Specifies the number of days an object is noncurrent before Amazon S3 can perform the
 associated action. For information about the noncurrent days calculations, see [How
 Amazon S3 Calculates When an Object Became Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations") in the
 *Amazon S3 User Guide*.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionExpiration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionExpiration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionExpiration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionExpiration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionExpiration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionExpiration")

# NoncurrentVersionTransition

Container for the transition rule that describes when noncurrent objects transition to the
 `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`,
 `GLACIER_IR`, `GLACIER`, or `DEEP_ARCHIVE` storage class. If your
 bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3
 transition noncurrent object versions to the `STANDARD_IA`, `ONEZONE_IA`,
 `INTELLIGENT_TIERING`, `GLACIER_IR`, `GLACIER`, or
 `DEEP_ARCHIVE` storage class at a specific period in the object's lifetime.


## Contents





**NewerNoncurrentVersions** 


Specifies how many noncurrent versions Amazon S3 will retain in the same storage class before
 transitioning objects. You can specify up to 100 noncurrent versions to retain. Amazon S3 will transition any
 additional noncurrent versions beyond the specified number to retain. For more information about
 noncurrent versions, see [Lifecycle configuration elements](../userguide/intro-lifecycle-rules.md "../userguide/intro-lifecycle-rules.md") in
 the *Amazon S3 User Guide*.


Type: Integer


Required: No




**NoncurrentDays** 


Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action.
 For information about the noncurrent days calculations, see [How Amazon S3 Calculates
 How Long an Object Has Been Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations") in the *Amazon S3 User Guide*.


Type: Integer


Required: No




**StorageClass** 


The class of storage used to store the object.


Type: String


Valid Values: `GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE | GLACIER_IR`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NoncurrentVersionTransition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NoncurrentVersionTransition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NoncurrentVersionTransition")

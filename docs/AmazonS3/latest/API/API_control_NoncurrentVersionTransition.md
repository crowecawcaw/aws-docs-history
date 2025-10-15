# NoncurrentVersionTransition

The container for the noncurrent version transition.


## Contents





**NoncurrentDays** 


Specifies the number of days an object is noncurrent before Amazon S3 can perform the
 associated action. For information about the noncurrent days calculations, see  [How
 Amazon S3 Calculates How Long an Object Has Been Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations") in the
 *Amazon S3 User Guide*.


Type: Integer


Required: No




**StorageClass** 


The class of storage used to store the object.


Type: String


Valid Values: `GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionTransition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionTransition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionTransition "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionTransition")

# Tiering

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically
 moving data to the most cost-effective storage access tier, without additional operational
 overhead.


## Contents





**AccessTier** 


S3 Intelligent-Tiering access tier. See [Storage class for
 automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access") for a list of access
 tiers in the S3 Intelligent-Tiering storage class.


Type: String


Valid Values: `ARCHIVE_ACCESS | DEEP_ARCHIVE_ACCESS`



Required: Yes




**Days** 


The number of consecutive days of no access after which an object will be eligible to be
 transitioned to the corresponding tier. The minimum number of days specified for Archive Access tier
 must be at least 90 days and Deep Archive Access tier must be at least 180 days. The maximum can be up to
 2 years (730 days).


Type: Integer


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Tiering "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Tiering")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Tiering "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Tiering")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Tiering "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Tiering")

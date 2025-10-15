# VersioningConfiguration

Describes the versioning state of an Amazon S3 bucket. For more information, see [PUT Bucket
 versioning](RESTBucketPUTVersioningStatus.md "RESTBucketPUTVersioningStatus.md") in the *Amazon S3 API Reference*.


## Contents





**MFADelete** 


Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only
 returned if the bucket has been configured with MFA delete. If the bucket has never been so configured,
 this element is not returned.


Type: String


Valid Values: `Enabled | Disabled`



Required: No




**Status** 


The versioning state of the bucket.


Type: String


Valid Values: `Enabled | Suspended`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/VersioningConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/VersioningConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/VersioningConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/VersioningConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/VersioningConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/VersioningConfiguration")

# Region

A Region that supports a Multi-Region Access Point as well as the associated bucket for the Region.


## Contents





**Bucket** 


The name of the associated bucket for the Region.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**BucketAccountId** 


The AWS account ID that owns the Amazon S3 bucket that's associated with this
 Multi-Region Access Point.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Region "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Region")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Region "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Region")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Region "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Region")

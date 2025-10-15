# CreateMultiRegionAccessPointInput

A container for the information associated with a [CreateMultiRegionAccessPoint](API_control_CreateMultiRegionAccessPoint.md "API_control_CreateMultiRegionAccessPoint.md") request. 


## Contents





**Name** 


The name of the Multi-Region Access Point associated with this request.


Type: String


Length Constraints: Maximum length of 50.


Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`



Required: Yes




**Regions** 


The buckets in different Regions that are associated with the Multi-Region Access Point.


Type: Array of [Region](API_control_Region.md "API_control_Region.md") data types


Required: Yes




**PublicAccessBlock** 


The `PublicAccessBlock` configuration that you want to apply to this Amazon S3
 account. You can enable the configuration options in any combination. For more information
 about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status") in the *Amazon S3 User Guide*.


This data type is not supported for Amazon S3 on Outposts.


Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md "API_control_PublicAccessBlockConfiguration.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateMultiRegionAccessPointInput "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateMultiRegionAccessPointInput")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateMultiRegionAccessPointInput "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateMultiRegionAccessPointInput")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateMultiRegionAccessPointInput "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateMultiRegionAccessPointInput")

# OriginShield

CloudFront Origin Shield.

Using Origin Shield can help reduce the load on your origin. For more information, see
 [Using Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md") in the
 *Amazon CloudFront Developer Guide*.


## Contents





**Enabled** 


A flag that specifies whether Origin Shield is enabled.


When it's enabled, CloudFront routes all requests through Origin Shield, which can help
 protect your origin. When it's disabled, CloudFront might send requests directly to your
 origin from multiple edge locations or regional edge caches.


Type: Boolean


Required: Yes




**OriginShieldRegion** 


The AWS Region for Origin Shield.


Specify the AWS Region that has the lowest latency to your origin. To specify a
 region, use the region code, not the region name. For example, specify the US East
 (Ohio) region as `us-east-2`.


When you enable CloudFront Origin Shield, you must specify the AWS Region for Origin
 Shield. For the list of AWS Regions that you can specify, and for help choosing the
 best Region for your origin, see [Choosing the AWS Region for Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md#choose-origin-shield-region "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md#choose-origin-shield-region") in the
 *Amazon CloudFront Developer Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `[a-z]{2}-[a-z]+-\d`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginShield "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginShield")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginShield "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginShield")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginShield "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginShield")

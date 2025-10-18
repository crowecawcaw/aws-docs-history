# StreamingDistributionSummary

A summary of the information for a CloudFront streaming distribution.


## Contents





**Aliases** 


A complex type that contains information about CNAMEs (alternate domain names), if
 any, for this streaming distribution.


Type: [Aliases](API_Aliases.md "API_Aliases.md") object


Required: Yes




**ARN** 


The ARN (Amazon Resource Name) for the streaming distribution. For example:
 `arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`,
 where `123456789012` is your AWS account ID.


Type: String


Required: Yes




**Comment** 


The comment originally specified when this distribution was created.


Type: String


Required: Yes




**DomainName** 


The domain name corresponding to the distribution, for example,
 `d111111abcdef8.cloudfront.net`.


Type: String


Required: Yes




**Enabled** 


Whether the distribution is enabled to accept end user requests for content.


Type: Boolean


Required: Yes




**Id** 


The identifier for the distribution, for example, `EDFDVBD632BHDS5`.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time the distribution was last modified.


Type: Timestamp


Required: Yes




**PriceClass** 


A complex type that contains information about price class for this streaming
 distribution.


Type: String


Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None`



Required: Yes




**S3Origin** 


A complex type that contains information about the Amazon S3 bucket from which you want
 CloudFront to get your media files for distribution.


Type: [S3Origin](API_S3Origin.md "API_S3Origin.md") object


Required: Yes




**Status** 


Indicates the current status of the distribution. When the status is
 `Deployed`, the distribution's information is fully propagated throughout
 the Amazon CloudFront system.


Type: String


Required: Yes




**TrustedSigners** 


A complex type that specifies the AWS accounts, if any, that you want to allow to
 create signed URLs for private content. If you want to require signed URLs in requests
 for objects in the target origin that match the `PathPattern` for this cache
 behavior, specify `true` for `Enabled`, and specify the applicable
 values for `Quantity` and `Items`.If you don't want to require
 signed URLs in requests for objects that match `PathPattern`, specify
 `false` for `Enabled` and `0` for
 `Quantity`. Omit `Items`. To add, change, or remove one or
 more trusted signers, change `Enabled` to `true` (if it's
 currently `false`), change `Quantity` as applicable, and specify
 all of the trusted signers that you want to include in the updated distribution.


For more information, see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


Type: [TrustedSigners](API_TrustedSigners.md "API_TrustedSigners.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionSummary")

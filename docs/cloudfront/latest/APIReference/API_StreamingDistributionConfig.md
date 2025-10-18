# StreamingDistributionConfig

The RTMP distribution's configuration information.


## Contents





**CallerReference** 


A unique value (for example, a date-time stamp) that ensures that the request can't be
 replayed.


If the value of `CallerReference` is new (regardless of the content of the
 `StreamingDistributionConfig` object), CloudFront creates a new
 distribution.


If `CallerReference` is a value that you already sent in a previous request
 to create a distribution, CloudFront returns a `DistributionAlreadyExists`
 error.


Type: String


Required: Yes




**Comment** 


Any comments you want to include about the streaming distribution.


Type: String


Required: Yes




**Enabled** 


Whether the streaming distribution is enabled to accept user requests for
 content.


Type: Boolean


Required: Yes




**S3Origin** 


A complex type that contains information about the Amazon S3 bucket from which you want
 CloudFront to get your media files for distribution.


Type: [S3Origin](API_S3Origin.md "API_S3Origin.md") object


Required: Yes




**TrustedSigners** 


A complex type that specifies any AWS accounts that you want to permit to create
 signed URLs for private content. If you want the distribution to use signed URLs,
 include this element; if you want the distribution to use public URLs, remove this
 element. For more information, see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


Type: [TrustedSigners](API_TrustedSigners.md "API_TrustedSigners.md") object


Required: Yes




**Aliases** 


A complex type that contains information about CNAMEs (alternate domain names), if
 any, for this streaming distribution.


Type: [Aliases](API_Aliases.md "API_Aliases.md") object


Required: No




**Logging** 


A complex type that controls whether access logs are written for the streaming
 distribution.


Type: [StreamingLoggingConfig](API_StreamingLoggingConfig.md "API_StreamingLoggingConfig.md") object


Required: No




**PriceClass** 


A complex type that contains information about price class for this streaming
 distribution.


Type: String


Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionConfig")

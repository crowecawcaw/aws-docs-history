# StreamingDistribution

A streaming distribution tells CloudFront where you want RTMP content to be delivered from,
 and the details about how to track and manage content delivery.


## Contents





**ActiveTrustedSigners** 


A complex type that lists the AWS accounts, if any, that you included in the
 `TrustedSigners` complex type for this distribution. These are the
 accounts that you want to allow to create signed URLs for private content.


The `Signer` complex type lists the AWS account number of the trusted
 signer or `self` if the signer is the AWS account that created the
 distribution. The `Signer` element also includes the IDs of any active CloudFront
 key pairs that are associated with the trusted signer's AWS account. If no
 `KeyPairId` element appears for a `Signer`, that signer can't
 create signed URLs.


For more information, see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md "API_ActiveTrustedSigners.md") object


Required: Yes




**ARN** 


The ARN (Amazon Resource Name) for the distribution. For example:
 `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where
 `123456789012` is your AWS account ID.


Type: String


Required: Yes




**DomainName** 


The domain name that corresponds to the streaming distribution, for example,
 `s5c39gqb8ow64r.cloudfront.net`.


Type: String


Required: Yes




**Id** 


The identifier for the RTMP distribution. For example:
 `EGTXBD79EXAMPLE`.


Type: String


Required: Yes




**Status** 


The current status of the RTMP distribution. When the status is `Deployed`,
 the distribution's information is propagated to all CloudFront edge locations.


Type: String


Required: Yes




**StreamingDistributionConfig** 


The current configuration information for the RTMP distribution.


Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md "API_StreamingDistributionConfig.md") object


Required: Yes




**LastModifiedTime** 


The date and time that the distribution was last modified.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistribution "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistribution")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistribution "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistribution")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistribution "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistribution")

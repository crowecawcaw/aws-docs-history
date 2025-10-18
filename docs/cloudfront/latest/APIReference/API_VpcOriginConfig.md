# VpcOriginConfig

An Amazon CloudFront VPC origin configuration.


## Contents





**VpcOriginId** 


The VPC origin ID.


Type: String


Required: Yes




**OriginKeepaliveTimeout** 


Specifies how long, in seconds, CloudFront persists its connection to the origin. The
 minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't
 specify otherwise) is 5 seconds.


For more information, see [Keep-alive timeout (custom origins only)](../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout "../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout") in the
 *Amazon CloudFront Developer Guide*.


Type: Integer


Required: No




**OriginReadTimeout** 


Specifies how long, in seconds, CloudFront waits for a response from the origin. This is
 also known as the *origin response timeout*. The minimum timeout is 1
 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is
 30 seconds.


For more information, see [Response timeout](../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout "../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout") in the
 *Amazon CloudFront Developer Guide*.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginConfig")

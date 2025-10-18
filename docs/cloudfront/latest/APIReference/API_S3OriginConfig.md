# S3OriginConfig

A complex type that contains information about the Amazon S3 origin. If the origin is a
 custom origin or an S3 bucket that is configured as a website endpoint, use the
 `CustomOriginConfig` element instead.


## Contents





**OriginAccessIdentity** 


###### Note

If you're using origin access control (OAC) instead of origin access identity,
 specify an empty `OriginAccessIdentity` element. For more information,
 see [Restricting access to an AWS](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.md") in the
 *Amazon CloudFront Developer Guide*.


The CloudFront origin access identity to associate with the origin. Use an origin access
 identity to configure the origin so that viewers can *only* access
 objects in an Amazon S3 bucket through CloudFront. The format of the value is:



`origin-access-identity/cloudfront/ID-of-origin-access-identity`



The `*ID-of-origin-access-identity*` is the value that CloudFront
 returned in the `ID` element when you created the origin access
 identity.


If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3
 URL, specify an empty `OriginAccessIdentity` element.


To delete the origin access identity from an existing distribution, update the
 distribution configuration and include an empty `OriginAccessIdentity`
 element.


To replace the origin access identity, update the distribution configuration and
 specify the new origin access identity.


For more information about the origin access identity, see [Serving Private
 Content through CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the *Amazon CloudFront Developer Guide*.


Type: String


Required: Yes




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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/S3OriginConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/S3OriginConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/S3OriginConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/S3OriginConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/S3OriginConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/S3OriginConfig")

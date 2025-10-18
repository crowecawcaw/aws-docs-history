# Origin

An origin.

An origin is the location where content is stored, and from which CloudFront gets content to
 serve to viewers. To specify an origin:


* Use `S3OriginConfig` to specify an Amazon S3 bucket that is not
 configured with static website hosting.
* Use `VpcOriginConfig` to specify a VPC origin.
* Use `CustomOriginConfig` to specify all other kinds of origins,
 including:




	+ An Amazon S3 bucket that is configured with static website hosting
	+ An Elastic Load Balancing load balancer
	+ An AWS Elemental MediaPackage endpoint
	+ An AWS Elemental MediaStore container
	+ Any other HTTP server, running on an Amazon EC2 instance or any other kind
	 of host
For the current maximum number of origins that you can specify per distribution, see
 [General Quotas on Web Distributions](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md#limits-web-distributions "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md#limits-web-distributions") in the
 *Amazon CloudFront Developer Guide* (quotas were formerly referred to as
 limits).


## Contents





**DomainName** 


The domain name for the origin.


For more information, see [Origin Domain Name](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesDomainName "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesDomainName") in the *Amazon CloudFront Developer Guide*.


Type: String


Required: Yes




**Id** 


A unique identifier for the origin. This value must be unique within the
 distribution.


Use this value to specify the `TargetOriginId` in a
 `CacheBehavior` or `DefaultCacheBehavior`.


Type: String


Required: Yes




**ConnectionAttempts** 


The number of times that CloudFront attempts to connect to the origin. The minimum number is
 1, the maximum is 3, and the default (if you don't specify otherwise) is 3.


For a custom origin (including an Amazon S3 bucket that's configured with static website
 hosting), this value also specifies the number of times that CloudFront attempts to get a
 response from the origin, in the case of an [Origin Response Timeout](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginResponseTimeout "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginResponseTimeout").


For more information, see [Origin Connection Attempts](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#origin-connection-attempts "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#origin-connection-attempts") in the
 *Amazon CloudFront Developer Guide*.


Type: Integer


Required: No




**ConnectionTimeout** 


The number of seconds that CloudFront waits when trying to establish a connection to the
 origin. The minimum timeout is 1 second, the maximum is 10 seconds, and the default (if
 you don't specify otherwise) is 10 seconds.


For more information, see [Origin Connection Timeout](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#origin-connection-timeout "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#origin-connection-timeout") in the
 *Amazon CloudFront Developer Guide*.


Type: Integer


Required: No




**CustomHeaders** 


A list of HTTP header names and values that CloudFront adds to the requests that it sends to
 the origin.


For more information, see [Adding Custom Headers to Origin Requests](../../../AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.md "../../../AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.md") in the
 *Amazon CloudFront Developer Guide*.


Type: [CustomHeaders](API_CustomHeaders.md "API_CustomHeaders.md") object


Required: No




**CustomOriginConfig** 


Use this type to specify an origin that is not an Amazon S3 bucket, with one exception. If
 the Amazon S3 bucket is configured with static website hosting, use this type. If the Amazon S3
 bucket is not configured with static website hosting, use the
 `S3OriginConfig` type instead.


Type: [CustomOriginConfig](API_CustomOriginConfig.md "API_CustomOriginConfig.md") object


Required: No




**OriginAccessControlId** 


The unique identifier of an origin access control for this origin.


For more information, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the
 *Amazon CloudFront Developer Guide*.


Type: String


Required: No




**OriginPath** 


An optional path that CloudFront appends to the origin domain name when CloudFront requests
 content from the origin.


For more information, see [Origin Path](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginPath "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginPath") in the
 *Amazon CloudFront Developer Guide*.


Type: String


Required: No




**OriginShield** 


CloudFront Origin Shield. Using Origin Shield can help reduce the load on your
 origin.


For more information, see [Using Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md") in the *Amazon CloudFront Developer Guide*.


Type: [OriginShield](API_OriginShield.md "API_OriginShield.md") object


Required: No




**ResponseCompletionTimeout** 


The time (in seconds) that a request from CloudFront to the origin can stay open and wait
 for a response. If the complete response isn't received from the origin by this time,
 CloudFront ends the connection.


The value for `ResponseCompletionTimeout` must be equal to or greater than
 the value for `OriginReadTimeout`. If you don't set a value for
 `ResponseCompletionTimeout`, CloudFront doesn't enforce a maximum value.


For more information, see [Response completion timeout](../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#response-completion-timeout "../../../AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.md#response-completion-timeout") in the
 *Amazon CloudFront Developer Guide*.


Type: Integer


Required: No




**S3OriginConfig** 


Use this type to specify an origin that is an Amazon S3 bucket that is not configured with
 static website hosting. To specify any other type of origin, including an Amazon S3 bucket
 that is configured with static website hosting, use the `CustomOriginConfig`
 type instead.


Type: [S3OriginConfig](API_S3OriginConfig.md "API_S3OriginConfig.md") object


Required: No




**VpcOriginConfig** 


The VPC origin configuration.


Type: [VpcOriginConfig](API_VpcOriginConfig.md "API_VpcOriginConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Origin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Origin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Origin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Origin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Origin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Origin")

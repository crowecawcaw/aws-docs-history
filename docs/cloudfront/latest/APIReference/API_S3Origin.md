# S3Origin

A complex type that contains information about the Amazon S3 bucket from which you want
 CloudFront to get your media files for distribution.


## Contents





**DomainName** 


The DNS name of the Amazon S3 origin.


Type: String


Required: Yes




**OriginAccessIdentity** 


The CloudFront origin access identity to associate with the distribution. Use an origin
 access identity to configure the distribution so that end users can only access objects
 in an Amazon S3 bucket through CloudFront.


If you want end users to be able to access objects using either the CloudFront URL or the
 Amazon S3 URL, specify an empty `OriginAccessIdentity` element.


To delete the origin access identity from an existing distribution, update the
 distribution configuration and include an empty `OriginAccessIdentity`
 element.


To replace the origin access identity, update the distribution configuration and
 specify the new origin access identity.


For more information, see [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in
 the  *Amazon CloudFront Developer Guide*.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/S3Origin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/S3Origin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/S3Origin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/S3Origin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/S3Origin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/S3Origin")

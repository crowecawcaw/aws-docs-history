# ResponseHeadersPolicy

A response headers policy.

A response headers policy contains information about a set of HTTP response headers.

After you create a response headers policy, you can use its ID to attach it to one or more
 cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the
 response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to
 requests that match the cache behavior. CloudFront adds or removes response headers according
 to the configuration of the response headers policy.

For more information, see [Adding or removing HTTP headers in CloudFront responses](../../../AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.md "../../../AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.md") in the
 *Amazon CloudFront Developer Guide*.


## Contents





**Id** 


The identifier for the response headers policy.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time when the response headers policy was last modified.


Type: Timestamp


Required: Yes




**ResponseHeadersPolicyConfig** 


A response headers policy configuration.


Type: [ResponseHeadersPolicyConfig](API_ResponseHeadersPolicyConfig.md "API_ResponseHeadersPolicyConfig.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicy")

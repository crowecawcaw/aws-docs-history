# CachePolicy

A cache policy.

When it's attached to a cache behavior, the cache policy determines the
 following:


* The values that CloudFront includes in the cache key. These values can include HTTP
 headers, cookies, and URL query strings. CloudFront uses the cache key to find an
 object in its cache that it can return to the viewer.
* The default, minimum, and maximum time to live (TTL) values that you want
 objects to stay in the CloudFront cache.
The headers, cookies, and query strings that are included in the cache key are also included
 in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find a
 valid object in its cache that matches the request's cache key. If you want to send
 values to the origin but *not* include them in the cache key, use
 `OriginRequestPolicy`.


## Contents





**CachePolicyConfig** 


The cache policy configuration.


Type: [CachePolicyConfig](API_CachePolicyConfig.md "API_CachePolicyConfig.md") object


Required: Yes




**Id** 


The unique identifier for the cache policy.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time when the cache policy was last modified.


Type: Timestamp


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicy")

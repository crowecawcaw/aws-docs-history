# CachePolicyHeadersConfig

An object that determines whether any HTTP headers (and if so, which headers) are included
 in the cache key and in requests that CloudFront sends to the origin.


## Contents





**HeaderBehavior** 


Determines whether any HTTP headers are included in the cache key and in requests that CloudFront
 sends to the origin. Valid values are:



* `none` – No HTTP headers are included in the cache key or in requests that CloudFront
 sends to the origin. Even when this field is set to `none`, any
 headers that are listed in an `OriginRequestPolicy`
*are* included in origin requests.
* `whitelist` – Only the HTTP headers that are listed in the `Headers`
 type are included in the cache key and in requests that CloudFront sends to the
 origin.

Type: String


Valid Values: `none | whitelist`



Required: Yes




**Headers** 


Contains a list of HTTP header names.


Type: [Headers](API_Headers.md "API_Headers.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyHeadersConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyHeadersConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyHeadersConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyHeadersConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyHeadersConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyHeadersConfig")

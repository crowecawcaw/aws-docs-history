# OriginRequestPolicyConfig

An origin request policy configuration.

This configuration determines the values that CloudFront includes in requests that it sends
 to the origin. Each request that CloudFront sends to the origin includes the following:


* The request body and the URL path (without the domain name) from the viewer
 request.
* The headers that CloudFront automatically includes in every origin request,
 including `Host`, `User-Agent`, and
 `X-Amz-Cf-Id`.
* All HTTP headers, cookies, and URL query strings that are specified in the
 cache policy or the origin request policy. These can include items from the
 viewer request and, in the case of headers, additional ones that are added by
 CloudFront.
CloudFront sends a request when it can't find an object in its cache that matches the
 request. If you want to send values to the origin and also include them in the cache
 key, use `CachePolicy`.


## Contents





**CookiesConfig** 


The cookies from viewer requests to include in origin requests.


Type: [OriginRequestPolicyCookiesConfig](API_OriginRequestPolicyCookiesConfig.md "API_OriginRequestPolicyCookiesConfig.md") object


Required: Yes




**HeadersConfig** 


The HTTP headers to include in origin requests. These can include headers from viewer
 requests and additional headers added by CloudFront.


Type: [OriginRequestPolicyHeadersConfig](API_OriginRequestPolicyHeadersConfig.md "API_OriginRequestPolicyHeadersConfig.md") object


Required: Yes




**Name** 


A unique name to identify the origin request policy.


Type: String


Required: Yes




**QueryStringsConfig** 


The URL query strings from viewer requests to include in origin requests.


Type: [OriginRequestPolicyQueryStringsConfig](API_OriginRequestPolicyQueryStringsConfig.md "API_OriginRequestPolicyQueryStringsConfig.md") object


Required: Yes




**Comment** 


A comment to describe the origin request policy. The comment cannot be longer than 128
 characters.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginRequestPolicyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginRequestPolicyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginRequestPolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginRequestPolicyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginRequestPolicyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginRequestPolicyConfig")

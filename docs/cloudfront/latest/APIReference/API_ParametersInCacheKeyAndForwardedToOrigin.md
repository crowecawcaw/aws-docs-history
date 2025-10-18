# ParametersInCacheKeyAndForwardedToOrigin

This object determines the values that CloudFront includes in the cache key. These values
 can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to
 find an object in its cache that it can return to the viewer.

The headers, cookies, and query strings that are included in the cache key are also included
 in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find an
 object in its cache that matches the request's cache key. If you want to send values to
 the origin but *not* include them in the cache key, use
 `OriginRequestPolicy`.


## Contents





**CookiesConfig** 


An object that determines whether any cookies in viewer requests (and if so, which cookies)
 are included in the cache key and in requests that CloudFront sends to the origin.


Type: [CachePolicyCookiesConfig](API_CachePolicyCookiesConfig.md "API_CachePolicyCookiesConfig.md") object


Required: Yes




**EnableAcceptEncodingGzip** 


A flag that can affect whether the `Accept-Encoding` HTTP header is
 included in the cache key and included in requests that CloudFront sends to the origin.


This field is related to the `EnableAcceptEncodingBrotli` field. If one or
 both of these fields is `true`
*and* the viewer request includes the `Accept-Encoding`
 header, then CloudFront does the following:



* Normalizes the value of the viewer's `Accept-Encoding`
 header
* Includes the normalized header in the cache key
* Includes the normalized header in the request to the origin, if a request is
 necessary

For more information, see [Compression support](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-policy-compressed-objects "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-policy-compressed-objects") in the
 *Amazon CloudFront Developer Guide*.


If you set this value to `true`, and this cache behavior also has an origin
 request policy attached, do not include the `Accept-Encoding` header in the
 origin request policy. CloudFront always includes the `Accept-Encoding` header in
 origin requests when the value of this field is `true`, so including this
 header in an origin request policy has no effect.


If both of these fields are `false`, then CloudFront treats the
 `Accept-Encoding` header the same as any other HTTP header in the viewer
 request. By default, it's not included in the cache key and it's not included in origin
 requests. In this case, you can manually add `Accept-Encoding` to the headers
 whitelist like any other HTTP header.


Type: Boolean


Required: Yes




**HeadersConfig** 


An object that determines whether any HTTP headers (and if so, which headers) are included
 in the cache key and in requests that CloudFront sends to the origin.


Type: [CachePolicyHeadersConfig](API_CachePolicyHeadersConfig.md "API_CachePolicyHeadersConfig.md") object


Required: Yes




**QueryStringsConfig** 


An object that determines whether any URL query strings in viewer requests (and if so, which
 query strings) are included in the cache key and in requests that CloudFront sends to the
 origin.


Type: [CachePolicyQueryStringsConfig](API_CachePolicyQueryStringsConfig.md "API_CachePolicyQueryStringsConfig.md") object


Required: Yes




**EnableAcceptEncodingBrotli** 


A flag that can affect whether the `Accept-Encoding` HTTP header is
 included in the cache key and included in requests that CloudFront sends to the origin.


This field is related to the `EnableAcceptEncodingGzip` field. If one or
 both of these fields is `true`
*and* the viewer request includes the `Accept-Encoding`
 header, then CloudFront does the following:



* Normalizes the value of the viewer's `Accept-Encoding`
 header
* Includes the normalized header in the cache key
* Includes the normalized header in the request to the origin, if a request is
 necessary

For more information, see [Compression support](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-policy-compressed-objects "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-policy-compressed-objects") in the
 *Amazon CloudFront Developer Guide*.


If you set this value to `true`, and this cache behavior also has an origin
 request policy attached, do not include the `Accept-Encoding` header in the
 origin request policy. CloudFront always includes the `Accept-Encoding` header in
 origin requests when the value of this field is `true`, so including this
 header in an origin request policy has no effect.


If both of these fields are `false`, then CloudFront treats the
 `Accept-Encoding` header the same as any other HTTP header in the viewer
 request. By default, it's not included in the cache key and it's not included in origin
 requests. In this case, you can manually add `Accept-Encoding` to the headers
 whitelist like any other HTTP header.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ParametersInCacheKeyAndForwardedToOrigin")

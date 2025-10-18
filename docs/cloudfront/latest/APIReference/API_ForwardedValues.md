# ForwardedValues

###### Note

This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.md#unsupported-saas "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.md#unsupported-saas") in the *Amazon CloudFront Developer Guide*.

This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.

If you want to include values in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.

If you want to send values to the origin but not include them in the cache key, use an
 origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.

A complex type that specifies how CloudFront handles query strings, cookies, and HTTP
 headers.


## Contents





**Cookies** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include cookies in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send cookies to the origin but not include them in the cache key, use
 an origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


A complex type that specifies whether you want CloudFront to forward cookies to the origin
 and, if so, which ones. For more information about forwarding cookies to the origin, see
 [How CloudFront Forwards, Caches,
 and Logs Cookies](../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md "../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md") in the *Amazon CloudFront Developer Guide*.


Type: [CookiePreference](API_CookiePreference.md "API_CookiePreference.md") object


Required: Yes




**QueryString** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include query strings in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send query strings to the origin but not include them in the cache key,
 use an origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


Indicates whether you want CloudFront to forward query strings to the origin that is
 associated with this cache behavior and cache based on the query string parameters. CloudFront
 behavior depends on the value of `QueryString` and on the values that you
 specify for `QueryStringCacheKeys`, if any:


If you specify true for `QueryString` and you don't specify any values for
 `QueryStringCacheKeys`, CloudFront forwards all query string parameters to the
 origin and caches based on all query string parameters. Depending on how many query
 string parameters and values you have, this can adversely affect performance because
 CloudFront must forward more requests to the origin.


If you specify true for `QueryString` and you specify one or more values
 for `QueryStringCacheKeys`, CloudFront forwards all query string parameters to the
 origin, but it only caches based on the query string parameters that you specify.


If you specify false for `QueryString`, CloudFront doesn't forward any query
 string parameters to the origin, and doesn't cache based on query string
 parameters.


For more information, see [Configuring
 CloudFront to Cache Based on Query String Parameters](../../../AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.md "../../../AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.md") in the
 *Amazon CloudFront Developer Guide*.


Type: Boolean


Required: Yes




**Headers** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include headers in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send headers to the origin but not include them in the cache key, use
 an origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


A complex type that specifies the `Headers`, if any, that you want CloudFront to
 forward to the origin for this cache behavior (whitelisted headers). For the headers
 that you specify, CloudFront also caches separate versions of a specified object that is based
 on the header values in viewer requests.


For more information, see  [Caching Content
 Based on Request Headers](../../../AmazonCloudFront/latest/DeveloperGuide/header-caching.md "../../../AmazonCloudFront/latest/DeveloperGuide/header-caching.md") in the *Amazon CloudFront Developer Guide*.


Type: [Headers](API_Headers.md "API_Headers.md") object


Required: No




**QueryStringCacheKeys** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include query strings in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send query strings to the origin but not include them in the cache key,
 use an origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


A complex type that contains information about the query string parameters that you
 want CloudFront to use for caching for this cache behavior.


Type: [QueryStringCacheKeys](API_QueryStringCacheKeys.md "API_QueryStringCacheKeys.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ForwardedValues "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ForwardedValues")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ForwardedValues "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ForwardedValues")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ForwardedValues "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ForwardedValues")

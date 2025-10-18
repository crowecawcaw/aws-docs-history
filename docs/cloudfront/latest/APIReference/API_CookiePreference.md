# CookiePreference

This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.

If you want to include cookies in the cache key, use `CookiesConfig` in a
 cache policy. See `CachePolicy`.

If you want to send cookies to the origin but not include them in the cache key, use
 `CookiesConfig` in an origin request policy. See
 `OriginRequestPolicy`.

A complex type that specifies whether you want CloudFront to forward cookies to the origin
 and, if so, which ones. For more information about forwarding cookies to the origin, see
 [Caching Content Based on
 Cookies](../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md "../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md") in the *Amazon CloudFront Developer Guide*.


## Contents





**Forward** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include cookies in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send cookies to the origin but not include them in the cache key, use
 origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


Specifies which cookies to forward to the origin for this cache behavior: all, none,
 or the list of cookies specified in the `WhitelistedNames` complex
 type.


Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
 Amazon S3 origin, specify none for the `Forward` element.


Type: String


Valid Values: `none | whitelist | all`



Required: Yes




**WhitelistedNames** 


This field is deprecated. We recommend that you use a cache policy or an origin
 request policy instead of this field.


If you want to include cookies in the cache key, use a cache policy. For more
 information, see [Creating cache policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md#cache-key-create-cache-policy") in the *Amazon CloudFront Developer Guide*.


If you want to send cookies to the origin but not include them in the cache key, use
 an origin request policy. For more information, see [Creating origin request policies](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md#origin-request-create-origin-request-policy") in the
 *Amazon CloudFront Developer Guide*.


Required if you specify `whitelist` for the value of `Forward`.
 A complex type that specifies how many different cookies you want CloudFront to forward to the
 origin for this cache behavior and, if you want to forward selected cookies, the names
 of those cookies.


If you specify `all` or `none` for the value of
 `Forward`, omit `WhitelistedNames`. If you change the value of
 `Forward` from `whitelist` to `all` or
 `none` and you don't delete the `WhitelistedNames` element and
 its child elements, CloudFront deletes them automatically.


For the current limit on the number of cookie names that you can whitelist for each
 cache behavior, see  [CloudFront
 Limits](https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront "https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront") in the *AWS General Reference*.


Type: [CookieNames](API_CookieNames.md "API_CookieNames.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CookiePreference "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CookiePreference")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CookiePreference "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CookiePreference")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CookiePreference "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CookiePreference")

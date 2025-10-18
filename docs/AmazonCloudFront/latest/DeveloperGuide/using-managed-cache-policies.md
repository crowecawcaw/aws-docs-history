# Use managed cache policies

CloudFront provides a set of managed cache policies that you can attach to any of your
 distribution's cache behaviors. With a managed cache policy, you don't need to write or
 maintain your own cache policy. The managed policies use settings that are optimized for
 specific use cases.

To use a managed cache policy, you attach it to a cache behavior in your distribution.
 The process is the same as when you create a cache policy, but instead of creating a new
 one, you just attach one of the managed cache policies. You attach the policy either by
 name (with the console) or by ID (with the AWS CLI or SDKs). The names and IDs are listed
 in the following section.

For more information, see [Create cache policies](cache-key-create-cache-policy.md "cache-key-create-cache-policy.md").

The following topics describe the managed cache policies that you can use.

###### Topics

* [Amplify](#managed-cache-policy-amplify "#managed-cache-policy-amplify")
* [CachingDisabled](#managed-cache-policy-caching-disabled "#managed-cache-policy-caching-disabled")
* [CachingOptimized](#managed-cache-caching-optimized "#managed-cache-caching-optimized")
* [CachingOptimizedForUncompressedObjects](#managed-cache-caching-optimized-uncompressed "#managed-cache-caching-optimized-uncompressed")
* [Elemental-MediaPackage](#managed-cache-policy-mediapackage "#managed-cache-policy-mediapackage")
* [UseOriginCacheControlHeaders](#managed-cache-policy-origin-cache-headers "#managed-cache-policy-origin-cache-headers")
* [UseOriginCacheControlHeaders-QueryStrings](#managed-cache-policy-origin-cache-headers-query-strings "#managed-cache-policy-origin-cache-headers-query-strings")

## Amplify


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/2e54312d-136d-493c-8eb9-b001f22f67d2 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/2e54312d-136d-493c-8eb9-b001f22f67d2")


This policy is designed for use with an origin that is an [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") web app.


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`2e54312d-136d-493c-8eb9-b001f22f67d2`


This policy has the following settings:



* **Minimum TTL:** 2 seconds
* **Maximum TTL:** 600 seconds (10
 minutes)
* **Default TTL:** 2 seconds
* **Headers included in cache key:**




	+ `Authorization`
	+ `CloudFront-Viewer-Country`
	+ `Host`
The normalized `Accept-Encoding` header is also included
 because the cache compressed objects setting is enabled. For more
 information, see [Compression
 support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").
* **Cookies included in cache key:** All
 cookies are included.
* **Query strings included in cache key:** All
 query strings are included.
* **Cache compressed objects setting:**
 Enabled. For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").

###### Warning

Because this policy has a minimum TTL greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.


### AWS Amplify Hosting cache
 policies


Amplify uses the following managed cache policies to optimize the default cache
 configuration for customers' applications:



* [Amplify-Default](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4d1d2f1d-3a71-49ad-9e08-7ea5d843a556 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4d1d2f1d-3a71-49ad-9e08-7ea5d843a556")
* [Amplify-DefaultNoCookies](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/a6bad946-36c3-4c33-aa98-362c74a7fb13 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/a6bad946-36c3-4c33-aa98-362c74a7fb13")
* [Amplify-ImageOptimization](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/1c6db51a-a33f-469a-8245-dae26771f530 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/1c6db51a-a33f-469a-8245-dae26771f530")
* [Amplify-StaticContent](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/7e5fad67-ee98-4ad0-b05a-394999eefc1a "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/7e5fad67-ee98-4ad0-b05a-394999eefc1a")

###### Note

These policies are only used by Amplify. We don't recommend that you use
 these policies for your distributions. 


For more information about managing cache configuration for your Amplify hosted
 application, see [Managing cache configuration](https://docs.aws.amazon.com/amplify/latest/userguide/caching.html "https://docs.aws.amazon.com/amplify/latest/userguide/caching.html")
 in the *Amplify Hosting User Guide*.


## CachingDisabled


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4135ea2d-6df8-44a3-9df3-4b5a84be39ad "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4135ea2d-6df8-44a3-9df3-4b5a84be39ad")


This policy disables caching. This policy is useful for dynamic content and for
 requests that are not cacheable.


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`4135ea2d-6df8-44a3-9df3-4b5a84be39ad`


This policy has the following settings:



* **Minimum TTL:** 0 seconds
* **Maximum TTL:** 0 seconds
* **Default TTL:** 0 seconds
* **Headers included in the cache key:**
 None
* **Cookies included in the cache key:**
 None
* **Query strings included in the cache key:**
 None
* **Cache compressed objects setting:**
 Disabled

## CachingOptimized


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/658327ea-f89d-4fab-a63d-7e88639e58f6 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/658327ea-f89d-4fab-a63d-7e88639e58f6")


This policy is designed to optimize cache efficiency by minimizing the values that
 CloudFront includes in the cache key. CloudFront doesn't include any query strings or cookies in
 the cache key, and only includes the normalized `Accept-Encoding` header.
 This enables CloudFront to separately cache objects in the Gzip and Brotli compressions
 formats when the origin returns them or when [CloudFront edge compression](ServingCompressedFiles.md "ServingCompressedFiles.md") is enabled.


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`658327ea-f89d-4fab-a63d-7e88639e58f6`


This policy has the following settings:



* **Minimum TTL:** 1 second.
* **Maximum TTL:** 31,536,000 seconds (365
 days).
* **Default TTL:** 86,400 seconds (24
 hours).
* **Headers included in the cache key:** None
 are explicitly included. The normalized `Accept-Encoding` header
 is included because the cache compressed objects setting is enabled. For
 more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").
* **Cookies included in the cache key:**
 None.
* **Query strings included in the cache key:**
 None.
* **Cache compressed objects setting:**
 Enabled. For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").

###### Warning

Because this policy has a minimum TTL greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.


## CachingOptimizedForUncompressedObjects


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/b2884449-e4de-46a7-ac36-70bc7f1ddd6d "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/b2884449-e4de-46a7-ac36-70bc7f1ddd6d")


This policy is designed to optimize cache efficiency by minimizing the values
 included in the cache key. No query strings, headers, or cookies are included. This
 policy is identical to the previous one, but it disables the cache compressed
 objects setting.


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`b2884449-e4de-46a7-ac36-70bc7f1ddd6d`


This policy has the following settings:



* **Minimum TTL:** 1 second
* **Maximum TTL:** 31,536,000 seconds (365
 days)
* **Default TTL:** 86,400 seconds (24
 hours)
* **Headers included in the cache key:**
 None
* **Cookies included in the cache key:**
 None
* **Query strings included in the cache key:**
 None
* **Cache compressed objects setting:**
 Disabled

###### Warning

Because this policy has a minimum TTL greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.


## Elemental-MediaPackage


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/08627262-05a9-4f76-9ded-b50ca2e3a84f "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/08627262-05a9-4f76-9ded-b50ca2e3a84f")


This policy is designed for use with an origin that is an AWS Elemental MediaPackage
 endpoint.


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`08627262-05a9-4f76-9ded-b50ca2e3a84f`


This policy has the following settings:



* **Minimum TTL:** 0 seconds
* **Maximum TTL:** 31,536,000 seconds (365
 days)
* **Default TTL:** 86,400 seconds (24
 hours)
* **Headers included in the cache key:**




	+ `Origin`
The normalized `Accept-Encoding` header is also included
 because the cache compressed objects setting is enabled for Gzip. For more
 information, see [Compression
 support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").
* **Cookies included in the cache key:**
 None
* **Query strings included in the cache
 key:**




	+ `aws.manifestfilter`
	+ `start`
	+ `end`
	+ `m`
* **Cache compressed objects setting:** Enabled
 for Gzip. For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").

## UseOriginCacheControlHeaders


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/83da9c7e-98b4-4e11-a168-04f0df8e2c65 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/83da9c7e-98b4-4e11-a168-04f0df8e2c65")


This policy is designed for use with an origin that returns `Cache-Control` HTTP response headers and does not serve different content based on values present in the query string. If your origin serves different content based on values present in the query string, consider using [UseOriginCacheControlHeaders-QueryStrings](#managed-cache-policy-origin-cache-headers-query-strings "#managed-cache-policy-origin-cache-headers-query-strings").


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`83da9c7e-98b4-4e11-a168-04f0df8e2c65`


This policy has the following settings:



* **Minimum TTL:** 0 seconds
* **Maximum TTL:** 31,536,000 seconds (365
 days)
* **Default TTL:** 0 seconds
* **Headers included in the cache key:**




	+ `Host`
	+ `Origin`
	+ `X-HTTP-Method-Override`
	+ `X-HTTP-Method`
	+ `X-Method-Override`
The normalized `Accept-Encoding` header is also included
 because the cache compressed objects setting is enabled. For more
 information, see [Compression
 support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").
* **Cookies included in the cache key:**
 All cookies are included.
* **Query strings included in the cache
 key:** None.
* **Cache compressed objects setting:** Enabled. For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").

## UseOriginCacheControlHeaders-QueryStrings


[View
 this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4cc15a8a-d715-48a4-82b8-cc0b614638fe "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4cc15a8a-d715-48a4-82b8-cc0b614638fe")


This policy is designed for use with an origin that returns `Cache-Control` HTTP response headers and serves different content based on values present in the query string. If your origin does not serve different content based on values present in the query string, consider using [UseOriginCacheControlHeaders](#managed-cache-policy-origin-cache-headers "#managed-cache-policy-origin-cache-headers").


When using AWS CloudFormation, the AWS CLI, or the CloudFront API, the ID for this policy is:


`4cc15a8a-d715-48a4-82b8-cc0b614638fe`


This policy has the following settings:



* **Minimum TTL:** 0 seconds
* **Maximum TTL:** 31,536,000 seconds (365
 days)
* **Default TTL:** 0 seconds
* **Headers included in the cache key:**




	+ `Host`
	+ `Origin`
	+ `X-HTTP-Method-Override`
	+ `X-HTTP-Method`
	+ `X-Method-Override`
The normalized `Accept-Encoding` header is also included
 because the cache compressed objects setting is enabled. For more
 information, see [Compression
 support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").
* **Cookies included in the cache key:**
 All cookies are included.
* **Query strings included in the cache
 key:** All query strings are included.
* **Cache compressed objects setting:** Enabled. For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects").

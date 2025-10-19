# CreateCachePolicy

Creates a cache policy.

After you create a cache policy, you can attach it to one or more cache behaviors.
 When it's attached to a cache behavior, the cache policy determines the
 following:


* The values that CloudFront includes in the *cache key*. These
 values can include HTTP headers, cookies, and URL query strings. CloudFront uses the
 cache key to find an object in its cache that it can return to the
 viewer.
* The default, minimum, and maximum time to live (TTL) values that you want
 objects to stay in the CloudFront cache.


###### Important

If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the `Cache-Control: no-cache`, `no-store`, or `private` directives are present in the origin headers.
The headers, cookies, and query strings that are included in the cache key are also included
 in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find an
 object in its cache that matches the request's cache key. If you want to send values to
 the origin but *not* include them in the cache key, use
 `OriginRequestPolicy`.

For more information about cache policies, see [Controlling the cache key](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.md") in the
 *Amazon CloudFront Developer Guide*.


## Request Syntax



```
POST /2020-05-31/cache-policy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CachePolicyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>`string`</Comment>
   <DefaultTTL>`long`</DefaultTTL>
   <MaxTTL>`long`</MaxTTL>
   <MinTTL>`long`</MinTTL>
   <Name>`string`</Name>
   <ParametersInCacheKeyAndForwardedToOrigin>
      <CookiesConfig>
         <CookieBehavior>`string`</CookieBehavior>
         <Cookies>
            <Items>
               <Name>`string`</Name>
            </Items>
            <Quantity>`integer`</Quantity>
         </Cookies>
      </CookiesConfig>
      <EnableAcceptEncodingBrotli>`boolean`</EnableAcceptEncodingBrotli>
      <EnableAcceptEncodingGzip>`boolean`</EnableAcceptEncodingGzip>
      <HeadersConfig>
         <HeaderBehavior>`string`</HeaderBehavior>
         <Headers>
            <Items>
               <Name>`string`</Name>
            </Items>
            <Quantity>`integer`</Quantity>
         </Headers>
      </HeadersConfig>
      <QueryStringsConfig>
         <QueryStringBehavior>`string`</QueryStringBehavior>
         <QueryStrings>
            <Items>
               <Name>`string`</Name>
            </Items>
            <Quantity>`integer`</Quantity>
         </QueryStrings>
      </QueryStringsConfig>
   </ParametersInCacheKeyAndForwardedToOrigin>
</CachePolicyConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[CachePolicyConfig](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


Root level tag for the CachePolicyConfig parameters.


Required: Yes




**[Comment](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


A comment to describe the cache policy. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[DefaultTTL](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


The default amount of time, in seconds, that you want objects to stay in the CloudFront
 cache before CloudFront sends another request to the origin to see if the object has been
 updated. CloudFront uses this value as the object's time to live (TTL) only when the origin
 does *not* send `Cache-Control` or `Expires`
 headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md") in the
 *Amazon CloudFront Developer Guide*.


The default value for this field is 86400 seconds (one day). If the value of
 `MinTTL` is more than 86400 seconds, then the default value for this
 field is the same as the value of `MinTTL`.


Type: Long


Required: No




**[MaxTTL](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


The maximum amount of time, in seconds, that objects stay in the CloudFront cache before
 CloudFront sends another request to the origin to see if the object has been updated. CloudFront
 uses this value only when the origin sends `Cache-Control` or
 `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md") in the
 *Amazon CloudFront Developer Guide*.


The default value for this field is 31536000 seconds (one year). If the value of
 `MinTTL` or `DefaultTTL` is more than 31536000 seconds, then
 the default value for this field is the same as the value of
 `DefaultTTL`.


Type: Long


Required: No




**[MinTTL](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


The minimum amount of time, in seconds, that you want objects to stay in the CloudFront
 cache before CloudFront sends another request to the origin to see if the object has been
 updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md") in the
 *Amazon CloudFront Developer Guide*.


Type: Long


Required: Yes




**[Name](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


A unique name to identify the cache policy.


Type: String


Required: Yes




**[ParametersInCacheKeyAndForwardedToOrigin](#API_CreateCachePolicy_RequestSyntax "#API_CreateCachePolicy_RequestSyntax")**


The HTTP headers, cookies, and URL query strings to include in the cache key. The values
 included in the cache key are also included in requests that CloudFront sends to the
 origin.


Type: [ParametersInCacheKeyAndForwardedToOrigin](API_ParametersInCacheKeyAndForwardedToOrigin.md "API_ParametersInCacheKeyAndForwardedToOrigin.md") object


Required: No




## Response Syntax



```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<CachePolicy>
   <CachePolicyConfig>
      <Comment>***string***</Comment>
      <DefaultTTL>***long***</DefaultTTL>
      <MaxTTL>***long***</MaxTTL>
      <MinTTL>***long***</MinTTL>
      <Name>***string***</Name>
      <ParametersInCacheKeyAndForwardedToOrigin>
         <CookiesConfig>
            <CookieBehavior>***string***</CookieBehavior>
            <Cookies>
               <Items>
                  <Name>***string***</Name>
               </Items>
               <Quantity>***integer***</Quantity>
            </Cookies>
         </CookiesConfig>
         <EnableAcceptEncodingBrotli>***boolean***</EnableAcceptEncodingBrotli>
         <EnableAcceptEncodingGzip>***boolean***</EnableAcceptEncodingGzip>
         <HeadersConfig>
            <HeaderBehavior>***string***</HeaderBehavior>
            <Headers>
               <Items>
                  <Name>***string***</Name>
               </Items>
               <Quantity>***integer***</Quantity>
            </Headers>
         </HeadersConfig>
         <QueryStringsConfig>
            <QueryStringBehavior>***string***</QueryStringBehavior>
            <QueryStrings>
               <Items>
                  <Name>***string***</Name>
               </Items>
               <Quantity>***integer***</Quantity>
            </QueryStrings>
         </QueryStringsConfig>
      </ParametersInCacheKeyAndForwardedToOrigin>
   </CachePolicyConfig>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
</CachePolicy>
```

## Response Elements


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[CachePolicy](#API_CreateCachePolicy_ResponseSyntax "#API_CreateCachePolicy_ResponseSyntax")**


Root level tag for the CachePolicy parameters.


Required: Yes




**[CachePolicyConfig](#API_CreateCachePolicy_ResponseSyntax "#API_CreateCachePolicy_ResponseSyntax")**


The cache policy configuration.


Type: [CachePolicyConfig](API_CachePolicyConfig.md "API_CachePolicyConfig.md") object




**[Id](#API_CreateCachePolicy_ResponseSyntax "#API_CreateCachePolicy_ResponseSyntax")**


The unique identifier for the cache policy.


Type: String




**[LastModifiedTime](#API_CreateCachePolicy_ResponseSyntax "#API_CreateCachePolicy_ResponseSyntax")**


The date and time when the cache policy was last modified.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**CachePolicyAlreadyExists** 


A cache policy with this name already exists. You must provide a unique name. To
 modify an existing cache policy, use `UpdateCachePolicy`.


HTTP Status Code: 409




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**TooManyCachePolicies** 


You have reached the maximum number of cache policies for this AWS account. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyCookiesInCachePolicy** 


The number of cookies in the cache policy exceeds the maximum. For more information,
 see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyHeadersInCachePolicy** 


The number of headers in the cache policy exceeds the maximum. For more information,
 see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyQueryStringsInCachePolicy** 


The number of query strings in the cache policy exceeds the maximum. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateCachePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateCachePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateCachePolicy")

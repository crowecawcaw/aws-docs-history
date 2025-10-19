# GetCachePolicyConfig

Gets a cache policy configuration.

To get a cache policy configuration, you must provide the policy's identifier. If the
 cache policy is attached to a distribution's cache behavior, you can get the policy's
 identifier using `ListDistributions` or `GetDistribution`. If the
 cache policy is not attached to a cache behavior, you can get the identifier using
 `ListCachePolicies`.


## Request Syntax



```
GET /2020-05-31/cache-policy/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetCachePolicyConfig_RequestSyntax "#API_GetCachePolicyConfig_RequestSyntax")**


The unique identifier for the cache policy. If the cache policy is attached to a
 distribution's cache behavior, you can get the policy's identifier using
 `ListDistributions` or `GetDistribution`. If the cache policy
 is not attached to a cache behavior, you can get the identifier using
 `ListCachePolicies`.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
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
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CachePolicyConfig](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


Root level tag for the CachePolicyConfig parameters.


Required: Yes




**[Comment](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


A comment to describe the cache policy. The comment cannot be longer than 128
 characters.


Type: String




**[DefaultTTL](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


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




**[MaxTTL](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


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




**[MinTTL](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


The minimum amount of time, in seconds, that you want objects to stay in the CloudFront
 cache before CloudFront sends another request to the origin to see if the object has been
 updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md") in the
 *Amazon CloudFront Developer Guide*.


Type: Long




**[Name](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


A unique name to identify the cache policy.


Type: String




**[ParametersInCacheKeyAndForwardedToOrigin](#API_GetCachePolicyConfig_ResponseSyntax "#API_GetCachePolicyConfig_ResponseSyntax")**


The HTTP headers, cookies, and URL query strings to include in the cache key. The values
 included in the cache key are also included in requests that CloudFront sends to the
 origin.


Type: [ParametersInCacheKeyAndForwardedToOrigin](API_ParametersInCacheKeyAndForwardedToOrigin.md "API_ParametersInCacheKeyAndForwardedToOrigin.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchCachePolicy** 


The cache policy does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetCachePolicyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetCachePolicyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetCachePolicyConfig")

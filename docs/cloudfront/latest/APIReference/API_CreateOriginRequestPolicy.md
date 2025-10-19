# CreateOriginRequestPolicy

Creates an origin request policy.

After you create an origin request policy, you can attach it to one or more cache
 behaviors. When it's attached to a cache behavior, the origin request policy determines
 the values that CloudFront includes in requests that it sends to the origin. Each request that
 CloudFront sends to the origin includes the following:


* The request body and the URL path (without the domain name) from the viewer
 request.
* The headers that CloudFront automatically includes in every origin request,
 including `Host`, `User-Agent`, and
 `X-Amz-Cf-Id`.
* All HTTP headers, cookies, and URL query strings that are specified in the
 cache policy or the origin request policy. These can include items from the
 viewer request and, in the case of headers, additional ones that are added by
 CloudFront.
CloudFront sends a request when it can't find a valid object in its cache that matches the
 request. If you want to send values to the origin and also include them in the cache
 key, use `CachePolicy`.

For more information about origin request policies, see [Controlling origin requests](../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md "../../../AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.md") in the
 *Amazon CloudFront Developer Guide*.


## Request Syntax



```
POST /2020-05-31/origin-request-policy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<OriginRequestPolicyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>`string`</Comment>
   <CookiesConfig>
      <CookieBehavior>`string`</CookieBehavior>
      <Cookies>
         <Items>
            <Name>`string`</Name>
         </Items>
         <Quantity>`integer`</Quantity>
      </Cookies>
   </CookiesConfig>
   <HeadersConfig>
      <HeaderBehavior>`string`</HeaderBehavior>
      <Headers>
         <Items>
            <Name>`string`</Name>
         </Items>
         <Quantity>`integer`</Quantity>
      </Headers>
   </HeadersConfig>
   <Name>`string`</Name>
   <QueryStringsConfig>
      <QueryStringBehavior>`string`</QueryStringBehavior>
      <QueryStrings>
         <Items>
            <Name>`string`</Name>
         </Items>
         <Quantity>`integer`</Quantity>
      </QueryStrings>
   </QueryStringsConfig>
</OriginRequestPolicyConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[OriginRequestPolicyConfig](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


Root level tag for the OriginRequestPolicyConfig parameters.


Required: Yes




**[Comment](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


A comment to describe the origin request policy. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[CookiesConfig](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


The cookies from viewer requests to include in origin requests.


Type: [OriginRequestPolicyCookiesConfig](API_OriginRequestPolicyCookiesConfig.md "API_OriginRequestPolicyCookiesConfig.md") object


Required: Yes




**[HeadersConfig](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


The HTTP headers to include in origin requests. These can include headers from viewer
 requests and additional headers added by CloudFront.


Type: [OriginRequestPolicyHeadersConfig](API_OriginRequestPolicyHeadersConfig.md "API_OriginRequestPolicyHeadersConfig.md") object


Required: Yes




**[Name](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


A unique name to identify the origin request policy.


Type: String


Required: Yes




**[QueryStringsConfig](#API_CreateOriginRequestPolicy_RequestSyntax "#API_CreateOriginRequestPolicy_RequestSyntax")**


The URL query strings from viewer requests to include in origin requests.


Type: [OriginRequestPolicyQueryStringsConfig](API_OriginRequestPolicyQueryStringsConfig.md "API_OriginRequestPolicyQueryStringsConfig.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<OriginRequestPolicy>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <OriginRequestPolicyConfig>
      <Comment>***string***</Comment>
      <CookiesConfig>
         <CookieBehavior>***string***</CookieBehavior>
         <Cookies>
            <Items>
               <Name>***string***</Name>
            </Items>
            <Quantity>***integer***</Quantity>
         </Cookies>
      </CookiesConfig>
      <HeadersConfig>
         <HeaderBehavior>***string***</HeaderBehavior>
         <Headers>
            <Items>
               <Name>***string***</Name>
            </Items>
            <Quantity>***integer***</Quantity>
         </Headers>
      </HeadersConfig>
      <Name>***string***</Name>
      <QueryStringsConfig>
         <QueryStringBehavior>***string***</QueryStringBehavior>
         <QueryStrings>
            <Items>
               <Name>***string***</Name>
            </Items>
            <Quantity>***integer***</Quantity>
         </QueryStrings>
      </QueryStringsConfig>
   </OriginRequestPolicyConfig>
</OriginRequestPolicy>
```

## Response Elements


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[OriginRequestPolicy](#API_CreateOriginRequestPolicy_ResponseSyntax "#API_CreateOriginRequestPolicy_ResponseSyntax")**


Root level tag for the OriginRequestPolicy parameters.


Required: Yes




**[Id](#API_CreateOriginRequestPolicy_ResponseSyntax "#API_CreateOriginRequestPolicy_ResponseSyntax")**


The unique identifier for the origin request policy.


Type: String




**[LastModifiedTime](#API_CreateOriginRequestPolicy_ResponseSyntax "#API_CreateOriginRequestPolicy_ResponseSyntax")**


The date and time when the origin request policy was last modified.


Type: Timestamp




**[OriginRequestPolicyConfig](#API_CreateOriginRequestPolicy_ResponseSyntax "#API_CreateOriginRequestPolicy_ResponseSyntax")**


The origin request policy configuration.


Type: [OriginRequestPolicyConfig](API_OriginRequestPolicyConfig.md "API_OriginRequestPolicyConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**OriginRequestPolicyAlreadyExists** 


An origin request policy with this name already exists. You must provide a unique
 name. To modify an existing origin request policy, use
 `UpdateOriginRequestPolicy`.


HTTP Status Code: 409




**TooManyCookiesInOriginRequestPolicy** 


The number of cookies in the origin request policy exceeds the maximum. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyHeadersInOriginRequestPolicy** 


The number of headers in the origin request policy exceeds the maximum. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyOriginRequestPolicies** 


You have reached the maximum number of origin request policies for this AWS account.
 For more information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyQueryStringsInOriginRequestPolicy** 


The number of query strings in the origin request policy exceeds the maximum. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateOriginRequestPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateOriginRequestPolicy")

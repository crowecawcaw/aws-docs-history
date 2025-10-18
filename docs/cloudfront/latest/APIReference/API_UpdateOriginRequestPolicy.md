# UpdateOriginRequestPolicy

Updates an origin request policy configuration.

When you update an origin request policy configuration, all the fields are updated
 with the values provided in the request. You cannot update some fields independent of
 others. To update an origin request policy configuration:


1. Use `GetOriginRequestPolicyConfig` to get the current
 configuration.
2. Locally modify the fields in the origin request policy configuration that you
 want to update.
3. Call `UpdateOriginRequestPolicy` by providing the entire origin
 request policy configuration, including the fields that you modified and those
 that you didn't.

## Request Syntax



```
PUT /2020-05-31/origin-request-policy/`Id` HTTP/1.1
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





**[OriginRequestPolicyConfig](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


Root level tag for the OriginRequestPolicyConfig parameters.


Required: Yes




**[Comment](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


A comment to describe the origin request policy. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[CookiesConfig](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


The cookies from viewer requests to include in origin requests.


Type: [OriginRequestPolicyCookiesConfig](API_OriginRequestPolicyCookiesConfig.md "API_OriginRequestPolicyCookiesConfig.md") object


Required: Yes




**[HeadersConfig](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


The HTTP headers to include in origin requests. These can include headers from viewer
 requests and additional headers added by CloudFront.


Type: [OriginRequestPolicyHeadersConfig](API_OriginRequestPolicyHeadersConfig.md "API_OriginRequestPolicyHeadersConfig.md") object


Required: Yes




**[Name](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


A unique name to identify the origin request policy.


Type: String


Required: Yes




**[QueryStringsConfig](#API_UpdateOriginRequestPolicy_RequestSyntax "#API_UpdateOriginRequestPolicy_RequestSyntax")**


The URL query strings from viewer requests to include in origin requests.


Type: [OriginRequestPolicyQueryStringsConfig](API_OriginRequestPolicyQueryStringsConfig.md "API_OriginRequestPolicyQueryStringsConfig.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200
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


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[OriginRequestPolicy](#API_UpdateOriginRequestPolicy_ResponseSyntax "#API_UpdateOriginRequestPolicy_ResponseSyntax")**


Root level tag for the OriginRequestPolicy parameters.


Required: Yes




**[Id](#API_UpdateOriginRequestPolicy_ResponseSyntax "#API_UpdateOriginRequestPolicy_ResponseSyntax")**


The unique identifier for the origin request policy.


Type: String




**[LastModifiedTime](#API_UpdateOriginRequestPolicy_ResponseSyntax "#API_UpdateOriginRequestPolicy_ResponseSyntax")**


The date and time when the origin request policy was last modified.


Type: Timestamp




**[OriginRequestPolicyConfig](#API_UpdateOriginRequestPolicy_ResponseSyntax "#API_UpdateOriginRequestPolicy_ResponseSyntax")**


The origin request policy configuration.


Type: [OriginRequestPolicyConfig](API_OriginRequestPolicyConfig.md "API_OriginRequestPolicyConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**IllegalUpdate** 


The update contains modifications that are not allowed.


HTTP Status Code: 400




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**NoSuchOriginRequestPolicy** 


The origin request policy does not exist.


HTTP Status Code: 404




**OriginRequestPolicyAlreadyExists** 


An origin request policy with this name already exists. You must provide a unique
 name. To modify an existing origin request policy, use
 `UpdateOriginRequestPolicy`.


HTTP Status Code: 409




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




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




**TooManyQueryStringsInOriginRequestPolicy** 


The number of query strings in the origin request policy exceeds the maximum. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateOriginRequestPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateOriginRequestPolicy")

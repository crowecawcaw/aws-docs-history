# GetOriginRequestPolicy

Gets an origin request policy, including the following metadata:


* The policy's identifier.
* The date and time when the policy was last modified.
To get an origin request policy, you must provide the policy's identifier. If the
 origin request policy is attached to a distribution's cache behavior, you can get the
 policy's identifier using `ListDistributions` or
 `GetDistribution`. If the origin request policy is not attached to a cache
 behavior, you can get the identifier using
 `ListOriginRequestPolicies`.


## Request Syntax



```
GET /2020-05-31/origin-request-policy/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetOriginRequestPolicy_RequestSyntax "#API_GetOriginRequestPolicy_RequestSyntax")**


The unique identifier for the origin request policy. If the origin request policy is
 attached to a distribution's cache behavior, you can get the policy's identifier using
 `ListDistributions` or `GetDistribution`. If the origin
 request policy is not attached to a cache behavior, you can get the identifier using
 `ListOriginRequestPolicies`.


Required: Yes




## Request Body


The request does not have a request body.


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





**[OriginRequestPolicy](#API_GetOriginRequestPolicy_ResponseSyntax "#API_GetOriginRequestPolicy_ResponseSyntax")**


Root level tag for the OriginRequestPolicy parameters.


Required: Yes




**[Id](#API_GetOriginRequestPolicy_ResponseSyntax "#API_GetOriginRequestPolicy_ResponseSyntax")**


The unique identifier for the origin request policy.


Type: String




**[LastModifiedTime](#API_GetOriginRequestPolicy_ResponseSyntax "#API_GetOriginRequestPolicy_ResponseSyntax")**


The date and time when the origin request policy was last modified.


Type: Timestamp




**[OriginRequestPolicyConfig](#API_GetOriginRequestPolicy_ResponseSyntax "#API_GetOriginRequestPolicy_ResponseSyntax")**


The origin request policy configuration.


Type: [OriginRequestPolicyConfig](API_OriginRequestPolicyConfig.md "API_OriginRequestPolicyConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchOriginRequestPolicy** 


The origin request policy does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginRequestPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginRequestPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginRequestPolicy")

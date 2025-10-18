# GetResponseHeadersPolicyConfig

Gets a response headers policy configuration.

To get a response headers policy configuration, you must provide the policy's
 identifier. If the response headers policy is attached to a distribution's cache
 behavior, you can get the policy's identifier using `ListDistributions` or
 `GetDistribution`. If the response headers policy is not attached to a
 cache behavior, you can get the identifier using
 `ListResponseHeadersPolicies`.


## Request Syntax



```
GET /2020-05-31/response-headers-policy/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetResponseHeadersPolicyConfig_RequestSyntax "#API_GetResponseHeadersPolicyConfig_RequestSyntax")**


The identifier for the response headers policy.


If the response headers policy is attached to a distribution's cache behavior, you can
 get the policy's identifier using `ListDistributions` or
 `GetDistribution`. If the response headers policy is not attached to a
 cache behavior, you can get the identifier using
 `ListResponseHeadersPolicies`.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ResponseHeadersPolicyConfig>
   <Comment>***string***</Comment>
   <CorsConfig>
      <AccessControlAllowCredentials>***boolean***</AccessControlAllowCredentials>
      <AccessControlAllowHeaders>
         <Items>
            <Header>***string***</Header>
         </Items>
         <Quantity>***integer***</Quantity>
      </AccessControlAllowHeaders>
      <AccessControlAllowMethods>
         <Items>
            <Method>***string***</Method>
         </Items>
         <Quantity>***integer***</Quantity>
      </AccessControlAllowMethods>
      <AccessControlAllowOrigins>
         <Items>
            <Origin>***string***</Origin>
         </Items>
         <Quantity>***integer***</Quantity>
      </AccessControlAllowOrigins>
      <AccessControlExposeHeaders>
         <Items>
            <Header>***string***</Header>
         </Items>
         <Quantity>***integer***</Quantity>
      </AccessControlExposeHeaders>
      <AccessControlMaxAgeSec>***integer***</AccessControlMaxAgeSec>
      <OriginOverride>***boolean***</OriginOverride>
   </CorsConfig>
   <CustomHeadersConfig>
      <Items>
         <ResponseHeadersPolicyCustomHeader>
            <Header>***string***</Header>
            <Override>***boolean***</Override>
            <Value>***string***</Value>
         </ResponseHeadersPolicyCustomHeader>
      </Items>
      <Quantity>***integer***</Quantity>
   </CustomHeadersConfig>
   <Name>***string***</Name>
   <RemoveHeadersConfig>
      <Items>
         <ResponseHeadersPolicyRemoveHeader>
            <Header>***string***</Header>
         </ResponseHeadersPolicyRemoveHeader>
      </Items>
      <Quantity>***integer***</Quantity>
   </RemoveHeadersConfig>
   <SecurityHeadersConfig>
      <ContentSecurityPolicy>
         <ContentSecurityPolicy>***string***</ContentSecurityPolicy>
         <Override>***boolean***</Override>
      </ContentSecurityPolicy>
      <ContentTypeOptions>
         <Override>***boolean***</Override>
      </ContentTypeOptions>
      <FrameOptions>
         <FrameOption>***string***</FrameOption>
         <Override>***boolean***</Override>
      </FrameOptions>
      <ReferrerPolicy>
         <Override>***boolean***</Override>
         <ReferrerPolicy>***string***</ReferrerPolicy>
      </ReferrerPolicy>
      <StrictTransportSecurity>
         <AccessControlMaxAgeSec>***integer***</AccessControlMaxAgeSec>
         <IncludeSubdomains>***boolean***</IncludeSubdomains>
         <Override>***boolean***</Override>
         <Preload>***boolean***</Preload>
      </StrictTransportSecurity>
      <XSSProtection>
         <ModeBlock>***boolean***</ModeBlock>
         <Override>***boolean***</Override>
         <Protection>***boolean***</Protection>
         <ReportUri>***string***</ReportUri>
      </XSSProtection>
   </SecurityHeadersConfig>
   <ServerTimingHeadersConfig>
      <Enabled>***boolean***</Enabled>
      <SamplingRate>***double***</SamplingRate>
   </ServerTimingHeadersConfig>
</ResponseHeadersPolicyConfig>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ResponseHeadersPolicyConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


Root level tag for the ResponseHeadersPolicyConfig parameters.


Required: Yes




**[Comment](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A comment to describe the response headers policy.


The comment cannot be longer than 128 characters.


Type: String




**[CorsConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A configuration for a set of HTTP response headers that are used for cross-origin
 resource sharing (CORS).


Type: [ResponseHeadersPolicyCorsConfig](API_ResponseHeadersPolicyCorsConfig.md "API_ResponseHeadersPolicyCorsConfig.md") object




**[CustomHeadersConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A configuration for a set of custom HTTP response headers.


Type: [ResponseHeadersPolicyCustomHeadersConfig](API_ResponseHeadersPolicyCustomHeadersConfig.md "API_ResponseHeadersPolicyCustomHeadersConfig.md") object




**[Name](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A name to identify the response headers policy.


The name must be unique for response headers policies in this AWS account.


Type: String




**[RemoveHeadersConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A configuration for a set of HTTP headers to remove from the HTTP response.


Type: [ResponseHeadersPolicyRemoveHeadersConfig](API_ResponseHeadersPolicyRemoveHeadersConfig.md "API_ResponseHeadersPolicyRemoveHeadersConfig.md") object




**[SecurityHeadersConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A configuration for a set of security-related HTTP response headers.


Type: [ResponseHeadersPolicySecurityHeadersConfig](API_ResponseHeadersPolicySecurityHeadersConfig.md "API_ResponseHeadersPolicySecurityHeadersConfig.md") object




**[ServerTimingHeadersConfig](#API_GetResponseHeadersPolicyConfig_ResponseSyntax "#API_GetResponseHeadersPolicyConfig_ResponseSyntax")**


A configuration for enabling the `Server-Timing` header in HTTP responses
 sent from CloudFront.


Type: [ResponseHeadersPolicyServerTimingHeadersConfig](API_ResponseHeadersPolicyServerTimingHeadersConfig.md "API_ResponseHeadersPolicyServerTimingHeadersConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchResponseHeadersPolicy** 


The response headers policy does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetResponseHeadersPolicyConfig")

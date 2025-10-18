# ResponseHeadersPolicyConfig

A response headers policy configuration.

A response headers policy configuration contains metadata about the response headers policy,
 and configurations for sets of HTTP response headers.


## Contents





**Name** 


A name to identify the response headers policy.


The name must be unique for response headers policies in this AWS account.


Type: String


Required: Yes




**Comment** 


A comment to describe the response headers policy.


The comment cannot be longer than 128 characters.


Type: String


Required: No




**CorsConfig** 


A configuration for a set of HTTP response headers that are used for cross-origin
 resource sharing (CORS).


Type: [ResponseHeadersPolicyCorsConfig](API_ResponseHeadersPolicyCorsConfig.md "API_ResponseHeadersPolicyCorsConfig.md") object


Required: No




**CustomHeadersConfig** 


A configuration for a set of custom HTTP response headers.


Type: [ResponseHeadersPolicyCustomHeadersConfig](API_ResponseHeadersPolicyCustomHeadersConfig.md "API_ResponseHeadersPolicyCustomHeadersConfig.md") object


Required: No




**RemoveHeadersConfig** 


A configuration for a set of HTTP headers to remove from the HTTP response.


Type: [ResponseHeadersPolicyRemoveHeadersConfig](API_ResponseHeadersPolicyRemoveHeadersConfig.md "API_ResponseHeadersPolicyRemoveHeadersConfig.md") object


Required: No




**SecurityHeadersConfig** 


A configuration for a set of security-related HTTP response headers.


Type: [ResponseHeadersPolicySecurityHeadersConfig](API_ResponseHeadersPolicySecurityHeadersConfig.md "API_ResponseHeadersPolicySecurityHeadersConfig.md") object


Required: No




**ServerTimingHeadersConfig** 


A configuration for enabling the `Server-Timing` header in HTTP responses
 sent from CloudFront.


Type: [ResponseHeadersPolicyServerTimingHeadersConfig](API_ResponseHeadersPolicyServerTimingHeadersConfig.md "API_ResponseHeadersPolicyServerTimingHeadersConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyConfig")

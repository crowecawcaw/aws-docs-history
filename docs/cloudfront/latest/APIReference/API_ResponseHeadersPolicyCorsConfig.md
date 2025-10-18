# ResponseHeadersPolicyCorsConfig

A configuration for a set of HTTP response headers that are used for cross-origin
 resource sharing (CORS). CloudFront adds these headers to HTTP responses that it sends for
 CORS requests that match a cache behavior associated with this response headers
 policy.

For more information about CORS, see [Cross-Origin Resource
 Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS") in the MDN Web Docs.


## Contents





**AccessControlAllowCredentials** 


A Boolean that CloudFront uses as the value for the
 `Access-Control-Allow-Credentials` HTTP response header.


For more information about the `Access-Control-Allow-Credentials` HTTP
 response header, see [Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials") in the MDN Web Docs.


Type: Boolean


Required: Yes




**AccessControlAllowHeaders** 


A list of HTTP header names that CloudFront includes as values for the
 `Access-Control-Allow-Headers` HTTP response header.


For more information about the `Access-Control-Allow-Headers` HTTP response
 header, see [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers") in the MDN Web Docs.


Type: [ResponseHeadersPolicyAccessControlAllowHeaders](API_ResponseHeadersPolicyAccessControlAllowHeaders.md "API_ResponseHeadersPolicyAccessControlAllowHeaders.md") object


Required: Yes




**AccessControlAllowMethods** 


A list of HTTP methods that CloudFront includes as values for the
 `Access-Control-Allow-Methods` HTTP response header.


For more information about the `Access-Control-Allow-Methods` HTTP response
 header, see [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods") in the MDN Web Docs.


Type: [ResponseHeadersPolicyAccessControlAllowMethods](API_ResponseHeadersPolicyAccessControlAllowMethods.md "API_ResponseHeadersPolicyAccessControlAllowMethods.md") object


Required: Yes




**AccessControlAllowOrigins** 


A list of origins (domain names) that CloudFront can use as the value for the
 `Access-Control-Allow-Origin` HTTP response header.


For more information about the `Access-Control-Allow-Origin` HTTP response
 header, see [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin") in the MDN Web Docs.


Type: [ResponseHeadersPolicyAccessControlAllowOrigins](API_ResponseHeadersPolicyAccessControlAllowOrigins.md "API_ResponseHeadersPolicyAccessControlAllowOrigins.md") object


Required: Yes




**OriginOverride** 


A Boolean that determines whether CloudFront overrides HTTP response headers received from
 the origin with the ones specified in this response headers policy.


Type: Boolean


Required: Yes




**AccessControlExposeHeaders** 


A list of HTTP headers that CloudFront includes as values for the
 `Access-Control-Expose-Headers` HTTP response header.


For more information about the `Access-Control-Expose-Headers` HTTP
 response header, see [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers") in the MDN Web Docs.


Type: [ResponseHeadersPolicyAccessControlExposeHeaders](API_ResponseHeadersPolicyAccessControlExposeHeaders.md "API_ResponseHeadersPolicyAccessControlExposeHeaders.md") object


Required: No




**AccessControlMaxAgeSec** 


A number that CloudFront uses as the value for the `Access-Control-Max-Age` HTTP
 response header.


For more information about the `Access-Control-Max-Age` HTTP response
 header, see [Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age") in the MDN Web Docs.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCorsConfig")

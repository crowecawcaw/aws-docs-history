# ResponseHeadersPolicyStrictTransportSecurity

Determines whether CloudFront includes the `Strict-Transport-Security` HTTP
 response header and the header's value.

For more information about the `Strict-Transport-Security` HTTP response
 header, see [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security") in the MDN Web Docs.


## Contents





**AccessControlMaxAgeSec** 


A number that CloudFront uses as the value for the `max-age` directive in the
 `Strict-Transport-Security` HTTP response header.


Type: Integer


Required: Yes




**Override** 


A Boolean that determines whether CloudFront overrides the
 `Strict-Transport-Security` HTTP response header received from the origin
 with the one specified in this response headers policy.


Type: Boolean


Required: Yes




**IncludeSubdomains** 


A Boolean that determines whether CloudFront includes the `includeSubDomains`
 directive in the `Strict-Transport-Security` HTTP response header.


Type: Boolean


Required: No




**Preload** 


A Boolean that determines whether CloudFront includes the `preload` directive in
 the `Strict-Transport-Security` HTTP response header.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity")

# ResponseHeadersPolicyXSSProtection

Determines whether CloudFront includes the `X-XSS-Protection` HTTP response
 header and the header's value.

For more information about the `X-XSS-Protection` HTTP response header, see
 [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection") in the MDN Web Docs.


## Contents





**Override** 


A Boolean that determines whether CloudFront overrides the `X-XSS-Protection`
 HTTP response header received from the origin with the one specified in this response
 headers policy.


Type: Boolean


Required: Yes




**Protection** 


A Boolean that determines the value of the `X-XSS-Protection` HTTP response
 header. When this setting is `true`, the value of the
 `X-XSS-Protection` header is `1`. When this setting is
 `false`, the value of the `X-XSS-Protection` header is
 `0`.


For more information about these settings, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection") in the MDN Web Docs.


Type: Boolean


Required: Yes




**ModeBlock** 


A Boolean that determines whether CloudFront includes the `mode=block` directive
 in the `X-XSS-Protection` header.


For more information about this directive, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection") in the MDN Web Docs.


Type: Boolean


Required: No




**ReportUri** 


A reporting URI, which CloudFront uses as the value of the `report` directive in
 the `X-XSS-Protection` header.


You cannot specify a `ReportUri` when `ModeBlock` is
 `true`.


For more information about using a reporting URL, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection") in the MDN Web Docs.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection")

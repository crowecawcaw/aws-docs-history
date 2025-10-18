# ResponseHeadersPolicyFrameOptions

Determines whether CloudFront includes the `X-Frame-Options` HTTP response header
 and the header's value.

For more information about the `X-Frame-Options` HTTP response header, see
 [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options") in the MDN Web Docs.


## Contents





**FrameOption** 


The value of the `X-Frame-Options` HTTP response header. Valid values are
 `DENY` and `SAMEORIGIN`.


For more information about these values, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options") in the MDN Web Docs.


Type: String


Valid Values: `DENY | SAMEORIGIN`



Required: Yes




**Override** 


A Boolean that determines whether CloudFront overrides the `X-Frame-Options` HTTP
 response header received from the origin with the one specified in this response headers
 policy.


Type: Boolean


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyFrameOptions")

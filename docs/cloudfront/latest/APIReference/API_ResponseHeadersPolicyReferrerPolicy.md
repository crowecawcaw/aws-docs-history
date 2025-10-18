# ResponseHeadersPolicyReferrerPolicy

Determines whether CloudFront includes the `Referrer-Policy` HTTP response header
 and the header's value.

For more information about the `Referrer-Policy` HTTP response header, see
 [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy") in the MDN Web Docs.


## Contents





**Override** 


A Boolean that determines whether CloudFront overrides the `Referrer-Policy` HTTP
 response header received from the origin with the one specified in this response headers
 policy.


Type: Boolean


Required: Yes




**ReferrerPolicy** 


The value of the `Referrer-Policy` HTTP response header. Valid values
 are:



* `no-referrer`
* `no-referrer-when-downgrade`
* `origin`
* `origin-when-cross-origin`
* `same-origin`
* `strict-origin`
* `strict-origin-when-cross-origin`
* `unsafe-url`

For more information about these values, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy") in the MDN Web Docs.


Type: String


Valid Values: `no-referrer | no-referrer-when-downgrade | origin | origin-when-cross-origin | same-origin | strict-origin | strict-origin-when-cross-origin | unsafe-url`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyReferrerPolicy")

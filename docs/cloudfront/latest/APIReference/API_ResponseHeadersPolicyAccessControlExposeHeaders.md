# ResponseHeadersPolicyAccessControlExposeHeaders

A list of HTTP headers that CloudFront includes as values for the
 `Access-Control-Expose-Headers` HTTP response header.

For more information about the `Access-Control-Expose-Headers` HTTP
 response header, see [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers") in the MDN Web Docs.


## Contents





**Quantity** 


The number of HTTP headers in the list.


Type: Integer


Required: Yes




**Items** 


The list of HTTP headers. You can specify `*` to expose all headers.


Type: Array of strings


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders")

# ResponseHeadersPolicyCustomHeader

An HTTP response header name and its value. CloudFront includes this header in HTTP
 responses that it sends for requests that match a cache behavior that's associated with
 this response headers policy.


## Contents





**Header** 


The HTTP response header name.


Type: String


Required: Yes




**Override** 


A Boolean that determines whether CloudFront overrides a response header with the same name
 received from the origin with the header specified here.


Type: Boolean


Required: Yes




**Value** 


The value for the HTTP response header.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader")

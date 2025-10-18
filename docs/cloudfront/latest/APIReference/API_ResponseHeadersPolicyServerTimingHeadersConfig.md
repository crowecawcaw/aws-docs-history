# ResponseHeadersPolicyServerTimingHeadersConfig

A configuration for enabling the `Server-Timing` header in HTTP responses
 sent from CloudFront. CloudFront adds this header to HTTP responses that it sends in response to
 requests that match a cache behavior that's associated with this response headers
 policy.

You can use the `Server-Timing` header to view metrics that can help you
 gain insights about the behavior and performance of CloudFront. For example, you can see which
 cache layer served a cache hit, or the first byte latency from the origin when there was
 a cache miss. You can use the metrics in the `Server-Timing` header to
 troubleshoot issues or test the efficiency of your CloudFront configuration. For more
 information, see [Server-Timing header](../../../AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.md#server-timing-header "../../../AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.md#server-timing-header") in the
 *Amazon CloudFront Developer Guide*.


## Contents





**Enabled** 


A Boolean that determines whether CloudFront adds the `Server-Timing` header to
 HTTP responses that it sends in response to requests that match a cache behavior that's
 associated with this response headers policy.


Type: Boolean


Required: Yes




**SamplingRate** 


A number 0–100 (inclusive) that specifies the percentage of responses that you want
 CloudFront to add the `Server-Timing` header to. When you set the sampling rate to
 100, CloudFront adds the `Server-Timing` header to the HTTP response for every
 request that matches the cache behavior that this response headers policy is attached
 to. When you set it to 50, CloudFront adds the header to 50% of the responses for requests
 that match the cache behavior. You can set the sampling rate to any number 0–100 with up
 to four decimal places.


Type: Double


Valid Range: Minimum value of 0.0. Maximum value of 100.0.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig")

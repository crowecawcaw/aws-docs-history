# SessionStickinessConfig

Session stickiness provides the ability to define multiple requests from a single
 viewer as a single session. This prevents the potentially inconsistent experience of
 sending some of a given user's requests to your staging distribution, while others are
 sent to your primary distribution. Define the session duration using TTL values.


## Contents





**IdleTTL** 


The amount of time after which you want sessions to cease if no requests are
 received. Allowed values are 300–3600 seconds (5–60 minutes).


The value must be less than or equal to `MaximumTTL`.


Type: Integer


Required: Yes




**MaximumTTL** 


The maximum amount of time to consider requests from the viewer as being part of the
 same session. Allowed values are 300–3600 seconds (5–60 minutes).


The value must be greater than or equal to `IdleTTL`.


Type: Integer


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/SessionStickinessConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/SessionStickinessConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/SessionStickinessConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/SessionStickinessConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/SessionStickinessConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/SessionStickinessConfig")

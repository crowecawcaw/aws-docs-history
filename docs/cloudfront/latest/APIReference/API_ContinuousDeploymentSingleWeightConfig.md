# ContinuousDeploymentSingleWeightConfig

Contains the percentage of traffic to send to a staging distribution.


## Contents





**Weight** 


The percentage of traffic to send to a staging distribution, expressed as a decimal
 number between 0 and 0.15. For example, a value of 0.10 means 10% of traffic is sent to the staging distribution.


Type: Float


Required: Yes




**SessionStickinessConfig** 


Session stickiness provides the ability to define multiple requests from a single
 viewer as a single session. This prevents the potentially inconsistent experience of
 sending some of a given user's requests to your staging distribution, while others are
 sent to your primary distribution. Define the session duration using TTL values.


Type: [SessionStickinessConfig](API_SessionStickinessConfig.md "API_SessionStickinessConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentSingleWeightConfig")

# ContinuousDeploymentPolicyConfig

Contains the configuration for a continuous deployment policy.


## Contents





**Enabled** 


A Boolean that indicates whether this continuous deployment policy is enabled (in
 effect). When this value is `true`, this policy is enabled and in effect.
 When this value is `false`, this policy is not enabled and has no
 effect.


Type: Boolean


Required: Yes




**StagingDistributionDnsNames** 


The CloudFront domain name of the staging distribution. For example:
 `d111111abcdef8.cloudfront.net`.


Type: [StagingDistributionDnsNames](API_StagingDistributionDnsNames.md "API_StagingDistributionDnsNames.md") object


Required: Yes




**TrafficConfig** 


Contains the parameters for routing production traffic from your primary to staging
 distributions.


Type: [TrafficConfig](API_TrafficConfig.md "API_TrafficConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyConfig")

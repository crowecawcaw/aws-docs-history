# TrafficConfig

The traffic configuration of your continuous deployment.


## Contents





**Type** 


The type of traffic configuration.


Type: String


Valid Values: `SingleWeight | SingleHeader`



Required: Yes




**SingleHeaderConfig** 


Determines which HTTP requests are sent to the staging distribution.


Type: [ContinuousDeploymentSingleHeaderConfig](API_ContinuousDeploymentSingleHeaderConfig.md "API_ContinuousDeploymentSingleHeaderConfig.md") object


Required: No




**SingleWeightConfig** 


Contains the percentage of traffic to send to the staging distribution.


Type: [ContinuousDeploymentSingleWeightConfig](API_ContinuousDeploymentSingleWeightConfig.md "API_ContinuousDeploymentSingleWeightConfig.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrafficConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TrafficConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrafficConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TrafficConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrafficConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TrafficConfig")

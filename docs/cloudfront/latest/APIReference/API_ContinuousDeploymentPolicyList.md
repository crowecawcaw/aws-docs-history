# ContinuousDeploymentPolicyList

Contains a list of continuous deployment policies.


## Contents





**MaxItems** 


The maximum number of continuous deployment policies that were specified in your
 request.


Type: Integer


Required: Yes




**Quantity** 


The total number of continuous deployment policies in your AWS account, regardless
 of the `MaxItems` value.


Type: Integer


Required: Yes




**Items** 


A list of continuous deployment policy items.


Type: Array of [ContinuousDeploymentPolicySummary](API_ContinuousDeploymentPolicySummary.md "API_ContinuousDeploymentPolicySummary.md") objects


Required: No




**NextMarker** 


Indicates the next page of continuous deployment policies. To get the next page of the
 list, use this value in the `Marker` field of your request.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContinuousDeploymentPolicyList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContinuousDeploymentPolicyList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContinuousDeploymentPolicyList")

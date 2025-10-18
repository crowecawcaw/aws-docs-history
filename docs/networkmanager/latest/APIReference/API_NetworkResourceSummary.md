# NetworkResourceSummary

Describes a network resource.


## Contents





**Definition** 


Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**IsMiddlebox** 


Indicates whether this is a middlebox appliance.


Type: Boolean


Required: No




**NameTag** 


The value for the Name tag.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**RegisteredGatewayArn** 


The ARN of the gateway.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceType** 


The resource type.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResourceSummary "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResourceSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResourceSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResourceSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResourceSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResourceSummary")

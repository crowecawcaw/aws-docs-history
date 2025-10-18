# CoreNetworkPolicyVersion

Describes a core network policy version.


## Contents





**Alias** 


Whether a core network policy is the current policy or the most recently submitted policy.


Type: String


Valid Values: `LIVE | LATEST`



Required: No




**ChangeSetState** 


The status of the policy version change set.


Type: String


Valid Values: `PENDING_GENERATION | FAILED_GENERATION | READY_TO_EXECUTE | EXECUTING | EXECUTION_SUCCEEDED | OUT_OF_DATE`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when a core network policy version was created.


Type: Timestamp


Required: No




**Description** 


The description of a core network policy version.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**PolicyVersionId** 


The ID of the policy version.


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkPolicyVersion "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkPolicyVersion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkPolicyVersion "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkPolicyVersion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkPolicyVersion "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkPolicyVersion")

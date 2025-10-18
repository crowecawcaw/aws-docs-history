# CoreNetworkChange

Details describing a core network change.


## Contents





**Action** 


The action to take for a core network.


Type: String


Valid Values: `ADD | MODIFY | REMOVE`



Required: No




**Identifier** 


The resource identifier.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**IdentifierPath** 


Uniquely identifies the path for a change within the changeset. For example, the `IdentifierPath` for a core network segment change might be `"CORE_NETWORK_SEGMENT/us-east-1/devsegment"`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**NewValues** 


The new value for a core network


Type: [CoreNetworkChangeValues](API_CoreNetworkChangeValues.md "API_CoreNetworkChangeValues.md") object


Required: No




**PreviousValues** 


The previous values for a core network.


Type: [CoreNetworkChangeValues](API_CoreNetworkChangeValues.md "API_CoreNetworkChangeValues.md") object


Required: No




**Type** 


The type of change.


Type: String


Valid Values: `CORE_NETWORK_SEGMENT | NETWORK_FUNCTION_GROUP | CORE_NETWORK_EDGE | ATTACHMENT_MAPPING | ATTACHMENT_ROUTE_PROPAGATION | ATTACHMENT_ROUTE_STATIC | CORE_NETWORK_CONFIGURATION | SEGMENTS_CONFIGURATION | SEGMENT_ACTIONS_CONFIGURATION | ATTACHMENT_POLICIES_CONFIGURATION`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChange "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChange")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChange "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChange")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChange "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChange")

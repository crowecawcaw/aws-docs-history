# CoreNetwork

Describes a core network.


## Contents





**CoreNetworkArn** 


The ARN of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when a core network was created.


Type: Timestamp


Required: No




**Description** 


The description of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Edges** 


The edges within a core network.


Type: Array of [CoreNetworkEdge](API_CoreNetworkEdge.md "API_CoreNetworkEdge.md") objects


Required: No




**GlobalNetworkId** 


The ID of the global network that your core network is a part of. 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**NetworkFunctionGroups** 


The network function groups associated with a core network.


Type: Array of [CoreNetworkNetworkFunctionGroup](API_CoreNetworkNetworkFunctionGroup.md "API_CoreNetworkNetworkFunctionGroup.md") objects


Required: No




**Segments** 


The segments within a core network.


Type: Array of [CoreNetworkSegment](API_CoreNetworkSegment.md "API_CoreNetworkSegment.md") objects


Required: No




**State** 


The current state of a core network.


Type: String


Valid Values: `CREATING | UPDATING | AVAILABLE | DELETING`



Required: No




**Tags** 


The list of key-value tags associated with a core network.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetwork "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetwork")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetwork "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetwork")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetwork "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetwork")

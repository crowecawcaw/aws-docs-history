# CoreNetworkChangeValues

Describes a core network change.


## Contents





**Asn** 


The ASN of a core network.


Type: Long


Required: No




**Cidr** 


The IP addresses used for a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**DestinationIdentifier** 


The ID of the destination.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**DnsSupport** 


Indicates whether public DNS support is supported. The default is `true`. 


Type: Boolean


Required: No




**EdgeLocations** 


The Regions where edges are located in a core network. 


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**InsideCidrBlocks** 


The inside IP addresses used for core network change values.


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**NetworkFunctionGroupName** 


The network function group name if the change event is associated with a network function group.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SecurityGroupReferencingSupport** 


Indicates whether security group referencing is enabled for the core network.


Type: Boolean


Required: No




**SegmentName** 


The names of the segments in a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**ServiceInsertionActions** 


Describes the service insertion action. 


Type: Array of [ServiceInsertionAction](API_ServiceInsertionAction.md "API_ServiceInsertionAction.md") objects


Required: No




**SharedSegments** 


The shared segments for a core network change value. 


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**VpnEcmpSupport** 


Indicates whether Equal Cost Multipath (ECMP) is enabled for the core network.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeValues "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeValues")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeValues "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeValues")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeValues "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeValues")

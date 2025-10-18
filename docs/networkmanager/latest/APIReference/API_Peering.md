# Peering

Describes a peering connection.


## Contents





**CoreNetworkArn** 


The ARN of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**CoreNetworkId** 


The ID of the core network for the peering request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when the attachment peer was created.


Type: Timestamp


Required: No




**EdgeLocation** 


The edge location for the peer.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**LastModificationErrors** 


Describes the error associated with the Connect peer request.


Type: Array of [PeeringError](API_PeeringError.md "API_PeeringError.md") objects


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Required: No




**OwnerAccountId** 


The ID of the account owner.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`



Required: No




**PeeringId** 


The ID of the peering attachment. 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^peering-([0-9a-f]{8,17})$`



Required: No




**PeeringType** 


The type of peering. This will be `TRANSIT_GATEWAY`.


Type: String


Valid Values: `TRANSIT_GATEWAY`



Required: No




**ResourceArn** 


The resource ARN of the peer.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**State** 


The current state of the peering connection. 


Type: String


Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`



Required: No




**Tags** 


The list of key-value tags associated with the peering.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Peering "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Peering")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Peering "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Peering")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Peering "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Peering")

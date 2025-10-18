# ConnectPeer

Describes a core network Connect peer.


## Contents





**Configuration** 


The configuration of the Connect peer.


Type: [ConnectPeerConfiguration](API_ConnectPeerConfiguration.md "API_ConnectPeerConfiguration.md") object


Required: No




**ConnectAttachmentId** 


The ID of the attachment to connect.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: No




**ConnectPeerId** 


The ID of the Connect peer.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^connect-peer-([0-9a-f]{8,17})$`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when the Connect peer was created.


Type: Timestamp


Required: No




**EdgeLocation** 


The Connect peer Regions where edges are located.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**LastModificationErrors** 


Describes the error associated with the attachment request.


Type: Array of [ConnectPeerError](API_ConnectPeerError.md "API_ConnectPeerError.md") objects


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Required: No




**State** 


The state of the Connect peer.


Type: String


Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`



Required: No




**SubnetArn** 


The subnet ARN for the Connect peer. This only applies only when the protocol is NO\_ENCAP.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`



Required: No




**Tags** 


The list of key-value tags associated with the Connect peer.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeer "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeer")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeer "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeer")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeer "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeer")

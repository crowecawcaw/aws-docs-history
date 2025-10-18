# ConnectPeerSummary

Summary description of a Connect peer.


## Contents





**ConnectAttachmentId** 


The ID of a Connect peer attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: No




**ConnectPeerId** 


The ID of a Connect peer.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^connect-peer-([0-9a-f]{8,17})$`



Required: No




**ConnectPeerState** 


The state of a Connect peer.


Type: String


Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when a Connect peer was created.


Type: Timestamp


Required: No




**EdgeLocation** 


The Region where the edge is located.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**SubnetArn** 


The subnet ARN for the Connect peer summary.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`



Required: No




**Tags** 


The list of key-value tags associated with the Connect peer summary.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerSummary "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerSummary")

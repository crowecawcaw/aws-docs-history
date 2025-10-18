# ConnectPeerConfiguration

Describes a core network Connect peer configuration.


## Contents





**BgpConfigurations** 


The Connect peer BGP configurations.


Type: Array of [ConnectPeerBgpConfiguration](API_ConnectPeerBgpConfiguration.md "API_ConnectPeerBgpConfiguration.md") objects


Required: No




**CoreNetworkAddress** 


The IP address of a core network.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**InsideCidrBlocks** 


The inside IP addresses used for a Connect peer configuration.


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**PeerAddress** 


The IP address of the Connect peer.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**Protocol** 


The protocol used for a Connect peer configuration.


Type: String


Valid Values: `GRE | NO_ENCAP`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectPeerConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectPeerConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectPeerConfiguration")

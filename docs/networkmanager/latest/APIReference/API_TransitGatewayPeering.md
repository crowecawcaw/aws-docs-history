# TransitGatewayPeering

Describes a transit gateway peering attachment.


## Contents





**Peering** 


Describes a transit gateway peer connection.


Type: [Peering](API_Peering.md "API_Peering.md") object


Required: No




**TransitGatewayArn** 


The ARN of the transit gateway.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**TransitGatewayPeeringAttachmentId** 


The ID of the transit gateway peering attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^tgw-attach-([0-9a-f]{8,17})$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayPeering "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayPeering")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayPeering "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayPeering")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayPeering "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayPeering")

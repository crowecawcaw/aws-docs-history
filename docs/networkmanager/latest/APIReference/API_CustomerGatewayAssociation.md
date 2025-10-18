# CustomerGatewayAssociation

Describes the association between a customer gateway, a device, and a link.


## Contents





**CustomerGatewayArn** 


The Amazon Resource Name (ARN) of the customer gateway.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**DeviceId** 


The ID of the device.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**GlobalNetworkId** 


The ID of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**LinkId** 


The ID of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The association state.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | DELETED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CustomerGatewayAssociation "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CustomerGatewayAssociation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CustomerGatewayAssociation "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CustomerGatewayAssociation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CustomerGatewayAssociation "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CustomerGatewayAssociation")

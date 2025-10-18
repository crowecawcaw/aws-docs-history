# TransitGatewayRouteTableAttachment

Describes a transit gateway route table attachment.


## Contents





**Attachment** 


Describes a core network attachment.


Type: [Attachment](API_Attachment.md "API_Attachment.md") object


Required: No




**PeeringId** 


The ID of the peering attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^peering-([0-9a-f]{8,17})$`



Required: No




**TransitGatewayRouteTableArn** 


The ARN of the transit gateway attachment route table. For example, `"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayRouteTableAttachment")

# RouteTableIdentifier

Describes a route table.


## Contents





**CoreNetworkNetworkFunctionGroup** 


The route table identifier associated with the network function group.


Type: [CoreNetworkNetworkFunctionGroupIdentifier](API_CoreNetworkNetworkFunctionGroupIdentifier.md "API_CoreNetworkNetworkFunctionGroupIdentifier.md") object


Required: No




**CoreNetworkSegmentEdge** 


The segment edge in a core network.


Type: [CoreNetworkSegmentEdgeIdentifier](API_CoreNetworkSegmentEdgeIdentifier.md "API_CoreNetworkSegmentEdgeIdentifier.md") object


Required: No




**TransitGatewayRouteTableArn** 


The ARN of the transit gateway route table for the attachment request. For example, `"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteTableIdentifier "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RouteTableIdentifier")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteTableIdentifier "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RouteTableIdentifier")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteTableIdentifier "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RouteTableIdentifier")

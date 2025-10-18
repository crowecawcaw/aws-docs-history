# NetworkResource

Describes a network resource.


## Contents





**AccountId** 


The AWS account ID.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`



Required: No




**AwsRegion** 


The AWS Region.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**Definition** 


Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**DefinitionTimestamp** 


The time that the resource definition was retrieved.


Type: Timestamp


Required: No




**Metadata** 


The resource metadata.


Type: String to string map


Key Length Constraints: Minimum length of 0. Maximum length of 256.


Key Pattern: `[\s\S]*`



Value Length Constraints: Minimum length of 0. Maximum length of 256.


Value Pattern: `[\s\S]*`



Required: No




**RegisteredGatewayArn** 


The ARN of the gateway.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**ResourceId** 


The ID of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**ResourceType** 


The resource type.


The following are the supported resource types for AWS Direct Connect:



* `dxcon`
* `dx-gateway`
* `dx-vif`

The following are the supported resource types for Network Manager:



* `attachment`
* `connect-peer`
* `connection`
* `core-network`
* `device`
* `link`
* `peering`
* `site`

The following are the supported resource types for Amazon VPC:



* `customer-gateway`
* `transit-gateway`
* `transit-gateway-attachment`
* `transit-gateway-connect-peer`
* `transit-gateway-route-table`
* `vpn-connection`

Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Tags** 


The tags.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResource "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkResource")

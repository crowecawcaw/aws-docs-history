# NetworkRoute

Describes a network route.


## Contents





**DestinationCidrBlock** 


A unique identifier for the route, such as a CIDR block.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Destinations** 


The destinations.


Type: Array of [NetworkRouteDestination](API_NetworkRouteDestination.md "API_NetworkRouteDestination.md") objects


Required: No




**PrefixListId** 


The ID of the prefix list.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**State** 


The route state. The possible values are `active` and `blackhole`.


Type: String


Valid Values: `ACTIVE | BLACKHOLE`



Required: No




**Type** 


The route type. The possible values are `propagated` and `static`.


Type: String


Valid Values: `PROPAGATED | STATIC`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRoute "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRoute")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRoute "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRoute")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRoute "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRoute")

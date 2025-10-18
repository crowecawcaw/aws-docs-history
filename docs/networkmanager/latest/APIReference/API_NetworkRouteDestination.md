# NetworkRouteDestination

Describes the destination of a network route.


## Contents





**CoreNetworkAttachmentId** 


The ID of a core network attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: No




**EdgeLocation** 


The edge location for the network destination.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**NetworkFunctionGroupName** 


The network function group name associated with the destination.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


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


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SegmentName** 


The name of the segment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**TransitGatewayAttachmentId** 


The ID of the transit gateway attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRouteDestination "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRouteDestination")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRouteDestination "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRouteDestination")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRouteDestination "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRouteDestination")

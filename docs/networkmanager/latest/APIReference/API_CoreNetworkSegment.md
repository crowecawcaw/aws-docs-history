# CoreNetworkSegment

Describes a core network segment, which are dedicated routes. Only attachments within this segment can communicate with each other.


## Contents





**EdgeLocations** 


The Regions where the edges are located.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**Name** 


The name of a core network segment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SharedSegments** 


The shared segments of a core network.


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkSegment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkSegment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkSegment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkSegment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkSegment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkSegment")

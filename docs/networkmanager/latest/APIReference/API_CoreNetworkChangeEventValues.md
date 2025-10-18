# CoreNetworkChangeEventValues

Describes a core network change event.


## Contents





**AttachmentId** 


The ID of the attachment if the change event is associated with an attachment. 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: No




**Cidr** 


For a `STATIC_ROUTE` event, this is the IP address.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**EdgeLocation** 


The edge location for the core network change event.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**NetworkFunctionGroupName** 


The changed network function group name.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SegmentName** 


The segment name if the change event is associated with a segment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeEventValues "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeEventValues")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeEventValues "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeEventValues")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeEventValues "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeEventValues")

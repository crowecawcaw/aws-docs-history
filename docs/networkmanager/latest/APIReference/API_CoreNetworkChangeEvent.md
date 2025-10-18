# CoreNetworkChangeEvent

Describes a core network change event. This can be a change to a segment, attachment, route, etc.


## Contents





**Action** 


The action taken for the change event.


Type: String


Valid Values: `ADD | MODIFY | REMOVE`



Required: No




**EventTime** 


The timestamp for an event change in status.


Type: Timestamp


Required: No




**IdentifierPath** 


Uniquely identifies the path for a change within the changeset. For example, the `IdentifierPath` for a core network segment change might be `"CORE_NETWORK_SEGMENT/us-east-1/devsegment"`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Status** 


The status of the core network change event.


Type: String


Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETE | FAILED`



Required: No




**Type** 


Describes the type of change event. 


Type: String


Valid Values: `CORE_NETWORK_SEGMENT | NETWORK_FUNCTION_GROUP | CORE_NETWORK_EDGE | ATTACHMENT_MAPPING | ATTACHMENT_ROUTE_PROPAGATION | ATTACHMENT_ROUTE_STATIC | CORE_NETWORK_CONFIGURATION | SEGMENTS_CONFIGURATION | SEGMENT_ACTIONS_CONFIGURATION | ATTACHMENT_POLICIES_CONFIGURATION`



Required: No




**Values** 


Details of the change event.


Type: [CoreNetworkChangeEventValues](API_CoreNetworkChangeEventValues.md "API_CoreNetworkChangeEventValues.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeEvent "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkChangeEvent")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeEvent "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkChangeEvent")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeEvent "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkChangeEvent")

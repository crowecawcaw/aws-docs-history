# ServiceInsertionAction

Describes the action that the service insertion will take for any segments associated with it.


## Contents





**Action** 


The action the service insertion takes for traffic. 
 `send-via` sends east-west traffic between attachments. 
 `send-to` sends north-south traffic to the 
 security appliance, and then from that to either the Internet or to an on-premesis 
 location. 


Type: String


Valid Values: `send-via | send-to`



Required: No




**Mode** 


Describes the mode packets take for the `send-via` action. This is not used when the action is `send-to`. `dual-hop` packets traverse attachments in both the source to the destination core network edges. This mode requires that an inspection attachment must be present in all Regions of the service insertion-enabled segments. 
 For `single-hop`, packets traverse a single intermediate inserted attachment. You can use `EdgeOverride` to specify a specific edge to use. 


Type: String


Valid Values: `dual-hop | single-hop`



Required: No




**Via** 


The list of network function groups and any edge overrides for the chosen service
 insertion action. Used for both `send-to` or `send-via`.


Type: [Via](API_Via.md "API_Via.md") object


Required: No




**WhenSentTo** 


The list of destination segments if the service insertion action is `send-via`.


Type: [WhenSentTo](API_WhenSentTo.md "API_WhenSentTo.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ServiceInsertionAction "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ServiceInsertionAction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ServiceInsertionAction "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ServiceInsertionAction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ServiceInsertionAction "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ServiceInsertionAction")

# Connection

Describes a connection.


## Contents





**ConnectedDeviceId** 


The ID of the second device in the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**ConnectedLinkId** 


The ID of the link for the second device in the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**ConnectionArn** 


The Amazon Resource Name (ARN) of the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**ConnectionId** 


The ID of the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**CreatedAt** 


The date and time that the connection was created.


Type: Timestamp


Required: No




**Description** 


The description of the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**DeviceId** 


The ID of the first device in the connection.


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


The ID of the link for the first device in the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The state of the connection.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`



Required: No




**Tags** 


The tags for the connection.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Connection "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Connection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Connection "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Connection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Connection "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Connection")

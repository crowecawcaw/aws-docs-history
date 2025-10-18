# GlobalNetwork

Describes a global network. This is a single private network acting as a high-level container for your network objects, including an AWS-managed Core Network.


## Contents





**CreatedAt** 


The date and time that the global network was created.


Type: Timestamp


Required: No




**Description** 


The description of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**GlobalNetworkArn** 


The Amazon Resource Name (ARN) of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**GlobalNetworkId** 


The ID of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The state of the global network.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`



Required: No




**Tags** 


The tags for the global network.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GlobalNetwork "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GlobalNetwork")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GlobalNetwork "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GlobalNetwork")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GlobalNetwork "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GlobalNetwork")

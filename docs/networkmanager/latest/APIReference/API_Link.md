# Link

Describes a link.


## Contents





**Bandwidth** 


The bandwidth for the link.


Type: [Bandwidth](API_Bandwidth.md "API_Bandwidth.md") object


Required: No




**CreatedAt** 


The date and time that the link was created.


Type: Timestamp


Required: No




**Description** 


The description of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**GlobalNetworkId** 


The ID of the global network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**LinkArn** 


The Amazon Resource Name (ARN) of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**LinkId** 


The ID of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**Provider** 


The provider of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SiteId** 


The ID of the site.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The state of the link.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`



Required: No




**Tags** 


The tags for the link.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**Type** 


The type of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Link "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Link")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Link "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Link")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Link "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Link")

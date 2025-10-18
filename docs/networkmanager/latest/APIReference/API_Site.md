# Site

Describes a site.


## Contents





**CreatedAt** 


The date and time that the site was created.


Type: Timestamp


Required: No




**Description** 


The description of the site.


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




**Location** 


The location of the site.


Type: [Location](API_Location.md "API_Location.md") object


Required: No




**SiteArn** 


The Amazon Resource Name (ARN) of the site.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**SiteId** 


The ID of the site.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The state of the site.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`



Required: No




**Tags** 


The tags for the site.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Site "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Site")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Site "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Site")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Site "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Site")

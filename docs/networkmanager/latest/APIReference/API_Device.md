# Device

Describes a device.


## Contents





**AWSLocation** 


The AWS location of the device.


Type: [AWSLocation](API_AWSLocation.md "API_AWSLocation.md") object


Required: No




**CreatedAt** 


The date and time that the site was created.


Type: Timestamp


Required: No




**Description** 


The description of the device.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**DeviceArn** 


The Amazon Resource Name (ARN) of the device.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**DeviceId** 


The ID of the device.


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




**Location** 


The site location.


Type: [Location](API_Location.md "API_Location.md") object


Required: No




**Model** 


The device model.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SerialNumber** 


The device serial number.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**SiteId** 


The site ID.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**State** 


The device state.


Type: String


Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`



Required: No




**Tags** 


The tags for the device.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**Type** 


The device type.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Vendor** 


The device vendor.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Device "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Device")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Device "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Device")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Device "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Device")

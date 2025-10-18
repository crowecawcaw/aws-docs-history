# AWSLocation

Specifies a location in AWS.


## Contents





**SubnetArn** 


The Amazon Resource Name (ARN) of the subnet that the device is located in.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`



Required: No




**Zone** 


The Zone that the device is located in. Specify the ID of an Availability Zone, Local
 Zone, Wavelength Zone, or an Outpost.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AWSLocation "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AWSLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AWSLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AWSLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AWSLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AWSLocation")

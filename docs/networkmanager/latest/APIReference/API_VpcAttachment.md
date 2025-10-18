# VpcAttachment

Describes a VPC attachment.


## Contents





**Attachment** 


Provides details about the VPC attachment.


Type: [Attachment](API_Attachment.md "API_Attachment.md") object


Required: No




**Options** 


Provides details about the VPC attachment.


Type: [VpcOptions](API_VpcOptions.md "API_VpcOptions.md") object


Required: No




**SubnetArns** 


The subnet ARNs.


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/VpcAttachment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/VpcAttachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/VpcAttachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/VpcAttachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/VpcAttachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/VpcAttachment")

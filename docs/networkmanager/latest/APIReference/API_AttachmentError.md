# AttachmentError

Describes the error associated with an attachment request.


## Contents





**Code** 


The error code for the attachment request. 


Type: String


Valid Values: `VPC_NOT_FOUND | SUBNET_NOT_FOUND | SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE | SUBNET_NO_FREE_ADDRESSES | SUBNET_UNSUPPORTED_AVAILABILITY_ZONE | SUBNET_NO_IPV6_CIDRS | VPN_CONNECTION_NOT_FOUND | MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED | DIRECT_CONNECT_GATEWAY_NOT_FOUND | DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS | DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF`



Required: No




**Message** 


The message associated with the error `code`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**RequestId** 


The ID of the attachment request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**ResourceArn** 


The ARN of the requested attachment resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AttachmentError "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AttachmentError")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AttachmentError "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AttachmentError")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AttachmentError "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AttachmentError")

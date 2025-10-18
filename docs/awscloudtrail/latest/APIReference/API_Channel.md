# Channel

Contains information about a returned CloudTrail channel.


## Contents





**ChannelArn** 


The Amazon Resource Name (ARN) of a channel.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**Name** 


 The name of the CloudTrail channel. For service-linked channels, the name is
 `aws-service-channel/service-name/custom-suffix` where
 `service-name` represents the name of the AWS service that
 created the channel and `custom-suffix` represents the suffix created by the
 AWS service. 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9._\-]+$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Channel "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Channel")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Channel "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Channel")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Channel "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Channel")

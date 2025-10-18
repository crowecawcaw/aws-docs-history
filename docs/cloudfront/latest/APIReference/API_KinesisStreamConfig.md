# KinesisStreamConfig

Contains information about the Amazon Kinesis data stream where you are sending real-time
 log data.


## Contents





**RoleARN** 


The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that CloudFront can use to
 send real-time log data to your Kinesis data stream.


For more information the IAM role, see [Real-time log configuration IAM role](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-iam-role "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-iam-role") in the
 *Amazon CloudFront Developer Guide*.


Type: String


Required: Yes




**StreamARN** 


The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending
 real-time log data.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KinesisStreamConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KinesisStreamConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KinesisStreamConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KinesisStreamConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KinesisStreamConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KinesisStreamConfig")

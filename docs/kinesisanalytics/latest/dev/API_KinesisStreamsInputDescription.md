After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# KinesisStreamsInputDescription

Describes the Amazon Kinesis stream that is configured as the streaming source in the
application input configuration.

## Contents

**ResourceARN**

Amazon Resource Name (ARN) of the Amazon Kinesis stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

**RoleARN**

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the
stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/KinesisStreamsInputDescription.md")

After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# CloudWatchLoggingOption

Provides a description of CloudWatch logging options, including the log stream Amazon
Resource Name (ARN) and the role ARN.

## Contents

**LogStreamARN**

ARN of the CloudWatch log to receive application messages.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

**RoleARN**

IAM ARN of the role to use to send application messages. Note: To write application
messages to CloudWatch, the IAM role that is used must have the
`PutLogEvents` policy action enabled.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `arn:.*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md "../../../goto/SdkForCpp/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md "../../../goto/SdkForJavaV2/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md "../../../goto/SdkForRubyV3/kinesisanalytics-2015-08-14/CloudWatchLoggingOption.md")

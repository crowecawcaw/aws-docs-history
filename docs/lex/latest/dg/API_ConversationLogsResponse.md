End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ConversationLogsResponse

Contains information about conversation log settings.

## Contents

**iamRoleArn**

The Amazon Resource Name (ARN) of the IAM role used to write your logs
to CloudWatch Logs or an S3 bucket.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

Required: No

**logSettings**

The settings for your conversation logs. You can log text, audio, or
both.

Type: Array of [LogSettingsResponse](API_LogSettingsResponse.md "API_LogSettingsResponse.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/ConversationLogsResponse.md "../../../goto/SdkForCpp/lex-models-2017-04-19/ConversationLogsResponse.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/ConversationLogsResponse.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/ConversationLogsResponse.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/ConversationLogsResponse.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/ConversationLogsResponse.md")

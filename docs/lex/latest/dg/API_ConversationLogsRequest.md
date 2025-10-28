End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ConversationLogsRequest

Provides the settings needed for conversation logs.

## Contents

**iamRoleArn**

The Amazon Resource Name (ARN) of an IAM role with permission to write
to your CloudWatch Logs for text logs and your S3 bucket for audio logs.
If audio encryption is enabled, this role also provides access permission
for the AWS KMS key used for encrypting audio logs. For more information,
see [Creating an
IAM Role and Policy for Conversation Logs](conversation-logs-role-and-policy.md "conversation-logs-role-and-policy.md").

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:[\w\-]+:iam::[\d]{12}:role/.+$`

Required: Yes

**logSettings**

The settings for your conversation logs. You can log the conversation
text, conversation audio, or both.

Type: Array of [LogSettingsRequest](API_LogSettingsRequest.md "API_LogSettingsRequest.md") objects

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/ConversationLogsRequest.md "../../../goto/SdkForCpp/lex-models-2017-04-19/ConversationLogsRequest.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/ConversationLogsRequest.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/ConversationLogsRequest.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/ConversationLogsRequest.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/ConversationLogsRequest.md")

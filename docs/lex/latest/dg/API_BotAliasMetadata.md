End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# BotAliasMetadata

Provides information about a bot alias.

## Contents

**botName**

The name of the bot to which the alias points.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**botVersion**

The version of the Amazon Lex bot to which the alias points.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

**checksum**

Checksum of the bot alias.

Type: String

Required: No

**conversationLogs**

Settings that determine how Amazon Lex uses conversation logs for the
alias.

Type: [ConversationLogsResponse](API_ConversationLogsResponse.md "API_ConversationLogsResponse.md") object

Required: No

**createdDate**

The date that the bot alias was created.

Type: Timestamp

Required: No

**description**

A description of the bot alias.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**lastUpdatedDate**

The date that the bot alias was updated. When you create a
resource, the creation date and last updated date are the same.

Type: Timestamp

Required: No

**name**

The name of the bot alias.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/BotAliasMetadata.md "../../../goto/SdkForCpp/lex-models-2017-04-19/BotAliasMetadata.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotAliasMetadata.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotAliasMetadata.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotAliasMetadata.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotAliasMetadata.md")

End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# BotMetadata

Provides information about a bot. .

## Contents

**createdDate**

The date that the bot was created.

Type: Timestamp

Required: No

**description**

A description of the bot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**lastUpdatedDate**

The date that the bot was updated. When you create a bot, the
creation date and last updated date are the same.

Type: Timestamp

Required: No

**name**

The name of the bot.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**status**

The status of the bot.

Type: String

Valid Values: `BUILDING | READY | READY_BASIC_TESTING | FAILED | NOT_BUILT`

Required: No

**version**

The version of the bot. For a new bot, the version is always
`$LATEST`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/BotMetadata.md "../../../goto/SdkForCpp/lex-models-2017-04-19/BotMetadata.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotMetadata.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotMetadata.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotMetadata.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotMetadata.md")

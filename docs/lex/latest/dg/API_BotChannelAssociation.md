End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# BotChannelAssociation

Represents an association between an Amazon Lex bot and an external
messaging platform.

## Contents

**botAlias**

An alias pointing to the specific version of the Amazon Lex bot to which
this association is being made.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**botConfiguration**

Provides information necessary to communicate with the messaging
platform.

Type: String to string map

Map Entries: Maximum number of 10 items.

Required: No

**botName**

The name of the Amazon Lex bot to which this association is being made.

###### Note

Currently, Amazon Lex supports associations with Facebook and Slack,
and Twilio.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**createdDate**

The date that the association between the Amazon Lex bot and the channel
was created.

Type: Timestamp

Required: No

**description**

A text description of the association you are creating.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**failureReason**

If `status` is `FAILED`, Amazon Lex provides the
reason that it failed to create the association.

Type: String

Required: No

**name**

The name of the association between the bot and the channel.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: No

**status**

The status of the bot channel.

- `CREATED` - The channel has been created and is
  ready for use.
- `IN_PROGRESS` - Channel creation is in
  progress.
- `FAILED` - There was an error creating the channel.
  For information about the reason for the failure, see the
  `failureReason` field.

Type: String

Valid Values: `IN_PROGRESS | CREATED | FAILED`

Required: No

**type**

Specifies the type of association by indicating the type of channel
being established between the Amazon Lex bot and the external messaging
platform.

Type: String

Valid Values: `Facebook | Slack | Twilio-Sms | Kik`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/BotChannelAssociation.md "../../../goto/SdkForCpp/lex-models-2017-04-19/BotChannelAssociation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotChannelAssociation.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/BotChannelAssociation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotChannelAssociation.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/BotChannelAssociation.md")

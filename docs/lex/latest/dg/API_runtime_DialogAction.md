End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# DialogAction

Describes the next action that the bot should take in its interaction
with the user and provides information about the context in which the
action takes place. Use the `DialogAction` data type to set the
interaction to a specific state, or to return the interaction to a
previous state.

## Contents

**type**

The next action that the bot should take in its interaction with the
user. The possible values are:

- `ConfirmIntent` - The next action is asking the user if
  the intent is complete and ready to be fulfilled. This is a yes/no
  question such as "Place the order?"
- `Close` - Indicates that the there will not be a
  response from the user. For example, the statement "Your order has
  been placed" does not require a response.
- `Delegate` - The next action is determined by
  Amazon Lex.
- `ElicitIntent` - The next action is to determine the
  intent that the user wants to fulfill.
- `ElicitSlot` - The next action is to elicit a slot
  value from the user.

Type: String

Valid Values: `ElicitIntent | ConfirmIntent | ElicitSlot | Close | Delegate`

Required: Yes

**fulfillmentState**

The fulfillment state of the intent. The possible values are:

- `Failed` - The Lambda function associated with the
  intent failed to fulfill the intent.
- `Fulfilled` - The intent has fulfilled by the Lambda
  function associated with the intent.
- `ReadyForFulfillment` - All of the information
  necessary for the intent is present and the intent ready to be
  fulfilled by the client application.

Type: String

Valid Values: `Fulfilled | Failed | ReadyForFulfillment`

Required: No

**intentName**

The name of the intent.

Type: String

Required: No

**message**

The message that should be shown to the user. If you don't specify a
message, Amazon Lex will use the message configured for the intent.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

**messageFormat**

- `PlainText` - The message contains plain UTF-8
  text.
- `CustomPayload` - The message is a custom format for
  the client.
- `SSML` - The message contains text formatted for voice
  output.
- `Composite` - The message contains an escaped JSON
  object containing one or more messages. For more information, see
  [Message Groups](howitworks-manage-prompts.md "howitworks-manage-prompts.md").

Type: String

Valid Values: `PlainText | CustomPayload | SSML | Composite`

Required: No

**slots**

Map of the slots that have been gathered and their values.

Type: String to string map

Required: No

**slotToElicit**

The name of the slot that should be elicited from the user.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/DialogAction.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/DialogAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/DialogAction.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/DialogAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/DialogAction.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/DialogAction.md")

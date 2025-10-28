End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Message

The message object that provides the message text and its
type.

## Contents

**content**

The text of the message.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: Yes

**contentType**

The content type of the message string.

Type: String

Valid Values: `PlainText | SSML | CustomPayload`

Required: Yes

**groupNumber**

Identifies the message group that the message belongs to. When a group
is assigned to a message, Amazon Lex returns one message from each group in the
response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 5.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/Message.md "../../../goto/SdkForCpp/lex-models-2017-04-19/Message.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/Message.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/Message.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/Message.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/Message.md")

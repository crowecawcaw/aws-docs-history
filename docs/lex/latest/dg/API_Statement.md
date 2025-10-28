End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Statement

A collection of messages that convey information to the user. At
runtime, Amazon Lex selects the message to convey.

## Contents

**messages**

A collection of message objects.

Type: Array of [Message](API_Message.md "API_Message.md") objects

Array Members: Minimum number of 1 item. Maximum number of 15 items.

Required: Yes

**responseCard**

At runtime, if the client is using the [PostText](API_runtime_PostText.md "API_runtime_PostText.md") API, Amazon Lex includes the response card in the response.
It substitutes all of the session attributes and slot values for
placeholders in the response card.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/Statement.md "../../../goto/SdkForCpp/lex-models-2017-04-19/Statement.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/Statement.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/Statement.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/Statement.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/Statement.md")

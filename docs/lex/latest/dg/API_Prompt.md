End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Prompt

Obtains information from the user. To define a prompt, provide one
or more messages and specify the number of attempts to get information
from the user. If you provide more than one message, Amazon Lex chooses one of
the messages to use to prompt the user. For more information, see [Amazon Lex: How It Works](how-it-works.md "how-it-works.md").

## Contents

**maxAttempts**

The number of times to prompt the user for information.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 5.

Required: Yes

**messages**

An array of objects, each of which provides a message string and
its type. You can specify the message string in plain text or in Speech
Synthesis Markup Language (SSML).

Type: Array of [Message](API_Message.md "API_Message.md") objects

Array Members: Minimum number of 1 item. Maximum number of 15 items.

Required: Yes

**responseCard**

A response card. Amazon Lex uses this prompt at runtime, in the
`PostText` API response. It substitutes session attributes
and slot values for placeholders in the response card. For more
information, see [Using a Response Card](ex-resp-card.md "ex-resp-card.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/Prompt.md "../../../goto/SdkForCpp/lex-models-2017-04-19/Prompt.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/Prompt.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/Prompt.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/Prompt.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/Prompt.md")

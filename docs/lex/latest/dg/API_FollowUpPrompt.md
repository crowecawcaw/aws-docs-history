End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# FollowUpPrompt

A prompt for additional activity after an intent is fulfilled. For
example, after the `OrderPizza` intent is fulfilled, you might
prompt the user to find out whether the user wants to order
drinks.

## Contents

**prompt**

Prompts for information from the user.

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

Required: Yes

**rejectionStatement**

If the user answers "no" to the question defined in the
`prompt` field, Amazon Lex responds with this statement to
acknowledge that the intent was canceled.

Type: [Statement](API_Statement.md "API_Statement.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/FollowUpPrompt.md "../../../goto/SdkForCpp/lex-models-2017-04-19/FollowUpPrompt.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/FollowUpPrompt.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/FollowUpPrompt.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/FollowUpPrompt.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/FollowUpPrompt.md")

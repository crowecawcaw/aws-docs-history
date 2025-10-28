End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ResponseCard

If you configure a response card when creating your bots, Amazon Lex
substitutes the session attributes and slot values that are available, and
then returns it. The response card can also come from a Lambda function (
`dialogCodeHook` and `fulfillmentActivity` on an
intent).

## Contents

**contentType**

The content type of the response.

Type: String

Valid Values: `application/vnd.amazonaws.card.generic`

Required: No

**genericAttachments**

An array of attachment objects representing options.

Type: Array of [GenericAttachment](API_runtime_GenericAttachment.md "API_runtime_GenericAttachment.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: No

**version**

The version of the response card format.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/ResponseCard.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/ResponseCard.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ResponseCard.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ResponseCard.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ResponseCard.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ResponseCard.md")

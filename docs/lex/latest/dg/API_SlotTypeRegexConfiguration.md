End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# SlotTypeRegexConfiguration

Provides a regular expression used to validate the value of a
slot.

## Contents

**pattern**

A regular expression used to validate the value of a slot.

Use a standard regular expression. Amazon Lex supports the following
characters in the regular expression:

- A-Z, a-z
- 0-9
- Unicode characters ("\ u<Unicode>")

Represent Unicode characters with four digits, for example
"\u0041" or "\u005A".

The following regular expression operators are not supported:

- Infinite repeaters: \*, +, or {x,} with no upper bound.
- Wild card (.)

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/SlotTypeRegexConfiguration.md "../../../goto/SdkForCpp/lex-models-2017-04-19/SlotTypeRegexConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotTypeRegexConfiguration.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotTypeRegexConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotTypeRegexConfiguration.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotTypeRegexConfiguration.md")

End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# SlotDefaultValueSpec

Contains the default values for a slot. Default values are used when
Amazon Lex hasn't determined a value for a slot.

## Contents

**defaultValueList**

The default values for a slot. You can specify more than one default.
For example, you can specify a default value to use from a matching
context variable, a session attribute, or a fixed value.

The default value chosen is selected based on the order that you
specify them in the list. For example, if you specify a context variable
and a fixed value in that order, Amazon Lex uses the context variable if it is
available, else it uses the fixed value.

Type: Array of [SlotDefaultValue](API_SlotDefaultValue.md "API_SlotDefaultValue.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/SlotDefaultValueSpec.md "../../../goto/SdkForCpp/lex-models-2017-04-19/SlotDefaultValueSpec.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotDefaultValueSpec.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotDefaultValueSpec.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotDefaultValueSpec.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotDefaultValueSpec.md")

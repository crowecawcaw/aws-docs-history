End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# SlotDefaultValue

A default value for a slot.

## Contents

**defaultValue**

The default value for the slot. You can specify one of the
following:

- `#context-name.slot-name` - The slot value "slot-name"
  in the context "context-name."
- `{attribute}` - The slot value of the session attribute
  "attribute."
- `'value'` - The discrete value "value."

Type: String

Length Constraints: Minimum length of 1. Maximum length of 202.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/SlotDefaultValue.md "../../../goto/SdkForCpp/lex-models-2017-04-19/SlotDefaultValue.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotDefaultValue.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/SlotDefaultValue.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotDefaultValue.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/SlotDefaultValue.md")

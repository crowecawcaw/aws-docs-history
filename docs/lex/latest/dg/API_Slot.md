End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Slot

Identifies the version of a specific slot.

## Contents

**name**

The name of the slot.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z](-|_|.)?)+$`

Required: Yes

**slotConstraint**

Specifies whether the slot is required or optional.

Type: String

Valid Values: `Required | Optional`

Required: Yes

**defaultValueSpec**

A list of default values for the slot. Default values are used when
Amazon Lex hasn't determined a value for a slot. You can specify default values
from context variables, session attributes, and defined values.

Type: [SlotDefaultValueSpec](API_SlotDefaultValueSpec.md "API_SlotDefaultValueSpec.md") object

Required: No

**description**

A description of the slot.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**obfuscationSetting**

Determines whether a slot is obfuscated in conversation logs and
stored utterances. When you obfuscate a slot, the value is replaced by the
slot name in curly braces ({}). For example, if the slot name is
"full_name", obfuscated values are replaced with "{full_name}". For more
information, see [Slot Obfuscation](how-obfuscate.md "how-obfuscate.md") .

Type: String

Valid Values: `NONE | DEFAULT_OBFUSCATION`

Required: No

**priority**

Directs Amazon Lex the order in which to elicit this slot value from
the user. For example, if the intent has two slots with priorities 1 and
2, AWS Amazon Lex first elicits a value for the slot with priority 1.

If multiple slots share the same priority, the order in which Amazon Lex
elicits values is arbitrary.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**responseCard**

A set of possible responses for the slot type used by text-based
clients. A user chooses an option from the response card, instead of using
text to reply.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

Required: No

**sampleUtterances**

If you know a specific pattern with which users might respond to
an Amazon Lex request for a slot value, you can provide those utterances to
improve accuracy. This is optional. In most cases, Amazon Lex is capable of
understanding user utterances.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Length Constraints: Minimum length of 1. Maximum length of 200.

Required: No

**slotType**

The type of the slot, either a custom slot type that you defined or
one of the built-in slot types.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^((AMAZON\.)_?|[A-Za-z]_?)+`

Required: No

**slotTypeVersion**

The version of the slot type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

**valueElicitationPrompt**

The prompt that Amazon Lex uses to elicit the slot value from the
user.

Type: [Prompt](API_Prompt.md "API_Prompt.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/Slot.md "../../../goto/SdkForCpp/lex-models-2017-04-19/Slot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/Slot.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/Slot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/Slot.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/Slot.md")

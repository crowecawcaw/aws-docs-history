End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# EnumerationValue

Each slot type can have a set of values. Each enumeration value
represents a value the slot type can take.

For example, a pizza ordering bot could have a slot type that
specifies the type of crust that the pizza should have. The slot type
could include the values

- thick
- thin
- stuffed

## Contents

**value**

The value of the slot type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 140.

Required: Yes

**synonyms**

Additional values related to the slot type value.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 140.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/EnumerationValue.md "../../../goto/SdkForCpp/lex-models-2017-04-19/EnumerationValue.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/EnumerationValue.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/EnumerationValue.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/EnumerationValue.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/EnumerationValue.md")

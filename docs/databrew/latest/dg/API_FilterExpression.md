# FilterExpression

Represents a structure for defining parameter conditions. Supported conditions are described
here: [Supported
conditions for dynamic datasets](datasets.md#conditions.for.dynamic.datasets "datasets.md#conditions.for.dynamic.datasets") in the
_AWS Glue DataBrew Developer Guide_.

## Contents

###### Note

In the following list, the required parameters are described first.

**Expression**

The expression which includes condition names followed by substitution variables, possibly grouped
and combined with other conditions. For example, "(starts_with :prefix1 or starts_with :prefix2) and
(ends_with :suffix1 or ends_with :suffix2)". Substitution variables should start with ':' symbol.

Type: String

Length Constraints: Minimum length of 4. Maximum length of 1024.

Pattern: `^[<>0-9A-Za-z_.,:)(!= ]+$`

Required: Yes

**ValuesMap**

The map of substitution variable names to their values used in this filter expression.

Type: String to string map

Key Length Constraints: Minimum length of 2. Maximum length of 128.

Key Pattern: `^:[A-Za-z0-9_]+$`

Value Length Constraints: Maximum length of 1024.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/FilterExpression.md "../../../goto/SdkForCpp/databrew-2017-07-25/FilterExpression.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/FilterExpression.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/FilterExpression.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/FilterExpression.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/FilterExpression.md")

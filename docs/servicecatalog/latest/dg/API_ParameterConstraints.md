# ParameterConstraints

The constraints that the administrator has put on the parameter.

## Contents

**AllowedPattern**

A regular expression that represents the patterns that allow for `String` types. The pattern must match the entire parameter value provided.

Type: String

Required: No

**AllowedValues**

The values that the administrator has allowed for the parameter.

Type: Array of strings

Required: No

**ConstraintDescription**

A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of `[A-Za-z0-9]+` displays the following error message when the user specifies an invalid value:

`Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+`

By adding a constraint description, such as must only contain letters (uppercase and lowercase) and numbers, you can display the following customized error message:

`Malformed input-Parameter MyParameter must only contain uppercase and lowercase letters and numbers.`

Type: String

Required: No

**MaxLength**

An integer value that determines the largest number of characters you want to allow for `String` types.

Type: String

Required: No

**MaxValue**

A numeric value that determines the largest numeric value you want to allow for `Number` types.

Type: String

Required: No

**MinLength**

An integer value that determines the smallest number of characters you want to allow for `String` types.

Type: String

Required: No

**MinValue**

A numeric value that determines the smallest numeric value you want to allow for `Number` types.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ParameterConstraints.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ParameterConstraints.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ParameterConstraints.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ParameterConstraints.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ParameterConstraints.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ParameterConstraints.md")

# Rule

Represents a single data quality requirement that should be validated in the
scope of this dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**CheckExpression**

The expression which includes column references, condition names followed by variable
references, possibly grouped and combined with other conditions. For example,
`(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1
 ends_with :suffix1 or :col1 ends_with :suffix2)`. Column and value references
are substitution variables that should start with the ':' symbol. Depending on the
context, substitution variables' values can be either an actual value or a column name.
These values are defined in the SubstitutionMap. If a CheckExpression starts with a
column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors
has been defined, then there should be no column reference in the left side of a
condition, for example, `is_between :val1 and :val2`.

For more information, see [Available checks](profile.md "profile.md")

Type: String

Length Constraints: Minimum length of 4. Maximum length of 1024.

Pattern: `^[<>0-9A-Za-z_.,:)(!= ]+$`

Required: Yes

**Name**

The name of the rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

**ColumnSelectors**

List of column selectors. Selectors can be used to select columns using a name or regular
expression from the dataset. Rule will be applied to selected columns.

Type: Array of [ColumnSelector](API_ColumnSelector.md "API_ColumnSelector.md") objects

Array Members: Minimum number of 1 item.

Required: No

**Disabled**

A value that specifies whether the rule is disabled. Once a rule is
disabled, a profile job will not validate it during a job run. Default
value is false.

Type: Boolean

Required: No

**SubstitutionMap**

The map of substitution variable names to their values used in a check
expression. Variable names should start with a ':' (colon). Variable values can either
be actual values or column names. To differentiate between the two, column names
should be enclosed in backticks, for example, `":col1": "`Column A`".`

Type: String to string map

Key Length Constraints: Minimum length of 2. Maximum length of 128.

Key Pattern: `^:[A-Za-z0-9_]+$`

Value Length Constraints: Maximum length of 1024.

Required: No

**Threshold**

The threshold used with a non-aggregate check expression. Non-aggregate check expressions
will be applied to each row in a specific column, and the threshold will be used to determine
whether the validation succeeds.

Type: [Threshold](API_Threshold.md "API_Threshold.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Rule.md "../../../goto/SdkForCpp/databrew-2017-07-25/Rule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Rule.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Rule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Rule.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Rule.md")

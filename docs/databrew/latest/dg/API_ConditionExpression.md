# ConditionExpression

Represents an individual condition that evaluates to true or false.

Conditions are used with recipe actions. The action is only performed for column values where the
condition evaluates to true.

If a recipe requires more than one condition, then the recipe must specify multiple
`ConditionExpression` elements. Each condition is applied to the rows in a dataset first, before
the recipe action is performed.

## Contents

###### Note

In the following list, the required parameters are described first.

**Condition**

A specific condition to apply to a recipe action. For more information, see [Recipe
structure](recipes.md#recipes.structure "recipes.md#recipes.structure") in the _AWS Glue DataBrew Developer
Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[A-Z\_]+$`

Required: Yes

**TargetColumn**

A column to apply this condition to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**Value**

A value that the condition must evaluate to for the condition to succeed.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ConditionExpression.md "../../../goto/SdkForCpp/databrew-2017-07-25/ConditionExpression.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ConditionExpression.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ConditionExpression.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ConditionExpression.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ConditionExpression.md")

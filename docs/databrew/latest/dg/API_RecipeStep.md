# RecipeStep

Represents a single step from a DataBrew recipe to be performed.

## Contents

###### Note

In the following list, the required parameters are described first.

**Action**

The particular action to be performed in the recipe step.

Type: [RecipeAction](API_RecipeAction.md "API_RecipeAction.md") object

Required: Yes

**ConditionExpressions**

One or more conditions that must be met for the recipe step to succeed.

###### Note

All of the conditions in the array must be met. In other words, all of the
conditions must be combined using a logical AND operation.

Type: Array of [ConditionExpression](API_ConditionExpression.md "API_ConditionExpression.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/RecipeStep.md "../../../goto/SdkForCpp/databrew-2017-07-25/RecipeStep.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeStep.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeStep.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeStep.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeStep.md")

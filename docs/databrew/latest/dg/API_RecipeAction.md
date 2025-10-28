# RecipeAction

Represents a transformation and associated parameters that are used to apply a change
to a DataBrew dataset. For more information, see [Recipe
actions reference](recipe-actions-reference.md "recipe-actions-reference.md").

## Contents

###### Note

In the following list, the required parameters are described first.

**Operation**

The name of a valid DataBrew transformation to be performed on the data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[A-Z\_]+$`

Required: Yes

**Parameters**

Contextual parameters for the transformation.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^[A-Za-z0-9]+$`

Value Length Constraints: Minimum length of 1. Maximum length of 32768.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/RecipeAction.md "../../../goto/SdkForCpp/databrew-2017-07-25/RecipeAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeAction.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeAction.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeAction.md")

# RecipeSummary

Provides a summary of the properties of a recipe. For a complete listing, call the
[DescribeRecipe](API_DescribeRecipe.md "API_DescribeRecipe.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the recipe was created.

Type: Timestamp

Required: No

**domain**

The domain of the recipe (if the recipe is a Domain dataset group use case).

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the recipe was last updated.

Type: Timestamp

Required: No

**name**

The name of the recipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**recipeArn**

The Amazon Resource Name (ARN) of the recipe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the recipe.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/RecipeSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/RecipeSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/RecipeSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/RecipeSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/RecipeSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/RecipeSummary.md")

# Recipe

Represents one or more actions to be performed on a DataBrew dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The unique name for the recipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**CreateDate**

The date and time that the recipe was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who created the recipe.

Type: String

Required: No

**Description**

The description of the recipe.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the recipe.

Type: String

Required: No

**LastModifiedDate**

The last modification date and time of the recipe.

Type: Timestamp

Required: No

**ProjectName**

The name of the project that the recipe is associated with.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**PublishedBy**

The Amazon Resource Name (ARN) of the user who published the recipe.

Type: String

Required: No

**PublishedDate**

The date and time when the recipe was published.

Type: Timestamp

Required: No

**RecipeVersion**

The identifier for the version for the recipe. Must be one of the following:

- Numeric version (`X.Y`) - `X` and `Y` stand
  for major and minor version numbers. The maximum length of each is 6 digits, and
  neither can be negative values. Both `X` and `Y` are
  required, and "0.0" isn't a valid version.
- `LATEST_WORKING` - the most recent valid version being developed in
  a DataBrew project.
- `LATEST_PUBLISHED` - the most recent published version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16.

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) for the recipe.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**Steps**

A list of steps that are defined by the recipe.

Type: Array of [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") objects

Required: No

**Tags**

Metadata tags that have been applied to the recipe.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Recipe.md "../../../goto/SdkForCpp/databrew-2017-07-25/Recipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Recipe.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Recipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Recipe.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Recipe.md")

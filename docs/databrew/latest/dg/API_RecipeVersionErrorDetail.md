# RecipeVersionErrorDetail

Represents any errors encountered when attempting to delete multiple recipe
versions.

## Contents

###### Note

In the following list, the required parameters are described first.

**ErrorCode**

The HTTP status code for the error.

Type: String

Pattern: `^[1-5][0-9][0-9]$`

Required: No

**ErrorMessage**

The text of the error message.

Type: String

Required: No

**RecipeVersion**

The identifier for the recipe version associated with this error.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/RecipeVersionErrorDetail.md "../../../goto/SdkForCpp/databrew-2017-07-25/RecipeVersionErrorDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeVersionErrorDetail.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/RecipeVersionErrorDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeVersionErrorDetail.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/RecipeVersionErrorDetail.md")

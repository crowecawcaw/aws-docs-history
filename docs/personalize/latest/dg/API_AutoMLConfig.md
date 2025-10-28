# AutoMLConfig

When the solution performs AutoML (`performAutoML` is true in
[CreateSolution](API_CreateSolution.md "API_CreateSolution.md")), Amazon Personalize
determines which recipe, from the specified list, optimizes the given metric.
Amazon Personalize then uses that recipe for the solution.

## Contents

**metricName**

The metric to optimize.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**recipeList**

The list of candidate recipes.

Type: Array of strings

Array Members: Maximum number of 100 items.

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/AutoMLConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/AutoMLConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/AutoMLConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/AutoMLConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/AutoMLConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/AutoMLConfig.md")

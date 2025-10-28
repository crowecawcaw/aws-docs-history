# PredictedItem

An object that identifies an item.

The [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") and [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md") APIs return a list of
`PredictedItem`s.

## Contents

**itemId**

The recommended item ID.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**metadata**

Metadata about the item from your Items dataset.

Type: String to string map

Key Length Constraints: Maximum length of 150.

Value Length Constraints: Maximum length of 20000.

Required: No

**promotionName**

The name of the promotion that included the predicted item.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**reason**

If you use User-Personalization-v2, a list of reasons for why the item was included in recommendations. Possible reasons include the following:

- Promoted item - Indicates the item was included as part of a promotion that you applied in your recommendation request.
- Exploration - Indicates the item was included with exploration.
  With exploration, recommendations include items with less interactions data or relevance for the user.
  For more information about exploration, see
  [Exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration").
- Popular item - Indicates the item was included as a placeholder popular item.
  If you use a filter, depending on how many recommendations the filter removes,
  Amazon Personalize might add placeholder items to meet the `numResults` for your
  recommendation request. These items are popular items, based on interactions data, that satisfy your filter criteria.
  They don't have a relevance score for the user.

Type: Array of strings

Length Constraints: Maximum length of 256.

Required: No

**score**

A numeric representation of the model's certainty that the item will be the next user
selection. For more information on scoring logic, see [Recommendation scores](getting-recommendations.md#how-scores-work "getting-recommendations.md#how-scores-work").

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-runtime-2018-05-22/PredictedItem.md "../../../goto/SdkForCpp/personalize-runtime-2018-05-22/PredictedItem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/PredictedItem.md "../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/PredictedItem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/PredictedItem.md "../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/PredictedItem.md")

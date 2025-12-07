# BatchInferenceJobConfig

The configuration details of a batch inference job.

## Contents

**itemExplorationConfig**

A string to string map specifying the exploration configuration hyperparameters, including `explorationWeight` and
`explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when
recommending items.
See [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md").

Type: String to string map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Value Length Constraints: Maximum length of 1000.

Required: No

**rankingInfluence**

A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a
numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has
on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a
value closer to 0.0 reduces its influence. If not specified, both default to 0.0.

Type: String to double map

Valid Keys: `POPULARITY | FRESHNESS`

Valid Range: Minimum value of 0. Maximum value of 1.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/BatchInferenceJobConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/BatchInferenceJobConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchInferenceJobConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/BatchInferenceJobConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchInferenceJobConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/BatchInferenceJobConfig.md")

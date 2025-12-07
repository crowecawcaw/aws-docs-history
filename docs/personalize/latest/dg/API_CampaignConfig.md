# CampaignConfig

The configuration details of a campaign.

## Contents

**enableMetadataWithRecommendations**

Whether metadata with recommendations is enabled for the campaign.
If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response.
For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

Type: Boolean

Required: No

**itemExplorationConfig**

Specifies the exploration configuration hyperparameters, including `explorationWeight` and
`explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when
recommending items. Provide `itemExplorationConfig` data only if your solution uses the
[User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") recipe.

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

**syncWithLatestSolutionVersion**

Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify `True`,
you must specify the ARN of your _solution_ for the `SolutionVersionArn` parameter. It must be in `SolutionArn/$LATEST` format.
The default is `False` and you must manually update the campaign to deploy the latest solution version.

For more information about automatic campaign updates, see
[Enabling automatic campaign updates](campaigns.md#create-campaign-automatic-latest-sv-update "campaigns.md#create-campaign-automatic-latest-sv-update").

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CampaignConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/CampaignConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CampaignConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CampaignConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CampaignConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CampaignConfig.md")

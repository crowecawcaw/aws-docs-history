

# CampaignConfig
<a name="API_CampaignConfig"></a>

The configuration details of a campaign.

## Contents
<a name="API_CampaignConfig_Contents"></a>

 ** enableMetadataWithRecommendations **   <a name="personalize-Type-CampaignConfig-enableMetadataWithRecommendations"></a>
Whether metadata with recommendations is enabled for the campaign. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata).  
 If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).   
Type: Boolean  
Required: No

 ** itemExplorationConfig **   <a name="personalize-Type-CampaignConfig-itemExplorationConfig"></a>
Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your solution uses the [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) recipe.  
Type: String to string map  
Map Entries: Maximum number of 100 items.  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** rankingInfluence **   <a name="personalize-Type-CampaignConfig-rankingInfluence"></a>
A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a value closer to 0.0 reduces its influence. If not specified, both default to 0.0.  
Type: String to double map  
Valid Keys: `POPULARITY | FRESHNESS`   
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** syncWithLatestSolutionVersion **   <a name="personalize-Type-CampaignConfig-syncWithLatestSolutionVersion"></a>
Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify `True`, you must specify the ARN of your *solution* for the `SolutionVersionArn` parameter. It must be in `SolutionArn/$LATEST` format. The default is `False` and you must manually update the campaign to deploy the latest solution version.   
 For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update).   
Type: Boolean  
Required: No

## See Also
<a name="API_CampaignConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/CampaignConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/CampaignConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/CampaignConfig) 


# RecommenderConfig
<a name="API_RecommenderConfig"></a>

The configuration details of the recommender.

## Contents
<a name="API_RecommenderConfig_Contents"></a>

 ** enableMetadataWithRecommendations **   <a name="personalize-Type-RecommenderConfig-enableMetadataWithRecommendations"></a>
Whether metadata with recommendations is enabled for the recommender. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a recommender, see [Enabling metadata in recommendations for a recommender](https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata).  
 If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).   
Type: Boolean  
Required: No

 ** itemExplorationConfig **   <a name="personalize-Type-RecommenderConfig-itemExplorationConfig"></a>
Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your recommenders generate personalized recommendations for a user (not popular items or similar items).  
Type: String to string map  
Map Entries: Maximum number of 100 items.  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** minRecommendationRequestsPerSecond **   <a name="personalize-Type-RecommenderConfig-minRecommendationRequestsPerSecond"></a>
Specifies the requested minimum provisioned recommendation requests per second that Amazon Personalize will support. A high `minRecommendationRequestsPerSecond` will increase your bill. We recommend starting with 1 for `minRecommendationRequestsPerSecond` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minRecommendationRequestsPerSecond` as necessary.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** trainingDataConfig **   <a name="personalize-Type-RecommenderConfig-trainingDataConfig"></a>
 Specifies the training data configuration to use when creating a domain recommender.   
Type: [TrainingDataConfig](API_TrainingDataConfig.md) object  
Required: No

## See Also
<a name="API_RecommenderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/RecommenderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/RecommenderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/RecommenderConfig) 
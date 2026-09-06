

# BatchInferenceJobConfig
<a name="API_BatchInferenceJobConfig"></a>

The configuration details of a batch inference job.

## Contents
<a name="API_BatchInferenceJobConfig_Contents"></a>

 ** itemExplorationConfig **   <a name="personalize-Type-BatchInferenceJobConfig-itemExplorationConfig"></a>
A string to string map specifying the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. See [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html).  
Type: String to string map  
Map Entries: Maximum number of 100 items.  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** rankingInfluence **   <a name="personalize-Type-BatchInferenceJobConfig-rankingInfluence"></a>
A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a value closer to 0.0 reduces its influence. If not specified, both default to 0.0.  
Type: String to double map  
Valid Keys: `POPULARITY | FRESHNESS`   
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_BatchInferenceJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/BatchInferenceJobConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/BatchInferenceJobConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/BatchInferenceJobConfig) 
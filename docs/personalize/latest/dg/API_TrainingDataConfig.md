

# TrainingDataConfig
<a name="API_TrainingDataConfig"></a>

The training data configuration to use when creating a domain recommender or custom solution version (trained model).

## Contents
<a name="API_TrainingDataConfig_Contents"></a>

 ** excludedDatasetColumns **   <a name="personalize-Type-TrainingDataConfig-excludedDatasetColumns"></a>
Specifies the columns to exclude from training. Each key is a dataset type, and each value is a list of columns. Exclude columns to control what data Amazon Personalize uses to generate recommendations.  
 For example, you might have a column that you want to use only to filter recommendations. You can exclude this column from training and Amazon Personalize considers it only when filtering.   
Type: String to array of strings map  
Map Entries: Maximum number of 3 items.  
Key Length Constraints: Maximum length of 256.  
Key Pattern: `^[A-Za-z_]+$`   
Array Members: Maximum number of 50 items.  
Length Constraints: Maximum length of 150.  
Pattern: `[A-Za-z_][A-Za-z\d_]*`   
Required: No

 ** includedDatasetColumns **   <a name="personalize-Type-TrainingDataConfig-includedDatasetColumns"></a>
Specifies the columns to include from training. Each key is a dataset type, and each value is a list of columns. Include columns to control what data Amazon Personalize uses to generate recommendations.  
For example, you might have multiple columns in you items dataset but want to use only title and description for training. You can include only these two columns for training and Amazon Personalize will consider only the included columns for training.  
Type: String to array of strings map  
Map Entries: Maximum number of 3 items.  
Key Length Constraints: Maximum length of 256.  
Key Pattern: `^[A-Za-z_]+$`   
Array Members: Maximum number of 50 items.  
Length Constraints: Maximum length of 150.  
Pattern: `[A-Za-z_][A-Za-z\d_]*`   
Required: No

## See Also
<a name="API_TrainingDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/TrainingDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/TrainingDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/TrainingDataConfig) 


# SolutionConfig
<a name="API_SolutionConfig"></a>

Describes the configuration properties for the solution.

## Contents
<a name="API_SolutionConfig_Contents"></a>

 ** algorithmHyperParameters **   <a name="personalize-Type-SolutionConfig-algorithmHyperParameters"></a>
Lists the algorithm hyperparameters and their values.  
Type: String to string map  
Map Entries: Maximum number of 100 items.  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** autoMLConfig **   <a name="personalize-Type-SolutionConfig-autoMLConfig"></a>
The [AutoMLConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html) object containing a list of recipes to search when AutoML is performed.  
Type: [AutoMLConfig](API_AutoMLConfig.md) object  
Required: No

 ** autoTrainingConfig **   <a name="personalize-Type-SolutionConfig-autoTrainingConfig"></a>
Specifies the automatic training configuration to use.  
Type: [AutoTrainingConfig](API_AutoTrainingConfig.md) object  
Required: No

 ** eventsConfig **   <a name="personalize-Type-SolutionConfig-eventsConfig"></a>
Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.  
Type: [EventsConfig](API_EventsConfig.md) object  
Required: No

 ** eventValueThreshold **   <a name="personalize-Type-SolutionConfig-eventValueThreshold"></a>
Only events with a value greater than or equal to this threshold are used for training a model.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** featureTransformationParameters **   <a name="personalize-Type-SolutionConfig-featureTransformationParameters"></a>
Lists the feature transformation parameters.  
Type: String to string map  
Map Entries: Maximum number of 100 items.  
Key Length Constraints: Maximum length of 256.  
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** hpoConfig **   <a name="personalize-Type-SolutionConfig-hpoConfig"></a>
Describes the properties for hyperparameter optimization (HPO).  
Type: [HPOConfig](API_HPOConfig.md) object  
Required: No

 ** optimizationObjective **   <a name="personalize-Type-SolutionConfig-optimizationObjective"></a>
Describes the additional objective for the solution, such as maximizing streaming minutes or increasing revenue. For more information see [Optimizing a solution](https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-for-objective.html).  
Type: [OptimizationObjective](API_OptimizationObjective.md) object  
Required: No

 ** trainingDataConfig **   <a name="personalize-Type-SolutionConfig-trainingDataConfig"></a>
 Specifies the training data configuration to use when creating a custom solution version (trained model).   
Type: [TrainingDataConfig](API_TrainingDataConfig.md) object  
Required: No

## See Also
<a name="API_SolutionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/SolutionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/SolutionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/SolutionConfig) 
# SolutionConfig

Describes the configuration properties for the solution.

## Contents

**algorithmHyperParameters**

Lists the algorithm hyperparameters and their values.

Type: String to string map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Value Length Constraints: Maximum length of 1000.

Required: No

**autoMLConfig**

The [AutoMLConfig](API_AutoMLConfig.md "API_AutoMLConfig.md") object containing a list of recipes to search
when AutoML is performed.

Type: [AutoMLConfig](API_AutoMLConfig.md "API_AutoMLConfig.md") object

Required: No

**autoTrainingConfig**

Specifies the automatic training configuration to use.

Type: [AutoTrainingConfig](API_AutoTrainingConfig.md "API_AutoTrainingConfig.md") object

Required: No

**eventsConfig**

Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.

Type: [EventsConfig](API_EventsConfig.md "API_EventsConfig.md") object

Required: No

**eventValueThreshold**

Only events with a value greater than or equal to this threshold are
used for training a model.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**featureTransformationParameters**

Lists the feature transformation parameters.

Type: String to string map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Value Length Constraints: Maximum length of 1000.

Required: No

**hpoConfig**

Describes the properties for hyperparameter optimization (HPO).

Type: [HPOConfig](API_HPOConfig.md "API_HPOConfig.md") object

Required: No

**optimizationObjective**

Describes the additional objective for the solution, such as maximizing streaming
minutes or increasing revenue. For more information see [Optimizing a solution](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

Type: [OptimizationObjective](API_OptimizationObjective.md "API_OptimizationObjective.md") object

Required: No

**trainingDataConfig**

Specifies the training data configuration to use when creating a custom solution version (trained model).

Type: [TrainingDataConfig](API_TrainingDataConfig.md "API_TrainingDataConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/SolutionConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/SolutionConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionConfig.md")

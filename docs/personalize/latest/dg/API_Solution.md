# Solution

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can
[update the solution](API_UpdateSolution.md "API_UpdateSolution.md") to turn off automatic training.
For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

An object that provides information about a solution. A solution includes the custom recipe, customized parameters, and
trained models (Solution Versions) that Amazon Personalize uses to generate recommendations.

After you create a solution, you can’t change its configuration. If you need to make changes, you can [clone the solution](cloning-solution.md "cloning-solution.md") with the Amazon Personalize console
or create a new one.

## Contents

**autoMLResult**

When `performAutoML` is true, specifies the best recipe found.

Type: [AutoMLResult](API_AutoMLResult.md "API_AutoMLResult.md") object

Required: No

**creationDateTime**

The creation date and time (in Unix time) of the solution.

Type: Timestamp

Required: No

**datasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group that provides the training data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**eventType**

The event type (for example, 'click' or 'like') that is used for training the model.
If no `eventType` is provided, Amazon Personalize uses all interactions for training with
equal weight regardless of type.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the solution was last updated.

Type: Timestamp

Required: No

**latestSolutionUpdate**

Provides a summary of the latest updates to the solution.

Type: [SolutionUpdateSummary](API_SolutionUpdateSummary.md "API_SolutionUpdateSummary.md") object

Required: No

**latestSolutionVersion**

Describes the latest version of the solution, including the status and the ARN.

Type: [SolutionVersionSummary](API_SolutionVersionSummary.md "API_SolutionVersionSummary.md") object

Required: No

**name**

The name of the solution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**performAutoML**

###### Important

We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize
recipes. For more information, see [Determining your use case.](determining-use-case.md "determining-use-case.md")

When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from
the list specified in the solution configuration (`recipeArn` must not be specified).
When false (the default), Amazon Personalize uses `recipeArn` for training.

Type: Boolean

Required: No

**performAutoTraining**

Specifies whether the solution automatically creates solution versions. The default is `True`
and the solution automatically creates new solution versions every 7 days.

For more information about auto training, see [Creating and configuring a solution](customizing-solution-config.md "customizing-solution-config.md").

Type: Boolean

Required: No

**performHPO**

Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The
default is `false`.

Type: Boolean

Required: No

**recipeArn**

The ARN of the recipe used to create the solution. This is required when
`performAutoML` is false.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**solutionArn**

The ARN of the solution.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**solutionConfig**

Describes the configuration properties for the solution.

Type: [SolutionConfig](API_SolutionConfig.md "API_SolutionConfig.md") object

Required: No

**status**

The status of the solution.

A solution can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/Solution.md "../../../goto/SdkForCpp/personalize-2018-05-22/Solution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/Solution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/Solution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/Solution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/Solution.md")

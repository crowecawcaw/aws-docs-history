# SolutionVersion

An object that provides information about a specific version of a [Solution](API_Solution.md "API_Solution.md") in a Custom dataset group.

## Contents

**creationDateTime**

The date and
time
(in Unix time) that this version of the solution was created.

Type: Timestamp

Required: No

**datasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group providing the training data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**eventType**

The event type (for example, 'click' or 'like') that is used for training the
model.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**failureReason**

If training a solution version fails, the reason for the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in
Unix
time) that the solution was last updated.

Type: Timestamp

Required: No

**name**

The name of the solution version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**performAutoML**

When true, Amazon Personalize searches for the most optimal recipe according to the solution
configuration. When false (the default), Amazon Personalize uses `recipeArn`.

Type: Boolean

Required: No

**performHPO**

Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is
`false`.

Type: Boolean

Required: No

**recipeArn**

The ARN of the recipe used in the solution.

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

**solutionVersionArn**

The ARN of the solution version.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the solution version.

A solution version can be in one of the following states:

- CREATE PENDING
- CREATE IN_PROGRESS
- ACTIVE
- CREATE FAILED
- CREATE STOPPING
- CREATE STOPPED

Type: String

Length Constraints: Maximum length of 256.

Required: No

**trainingHours**

The time used to train the model. You are billed for the time it takes to train a model.
This field is visible only after Amazon Personalize successfully trains a model.

Type: Double

Valid Range: Minimum value of 0.

Required: No

**trainingMode**

The scope of training to be performed when creating the solution version. A
`FULL` training considers all of the data in your dataset group.
An `UPDATE` processes only the data that
has changed since the latest training. Only solution versions created with the User-Personalization
recipe can use `UPDATE`.

Type: String

Valid Values: `FULL | UPDATE | AUTOTRAIN`

Required: No

**trainingType**

Whether the solution version was created automatically or manually.

Type: String

Valid Values: `AUTOMATIC | MANUAL`

Required: No

**tunedHPOParams**

If hyperparameter optimization was performed, contains the hyperparameter values of the
best performing model.

Type: [TunedHPOParams](API_TunedHPOParams.md "API_TunedHPOParams.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/SolutionVersion.md "../../../goto/SdkForCpp/personalize-2018-05-22/SolutionVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionVersion.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionVersion.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionVersion.md")

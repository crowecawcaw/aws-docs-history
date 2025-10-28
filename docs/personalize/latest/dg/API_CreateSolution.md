# CreateSolution

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can
[update the solution](API_UpdateSolution.md "API_UpdateSolution.md") to turn off automatic training.
For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

Creates the configuration for training a model (creating a solution version). This configuration
includes the recipe to use for model training and optional training configuration, such as columns to use
in training and feature transformation parameters. For more information about configuring a solution, see [Creating and configuring a solution](customizing-solution-config.md "customizing-solution-config.md").

By default, new solutions use automatic training to create solution versions every 7 days. You can change the training frequency.
Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within
the hour, the solution skips the first automatic training. For more information,
see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

To turn off automatic training, set `performAutoTraining` to false. If you turn off automatic training, you must manually create a solution version
by calling the [CreateSolutionVersion](API_CreateSolutionVersion.md "API_CreateSolutionVersion.md") operation.

After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md").

After training completes you can evaluate model accuracy by calling
[GetSolutionMetrics](API_GetSolutionMetrics.md "API_GetSolutionMetrics.md"). When you are satisfied with the solution version, you
deploy it using [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md"). The campaign provides recommendations
to a client through the
[GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") API.

###### Note

Amazon Personalize doesn't support configuring the `hpoObjective`
for solution hyperparameter optimization at this time.

**Status**

A solution can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS
  To get the status of the solution, call [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md"). If you use
  manual training, the status must be ACTIVE before you call `CreateSolutionVersion`.

###### Related APIs

- [UpdateSolution](API_UpdateSolution.md "API_UpdateSolution.md")
- [ListSolutions](API_ListSolutions.md "API_ListSolutions.md")
- [CreateSolutionVersion](API_CreateSolutionVersion.md "API_CreateSolutionVersion.md")
- [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md")
- [DeleteSolution](API_DeleteSolution.md "API_DeleteSolution.md")

- [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md")
- [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md")

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "eventType": "`string`",
   "name": "`string`",
   "performAutoML": `boolean`,
   "performAutoTraining": `boolean`,
   "performHPO": `boolean`,
   "recipeArn": "`string`",
   "solutionConfig": {
      "algorithmHyperParameters": {
         "`string`" : "`string`"
      },
      "autoMLConfig": {
         "metricName": "`string`",
         "recipeList": [ "`string`" ]
      },
      "autoTrainingConfig": {
         "schedulingExpression": "`string`"
      },
      "eventsConfig": {
         "eventParametersList": [
            {
               "eventType": "`string`",
               "eventValueThreshold": `number`,
               "weight": `number`
            }
         ]
      },
      "eventValueThreshold": "`string`",
      "featureTransformationParameters": {
         "`string`" : "`string`"
      },
      "hpoConfig": {
         "algorithmHyperParameterRanges": {
            "categoricalHyperParameterRanges": [
               {
                  "name": "`string`",
                  "values": [ "`string`" ]
               }
            ],
            "continuousHyperParameterRanges": [
               {
                  "maxValue": `number`,
                  "minValue": `number`,
                  "name": "`string`"
               }
            ],
            "integerHyperParameterRanges": [
               {
                  "maxValue": `number`,
                  "minValue": `number`,
                  "name": "`string`"
               }
            ]
         },
         "hpoObjective": {
            "metricName": "`string`",
            "metricRegex": "`string`",
            "type": "`string`"
         },
         "hpoResourceConfig": {
            "maxNumberOfTrainingJobs": "`string`",
            "maxParallelTrainingJobs": "`string`"
         }
      },
      "optimizationObjective": {
         "itemAttribute": "`string`",
         "objectiveSensitivity": "`string`"
      },
      "trainingDataConfig": {
         "excludedDatasetColumns": {
            "`string`" : [ "`string`" ]
         }
      }
   },
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group that provides the training data.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[eventType](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

When your have multiple event types (using an `EVENT_TYPE` schema field),
this parameter specifies which event type (for example, 'click' or 'like') is used for
training the model.

If you do not provide an `eventType`, Amazon Personalize will use all interactions for training with
equal weight regardless of type.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**[name](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

The name for the solution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[performAutoML](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

###### Important

We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize
recipes. For more information, see [Choosing a recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

Whether to perform automated machine learning (AutoML). The default is `false`.
For this case, you must specify `recipeArn`.

When set to `true`, Amazon Personalize analyzes your training data and selects
the optimal USER_PERSONALIZATION recipe and hyperparameters. In this case, you must omit
`recipeArn`. Amazon Personalize determines the optimal recipe by running tests with
different values for the hyperparameters.
AutoML lengthens the training process as compared to selecting a specific recipe.

Type: Boolean

Required: No

**[performAutoTraining](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

Whether the solution uses automatic training to create new solution versions (trained models). The default is
`True` and the solution automatically creates new solution versions every 7 days. You can change the training
frequency by specifying a `schedulingExpression` in the `AutoTrainingConfig` as part of solution
configuration. For more information about automatic training,
see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within
the hour, the solution skips the first automatic training.

After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md").

Type: Boolean

Required: No

**[performHPO](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe.
The default is `false`.

When performing AutoML, this parameter is always `true` and you
should not set it to `false`.

Type: Boolean

Required: No

**[recipeArn](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

The Amazon Resource Name (ARN) of the recipe to use for model training. This is required when
`performAutoML` is false. For information about different Amazon Personalize recipes and their ARNs,
see [Choosing a recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[solutionConfig](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

The configuration properties for the solution. When `performAutoML` is set to
true, Amazon Personalize only evaluates the `autoMLConfig` section
of the solution configuration.

###### Note

Amazon Personalize doesn't support configuring the `hpoObjective`
at this time.

Type: [SolutionConfig](API_SolutionConfig.md "API_SolutionConfig.md") object

Required: No

**[tags](#API_CreateSolution_RequestSyntax "#API_CreateSolution_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the solution.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "solutionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[solutionArn](#API_CreateSolution_ResponseSyntax "#API_CreateSolution_ResponseSyntax")**

The ARN of the solution.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateSolution.md "../../../goto/cli2/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSolution.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateSolution.md "../../../goto/boto3/personalize-2018-05-22/CreateSolution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSolution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSolution.md")

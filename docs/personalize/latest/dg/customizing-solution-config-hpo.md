# Hyperparameters and

HPO

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

You specify hyperparameters before training to optimize the trained
model for your particular use case. This contrasts with model parameters
whose values are determined during the training process.

Hyperparameters are specified using the
`algorithmHyperParameters` key that is part of the [SolutionConfig](API_SolutionConfig.md "API_SolutionConfig.md")
object that is passed to the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md") operation.

A condensed version of the `CreateSolution` request is
below. The example includes the `solutionConfig` object. You
use `solutionConfig` to override the default parameters of a
recipe.

```
{
  "name": "string",
  "recipeArn": "string",
  "eventType": "string",
  "solutionConfig": {
      "optimizationObjective": {
          "itemAttribute": "string",
          "objectiveSensitivity": "string"
      },
      "eventValueThreshold": "string",
      "featureTransformationParameters": {
          "string" : "string"
      },
      "algorithmHyperParameters": {
          "string" : "string"
      },
      "hpoConfig": {
          "algorithmHyperParameterRanges": {
              ...
          },
          "hpoResourceConfig": {
              "maxNumberOfTrainingJobs": "string",
              "maxParallelTrainingJobs": "string"
          }
      },
  },
}
```

Different recipes use different hyperparameters. For the available
hyperparameters, see the individual recipes in [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

## Enabling hyperparameter

optimization

Hyperparameter optimization (HPO), or tuning, is the task of
choosing optimal hyperparameters for a specific learning objective.
The optimal hyperparameters are determined by running many training
jobs using different values from the specified ranges of
possibilities.

With [User-Personalization-v2](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md") and [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md"),
if you turn on automatic training, Amazon Personalize automatically performs HPO every 90 days. Without automatic training, no HPO occurs. For all other recipes, you must enable HPO. To
use HPO, set `performHPO` to `true`, and
include the `hpoConfig` object.

Hyperparameters can be categorical, continuous, or integer-valued.
The `hpoConfig` object has keys that correspond to each
of these types, where you specify the hyperparameters and their
ranges. You must provide each type in your request, but if a recipe doesn't have
a parameter of a type, you can leave it empty. For example, User-Personalization does
not have a tunable hyperparameter of continuous type. So for the `continousHyperParameterRange`, you would pass an empty array.

The following code shows how to create a solution with HPO enabled using the SDK for Python (Boto3).
The solution in the example uses the
[User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
recipe and
has HPO set to `true`. The code provides a value for `hidden_dimension` and the `categoricalHyperParameterRanges` and `integerHyperParameterRanges`.
The `continousHyperParameterRange` is empty and the `hpoResourceConfig` sets the `maxNumberOfTrainingJobs` and `maxParallelTrainingJobs`.

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
    name = "solution name",
    datasetGroupArn = 'arn:aws:personalize:region:accountId:dataset-group/datasetGroupName',
    recipeArn = 'arn:aws:personalize:::recipe/aws-user-personalization',
    performHPO = True,
    solutionConfig = {
        "algorithmHyperParameters": {
          "hidden_dimension": "55"
        },
        "hpoConfig": {
          "algorithmHyperParameterRanges": {
              "categoricalHyperParameterRanges": [
                  {
                      "name": "recency_mask",
                      "values": [ "true", "false"]
                  }
              ],
              "integerHyperParameterRanges": [
                  {
                      "name": "bptt",
                      "minValue": 2,
                      "maxValue": 22
                  }
              ],
              "continuousHyperParameterRanges": [

              ]
          },
          "hpoResourceConfig": {
              "maxNumberOfTrainingJobs": "4",
              "maxParallelTrainingJobs": "2"
          }
        }
    }
)
```

For more information about HPO, see [Automatic model tuning](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md").

## Viewing

hyperparameters

You can view the hyperparameters of the solution by calling the [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") operation. The following
sample shows a `DescribeSolution` output. After creating a solution version (training a model),
you can also view hyperparameters with the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") operation.

```
{
  "solution": {
    "name": "hpo_coonfig_solution",
    "solutionArn": "arn:aws:personalize:region:accountId:solution/solutionName",
    "performHPO": true,
    "performAutoML": false,
    "recipeArn": "arn:aws:personalize:::recipe/aws-user-personalization",
    "datasetGroupArn": "arn:aws:personalize:region:accountId:dataset-group/datasetGroupName",
    "eventType": "click",
    "solutionConfig": {
      "hpoConfig": {
        "hpoResourceConfig": {
          "maxNumberOfTrainingJobs": "4",
          "maxParallelTrainingJobs": "2"
        },
        "algorithmHyperParameterRanges": {
          "integerHyperParameterRanges": [
            {
              "name": "training.bptt",
              "minValue": 2,
              "maxValue": 22
            }
          ],
          "continuousHyperParameterRanges": [],
          "categoricalHyperParameterRanges": [
            {
              "name": "data.recency_mask",
              "values": [
                "true",
                "false"
              ]
            }
          ]
        }
      },
      "algorithmHyperParameters": {
        "hidden_dimension": "55"
      }
    },
    "status": "ACTIVE",
    "creationDateTime": "2022-07-08T12:12:48.565000-07:00",
    "lastUpdatedDateTime": "2022-07-08T12:12:48.565000-07:00"
  }
}
```

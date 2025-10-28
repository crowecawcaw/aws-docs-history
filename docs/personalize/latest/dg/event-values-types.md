# Choosing the item interaction data used for training

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

You can choose the events in an Item interactions dataset that Amazon Personalize uses when creating a solution version (training a model). Choosing item interaction data before training
allows you to use only a relevant subset of your data for training or remove noise to train a more optimized model. For more information
about Item interactions datasets, see
[Item interaction data](interactions-datasets.md "interactions-datasets.md").

###### Note

If you use User-Personalization-v2 or Personalized-Ranking-v2, your training cost is based on your item interactions data before filtering by event type or value.
For more information about pricing, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

You can choose item interaction data as follows:

- **Choose records based on type** – When you configure a solution,
  if your Item interactions dataset includes event types in an EVENT_TYPE column, you can optionally specify an event type to use in training.
  For example, if your Item interactions dataset includes
  _purchase_, _click_, and
  _watch_ event types, and you want Amazon Personalize to train the model with only _watch_ events, when you configure
  your solution, you would provide
  _watch_ as the `event type` that Amazon Personalize uses in training.

If you have multiple event types and use the User-Personalization-v2 recipe or Personalized-Ranking-v2 recipe,
when you configure a custom solution you can specify different weights for different types. For example, you can
configure a solution to give more weight to purchase events than click events.
For more information, see [Optimizing a solution with events configuration](optimizing-solution-events-config.md "optimizing-solution-events-config.md").

If your Item interactions dataset has multiple event types in an EVENT_TYPE column, and you do not provide an event type when you configure your solution, Amazon Personalize
uses all item interaction data for training with equal weight regardless of type.

- **Choose records based on type and value** – When you configure a solution, if your Item interactions dataset includes EVENT_TYPE and EVENT_VALUE fields, you can set a specific value
  as a threshold to exclude records from training. For example,
  if your EVENT_VALUE data for events with an EVENT_TYPE of _watch_
  is the percentage of a video that a user watched, if you set the event value threshold to 0.5,
  and the event type to _watch_, Amazon Personalize trains the model using only _watch_ interaction events
  with an EVENT_VALUE greater than or equal to 0.5.
  The following code shows how to use the SDK for Python (Boto3) to create a solution that uses only `watch` events where the use watched more than half of the video.

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
    name = 'solution name',
    datasetGroupArn = 'arn:aws:personalize:region:accountId:dataset-group/datasetGroupName',
    recipeArn = 'arn:aws:personalize:::recipe/aws-user-personalization-v2',
    eventType = 'watch',
    solutionConfig = {
        "eventValueThreshold": "0.5"
    }
)

# Store the solution ARN
solution_arn = create_solution_response['solutionArn']

# Use the solution ARN to get the solution status
solution_description = personalize.describe_solution(solutionArn = solution_arn)['solution']
print('Solution status: ' + solution_description['status'])
```

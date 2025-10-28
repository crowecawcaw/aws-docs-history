# Optimizing a solution with events configuration

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

If you use the User-Personalization-v2 recipe or Personalized-Ranking-v2 recipe, you can optimize an Amazon Personalize
solution with an events configuration.

With item recommendation recipes, the primary objective of Amazon Personalize to predict the most relevant items for your
users based on historical and real-time item interactions data. However, the interaction may carry additional
information like whether a user clicked or purchase a certain item. You can record this by recording the event's
type ([Event type and event value data](interactions-datasets.md#event-type-and-event-value-data "interactions-datasets.md#event-type-and-event-value-data")). When you configure a solution,
you can have the solution give different weights to different interaction event types. For example, you can
configure a solution to give more weight to `purchase` events than `click` events.

To have a solution give different weights to different event types, you specify the event types
and their corresponding weights in the solution's event configuration.
Additionally, you can set an event value threshold to exclude interactions with event value
below that threshold. For example, if your EVENT_VALUE data for events with an EVENT_TYPE of watch is the
percentage of a video that a user watched, if you set the event value threshold to 0.5, and the event type to
watch, Amazon Personalize trains the model using only watch interaction events with an EVENT_VALUE greater than
or equal to 0.5.

The weights associated with event types will determine their importance. An event type with higher weight
will cause the trained model to more likely recommend an item that would be interacted with that event type. For
example, if you specified “purchase” with a higher weight than “click” and the model learned that a user
would either click item B or purchase item C with his or her interaction history, the model will rank item C
higher.

To optimize a solution with events config, you create a new solution with the User-Personalization-v2
recipe or Personalized-Ranking-v2 recipe and specify an events configuration. You can also update an existing
solution ([Updating a solution to change its automatic training configuration](updating-solution.md "updating-solution.md")) with an
events configuration.

You can use the Amazon Personalize console, AWS Command Line Interface
(AWS CLI), or AWS SDKs. For information about using the Amazon Personalize console, see [Creating a solution (console)](create-solution.md#configure-solution-console "create-solution.md#configure-solution-console").

###### Topics

- [Guidelines and requirements](#optimize-event-config-guidelines-req "#optimize-event-config-guidelines-req")
- [Measuring performance with event weight configuration](#optimize-event-configuration-measuring-performance "#optimize-event-configuration-measuring-performance")
- [Optimizing a solution (AWS CLI)](#optimize-event-configuration-cli "#optimize-event-configuration-cli")
- [Optimizing a solution (AWS SDKs)](#optimize-event-configuration-sdk "#optimize-event-configuration-sdk")

## Guidelines and requirements

The following are guidelines and requirements for events configuration:

- To configure weights for different event types, your Item interactions dataset dataset must have an EVENT_TYPE column and optionally an EVENT_VALUE column.
- You can specify a list of event parameters in the configuration. Include all event types you want to be considered for solution creation. You can specify maximum of 10 different event types.
- You can specify event weight for each event type. Event weight must be between 0.0 and 1.0. Only
  the ratio of weights between event types matter. For example, setting an event type “purchase” with
  weight 0.3 and an event type “click” with weight 0.1 will have the same effect as setting “purchase
  with weight 0.6 and ”click“ with weight 0.2.
- You can update the event configuration for an existing solution using the [UpdateSolution](API_UpdateSolution.md "API_UpdateSolution.md") API operation.

## Measuring performance with event weight configuration

When you create a solution version (train a model) for a solution with an events configuration, Amazon Personalize
generates an `normalized_discounted_cumulative_gain_with_event_weights_at_k` metric. The score for
`normalized_discounted_cumulative_gain_with_event_weights_at_k` tells you how well the solution version
performs considering the events weight you set for each event types.

It is similar to normalized discounted cumulative gain (NDCG) at K but the reward for each correct
prediction will be weighted. In contrast, in the original NDCG at K, each correct prediction will all carry
a weight of 1. For example, with “purchase” of weight 0.3 and “click” of weight 0.1, correctly predicting
“purchase” item will get a reward of 1.5 while predicting “click” item will get a reward of 0.5.

For more information about generating
metrics, see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md").

## Optimizing a solution (AWS CLI)

You can optimize with events configuration with the User-Personalization-v2 or Personalized-Ranking-v2 recipe.

To optimize a solution with events configuration using the AWS CLI, create a new solution and specify
your events configuration details using the `eventsConfig` key in the `solutionConfig` object. The `eventsConfig` has a
key of `eventParametersList` under which you can specify up to 10 eventParameters. Each `eventParameter` has the
following fields:

- eventType: specify the event type you want to be considered for solution creation.
- eventValueThreshold: specify the event value threshold. Only events with event value greater
  or equal to this threshold will be considered for solution creation.
- weight: specify the weight for each event type. A higher weight means higher importance of the
  event type for the created solution.

The following is an example of the create-solution AWS CLI command. Replace the `solution name`, `dataset group arn`, and `recipe arn` values with your own.

```
aws personalize create-solution \
--name `solution name` \
--dataset-group-arn `dataset group arn` \
--recipe-arn `recipe arn` \
--solution-config "{\"eventsConfig\":{\"eventParametersList\":[{\"eventType\":\"Purchase\", \"eventValueThreshold\":0.1, \"weight\":0.3}, {\"eventType\":\"Click\", \"weight\":0.1}]}"
```

When your solution is ready, create a new
solution version (for an example command see [Creating a solution (AWS CLI)](create-solution.md#configure-solution-cli "create-solution.md#configure-solution-cli")). Once you create a solution version, you can view
the optimization performance with the solution version metrics. See [Measuring optimization performance](optimizing-solution-for-objective.md#measuring-performance "optimizing-solution-for-objective.md#measuring-performance").

## Optimizing a solution (AWS SDKs)

You can optimize with events configuration with the User-Personalization-v2 or Personalized-Ranking-v2 recipe.

To optimize a solution with events configuration using the AWS SDKs, create a new solution and specify
your events configuration details using the `eventsConfig` key in the `solutionConfig` object. The `eventsConfig` has a
key of `eventParametersList` under which you can specify up to 10 `eventParameters`. Each `eventParameter` has the
following fields:

- eventType: specify the event type you want to be considered for solution creation.
- eventValueThreshold: specify the event value threshold. Only events with event value greater
  or equal to this threshold will be considered for solution creation.
- weight: specify the weight for each event type. A higher weight means higher importance of the
  event type for the created solution.

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
    name= '`solution name`',
    recipeArn = '`recipe arn`',
    datasetGroupArn = '`dataset group arn`',
    solutionConfig = {
       "eventsConfig": {
          "eventParametersList": [
             {"eventType":"Purchase",
              "eventValueThreshold":0.1,
              "weight":0.3},
             {"eventType":"Click",
              "weight":0.1}
          ]
       }
    }
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)
```

SDK for Java 2.x

```
public static String createPersonalizeSolution(PersonalizeClient personalizeClient,
							  String datasetGroupArn,
							  String solutionName,
							  String recipeArn,
							  ) {

try {
    EventsConfig eventsConfig = EventsConfig.builder()
        .eventsParameterList(eventsParameterList)
        .build();

    SolutionConfig solutionConfig = SolutionConfig.builder()
        .eventsConfig(eventsConfig)
        .build();

    CreateSolutionRequest solutionRequest = CreateSolutionRequest.builder()
        .name(solutionName)
        .datasetGroupArn(datasetGroupArn)
        .recipeArn(recipeArn)
        .solutionConfig(solutionConfig)
        .build();

    CreateSolutionResponse solutionResponse = personalizeClient.createSolution(solutionRequest);

    return solutionResponse.solutionArn();

} catch (PersonalizeException e) {
    System.err.println(e.awsErrorDetails().errorMessage());
    System.exit(1);
}
return "";
```

When your solution is ready, create a new
solution version (for an example command see [Creating a solution (AWS SDKs)](create-solution.md#configure-solution-sdk "create-solution.md#configure-solution-sdk")). Once you create a solution version, you can view
the optimization performance with the solution version metrics. See [Measuring optimization performance](optimizing-solution-for-objective.md#measuring-performance "optimizing-solution-for-objective.md#measuring-performance").

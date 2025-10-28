# Configuring automatic training

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

When you create a solution, you can configure whether the solution uses automatic training. You can also configure the
training frequency. For example, you can configure the solution to create a new solution version every five days.

By default, all new solutions use automatic training to create a new solution version every
7 days. Automatic training occurs only
if you imported bulk or real-time interaction data since the last training. This includes item interactions or,
for solutions that use the Next-Best-Action recipe, action interactions data.
Automatic training continues until you delete the solution.

We recommend that you use automatic training. It makes maintaining your solution easier. It removes the manual training
required for the solution to learn from your most recent data. Without automatic training, you must manually create new
solution versions for the solution to learn from your most recent data. This can result in stale recommendations and a lower
conversion rate. For more information about maintaining Amazon Personalize recommendations, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").

You can configure automatic training with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs. For steps on configuring
automatic training with the console, see [Creating a solution (console)](create-solution.md#configure-solution-console "create-solution.md#configure-solution-console").

After you create the solution, record the solution ARN for future use.
With automatic training, solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within
the hour, the solution skips the first automatic training. After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") API operation.

###### Topics

- [Guidelines and requirements](#auto-training-guidelines "#auto-training-guidelines")
- [Configuring automatic training (AWS CLI)](#configure-solution-auto-training-cli "#configure-solution-auto-training-cli")
- [Configuring automatic training (SDKs)](#configure-solution-auto-training-sdk "#configure-solution-auto-training-sdk")

## Guidelines and requirements

The following are guidelines and requirements for automatic training:

- Automatic training occurs only
  if you imported bulk or real-time interaction data since the last training. This includes item interactions or,
  for solutions that use the Next-Best-Action recipe, action interactions data.
- Each training considers all of the data in your dataset group that you include in training. For information about
  configuring the columns used in training, see [Configuring columns used when training](custom-config-columns.md "custom-config-columns.md").
- You can still manually create solution versions.
- Automatic training starts within one hour after your solution is active. If you manually create a solution version within
  the hour, the solution skips the first automatic training.
- Training scheduling is based on training start date. For example, if your first solution version starts training at
  7:00 pm, and you use weekly training, the next solution version will start training a week later at 7:00 pm.
- For all recipes, we recommend at least a weekly training frequency. You can specify a training frequency between 1
  and 30 days. The default is every 7 days.
  - If you use User-Personalization-v2, User-Personalization, or Next-Best-Action, the solution automatically updates to consider new items or actions for
    recommendations. Automatic updates aren't the same as automatic training. An automatic update doesn't create a
    completely new solution version, and the model doesn't learn from your most recent data. To maintain your solution,
    your training frequency should still be at least weekly. For more formation about automatic updates, including
    additional guidelines and requirements, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates").
  - If you use Trending-Now, Amazon Personalize automatically identifies the top trending items in your interactions data over a configurable interval of time.
    Trending-Now can recommend items added since the last training through bulk or streaming interactions data. Your training frequency should still be at least weekly. For more information,
    see [Trending-Now
    recipe](native-recipe-trending-now.md "native-recipe-trending-now.md").
  - If you don't use a recipe with automatic updates or the Trending-Now recipe, Amazon Personalize considers new
    items for recommendations only after the next training. For example, if you use the Similar-Items recipe and add new
    items daily, you would have to use a daily automatic training frequency for these items to appear in recommendations
    that same day.

## Configuring automatic training (AWS CLI)

The following code shows you how to create a solution that automatically creates a solution version every five days. To
turn off automatic training, set `perform-auto-training` to `false`.

To change the training frequency, you can modify the `schedulingExpression` in the
`autoTrainingConfig`. The expression must be in `rate(*value*
*unit*)` format. For the value, specify a number between 1 and 30. For the unit, specify
`day` or `days`.

For a full explanation of the `create-solution` command, see [Creating a solution (AWS CLI)](create-solution.md#configure-solution-cli "create-solution.md#configure-solution-cli").

```
aws personalize create-solution \
--name `solution name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn `recipe ARN` \
--perform-auto-training \
--solution-config "{\"autoTrainingConfig\": {\"schedulingExpression\": \"rate(5 days)\"}}"
```

## Configuring automatic training (SDKs)

The following code shows you how to create a solution with automatic training with the AWS SDKs. The solution
automatically creates a solution version every five days. To turn off automatic training, set
`performAutoTraining` to `false`.

To change the training frequency, you can modify the `schedulingExpression` in the
`autoTrainingConfig`. The expression must be in `rate(*value*
*unit*)` format. For the value, specify a number between 1 and 30. For the unit, specify
`day` or `days`.

For a full explanation of the CreateSolution API operation, see [Creating a solution (AWS SDKs)](create-solution.md#configure-solution-sdk "create-solution.md#configure-solution-sdk").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
  name = '`solution name`',
  recipeArn = '`recipe ARN`',
  datasetGroupArn = '`dataset group ARN`',
  performAutoTraining = True,
  solutionConfig = {
    "autoTrainingConfig": {
      "schedulingExpression": "rate(5 days)"
    }
  }
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)
```

SDK for JavaScript v3

```

import {
  CreateSolutionCommand,
  PersonalizeClient,
} from "@aws-sdk/client-personalize";

// create client
const personalizeClient = new PersonalizeClient({ region: "REGION" });

// set the solution parameters
export const solutionParam = {
  datasetGroupArn: "DATASET_GROUP_ARN" /* required */,
  recipeArn: "RECIPE_ARN" /* required */,
  name: "SOLUTION_NAME" /* required */,
  performAutoTraining: true /* optional, default is true */,
  solutionConfig: {
    autoTrainingConfig: {
      schedulingExpression:
        "rate(5 days)" /* optional, default is every 7 days */,
    },
  },
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateSolutionCommand(solutionParam)
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

You can use the following Python code to wait for automatic training to start. The `wait_for_training_to_start`
method returns the ARN of the first solution version.

```
import time
import boto3

def wait_for_training_to_start(new_solution_arn):
    max_time = time.time() + 3 * 60 * 60    # 3 hours
    while time.time() < max_time:
        list_solution_versions_response = personalize.list_solution_versions(
            solutionArn=new_solution_arn
        )
        solution_versions = list_solution_versions_response.get('solutionVersions', [])
        if solution_versions:
            new_solution_version_arn = solution_versions[0]['solutionVersionArn']
            print(f"Solution version ARN: {new_solution_version_arn}")
            return new_solution_version_arn
        else:
            print(f"Training hasn't started yet. Training will start within the next hour.")
            time.sleep(60)


personalize = boto3.client('personalize')

solution_arn = "`solution_arn`"
solution_version_arn = wait_for_training_to_start(solution_arn)
```

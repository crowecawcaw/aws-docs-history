# Creating a solution

You can create a custom solution with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs. The following
includes detailed steps to create a solution with the Amazon Personalize console and code examples
that show how to create a solution with only the required fields.

###### Topics

- [Creating a solution (console)](#configure-solution-console "#configure-solution-console")
- [Creating a solution (AWS CLI)](#configure-solution-cli "#configure-solution-cli")
- [Creating a solution (AWS SDKs)](#configure-solution-sdk "#configure-solution-sdk")

## Creating a solution (console)

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

To create a solution in the console, choose your dataset group and then specify
a solution name, recipe, and optional training configuration.

###### To configure a solution (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home"), and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group.
3. On the **Overview** page, for **Step 3**, do one of the following:
   - If you created a Domain dataset group, choose **Use custom resources**, and choose
     **Create solutions**.
   - If you created a Custom dataset group, choose **Create solutions**.

4. For **Solution name**, specify a name for your solution.
5. For **Solution type**, choose the type of solution that you want to create. The type you choose
   determines what recipes are available.
   - Choose **Item recommendation** to get item recommendations for your users. For example,
     personalized movie recommendations.
   - Choose **Action recommendation** to get action recommendations for your users. For example,
     generate the next best action for a user, such as download your app.
   - Choose **User segmentation** to get user segments (groups of users) based on your item
     data.

6. For **Recipe**, choose a recipe (see [Choosing a
   recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md")).
7. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
   [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").
8. Choose **Next**.
9. On the **Training configuration** page, customize the solution to meet your business requirements.
   - In **Automatic training**, choose whether the solution uses automatic training. If you use
     automatic training, you can change the `Automatic training frequency`. The default training frequency is
     every 7 days.

   We recommend using automatic training. It makes it easier for you to maintain recommendation relevance.
   Your training frequency depends on your business
   requirements, the recipe that you use, and how frequently you import data. For more information, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md"). For information about
   maintaining relevance, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").
   - In **Hyperparameter configuration**, configure any hyperparameter options based on your recipe
     and business needs. Different recipes use different hyperparameters. For the hyperparameters available to you, see
     the individual recipes in [Choosing a
     recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").
   - In **Columns for training**, if your recipe generates item recommendations or user segments,
     optionally choose the columns that Amazon Personalize considers when creating solution versions. For more information, see [Configuring columns used when training](custom-config-columns.md "custom-config-columns.md").
   - In **Event configuration**, if your Item interactions dataset has EVENT_TYPE or both EVENT_TYPE and EVENT_VALUE columns,
     optionally use the **Event type** and **Event value threshold** fields to choose the item interactions data that Amazon Personalize uses when training the model.
     For more information, see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md").

   If you have multiple event types and use the User-Personalization-v2 recipe or Personalized-Ranking-v2 recipe,
   you can also specify different weights for different types. For example, you can
   configure a solution to give more weight to purchase events than click events.
   For more information, see [Optimizing a solution with events configuration](optimizing-solution-events-config.md "optimizing-solution-events-config.md").
   - If you use either the [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") or [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md") recipe, optionally specify an **Objective** and choose an
     **Objective sensitivity** to optimize your solution for an objective in addition to relevance.
     The objective sensitivity configures how Amazon Personalize balances recommending items based on your objective compared with
     relevance through interactions data. For more information, see [Optimizing a solution for an additional
     objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

10. Choose **Next** and review the solution details. You can't change your solution's configuration after you create it.
11. Choose **Create solution**. After you create a solution, Amazon Personalize starts creating your first solution version within an hour.
    When training starts, you can monitor it in the **Solution versions** section on the details page for you solution. Automatically created solution versions have a **Training type**
    of AUTOMATIC.

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

    * For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
     See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
    * For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
     segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

## Creating a solution (AWS CLI)

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

To create a solution with the AWS CLI, use the `create-solution` command. This command uses the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md") API operation. The following code shows you how to
create a solution that uses automatic training. It automatically creates a new solution version every five days.

To use the code, update it to give the solution a name, specify the Amazon Resource Name (ARN) of your
dataset group, optionally change the training frequency, and specify the ARN of the recipe to use. For information about recipes,
see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

```
aws personalize create-solution \
--name `solution name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn `recipe ARN` \
--perform-auto-training \
--solution-config "{\"autoTrainingConfig\": {\"schedulingExpression\": \"rate(5 days)\"}}"
```

- We recommend that you use automatic training. It makes it easier for you to maintain and improve recommendation
  relevance. By default, all new solutions use automatic training. The default training frequency is every
  7 days. Your training frequency depends on your business requirements, the recipe that you use,
  and how frequently you import data. For more information, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").
- Depending on your recipe, you can modify the code to configure recipe specific properties and hyperparameters (see
  [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md")), configure the
  columns used for training (see [Configuring columns used when training (AWS CLI)](custom-config-columns.md#custom-config-columns-cli "custom-config-columns.md#custom-config-columns-cli")), or filter the item interactions data used for training (see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md")).
- If you use either the [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") or [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md") recipe, you can optimize your solution for an objective, in addition to
  relevance. For more information, see [Optimizing a solution for an additional
  objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

After you create the solution, record the solution ARN for future use.
With automatic training, solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within
the hour, the solution skips the first automatic training. After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") API operation.

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

- For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
  See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
- For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
  segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

## Creating a solution (AWS SDKs)

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

To create a solution with AWS SDKs, use the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md")
API operation. The following code shows you how to create a solution that uses automatic training. It automatically creates
a new solution version every five days.

To use the code, update it to give the solution a name, specify the Amazon Resource Name (ARN) of your dataset group,
optionally change the training frequency, and specify the ARN of the recipe that you want to use. For information about
recipes, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

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

- We recommend that you use automatic training. It makes it easier for you to maintain and improve recommendation
  relevance. By default, all new solutions use automatic training. The default training frequency is every
  7 days. Your training frequency depends on your business requirements, the recipe that you use,
  and how frequently you import data. For more information, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").
- Depending on your recipe, you can modify the code to configure recipe specific properties and hyperparameters (see
  [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md")), configure the
  columns used for training (see [Configuring columns used when training (AWS SDKs)](custom-config-columns.md#custom-configure-columns-sdk "custom-config-columns.md#custom-configure-columns-sdk")), or filter the item interactions data used for training (see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md")).
- If you use either the [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") or [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md") recipe, you can optimize your solution for an objective, in addition to
  relevance. For more information, see [Optimizing a solution for an additional
  objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

After you create the solution, record the solution ARN for future use.
With automatic training, solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within
the hour, the solution skips the first automatic training. After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") API operation.

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

When the solution version is ACTIVE, you are ready to use it to get recommendations. How you use an active solution version depends on how you get recommendations:

- For real-time recommendations, you deploy an ACTIVE solution version with an Amazon Personalize campaign. You use the campaign to get recommendations for your users.
  See [Deploying an Amazon Personalize solution version with a campaign](campaigns.md "campaigns.md").
- For batch recommendations, you specify an ACTIVE solution version when you create a batch inference job or batch
  segment job. See [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

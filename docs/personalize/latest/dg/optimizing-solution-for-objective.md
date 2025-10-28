# Optimizing a solution for an additional

objective

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

If you use the User-Personalization recipe or Personalized-Ranking recipe,
you can optimize an Amazon Personalize solution for an objective in addition to maximum relevance,
such as maximizing revenue.

With item recommendation recipes, the primary objective of Amazon Personalize is to predict the most relevant items for your users
based on historical and real-time item interactions data. These are the items your users will
most likely interact with (for example, the items they will most likely click). If you have
an additional objective, such as maximizing streaming minutes or increasing revenue, you can
create a solution that generates recommendations based on both relevance and your objective.

To optimize a solution for an additional objective, create a new solution with the
User-Personalization recipe or Personalized-Ranking recipe and choose the numerical metadata
column in your Items dataset that is related to your objective. When generating recommendations, Amazon Personalize gives more importance to items with higher values
for this column of data. For example, you might
choose a VIDEO_LENGTH column to maximize streaming minutes or a PRICE column to maximize
revenue.

You can use the Amazon Personalize console, AWS Command Line Interface
(AWS CLI), or AWS SDKs. For information about using the Amazon Personalize console, see [Creating a solution (console)](create-solution.md#configure-solution-console "create-solution.md#configure-solution-console").

###### Topics

- [Guidelines and requirements](#optimize-objective-guidelines-req "#optimize-objective-guidelines-req")
- [Balancing objective emphasis and
  relevance](#balancing-objective-emphasis "#balancing-objective-emphasis")
- [Measuring optimization performance](#measuring-performance "#measuring-performance")
- [Optimizing a solution (AWS CLI)](#optimizing-solution-cli "#optimizing-solution-cli")
- [Optimizing a solution (AWS SDKs)](#optimizing-solution-sdk "#optimizing-solution-sdk")
- [Sample Jupyter
  notebook](#optimization-objective-sample-notebooks "#optimization-objective-sample-notebooks")

## Guidelines and requirements

Objective requirements are as follows:

- You can choose only one column for your objective.
- The column must have a numerical type in your schema.
- The column can't have a `null` type in your schema.

For more information about schemas and data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

## Balancing objective emphasis and

relevance

There can be a trade-off when recommending items based more on your objective than
relevance. For example, if you want to increase revenue through recommendations,
recommendations for only expensive items might make items less relevant for your users
and decrease user engagement and conversion.

To configure the balance between relevance and your
objective, choose one of the following objective sensitivity levels when you create the
solution:

- Off: Amazon Personalize uses primarily item interactions data to predict the most relevant
  items for your user.
- Low: Amazon Personalize places less emphasis on your objective. Relevance through item
  interactions data is more important.
- Medium: Amazon Personalize places equal emphasis on your objective and relevance through
  item interactions data.
- High: Amazon Personalize places more emphasis on your objective. Relevance through
  item interactions data is less important.

## Measuring optimization performance

When you create a solution version (train a model) for a solution with an optimization objective, Amazon Personalize generates an `average_rewards_at_k` metric.
The score for `average_rewards_at_k` tells you how well the solution version performs in achieving your objective. To calculate this metric,
Amazon Personalize calculates the rewards for each user as follows:

`rewards_per_user = total rewards from the user's interactions with their top 25 reward generating recommendations / total rewards from the user's interactions with recommendations`

The final `average_rewards_at_k` is the average of all `rewards_per_user` normalized to be a decimal value less than or equal to 1 and greater than 0.
The closer the value is to 1, the more gains on average per user you can expect from recommendations.

For example, if your objective is to maximize revenue from clicks, Amazon Personalize calculates each user score by dividing total revenue generated by the items the user clicked from their top 25 most
expensive recommendations by the revenue from all of the recommended items the user clicked. Amazon Personalize then returns a normalized average of all user scores. The closer the `average_rewards_at_k` is to 1, the more revenue on
average you can expect to gain per user from recommendations.

For more information about generating
metrics, see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md").

## Optimizing a solution (AWS CLI)

You can optimize for an objective only with the User-Personalization or
Personalized-Ranking recipe. To optimize a solution for an additional objective using
the AWS CLI, create a new solution and specify your objective details using the
`optimizationObjective` key in the `solutionConfig` object.
The `optimizationObjective` has the following fields:

- `itemAttribute`: Specify the name of the numerical metadata column
  from the Items dataset that relates to your objective.
- `objectiveSensitivity`: Specify the level of emphasis that the
  solution places on your objective when generating recommendations. The objective
  sensitivity level configures how Amazon Personalize balances recommending items based on
  your objective versus relevance through item interaction datas data. The
  `objectiveSensitivity` can be `OFF`, LOW,
  `MEDIUM` or `HIGH`. For more information, see [Balancing objective emphasis and
  relevance](#balancing-objective-emphasis "#balancing-objective-emphasis").

The following is an example of the `create-solution` AWS CLI command. Replace
the `solution name`, `dataset group arn`, and `recipe
 arn` values with your own.

For `optimizationObjective`, replace `COLUMN_NAME` with the
numerical metadata column name from the Items dataset that is related to your objective.
For `objectiveSensitivity`, specify OFF, LOW, MEDIUM, or HIGH.

```
aws personalize create-solution \
--name `solution name` \
--dataset-group-arn `dataset group arn` \
--recipe-arn `recipe arn` \
--solution-config "{\"optimizationObjective\":{\"itemAttribute\":\"`COLUMN_NAME`\",\"objectiveSensitivity\":\"`MEDIUM`\"}}"
```

When your solution is ready, create a new
solution version (for an example command see [Creating a solution (AWS CLI)](create-solution.md#configure-solution-cli "create-solution.md#configure-solution-cli")). Once you create a solution version, you can view
the optimization performance with the solution version metrics. See [Measuring optimization performance](#measuring-performance "#measuring-performance").

## Optimizing a solution (AWS SDKs)

You can optimize for an objective only with the User-Personalization or
Personalized-Ranking recipe.

To optimize a solution for an additional objective using the AWS SDKs, create a new
solution and specify your objective details using the `optimizationObjective`
key in the `solutionConfig` object for the solution. The
`optimizationObjective` has the following fields:

- `itemAttribute`: Specify the name of the numerical metadata column
  from the dataset group's Items dataset that relates to your objective.
- `objectiveSensitivity`: Specify the level of emphasis that the
  solution places on your objective when generating recommendations. The objective
  sensitivity level configures how Amazon Personalize balances recommending items based on
  your objective versus relevance through item interaction datas data. The
  `objectiveSensitivity` can be `OFF`, `LOW`,
  `MEDIUM` or `HIGH`. For more information, see [Balancing objective emphasis and
  relevance](#balancing-objective-emphasis "#balancing-objective-emphasis").

Use the following code to create a solution with an additional objective with the
AWS SDK for Python (Boto3) or the AWS SDK for Java 2.x.

When your solution is ready, create a new
solution version (for example code see [Creating a solution version (AWS SDKs)](creating-a-solution-version.md#create-solution-version-sdk "creating-a-solution-version.md#create-solution-version-sdk")). Once you create a solution version, you can view
the optimization performance with the solution version metrics. See [Measuring optimization performance](#measuring-performance "#measuring-performance").

SDK for Python (Boto3)
To create a solution that is optimized for an additional objective, use
the following `create_solution` method. Replace the
`solution name`, `dataset group arn`, and
`recipe arn` values with your own.

For `optimizationObjective`, replace `COLUMN_NAME`
with the numerical metadata column name from the Items dataset that is
related to your objective. For `objectiveSensitivity`, specify
OFF, LOW, MEDIUM, or HIGH.

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
    name= '`solution name`',
    recipeArn = '`recipe arn`',
    datasetGroupArn = '`dataset group arn`',
    solutionConfig = {
        "optimizationObjective": {
            "itemAttribute": "`COLUMN_NAME`",
            "objectiveSensitivity": "`MEDIUM`"
        }
    }
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)
```

SDK for Java 2.x
To create a solution that is optimized for an additional objective, use
the following `createPersonalizeSolution` method and pass the
following as parameters: an Amazon Personalize service client, the dataset group's Amazon
Resource Name (ARN), a solution name, the recipe ARN, the item attribute,
and the objective sensitivity level.

```
public static String createPersonalizeSolution(PersonalizeClient personalizeClient,
                                             String datasetGroupArn,
                                             String solutionName,
                                             String recipeArn,
                                             String itemAttribute,
                                             String objectiveSensitivity) {

    try {
        OptimizationObjective optimizationObjective = OptimizationObjective.builder()
            .itemAttribute(itemAttribute)
            .objectiveSensitivity(objectiveSensitivity)
            .build();

        SolutionConfig solutionConfig = SolutionConfig.builder()
            .optimizationObjective(optimizationObjective)
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

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { CreateSolutionCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create the personalizeClient
const personalizeClient = new PersonalizeClient({ region: "REGION"});

// set the solution parameters.
export const createSolutionParam = {
  datasetGroupArn: 'DATASET_GROUP_ARN',              /* required */
  recipeArn: 'RECIPE_ARN',                           /* required */
  name: 'NAME',                                      /* required */
  solutionConfig: {
    optimizationObjective: {
      itemAttribute: "COLUMN_NAME",           /* specify the numerical column from the Items dataset related to your objective */
      objectiveSensitivity: "MEDIUM"          /* specify OFF, LOW, MEDIUM, or HIGH */
    }
  }
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(new CreateSolutionCommand(createSolutionParam));
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

## Sample Jupyter

notebook

For a sample Jupyter notebook that shows how to create a solution that is optimized for an additional objective based item
metadata, see the [objective_optimization](https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/core_use_cases/objective_optimization "https://github.com/aws-samples/amazon-personalize-samples/tree/master/next_steps/core_use_cases/objective_optimization") folder of the [Amazon Personalize
samples](https://github.com/aws-samples/amazon-personalize-samples "https://github.com/aws-samples/amazon-personalize-samples") GitHub repository

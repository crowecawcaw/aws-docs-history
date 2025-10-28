# Configuring columns used when training

###### Important

By default, all new solutions use automatic training. With automatic training, you incur training costs while
your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](updating-solution.md "updating-solution.md") to turn off automatic training. For information about training
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

If your recipe generates item recommendations or user segments, you can modify the columns Amazon Personalize considers when creating
a solution version (training a model).

You can change the columns used when training to control what data Amazon Personalize uses when training a model (creating a solution version).
You might do this to experiment with different combinations of training data. Or you might exclude columns without meaningful data.
For example, might have a column that you want to use only to filter recommendations. You can
exclude this column from training and Amazon Personalize considers it only when filtering.

You can't exclude
EVENT_TYPE columns. By default, Amazon Personalize uses all columns that can be used when training. The following data is always excluded from training:

- Columns with the boolean data type
- [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data")
- Custom string fields that aren't categorical or textual

You can't include impressions data in training, but if your use case or recipe uses it, Amazon Personalize
uses impressions data to guide exploration when you get recommendations.

If you have already created a solution and you want to modify the columns it uses when training,
you can clone the solution. When you clone
a solution, you can use the configuration of the existing solution as a starting point, such as the recipe and hyperparameters,
and make any changes as necessary. For more information, see [Cloning a solution (console)](cloning-solution.md "cloning-solution.md").

You can configure the columns Amazon Personalize uses when training with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDK.
For information about choosing columns with the Amazon Personalize console, see the advanced configuration steps in
[Creating a solution (console)](create-solution.md#configure-solution-console "create-solution.md#configure-solution-console"). After you create a solution,
you can view the columns the solution uses on the solution's details page of the Amazon Personalize console, or with the [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md")
operation.

###### Topics

- [Configuring columns used when training (AWS CLI)](#custom-config-columns-cli "#custom-config-columns-cli")
- [Configuring columns used when training (AWS SDKs)](#custom-configure-columns-sdk "#custom-configure-columns-sdk")

## Configuring columns used when training (AWS CLI)

To exclude columns from training, provide the `excludedDatasetColumns` object in the `trainingDataConfig`
as part of the solution configuration.
For each key, provide the dataset type. For each value, provide the list of columns to exclude.
The following code shows how to exclude columns from training when you create a solution with the AWS CLI.

```
aws personalize create-solution \
--name `solution name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn `recipe ARN` \
--solution-config "{\"trainingDataConfig\": {\"excludedDatasetColumns\": { \"`datasetType`\" : [ \"`column1Name`\", \"`column2Name`\"]}}}"
```

## Configuring columns used when training (AWS SDKs)

To exclude columns from training, provide the `excludedDatasetColumns` object in the `trainingDataConfig`
as part of the solution configuration.
For each key, provide the dataset type. For each value, provide the list of columns to exclude.
The following code shows how to exclude columns from training when you create a solution with the SDK for Python (Boto3).

```
import boto3

personalize = boto3.client('personalize')

create_solution_response = personalize.create_solution(
  name = '`solution name`',
  recipeArn = '`recipe ARN`',
  datasetGroupArn = '`dataset group ARN`',
  solutionConfig = {
    "trainingDataConfig": {
      "excludedDatasetColumns": {
          "`datasetType`": ["`COLUMN_A`", "`COLUMN_B`"]
      }
    }
  }
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)
```

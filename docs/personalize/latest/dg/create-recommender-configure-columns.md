# Configuring columns used when creating an Amazon Personalize domain

recommender

When you create a recommender, you can modify the columns Amazon Personalize considers when training the models backing your
recommender.

You might do this to experiment with different combinations of training data. Or you might exclude columns without
meaningful data. For example, you might have a column that you want to use only to filter recommendations. You can exclude
this column from training and Amazon Personalize considers it only when filtering.

You can't exclude EVENT_TYPE columns. By default, Amazon Personalize uses all columns that can be used when training. The following
data is always excluded from training:

- Columns with the boolean data type
- [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data")
- Custom string fields that aren't categorical or textual
  You can't include impressions data in training, but if your use case or recipe uses it, Amazon Personalize uses impressions data to
  guide exploration when you get recommendations.

The following code samples show how configure columns used when training with the AWS CLI or the AWS SDKs. To do this
with the Amazon Personalize console, you specify the columns to use on the **Advanced configuration** page
when you create the recommender. For more information, see [Creating recommenders (console)](creating-domain-recommenders.md#creating-recommenders-console "creating-domain-recommenders.md#creating-recommenders-console").

To exclude columns from training, provide the `excludedDatasetColumns` object in the
`trainingDataConfig` as part of the recommender configuration. For each key in the object, provide the
dataset type. For each value, provide the list of columns to exclude. For more information, see [Configuring columns used when creating an Amazon Personalize domain
recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md").

```
aws personalize create-recommender \
--name `recommender name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn `recipe ARN` \
--recommender-config "{\"trainingDataConfig\": {\"excludedDatasetColumns\": { \"`datasetType`\" : [ \"`column1Name`\", \"`column2Name`\"]}}}"
```

To exclude columns from training, provide the `excludedDatasetColumns` object in the
`trainingDataConfig` as part of the recommender configuration. For each key, provide the dataset type. For
each value, provide the list of columns to exclude. The following code shows how to exclude columns from training when
you create a recommender. For more information, see [Configuring columns used when creating an Amazon Personalize domain
recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

create_recommender_response = personalize.create_recommender(
  name = '`recommender name`',
  recipeArn = '`recipe name`',
  datasetGroupArn = '`dataset group ARN`',
  recommenderConfig = {
    "trainingDataConfig": {
      "excludedDatasetColumns": {
        "`datasetType`": ["`COLUMN_A`", "`COLUMN_B`"]
      }
    }
  }
)

recommender_arn = create_recommender_response['recommenderArn']

print('Recommender ARN:' + recommender_arn)
```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { CreateRecommenderCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

// set the recommender's parameters
export const createRecommenderParam = {
  name: "RECOMMENDER_NAME",             /* required */
  recipeArn: "RECIPE_ARN",              /* required */
  datasetGroupArn: "DATASET_GROUP_ARN", /* required */
  recommenderConfig: {
    trainingDataConfig: {
      excludedDatasetColumns: {
        "DATASET_TYPE": ["COLUMN_A", "COLUMN_B"]
      }
    }
  }
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(new CreateRecommenderCommand(createRecommenderParam));
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

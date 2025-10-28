# Updating a recommender

After you create a recommender, you can update the recommender's configuration:

- You can update the columns the recommender uses in training. If you modify the columns used when training,
  Amazon Personalize automatically starts a full retraining of the models backing your
  recommender. While the update completes, you can still get recommendations from the recommender. The recommender
  uses the previous configuration until the update completes. To track the status of this update, use the
  `latestRecommenderUpdate` returned in the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") operation. If you provide the same columns you
  provided when you created the recommender, no update occurs.
- You can update the recommender's minimum recommendation requests per second.
  This specifies the baseline
  recommendation request throughput that's provisioned by Amazon Personalize. A high value will increase your bill. We recommend
  starting with 1. Track your usage using Amazon CloudWatch
  metrics, and increase it as necessary. For more information, see
  [Minimum recommendation requests per second and
  auto-scaling](creating-recommenders.md#min-rrps-auto-scaling "creating-recommenders.md#min-rrps-auto-scaling").
- For _Top picks for you_ and _Recommended for you_ use cases, you can update exploration configuration by adjusting the emphasis on exploring
  relevant items and the exploration item age cutoff. For information about exploration, see the section for your use case in
  [Choosing a use case](domain-use-cases.md "domain-use-cases.md").
  You can update recommenders with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

###### Topics

- [Updating a recommender (Amazon Personalize console)](#updating-recommender-console "#updating-recommender-console")
- [Updating a recommender (AWS CLI)](#update-recommender-cli "#update-recommender-cli")
- [Updating a recommender (AWS SDKs)](#update-recommender-sdks "#update-recommender-sdks")

## Updating a recommender (Amazon Personalize console)

After you create a recommender, you can update it. You can update the columns the recommender uses in training and
the recommender's minimum recommendation requests per second. For _Top picks for you_ and _Recommended for you_ use cases, you can update
exploration configuration. To update a recommender with the console, do the following.

###### To update a recommender's configuration (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your Domain dataset group.
3. From the navigation pane, choose **Recommenders**.
4. On the **Recommenders** page, choose the recommender that you want to update.
5. In **Recommender configuration** choose **Edit**.
6. Change the recommender's configuration and choose **Update**. For information on the
   different configuration options, see [Creating recommenders (console)](creating-domain-recommenders.md#creating-recommenders-console "creating-domain-recommenders.md#creating-recommenders-console").

## Updating a recommender (AWS CLI)

To update recommender with the AWS CLI, use the `update-recommender` command. Provide the
Amazon Resource Name (ARN) for the recommender and updated configuration. The following code
shows how to update the columns a recommender uses for training.

```
aws personalize update-recommender \
--dataset-group-arn `dataset group ARN` \
--recommender-config "{\"trainingDataConfig\": {\"excludedDatasetColumns\": { \"`datasetType`\" : [ \"`column1Name`\", \"`column2Name`\"]}}}"
```

If you modify the columns used in training, Amazon Personalize automatically starts a full retraining of
the models backing your recommender. While the update completes, you can still get recommendations from the recommender. The recommender
uses the previous configuration until the update completes.
To track the status of this update,
use the `latestRecommenderUpdate` returned in the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md")
operation.

For more information about the different configurations you can change, see [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md").

## Updating a recommender (AWS SDKs)

To update recommender with the AWS, use the [UpdateRecommender](API_UpdateRecommender.md "API_UpdateRecommender.md") operation. Provide the Amazon Resource
Name (ARN) for the recommender and specify the new configuration. The following code shows how to update the columns a
recommender uses for training.

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

update_recommender_response = personalize.update_recommender(
  recommenderArn = '`dataset group ARN`',
  recommenderConfig = {
    "trainingDataConfig": {
      "excludedDatasetColumns": {
        "`datasetType`": ["`COLUMN_A`", "`COLUMN_B`"]
      }
    }
  }
)

```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { UpdateRecommenderCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

// set the request's parameters
export const updateRecommenderParam = {
  recommenderArn: "RECOMMENDER_ARN", /* required */
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
    const response = await personalizeClient.send(new UpdateRecommenderCommand(updateRecommenderParam));
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

If you modify the columns used in training in the `excludedDatasetColumns` of the
`recommenderConfig`, Amazon Personalize automatically starts a full retraining of the models backing your
recommender. While the update completes, you can still get recommendations from the recommender. The recommender uses
the previous configuration until the update completes. To track the status of this update, use the
`latestRecommenderUpdate` returned in the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") operation.

For more information about the different configurations you can change, see [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md").

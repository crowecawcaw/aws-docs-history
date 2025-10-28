# Configuring exploration for a domain recommender

For `Top picks for your` or `Recommended for you` use cases, Amazon Personalize uses exploration when
recommending items. Exploration involves testing different item recommendations to learn how users respond to items with
very little interaction data. You can configure exploration with the following:

- Emphasis on exploring less relevant items (exploration weight) – Configure how
  much to explore. Specify a decimal value between 0 to 1. The default is 0.3. The closer the value is to 1, the more exploration. With more exploration,
  recommendations include more items with less item interactions data or relevance based on previous behavior. At zero, no
  exploration occurs and recommendations are based on current data
  (relevance).
- Exploration item age cutoff – Specify the maximum item age in days since
  the latest interaction across all items in the Item interactions dataset. This defines the scope of item exploration based on
  item age. Amazon Personalize determines item age based on its creation timestamp or, if creation timestamp data is missing, item interactions data. For
  more information how Amazon Personalize determines item age, see [Creation timestamp data](items-datasets.md#creation-timestamp-data "items-datasets.md#creation-timestamp-data").

To increase the items Amazon Personalize considers
during exploration, enter a greater value. The minimum is 1 day and the default is 30 days. Recommendations might include items
that are older than the item age cut off you specify. This is because these items are
relevant to the user and exploration didn't identify them.
The following code samples show how to configure exploration for a recommender with the AWS CLI or the AWS SDKs. To do this with the Amazon Personalize console, you specify
the exploration configuration on the **Advanced configuration** page when you create the recommender. For more information, see [Creating recommenders (console)](creating-domain-recommenders.md#creating-recommenders-console "creating-domain-recommenders.md#creating-recommenders-console").

The following code shows how to configure exploration when you create a recommender for
the `Top picks for you` use case. The example uses the default values.

If you have an Items dataset and want the option to include metadata when you get recommendations, update the `recommender-config` to add a `enableMetadataWithRecommendations`
field and set it to `true`.

```
aws personalize create-recommender \
--name `recommender name` \
--dataset-group-arn `dataset group ARN` \
--recipe-arn arn:aws:personalize:::recipe/aws-vod-top-picks \
--recommender-config "{\"itemExplorationConfig\":{\"explorationWeight\":\"0.3\",\"explorationItemAgeCutOff\":\"30\"}}"
```

For `Top picks for your` or `Recommended for you` use cases,
Amazon Personalize uses exploration when recommending items. Exploration involves testing different item
recommendations to learn how users respond to items with very little interaction data. You
can configure exploration with the following:

- Emphasis on exploring less relevant items (exploration weight) – Configure how
  much to explore. Specify a decimal value between 0 to 1. The default is 0.3. The closer the value is to 1, the more exploration. With more exploration,
  recommendations include more items with less item interactions data or relevance based on previous behavior. At zero, no
  exploration occurs and recommendations are based on current data
  (relevance).
- Exploration item age cutoff – Specify the maximum item age in days since
  the latest interaction across all items in the Item interactions dataset. This defines the scope of item exploration based on
  item age. Amazon Personalize determines item age based on its creation timestamp or, if creation timestamp data is missing, item interactions data. For
  more information how Amazon Personalize determines item age, see [Creation timestamp data](items-datasets.md#creation-timestamp-data "items-datasets.md#creation-timestamp-data").

To increase the items Amazon Personalize considers
during exploration, enter a greater value. The minimum is 1 day and the default is 30 days. Recommendations might include items
that are older than the item age cut off you specify. This is because these items are
relevant to the user and exploration didn't identify them.
The following code shows how to configure exploration when you create a recommender. The
example uses the default values.

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

create_recommender_response = personalize.create_recommender(
  name = '`recommender name`',
  recipeArn = 'arn:aws:personalize:::recipe/aws-vod-top-picks',
  datasetGroupArn = '`dataset group ARN`',
  recommenderConfig = {"itemExplorationConfig": {"explorationWeight": "`0.3`", "explorationItemAgeCutOff": "`30`"}}
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
  name: "RECOMMENDER_NAME",                    /* required */
  recipeArn: "RECIPE_ARN",                     /* required */
  datasetGroupArn: "DATASET_GROUP_ARN",        /* required */
  recommenderConfig: {
    itemExplorationConfig: {
      explorationWeight: "0.3",
      explorationItemAgeCutOff: "30"
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

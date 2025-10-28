# Enabling metadata in recommendations for a domain recommender in Amazon Personalize

###### Important

When you enable metadata in recommendations, you incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

When you create a recommender, you can enable the option to include item metadata from your Items dataset with recommendation results.
If enabled, you can specify the columns from your Items dataset in your request for
recommendations. Amazon Personalize returns this data for each item in the recommendation response.

You might use metadata to enrich recommendations in your user interface, such as adding the genres for
movies to carousels. Or you might use it to visually assess recommendation quality. If you use generative AI in your app, you can plug the
metadata into AI prompts to generate more relevant content. For more information about using Amazon Personalize with generative AI, see
[Amazon Personalize and generative AI](personalize-with-gen-ai.md "personalize-with-gen-ai.md").

To add metadata to recommendations, you must have an Items dataset with a column of metadata. You don't have
to use the metadata in training. For information
about creating a dataset, see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"). For information updating data in a dataset, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

The following code samples show how to enable the option to include item metadata with the AWS CLI or the AWS SDKs. To do this with the Amazon Personalize console, you
enable metadata on the **Advanced configuration** page when you create the recommender. For more information, see [Creating recommenders (console)](creating-domain-recommenders.md#creating-recommenders-console "creating-domain-recommenders.md#creating-recommenders-console").

If you have an Items dataset and want the option to include metadata when you get recommendations, set `enableMetadataWithRecommendations` to `true` in the `recommender-config`.

```
aws personalize create-recommender \
--name `recommender name` \
--dataset-group-arn `dataset group` \
--recipe-arn `recipe ARN` \
--recommender-config "{\"enableMetadataWithRecommendations\": "true"}"
```

If you have an Items dataset and want the option to include metadata when you get recommendations, set `enableMetadataWithRecommendations` to `true` in the `recommender-config`.

```
import boto3

personalize = boto3.client('personalize')

create_recommender_response = personalize.create_recommender(
  name = '`recommender name`',
  recipeArn = '`recipe name`',
  datasetGroupArn = '`dataset group ARN`',
  recommenderConfig = {"enableMetadataWithRecommendations": True}
)

recommender_arn = create_recommender_response['recommenderArn']

print('Recommender ARN:' + recommender_arn)
```

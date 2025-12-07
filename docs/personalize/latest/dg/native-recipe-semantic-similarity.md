# Semantic-Similarity recipe

The Semantic-Similarity recipe (aws-semantic-similarity) generates recommendations for
items that are semantically similar to a given item based on textual content. Unlike
traditional similarity recipes that rely on user-item interactions, this recipe analyzes the
textual descriptions and attributes of items to generate embeddings and identify
semantically similar items

This recipe is ideal for scenarios where you want to recommend items based on content
similarity, such as recommending books with similar themes, articles on related topics, or
products with similar descriptions. It works particularly well for new items with limited
interaction history (cold-start scenarios) and for catalogs where semantic relationships are
more important than co-occurrence patterns.

With Semantic-Similarity, you provide an item ID in a [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") operation (or the Amazon Personalize console) and Amazon Personalize
returns a list of similar items. Or you can use a batch workflow to get similar items for
all of the items in your inventory (see [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md")).

###### Topics

- [Recipe features](#semantic-similarity-features "#semantic-similarity-features")
- [Required and optional datasets](#semantic-similarity-datasets "#semantic-similarity-datasets")
- [Properties and hyperparameters](#semantic-similarity-hyperparameters "#semantic-similarity-hyperparameters")

## Recipe features

Semantic-Similarity uses the following Amazon Personalize recipe features when generating item recommendations:

- Real-time personalization – With the Semantic-Similarity recipe, Amazon
  Personalize automatically keeps your item catalog up to date. When you add new
  items to your Items dataset or update existing item metadata, these changes are
  reflected in your recommendations within approximately 30 minutes when using
  incremental training. This ensures that your customers always see the most
  current items available in your catalog without requiring manual intervention or
  waiting for a full retraining cycle. This is particularly valuable for catalogs
  that change frequently, such as news articles, blog posts, or seasonal product
  offerings. To enable incremental updates, customers must:

      + Set `performIncrementalUpdate` to `true` for the
       solution in the API
      + Choose either "Full and Incremental training" or "Incremental
       training" option under Training method in the UI

  Note that enabling incremental updates will incur additional costs whenever an
  update is being performed.

- Metadata with recommendations – With the Semantic-Similarity recipe,
  campaigns automatically have the option to include item metadata with
  recommendation results. You don't have manually enable metadata for your
  campaign. You might use metadata to enrich recommendations in your user
  interface, such as adding the genres for movies to carousels. For more
  information, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

## Required and optional datasets

To use the Semantic-Similarity recipe, you must create an Items dataset. Amazon Personalize
generates recommendations based on the semantic meaning of item metadata. For more
information, see [Item
metadata](items-datasets.md "items-datasets.md"). Semantic-Similarity can train on up to 10 million items in your
Items dataset.

With Semantic-Similarity, Amazon Personalize requires Items data that includes the
following

- itemName field – One string field with `itemName` set to
  `true`. This field should contain the title or name of the item.
- Textual description field – At least one string field marked as
  `textual` that contains the description of the item. This should
  be the field that best describes and represents the item.

Amazon Personalize uses this field to generate semantic embeddings that capture the meaning and
content of your items.

Additionally, the reserved CREATION_TIMESTAMP field should be set if you want to use
freshness-based ranking. For more information, see [Properties and hyperparameters](#semantic-similarity-hyperparameters "#semantic-similarity-hyperparameters").

The following datasets are optional and can improve recommendations:

- Interactions dataset– Amazon Personalize can use data in your Interactions dataset
  to calculate popularity scores based on user engagement with items. You can use
  popularity scores to rank similar items by how popular they are among users. You
  must provide an Interactions dataset if you want to use popularity-based
  ranking. You can also use data in an Interactions dataset to filter
  recommendations. For information about the interaction data you can import, see
  [Item interaction data](interactions-datasets.md "interactions-datasets.md")

## Properties and hyperparameters

The Semantic-Similarity recipe has the following properties:

- Name –
  `aws-semantic-similarity`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-semantic-similarity`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-semantic-similarity`
- Feature transformation ARN –
  `arn:aws:personalize:::feature-transformation/aws-semantic-similarity`
- Recipe type –
  `RELATED_ITEMS`

For more information, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

The Semantic-Similarity recipe has no exposed hyperparameters but you can configure
popularity and freshness factors when you create a campaign to influence the ranking of
similar items.

The table provides the following information for each factor:

- Range: [lower bound, upper bound]
- Value type: Integer, Continuous (float),
  Categorical (Boolean, list, string)

| Name       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Freshness  | The freshness factor represents how recent an item is. Freshness<br>is computed by normalizing the age of the item based on its<br>CREATION_TIMESTAMP. To use the freshness factor, you must include<br>the CREATION_TIMESTAMP field in your Items dataset schema. Higher<br>values of freshness factor will prioritize newer items among<br>semantically similar recommendations<br>Default value: `0.0`<br>Range: `[0.0, 1.0]`<br>Value type: Double                                                   |
| Popularity | The popularity factor represents how popular an item is based on<br>user interactions. Popularity is computed by normalizing the number<br>of interactions each item received. To use the popularity factor,<br>you must include an Interactions dataset when creating your dataset<br>group. Higher values of popularity factor prioritize items with more<br>customer interactions among semantically similar<br>recommendations.<br>Default value: `0.0`<br>Range: `[0.0, 1.0]`<br>Value type: Double |

Note that freshness and popularity scores are computed at training and incremental
updates will not update popularity and freshness scores. For the most recent popularity
and freshness factors to influence the ranking of recommended items, either use
automatic retraining or manually retrain the solution and update the campaign with the
new solution version.

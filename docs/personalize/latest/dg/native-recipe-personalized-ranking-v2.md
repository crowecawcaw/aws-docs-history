# Personalized-Ranking-v2 recipe

The Personalized-Ranking-v2 recipe generates personalized rankings of items. A _personalized ranking_ is a list of recommended items that are re-ranked by relevance for a
specific user. This is useful if you have a collection of ordered items, such as search results, promotions, or curated lists, and you want to provide
a personalized re-ranking for each of your users.

Personalized-Ranking-v2 can train on up to 5 million items from Item interactions and Items datasets. And it
generates more accurate rankings with lower latency than
[Personalized-Ranking](native-recipe-search.md "native-recipe-search.md").

When you use Personalized-Ranking-v2, you specify the items to rank in a [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md")
API operation. If you specify items without interactions data, Amazon Personalize will return these items without a recommendation
score in the GetPersonalizedRanking API response.

This recipe uses a transformer-based architecture to train a model that learns context
and tracks relationships and patterns in your data. _Transformers_ are a type of neural network architecture that transforms or changes an
input sequence into an output sequence.
For Amazon Personalize, the input sequence is a user's item interaction history in your data. The output sequence is their personalized recommendations. For more information about
transformers, see [What Are Transformers In Artificial Intelligence?](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/ "https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/") in the
AWS Cloud Computing Concepts Hub.

Personalized-Ranking-v2 uses a different pricing model than other recipes. For more information about pricing, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

###### Topics

- [Recipe features](#personalized-ranking-v2-features "#personalized-ranking-v2-features")
- [Required and optional datasets](#personalized-ranking-v2-datasets "#personalized-ranking-v2-datasets")
- [Properties and hyperparameters](#personalized-ranking-v2-hyperparameters "#personalized-ranking-v2-hyperparameters")

## Recipe features

Personalized-Ranking-v2 uses the following Amazon Personalize recipe features when ranking items:

- Real-time personalization – With real-time personalization, Amazon Personalize updates and adapts item recommendations
  according to a user's evolving interest. For more information, see [Real-time personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization").
- Metadata with recommendations – With the Personalized-Ranking-v2 recipe, if you have an Items dataset with at minimum one column of metadata,
  campaigns automatically have the option to include item metadata with recommendation results. You don't have manually enable metadata for
  your campaign. You might use metadata to enrich recommendations in your user interface, such as adding the genres for movies to carousels.
  For more information, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

## Required and optional datasets

To use the Personalized-Ranking-v2, you must create an Item interactions dataset and import at minimum 1000 item interactions.
Amazon Personalize generates rankings primarily based on item interaction data. For more information, see [Item interaction data](interactions-datasets.md "interactions-datasets.md").
Personalized-Ranking-v2 can train on up to 5 million items across Item interactions and Items datasets.

With Personalized-Ranking-v2,
Amazon Personalize can use Item interactions data that includes the following:

- Event type and event value data – Amazon Personalize uses event type data, such as click or watch event types, to
  identify user intent and interest through any patterns in their behavior. Also, you can use event type and
  event value data to filter records before training. For more information, see [Event type and event value data](interactions-datasets.md#event-type-and-event-value-data "interactions-datasets.md#event-type-and-event-value-data").

###### Note

With Personalized-Ranking-v2, your training cost is based on your interactions data before filtering by event type or value.
For more information about pricing, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

- Contextual metadata – Contextual metadata is interactions data you collect on the user's environment
  at the time of an event, such as their location or device type. For more information, see [Contextual metadata](interactions-datasets.md#interactions-contextual-metadata "interactions-datasets.md#interactions-contextual-metadata").

The following datasets are optional and can improve recommendations:

- Users dataset – Amazon Personalize can use data in your Users dataset to better understand your users and their interests. You
  can also use data in a Users dataset to filter recommendations. For information about the user data you
  can import, see [User metadata](users-datasets.md "users-datasets.md").
- Items dataset – Amazon Personalize can use data in your Items dataset to identify
  connections and patterns in their behavior. This helps Amazon Personalize understand your users and their interests. You
  can also use data in a Items dataset to filter recommendations. For
  information about the item data you can import, see [Item metadata](items-datasets.md "items-datasets.md").

## Properties and hyperparameters

The Personalized-Ranking-v2 recipe has the following properties:

- Name –
  `aws-personalized-ranking-v2`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-personalized-ranking-v2`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-personalized-ranking-v2`

For more information, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

The following table describes the hyperparameters for the Personalized-Ranking-v2 recipe.
A _hyperparameter_ is an algorithm parameter that you
can adjust to improve model performance. Algorithm hyperparameters control how the model
performs. The process of choosing the best value for a hyperparameter is called
hyperparameter optimization (HPO). With Personalized-Ranking-v2,
if you turn on automatic training, Amazon Personalize automatically performs HPO every 90 days. Without automatic training, no HPO occurs.

The table provides the following information for each hyperparameter:

- Range: [lower bound, upper bound]
- Value type: Integer, Continuous (float),
  Categorical (Boolean, list, string)

| Name                          | Description |
| ----------------------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm hyperparameters** |             | `apply_recency_bias` | Determines whether the model should give more weight to the most recent item interactions data in your Item interactions dataset. The most recent interactions data might include sudden changes in the underlying patterns of interaction events. To train a model that places more weight on recent events, set `apply_recency_bias` to `true`. To train a model that equally weighs all past interactions, set `apply_recency_bias` to `false`. Default value: `true` Range: `true` or `false` Value type: Boolean HPO tunable: No |

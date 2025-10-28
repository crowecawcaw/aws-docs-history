# Similar-Items

recipe

###### Note

All RELATED_ITEMS recipes use interactions data. Choose Similar-Items if you have also have item metadata
and want Amazon Personalize to use it to find similar items. Or choose the [SIMS recipe](native-recipe-sims.md "native-recipe-sims.md")
if you want to configure more hyperparameters for the model.

The Similar-Items (aws-similar-items) recipe generates recommendations for
items that are similar to an item you specify. Use Similar-Items to help
customers discover new items in your catalog based on their previous behavior
and item metadata. Recommending similar items can increase user engagement,
click-through rate, and conversion rate for your application.

Similar-Items calculates similarity based on interactions data and any item metadata you provide.
It takes into account the co-occurrence of
the item in user histories in your Interaction dataset, and any item
metadata similarities.
For example, with Similar-Items, Amazon Personalize could recommend
items customers frequently bought together with a similar style ([Categorical metadata](items-datasets.md#item-categorical-data "items-datasets.md#item-categorical-data")), or
movies that different users also watched with a similar description ([Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data")).

With Similar-Items, you provide an item ID in a [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") operation (or the Amazon Personalize
console) and Amazon Personalize returns a list of similar items. Or you can use a
batch workflow to get similar items for all of the items in your
inventory (see [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md")). When you get similar items,
you can filter the items based on an attribute of the item you specify in your request. You do this by adding a `CurrentItem`.`attribute`
element to your filter. For an example, see [item data filter examples](item-recommendation-filter-examples.md#item-examples "item-recommendation-filter-examples.md#item-examples").

To use Similar-Items, you must create an Item interactions dataset with at least 1000 unique historical and
event interactions (combined). For more accurate predictions, we recommend that you also create an Items dataset and
import metadata about items in your catalog. Similar-Items doesn't use data in a Users dataset when generating
recommendations. You can still filter recommendations based on data in a Users dataset. For more information, see
[Filtering recommendations and user segments](filter.md "filter.md").

If you have an Items dataset with textual data and item title data,
you can generate themes for related items in batch recommendations. For more information, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md")

You can get
recommendations for items that are similar to a cold item (an item with
fewer than five interactions). If Amazon Personalize can't find the item ID that you
specify in your recommendation request or batch input file, the recipe
returns popular items as recommendations.

After you create a solution version, make sure you keep your solution version and data up to date. With Similar-Items, you must
manually create a new solution version (retrain the model) for Amazon Personalize to consider new items for recommendations and update the model with your user’s most recent behavior. Then you must update any campaign using
the solution version. For more
information, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").

## Properties and

hyperparameters

The Similar-Items recipe has the following properties:

- Name –
  `aws-similar-items`
- Recipe Amazon Resource Name
  (ARN) –
  `arn:aws:personalize:::recipe/aws-similar-items`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-similar-items`

For more information, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

The following table describes the hyperparameters for the
Similar-Items recipe. A _hyperparameter_ is an algorithm parameter that you
can adjust to improve model performance. Algorithm hyperparameters
control how the model performs. The process of choosing the best
value for a hyperparameter is called hyperparameter optimization
(HPO). For more information, see [Hyperparameters and
HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

The table also provides the following information for each
hyperparameter:

- Range: [lower bound, upper
  bound]
- Value type: Integer,
  Continuous (float), Categorical (Boolean, list,
  string)
- HPO tunable: Can the
  parameter participate in HPO?

| Name                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm hyperparameters** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `popularity_discount_factor` | Configure how popularity influences recommendations. Specify a value closer to zero to include more popular items. Specify a value closer to one for less emphasis on popularity. Default value: 0.0 Range: [0.0, 1.0] Value type: Float HPO tunable: No |
| `item_id_hidden_dim`          | The number of hidden variables Amazon Personalize uses to model item ID embeddings based on interactions data. _Hidden variables_ recreate users' purchase history and item statistics to generate ranking scores. To use `item_id_hidden_dim`, you must use HPO and provide minimum and maximum range values. Amazon Personalize uses HPO to find the best value within the range you specify. Specify a greater maximum value when you have a large Item interactions dataset. Using a greater maximum value requires more time to process. To use HPO, set `performHPO` to `true` when you call the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md") operation. Default value: 100 Range: [30, 200] Value type: Integer HPO tunable: Yes |
| `item_metadata_hidden_dim`    | The number of hidden variables Amazon Personalize uses to model item metadata. To use `item_metadata_hidden_dim`, you must use HPO and provide minimum and maximum range values. Amazon Personalize uses HPO to find the best value within the range you specify. Specify a greater maximum value when you have a large Item interactions dataset. Using a greater maximum requires more time to process. To use HPO, set `performHPO` to `true` when you call the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md") operation. Default value: 100 Range: [30, 200] Value type: Integer HPO tunable: Yes                                                                                                                                     |

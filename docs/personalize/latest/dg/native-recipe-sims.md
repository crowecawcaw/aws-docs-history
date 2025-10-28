# SIMS recipe

###### Note

All RELATED_ITEMS recipes use interactions data. Choose SIMS if you want to configure more hyperparameters for the model.
Choose the [Similar-Items
recipe](native-recipe-similar-items.md "native-recipe-similar-items.md") if you have item metadata
and want Amazon Personalize to use it to find similar items.

The Item-to-item similarities (SIMS) recipe uses collaborative
filtering to recommend items that are most similar to an item you specify
when you get recommendations. SIMS uses your Item interactions dataset, not item
metadata such as color or price, to determine similarity. SIMS identifies
the co-occurrence of the item in user histories in your Interaction dataset
to recommend similar items. For example, with SIMS Amazon Personalize could recommend
coffee shop items customers frequently bought together or movies that
different users also watched.

When you get similar item recommendations,
you can filter the items based on an attribute of the item you specify in your request. You do this by adding a `CurrentItem`.`attribute`
element to your filter. For an example, see [item data filter examples](item-recommendation-filter-examples.md#item-examples "item-recommendation-filter-examples.md#item-examples").

To use SIMS, you must create an Item interactions dataset with at least 1000 unique historical and
event interactions (combined). SIMS doesn't use data in a Users or Items dataset when generating
recommendations. You can still filter recommendations based on data in a these datasets. For more information, see
[Filtering recommendations and user segments](filter.md "filter.md").

If there isn't sufficient user behavior data for an item or the item ID you
provide isn't found, SIMS recommends popular items.
After you create a solution version, make sure you keep your solution version and data up to date. With SIMS, you must
manually create a new solution version (retrain the model) for Amazon Personalize to consider new items for recommendations and update the model with your user’s most recent behavior. Then you must update any campaign using
the solution version. For more
information, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").

The SIMS recipe has the following properties:

- Name –
  `aws-sims`
- Recipe Amazon Resource Name (ARN)
  – `arn:aws:personalize:::recipe/aws-sims`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-sims`
- Feature transformation ARN –
  `arn:aws:personalize:::feature-transformation/sims`
- Recipe type –
  `RELATED_ITEMS`
  The following table describes the hyperparameters for the SIMS recipe. A
  _hyperparameter_ is an algorithm
  parameter that you can adjust to improve model performance. Algorithm
  hyperparameters control how the model performs. Featurization
  hyperparameters control how to filter the data to use in training. The
  process of choosing the best value for a hyperparameter is called
  hyperparameter optimization (HPO). For more information, see [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

The table also provides the following information for each
hyperparameter:

- Range: [lower bound, upper
  bound]
- Value type: Integer, Continuous
  (float), Categorical (Boolean, list, string)
- HPO tunable: Can the parameter
  participate in hyperparameter optimization (HPO)?

| Name                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm hyperparameters**           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `popularity_discount_factor`                                                                                                                                                                                                                                                                                                                                                                                                     | Configure how popularity influences recommendations. Specify a value closer to zero to include more popular items. Specify a value closer to one for less emphasis on popularity. Default value: 0.5 Range: [0.0, 1.0] Value type: Float HPO tunable: Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `min_cointeraction_count`               | The minimum number of co-interactions you need to calculate the similarity between a pair of items. For example, a value of `3` means that you need three or more users who interacted with both items for the algorithm to calculate their similarity. Default value: 3 Range: [0, 10] Value type: Integer HPO tunable: Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Featurization hyperparameters**       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `min_user_history_length_percentile`                                                                                                                                                                                                                                                                                                                                                                                             | The minimum percentile of user history lengths to include in model training. _History length_ is the total amount of available data on a user. Use `min_user_history_length_percentile` to exclude a percentage of users with short history lengths. Users with a short history often show patterns based on item popularity instead of the user's personal needs or wants. Removing them can train models with more focus on underlying patterns in your data. Choose an appropriate value after you review user history lengths, using a histogram or similar tool. We recommend setting a value that retains the majority of users, but removes the edge cases. Default value: 0.005 Range: [0.0, 1.0] Value type: Float HPO tunable: No |
| `max_user_history_length_percentile`    | The maximum percentile of user history lengths to include in model training. History length is the total amount of available data on a user. Use `max_user_history_length_percentile` to exclude a percentage of users with long history lengths. Users with a long history tend to contain noise. For example, a robot might have a long list of automated interactions. Removing these users limits noise in training. Choose an appropriate value after you review user history lengths using a histogram or similar tool. We recommend setting a value that retains the majority of users but removes the edge cases. For example, `min_hist_length_percentile = 0.05` and `max_hist_length_percentile = 0.95` includes all users except ones with history lengths at the bottom or top 5%. Default value: 0.995 Range: [0.0, 1.0] Value type: Float HPO tunable: No |
| `min_item_interaction_count_percentile` | The minimum percentile of item interaction counts to include in model training. Use `min_item_interaction_count_percentile` to exclude a percentage of items with a short history of interactions. Items with a short history often are new items. Removing them can train models with more focus on items with a known history. Choose an appropriate value after you review user history lengths, using a histogram or similar tool. We recommend setting a value that retains the majority of items, but removes the edge cases. Default value: 0.01 Range: [0.0, 1.0] Value type: Float HPO tunable: No                                                                                                                                                                                                                                                              |
| `max_item_interaction_count_percentile` | The maximum percentile of item interaction counts to include in model training. Use `max_item_interaction_count_percentile` to exclude a percentage of items with a long history of interactions. Items with a long history tend to be older and might be out of date. For example, a movie release that is out of print. Removing these items can focus on more relevant items. Choose an appropriate value after you review user history lengths using a histogram or similar tool. We recommend setting a value that retains the majority of items but removes the edge cases. For example, `min_item_interaction_count_percentile = 0.05` and `max_item_interaction_count_percentile = 0.95` includes all items except ones with an interaction count at the bottom or top 5%. Default value: 0.9 Range: [0.0, 1.0] Value type: Float HPO tunable: No                | ## SIMS sample notebook For a sample Jupyter notebook that shows you how to use the SIMS recipe, see [Finding similar items + HPO](https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/related_items/personalize_sims_example.ipynb "https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/related_items/personalize_sims_example.ipynb"). |

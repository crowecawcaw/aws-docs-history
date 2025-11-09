# HRNN-Coldstart recipe (legacy)

###### Note

Legacy HRNN recipes are no longer available. This documentation is for reference
purposes.

We recommend using the aws-user-personalizaton (User-Personalization) recipe over the legacy HRNN recipes.
User-Personalization improves upon and unifies the functionality offered by the HRNN
recipes. For more information, see [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md").

Use the HRNN-Coldstart recipe to predict the items that a user will interact with when you
frequently add new items and interactions and want to get recommendations for those items
immediately. The HRNN-Coldstart recipe is similar to the [HRNN-Metadata](native-recipe-hrnn-metadata.md "native-recipe-hrnn-metadata.md")
recipe, but it allows you to get recommendations for new items.

In addition, you can use the HRNN-Coldstart recipe when you want to exclude from training
items that have a long list of interactions either because of a recent popularity trend or
because the interactions might be highly unusual and introduce noise in training. With
HRNN-Coldstart, you can filter out less relevant items to create a subset for training. The
subset of items, called _cold items_, are items that have
related interaction events in the Item interactions dataset. An item is considered a cold item when
it has the following:

- Fewer interactions than a specified number of maximum interactions. You specify this
  value in the recipe's `cold_start_max_interactions` hyperparameter.
- A shorter relative duration than the maximum duration. You specify this value in the
  recipe's `cold_start_max_duration` hyperparameter.
  To reduce the number of cold items, set a lower value for
  `cold_start_max_interactions` or `cold_start_max_duration`. To increase
  the number of cold items, set a greater value for `cold_start_max_interactions` or
  `cold_start_max_duration`.

HRNN-Coldstart has the following cold item limits:

- `Maximum cold start items`: 80,000
- `Minimum cold start items`: 100
  If the number of cold items is outside this range, attempts to create a solution will
  fail.

The HRNN-Coldstart recipe has the following properties:

- Name – `aws-hrnn-coldstart`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-hrnn-coldstart`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-hrnn-coldstart`
- Feature transformation ARN –
  `arn:aws:personalize:::feature-transformation/featurize_coldstart`
- Recipe type – `USER_PERSONALIZATION`
  For more information, see [Choosing a
  recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

The following table describes the hyperparameters for the HRNN-Coldstart recipe. A _hyperparameter_ is an algorithm parameter that you can adjust to
improve model performance. Algorithm hyperparameters control how the model performs.
Featurization hyperparameters control how to filter the data to use in training. The process of
choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For
more information, see [Hyperparameters and
HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

The table also provides the following information for each hyperparameter:

- Range: [lower bound, upper bound]
- Value type: Integer, Continuous (float), Categorical
  (Boolean, list, string)
- HPO tunable: Can the parameter participate in HPO?

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm<br>hyperparameters**     |
| `hidden_dimension`                   | The number of hidden variables used in the model. \*Hidden variables<br>• recreate users' purchase history and item statistics to<br>generate ranking scores. Specify a greater number of hidden dimensions when your<br>Item interactions dataset includes more complicated patterns. Using more hidden dimensions<br>requires a larger dataset and more time to process. To decide on the optimal value,<br>use HPO. To use HPO, set `performHPO` to `true` when you call<br>[CreateSolution](API_CreateSolution.md "API_CreateSolution.md") and [CreateSolutionVersion](API_CreateSolutionVersion.md "API_CreateSolutionVersion.md")<br>operations.<br>Default value: 149<br>Range: [32, 256]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                                                            |
| `bptt`                               | Determines whether to use the back-propagation through time technique.<br>\*Back-propagation through time<br>• is a technique that<br>updates weights in recurrent neural network-based algorithms. Use `bptt`<br>for long-term credits to connect delayed rewards to early events. For example, a<br>delayed reward can be a purchase made after several clicks. An early event can be an<br>initial click. Even within the same event types, such as a click, it’s a good idea to<br>consider long-term effects and maximize the total rewards. To consider long-term<br>effects, use larger `bptt` values. Using a larger `bptt` value<br>requires larger datasets and more time to process.<br>Default value: 32<br>Range: [2, 32]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                      |
| `recency_mask`                       | Determines whether the model should consider the latest popularity trends in the<br>Item interactions dataset. Latest popularity trends might include sudden changes in the<br>underlying patterns of interaction events. To train a model that places more weight on<br>recent events, set `recency_mask` to `true`. To train a model<br>that equally weighs all past interactions, set `recency_mask` to<br>`false`. To get good recommendations using an equal weight, you might<br>need a larger training dataset.<br>Default value: `True`<br>Range: `True` or `False`<br>Value type: Boolean<br>HPO tunable: Yes                                                                                                                                                                                                                                                                                                                                                                 |
| **Featurization<br>hyperparameters** |
| `cold_start_max_interactions`        | The maximum number of user-item interactions an item can have to be considered a<br>cold item.<br>Default value: 15<br>Range: Positive integers<br>Value type: Integer<br>HPO tunable: No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `cold_start_max_duration`            | The maximum duration in days relative to the starting point for a user-item<br>interaction to be considered a cold start item. To set the starting point of the<br>user-item interaction, set the `cold_start_relative_from`<br>hyperparameter.<br>Default value: 5.0<br>Range: Positive floats<br>Value type: Float<br>HPO tunable: No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `cold_start_relative_from`           | Determines the starting point for the HRNN-Coldstart recipe to calculate<br>`cold_start_max_duration`. To calculate from the current time, choose<br>`currentTime`.<br>To calculate `cold_start_max_duration` from the timestamp of the latest<br>item in the Item interactions dataset, choose `latestItem`. This setting is<br>useful if you frequently add new items.<br>Default value: `latestItem`<br>Range: `currentTime`, `latestItem`<br>Value type: String<br>HPO tunable: No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `min_user_history_length_percentile` | The minimum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `min_user_history_length_percentile` to exclude a percentage of<br>users with short history lengths. Users with a short history often show patterns based<br>on item popularity instead of the user's personal needs or wants. Removing them can<br>train models with more focus on underlying patterns in your data. Choose an<br>appropriate value after you review user history lengths, using a histogram or similar<br>tool. We recommend setting a value that retains the majority of users, but removes the<br>edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.0<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No |
| `max_user_history_length_percentile` | The maximum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `max_user_history_length_percentile` to exclude a percentage of<br>users with long history lengths because data for these users tend to contain noise.<br>For example, a robot might have a long list of automated interactions. Removing these<br>users limits noise in training. Choose an appropriate value after you review user<br>history lengths using a histogram or similar tool. We recommend setting a value that<br>retains the majority of users but removes the edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.99<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No                                        |

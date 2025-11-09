# HRNN-Metadata recipe (legacy)

###### Note

Legacy HRNN recipes are no longer available. This documentation is for reference
purposes.

We recommend using the aws-user-personalizaton (User-Personalization) recipe over the legacy HRNN recipes.
User-Personalization improves upon and unifies the functionality offered by the HRNN
recipes. For more information, see [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md").

The HRNN-Metadata recipe predicts the items that a user will interact with. It is similar to
the [HRNN](native-recipe-hrnn.md "native-recipe-hrnn.md") recipe, with
additional features derived from contextual, user, and item metadata (from Interactions, Users,
and Items datasets, respectively). HRNN-Metadata provides accuracy benefits over non-metadata
models when high quality metadata is available. Using this recipe might require longer training
times.

The HRNN-Metadata recipe has the following properties:

- Name – `aws-hrnn-metadata`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-hrnn-metadata`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-hrnn-metadata`
- Feature transformation ARN –
  `arn:aws:personalize:::feature-transformation/featurize_metadata`
- Recipe type –
  `USER_PERSONALIZATION`
  The following table describes the hyperparameters for the HRNN-Metadata recipe. A _hyperparameter_ is an algorithm parameter that you can adjust to
  improve model performance. Algorithm hyperparameters control how the model performs.
  Featurization hyperparameters control how to filter the data to use in training. The process of
  choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For
  more information, see [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

The table also provides the following information for each hyperparameter:

- Range:
  [lower bound, upper bound]
- Value type: Integer, Continuous (float), Categorical (Boolean,
  list, string)
- HPO tunable:
  Can the parameter participate in hyperparameter optimization (HPO)?

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm<br>Hyperparameters**     |
| `hidden_dimension`                   | The number of hidden variables used in the model. \*Hidden<br>variables<br>• recreate users' purchase history and item statistics to<br>generate ranking scores. Specify a greater number of hidden dimensions when your<br>Item interactions dataset includes more complicated patterns. Using more hidden dimensions<br>requires a larger dataset and more time to process. To decide on the optimal value,<br>use HPO. To use HPO, set `performHPO` to `true` when you call<br>[CreateSolution](API_CreateSolution.md "API_CreateSolution.md") and [CreateSolutionVersion](API_CreateSolutionVersion.md "API_CreateSolutionVersion.md")<br>operations.<br>Default value: 43<br>Range: [32, 256]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                                                          |
| `bptt`                               | Determines whether to use the back-propagation through time technique. \*Back-propagation through time<br>• is a technique that updates<br>weights in recurrent neural network-based algorithms. Use `bptt` for<br>long-term credits to connect delayed rewards to early events. For example, a delayed<br>reward can be a purchase made after several clicks. An early event can be an initial<br>click. Even within the same event types, such as a click, it’s a good idea to consider<br>long-term effects and maximize the total rewards. To consider long-term effects, use<br>larger `bptt` values. Using a larger `bptt` value requires<br>larger datasets and more time to process.<br>Default value: 32<br>Range: [2, 32]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                         |
| `recency_mask`                       | Determines whether the model should consider the latest popularity trends in the<br>Item interactions dataset. Latest popularity trends might include sudden changes in the<br>underlying patterns of interaction events. To train a model that places more weight on<br>recent events, set `recency_mask` to `true`. To train a model<br>that equally weighs all past interactions, set `recency_mask` to<br>`false`. To get good recommendations using an equal weight, you might<br>need a larger training dataset.<br>Default value: `True`<br>Range: `True` or `False`<br>Value type: Boolean<br>HPO tunable: Yes                                                                                                                                                                                                                                                                                                                                                                 |
| **Featurization<br>hyperparameters** |
| `min_user_history_length_percentile` | The minimum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `min_user_history_length_percentile` to exclude a percentage of<br>users with short history lengths. Users with a short history often show patterns based<br>on item popularity instead of the user's personal needs or wants. Removing them can<br>train models with more focus on underlying patterns in your data. Choose an<br>appropriate value after you review user history lengths, using a histogram or similar<br>tool. We recommend setting a value that retains the majority of users, but removes the<br>edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.0<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No |
| `max_user_history_length_percentile` | The maximum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `max_user_history_length_percentile` to exclude a percentage of<br>users with long history lengths because data for these users tend to contain noise.<br>For example, a robot might have a long list of automated interactions. Removing these<br>users limits noise in training. Choose an appropriate value after you review user<br>history lengths using a histogram or similar tool. We recommend setting a value that<br>retains the majority of users but removes the edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.99<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No                                        |

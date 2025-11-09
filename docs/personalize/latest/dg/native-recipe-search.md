# Personalized-Ranking recipe

###### Important

We recommend using the [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md") recipe. It
can consider up to 5 million items with faster training, and generate more accurate rankings with lower
latency.

The Personalized-Ranking recipe generates personalized rankings of items. A _personalized ranking_ is a list of recommended items that are re-ranked for a
specific user. This is useful if you have a collection of ordered items, such as search results, promotions, or curated lists, and you want to provide
a personalized re-ranking for each of your users. For example, with Personalized-Ranking, Amazon Personalize can re-rank search results that you generate with
[OpenSearch](personalize-opensearch.md "personalize-opensearch.md").

To train a model, the Personalized-Ranking recipe uses the data in your Item interactions dataset,
and if you created them, the Items dataset and Users dataset in your dataset group (these datasets are optional).
With Personalized-Ranking, your Items dataset can include [Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data") and your Item interactions dataset
can include [Contextual metadata](interactions-datasets.md#interactions-contextual-metadata "interactions-datasets.md#interactions-contextual-metadata").
To get a personalized ranking, use the [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md") API.

After you create a solution version, make sure you keep your solution version and data up to date. With Personalized-Ranking, you must
manually create a new solution version (retrain the model) for Amazon Personalize to consider new items for recommendations and update the model with your user’s most recent behavior. Then you must update any campaign using
the solution version. For more
information, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").

###### Note

If you provide items without interactions data for ranking, Amazon Personalize will return these items without a recommendation
score in the GetPersonalizedRanking API response.

This recipe has the following properties:

- Name – `aws-personalized-ranking`
- Recipe Amazon Resource Name (ARN) –
  `arn:aws:personalize:::recipe/aws-personalized-ranking`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-personalized-ranking`
- Feature transformation ARN –
  `arn:aws:personalize:::feature-transformation/JSON-percentile-filtering`
- Recipe type – `PERSONALIZED_RANKING`

## Hyperparameters

The following table describes the hyperparameters for the Personalize-Ranking recipe. A
_hyperparameter_ is an algorithm parameter that you can
adjust to improve model performance. Algorithm hyperparameters control how the model performs.
Featurization hyperparameters control how to filter the data to use in training. The process of
choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For
more information, see [Hyperparameters and
HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

The table also provides the following information for each hyperparameter:

- Range: [lower bound, upper bound]
- Value type: Integer, Continuous (float), Categorical
  (Boolean, list, string)
- HPO tunable: Can the parameter participate in
  hyperparameter optimization (HPO)?

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Algorithm<br>hyperparameters**     |
| `hidden_dimension`                   | The number of hidden variables used in the model. \*Hidden<br>variables<br>• recreate users' purchase history and item statistics to<br>generate ranking scores. Specify a greater number of hidden dimensions when your<br>Item interactions dataset includes more complicated patterns. Using more hidden dimensions<br>requires a larger dataset and more time to process. To decide on the optimal value,<br>use HPO. To use HPO, set `performHPO` to `true` when you call<br>[CreateSolution](API_CreateSolution.md "API_CreateSolution.md") and [CreateSolutionVersion](API_CreateSolutionVersion.md "API_CreateSolutionVersion.md")<br>operations.<br>Default value: 149<br>Range: [32, 256]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                                                         |
| `bptt`                               | Determines whether to use the back-propagation through time technique. \*Back-propagation through time<br>• is a technique that updates<br>weights in recurrent neural network-based algorithms. Use `bptt` for<br>long-term credits to connect delayed rewards to early events. For example, a delayed<br>reward can be a purchase made after several clicks. An early event can be an initial<br>click. Even within the same event types, such as a click, it’s a good idea to consider<br>long-term effects and maximize the total rewards. To consider long-term effects, use<br>larger `bptt` values. Using a larger `bptt` value requires<br>larger datasets and more time to process.<br>Default value: 32<br>Range: [2, 32]<br>Value type: Integer<br>HPO tunable: Yes                                                                                                                                                                                                         |
| `recency_mask`                       | Determines whether the model should consider the latest popularity trends in the<br>Item interactions dataset. Latest popularity trends might include sudden changes in the<br>underlying patterns of interaction events. To train a model that places more weight on<br>recent events, set `recency_mask` to `true`. To train a model<br>that equally weighs all past interactions, set `recency_mask` to<br>`false`. To get good recommendations using an equal weight, you might<br>need a larger training dataset.<br>Default value: `True`<br>Range: `True` or `False`<br>Value type: Boolean<br>HPO tunable: Yes                                                                                                                                                                                                                                                                                                                                                                 |
| **Featurization<br>hyperparameters** |
| `min_user_history_length_percentile` | The minimum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `min_user_history_length_percentile` to exclude a percentage of<br>users with short history lengths. Users with a short history often show patterns based<br>on item popularity instead of the user's personal needs or wants. Removing them can<br>train models with more focus on underlying patterns in your data. Choose an<br>appropriate value after you review user history lengths, using a histogram or similar<br>tool. We recommend setting a value that retains the majority of users, but removes the<br>edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.0<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No |
| `max_user_history_length_percentile` | The maximum percentile of user history lengths to include in model training.<br>\*History length<br>• is the total amount of data about<br>a user. Use `max_user_history_length_percentile` to exclude a percentage of<br>users with long history lengths because data for these users tend to contain noise.<br>For example, a robot might have a long list of automated interactions. Removing these<br>users limits noise in training. Choose an appropriate value after you review user<br>history lengths using a histogram or similar tool. We recommend setting a value that<br>retains the majority of users but removes the edge cases.<br>For example, setting `min__user_history_length_percentile to 0.05` and<br>`max_user_history_length_percentile to 0.95` includes all users except<br>those with history lengths at the bottom or top 5%.<br>Default value: 0.99<br>Range: [0.0, 1.0]<br>Value type: Float<br>HPO tunable: No                                        |

## Personalized-Ranking sample notebook

For a sample Jupyter notebook that shows how to use the Personalized-Ranking recipe, see [Personalize Ranking Example](https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/personalized_ranking/personalize_ranking_example.ipynb "https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/personalized_ranking/personalize_ranking_example.ipynb").

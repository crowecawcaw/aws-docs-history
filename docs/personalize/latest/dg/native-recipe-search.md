

# Personalized-Ranking recipe
<a name="native-recipe-search"></a>

**Important**  
We recommend using the [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md) recipe. It can consider up to 5 million items with faster training, and generate more accurate rankings with lower latency.

The Personalized-Ranking recipe generates personalized rankings of items. A *personalized ranking* is a list of recommended items that are re-ranked for a specific user. This is useful if you have a collection of ordered items, such as search results, promotions, or curated lists, and you want to provide a personalized re-ranking for each of your users. For example, with Personalized-Ranking, Amazon Personalize can re-rank search results that you generate with [OpenSearch](personalize-opensearch.md). 

To train a model, the Personalized-Ranking recipe uses the data in your Item interactions dataset, and if you created them, the Items dataset and Users dataset in your dataset group (these datasets are optional). With Personalized-Ranking, your Items dataset can include [Unstructured text metadata](items-datasets.md#text-data) and your Item interactions dataset can include [Contextual metadata](interactions-datasets.md#interactions-contextual-metadata). To get a personalized ranking, use the [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md) API. 

 After you create a solution version, make sure you keep your solution version and data up to date. With Personalized-Ranking, you must manually create a new solution version (retrain the model) for Amazon Personalize to consider new items for recommendations and update the model with your user’s most recent behavior. Then you must update any campaign using the solution version. For more information, see [Maintaining recommendation relevance](maintaining-relevance.md). 

**Note**  
 If you provide items without interactions data for ranking, Amazon Personalize will return these items without a recommendation score in the GetPersonalizedRanking API response. 

This recipe has the following properties:
+  **Name** – `aws-personalized-ranking`
+  **Recipe Amazon Resource Name (ARN)** – `arn:aws:personalize:::recipe/aws-personalized-ranking`
+  **Algorithm ARN** – `arn:aws:personalize:::algorithm/aws-personalized-ranking`
+  **Feature transformation ARN** – `arn:aws:personalize:::feature-transformation/JSON-percentile-filtering`
+  **Recipe type** – `PERSONALIZED_RANKING`

## Hyperparameters
<a name="personalized-ranking-hyperparameters"></a>

The following table describes the hyperparameters for the Personalize-Ranking recipe. A *hyperparameter* is an algorithm parameter that you can adjust to improve model performance. Algorithm hyperparameters control how the model performs. Featurization hyperparameters control how to filter the data to use in training. The process of choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For more information, see [Hyperparameters and HPO](customizing-solution-config-hpo.md). 

The table also provides the following information for each hyperparameter:
+ **Range**: [lower bound, upper bound]
+ **Value type**: Integer, Continuous (float), Categorical (Boolean, list, string)
+ **HPO tunable**: Can the parameter participate in hyperparameter optimization (HPO)?


<table>
<thead>
  <tr><th>Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Algorithm hyperparameters</b></td></tr>
  <tr><td><code>hidden_dimension</code></td><td>The number of hidden variables used in the model. <i>Hidden variables</i> recreate users' purchase history and item statistics to generate ranking scores. Specify a greater number of hidden dimensions when your Item interactions dataset includes more complicated patterns. Using more hidden dimensions requires a larger dataset and more time to process. To decide on the optimal value, use HPO. To use HPO, set <code>performHPO</code> to <code>true</code> when you call <a href="API_CreateSolution.md">CreateSolution</a> and <a href="API_CreateSolutionVersion.md">CreateSolutionVersion</a> operations.<br />Default value: 149<br />Range: [32, 256]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>bptt</code></td><td>Determines whether to use the back-propagation through time technique. <i>Back-propagation through time</i> is a technique that updates weights in recurrent neural network-based algorithms. Use <code>bptt</code> for long-term credits to connect delayed rewards to early events. For example, a delayed reward can be a purchase made after several clicks. An early event can be an initial click. Even within the same event types, such as a click, it’s a good idea to consider long-term effects and maximize the total rewards. To consider long-term effects, use larger <code>bptt</code> values. Using a larger <code>bptt</code> value requires larger datasets and more time to process.<br />Default value: 32<br />Range: [2, 32]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>recency_mask</code></td><td>Determines whether the model should consider the latest popularity trends in the Item interactions dataset. Latest popularity trends might include sudden changes in the underlying patterns of interaction events. To train a model that places more weight on recent events, set <code>recency_mask</code> to <code>true</code>. To train a model that equally weighs all past interactions, set <code>recency_mask</code> to <code>false</code>. To get good recommendations using an equal weight, you might need a larger training dataset.<br />Default value: <code>True</code><br />Range: <code>True</code> or <code>False</code><br />Value type: Boolean<br />HPO tunable: Yes</td></tr>
  <tr><td colspan="2"><b>Featurization hyperparameters</b></td></tr>
  <tr><td><code>min_user_history_length_percentile</code></td><td>The minimum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>min_user_history_length_percentile</code> to exclude a percentage of users with short history lengths. Users with a short history often show patterns based on item popularity instead of the user's personal needs or wants. Removing them can train models with more focus on underlying patterns in your data. Choose an appropriate value after you review user history lengths, using a histogram or similar tool. We recommend setting a value that retains the majority of users, but removes the edge cases.<br /> For example, setting <code>min__user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.0<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td><code>max_user_history_length_percentile</code></td><td>The maximum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>max_user_history_length_percentile</code> to exclude a percentage of users with long history lengths because data for these users tend to contain noise. For example, a robot might have a long list of automated interactions. Removing these users limits noise in training. Choose an appropriate value after you review user history lengths using a histogram or similar tool. We recommend setting a value that retains the majority of users but removes the edge cases.<br />For example, setting <code>min__user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.99<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
</tbody>
</table>


## Personalized-Ranking sample notebook
<a name="personalized-ranking-sample-notebook"></a>

 For a sample Jupyter notebook that shows how to use the Personalized-Ranking recipe, see [Personalize Ranking Example](https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/personalized_ranking/personalize_ranking_example.ipynb). 
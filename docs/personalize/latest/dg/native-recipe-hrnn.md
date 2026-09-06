

# HRNN recipe (legacy)
<a name="native-recipe-hrnn"></a>

**Note**  
Legacy HRNN recipes are no longer available. This documentation is for reference purposes.  
 We recommend using the aws-user-personalizaton (User-Personalization) recipe over the legacy HRNN recipes. User-Personalization improves upon and unifies the functionality offered by the HRNN recipes. For more information, see [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md). 

The Amazon Personalize hierarchical recurrent neural network (HRNN) recipe models changes in user behavior to provide recommendations during a session. A session is a set of user interactions within a given timeframe with a goal of finding a specific item to fill a need, for example. By weighing a user's recent interactions higher, you can provide more relevant recommendations during a session.

HRNN accommodates user intent and interests, which can change over time. It takes ordered user histories and automatically weights them to make better inferences. HRNN uses a gating mechanism to model the discount weights as a learnable function of the items and timestamps.

Amazon Personalize derives the features for each user from your dataset. If you have done real-time data integration, these features are updated in real time according to user activity. To get a recommendation, you provide only the `USER_ID`. If you also provide an `ITEM_ID`, Amazon Personalize ignores it.

The HRNN recipe has the following properties:
+  **Name** – `aws-hrnn`
+  **Recipe Amazon Resource Name (ARN)** – `arn:aws:personalize:::recipe/aws-hrnn`
+  **Algorithm ARN** – `arn:aws:personalize:::algorithm/aws-hrnn`
+  **Feature transformation ARN** – `arn:aws:personalize:::feature-transformation/JSON-percentile-filtering`
+  **Recipe type** – `USER_PERSONALIZATION`

The following table describes the hyperparameters for the HRNN recipe. A *hyperparameter* is an algorithm parameter that you can adjust to improve model performance. Algorithm hyperparameters control how the model performs. Featurization hyperparameters control how to filter the data to use in training. The process of choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For more information, see [Hyperparameters and HPO](customizing-solution-config-hpo.md). 

The table also provides the following information for each hyperparameter:
+ **Range**: [lower bound, upper bound]
+ **Value type**: Integer, Continuous (float), Categorical (Boolean, list, string)
+ **HPO tunable**: Can the parameter participate in HPO?


<table>
<thead>
  <tr><th>Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Algorithm hyperparameters</b></td></tr>
  <tr><td><code>hidden_dimension</code></td><td>The number of hidden variables used in the model. <i>Hidden variables</i> recreate users' purchase history and item statistics to generate ranking scores. Specify a greater number of hidden dimensions when your Item interactions dataset includes more complicated patterns. Using more hidden dimensions requires a larger dataset and more time to process. To decide on the optimal value, use HPO. To use HPO, set <code>performHPO</code> to <code>true</code> when you call <a href="API_CreateSolution.md">CreateSolution</a> and <a href="API_CreateSolutionVersion.md">CreateSolutionVersion</a> operations.<br />Default value: 43<br />Range: [32, 256]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>bptt</code></td><td>Determines whether to use the back-propagation through time technique. <i>Back-propagation through time</i> is a technique that updates weights in recurrent neural network-based algorithms. Use <code>bptt</code> for long-term credits to connect delayed rewards to early events. For example, a delayed reward can be a purchase made after several clicks. An early event can be an initial click. Even within the same event types, such as a click, it’s a good idea to consider long-term effects and maximize the total rewards. To consider long-term effects, use larger <code>bptt</code> values. Using a larger <code>bptt</code> value requires larger datasets and more time to process.<br />Default value: 32<br />Range: [2, 32]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>recency_mask</code></td><td>Determines whether the model should consider the latest popularity trends in the Item interactions dataset. Latest popularity trends might include sudden changes in the underlying patterns of interaction events. To train a model that places more weight on recent events, set <code>recency_mask</code> to <code>true</code>. To train a model that equally weighs all past interactions, set <code>recency_mask</code> to <code>false</code>. To get good recommendations using an equal weight, you might need a larger training dataset.<br />Default value: <code>True</code><br />Range: <code>True</code> or <code>False</code><br />Value type: Boolean<br />HPO tunable: Yes</td></tr>
  <tr><td colspan="2"><b>Featurization hyperparameters</b></td></tr>
  <tr><td><code>min_user_history_length_percentile</code></td><td>The minimum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>min_user_history_length_percentile</code> to exclude a percentage of users with short history lengths. Users with a short history often show patterns based on item popularity instead of the user's personal needs or wants. Removing them can train models with more focus on underlying patterns in your data. Choose an appropriate value after you review user history lengths, using a histogram or similar tool. We recommend setting a value that retains the majority of users, but removes the edge cases.<br /> For example, setting <code>min__user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.0<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td><code>max_user_history_length_percentile</code></td><td>The maximum percentile of user history lengths to include in model training. <i>History length</i> is the total amount of data about a user. Use <code>max_user_history_length_percentile</code> to exclude a percentage of users with long history lengths because data for these users tend to contain noise. For example, a robot might have a long list of automated interactions. Removing these users limits noise in training. Choose an appropriate value after you review user history lengths using a histogram or similar tool. We recommend setting a value that retains the majority of users but removes the edge cases.<br />For example, setting <code>min__user_history_length_percentile to 0.05</code> and <code>max_user_history_length_percentile to 0.95</code> includes all users except those with history lengths at the bottom or top 5%.<br />Default value: 0.99<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
</tbody>
</table>

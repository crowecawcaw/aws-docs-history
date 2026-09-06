

# Similar-Items recipe
<a name="native-recipe-similar-items"></a>

**Note**  
 All RELATED\_ITEMS recipes use interactions data. Choose Similar-Items if you have also have item metadata and want Amazon Personalize to use it to find similar items. Or choose the [SIMS recipe](native-recipe-sims.md) if you want to configure more hyperparameters for the model. 

 The Similar-Items (aws-similar-items) recipe generates recommendations for items that are similar to an item you specify. Use Similar-Items to help customers discover new items in your catalog based on their previous behavior and item metadata. Recommending similar items can increase user engagement, click-through rate, and conversion rate for your application. 

Similar-Items calculates similarity based on interactions data and any item metadata you provide. It takes into account the co-occurrence of the item in user histories in your Interaction dataset, and any item metadata similarities. For example, with Similar-Items, Amazon Personalize could recommend items customers frequently bought together with a similar style ([Categorical metadata](items-datasets.md#item-categorical-data)), or movies that different users also watched with a similar description ([Unstructured text metadata](items-datasets.md#text-data)).

With Similar-Items, you provide an item ID in a [GetRecommendations](API_RS_GetRecommendations.md) operation (or the Amazon Personalize console) and Amazon Personalize returns a list of similar items. Or you can use a batch workflow to get similar items for all of the items in your inventory (see [Getting batch item recommendations](getting-batch-recommendations.md)). When you get similar items, you can filter the items based on an attribute of the item you specify in your request. You do this by adding a `CurrentItem`.`attribute` element to your filter. For an example, see [item data filter examples](item-recommendation-filter-examples.md#item-examples). 

 To use Similar-Items, you must create an Item interactions dataset with at least 1000 unique historical and event interactions (combined). For more accurate predictions, we recommend that you also create an Items dataset and import metadata about items in your catalog. Similar-Items doesn't use data in a Users dataset when generating recommendations. You can still filter recommendations based on data in a Users dataset. For more information, see [Filtering recommendations and user segments](filter.md).

 If you have an Items dataset with textual data and item title data, you can generate themes for related items in batch recommendations. For more information, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md) 

 You can get recommendations for items that are similar to a cold item (an item with fewer than five interactions). If Amazon Personalize can't find the item ID that you specify in your recommendation request or batch input file, the recipe returns popular items as recommendations. 

 After you create a solution version, make sure you keep your solution version and data up to date. With Similar-Items, you must manually create a new solution version (retrain the model) for Amazon Personalize to consider new items for recommendations and update the model with your user’s most recent behavior. Then you must update any campaign using the solution version. For more information, see [Maintaining recommendation relevance](maintaining-relevance.md). 

## Properties and hyperparameters
<a name="similar-items-hyperparameters"></a>

The Similar-Items recipe has the following properties:
+  **Name** – `aws-similar-items`
+  **Recipe Amazon Resource Name (ARN)** – `arn:aws:personalize:::recipe/aws-similar-items`
+  **Algorithm ARN** – `arn:aws:personalize:::algorithm/aws-similar-items`

For more information, see [Choosing a recipe](working-with-predefined-recipes.md).

The following table describes the hyperparameters for the Similar-Items recipe. A *hyperparameter* is an algorithm parameter that you can adjust to improve model performance. Algorithm hyperparameters control how the model performs. The process of choosing the best value for a hyperparameter is called hyperparameter optimization (HPO). For more information, see [Hyperparameters and HPO](customizing-solution-config-hpo.md). 

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
  <tr><td><code>popularity_discount_factor</code></td><td> Configure how popularity influences recommendations. Specify a value closer to zero to include more popular items. Specify a value closer to one for less emphasis on popularity. <br />Default value: 0.0<br />Range: [0.0, 1.0]<br />Value type: Float<br />HPO tunable: No</td></tr>
  <tr><td><code>item_id_hidden_dim</code></td><td>The number of hidden variables Amazon Personalize uses to model item ID embeddings based on interactions data. <i>Hidden variables</i> recreate users' purchase history and item statistics to generate ranking scores. To use <code>item_id_hidden_dim</code>, you must use HPO and provide minimum and maximum range values. Amazon Personalize uses HPO to find the best value within the range you specify. Specify a greater maximum value when you have a large Item interactions dataset. Using a greater maximum value requires more time to process. <br /> To use HPO, set <code>performHPO</code> to <code>true</code> when you call the <a href="API_CreateSolution.md">CreateSolution</a> operation.<br />Default value: 100<br />Range: [30, 200]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
  <tr><td><code>item_metadata_hidden_dim</code></td><td>The number of hidden variables Amazon Personalize uses to model item metadata. To use <code>item_metadata_hidden_dim</code>, you must use HPO and provide minimum and maximum range values. Amazon Personalize uses HPO to find the best value within the range you specify. Specify a greater maximum value when you have a large Item interactions dataset. Using a greater maximum requires more time to process. <br /> To use HPO, set <code>performHPO</code> to <code>true</code> when you call the <a href="API_CreateSolution.md">CreateSolution</a> operation.<br />Default value: 100<br />Range: [30, 200]<br />Value type: Integer<br />HPO tunable: Yes</td></tr>
</tbody>
</table>

# Trending-Now

recipe

The Trending-Now recipe (aws-trending-now) generates recommendations for items that are rapidly
becoming more popular with your users. You might use the Trending-Now recipe if items gaining in popularity are
more relevant to your customers. For example, your customers might highly value what other users are interacting with.
Common uses include recommending viral social media content, breaking news articles, or recent sports videos.

Trending-Now automatically identifies the top trending items by calculating the increase in interactions that each item has
over configurable intervals of time. The items with highest rate of increase are considered trending items. The time is based on
timestamp data in your Item interactions dataset. The items considered come from the interactions data you imported in bulk
and incrementally. You don't have to manually create a new solution version for Trending-Now to consider
new items in interactions data.

You can specify the time interval by providing a
`Trend discovery frequency` when you create your solution.
For example, if you specify `30 minutes` for `Trend discovery frequency`, for every 30 minutes of data,
Amazon Personalize identifies the items with the greatest rate of increase in interactions since the last evaluation. Possible frequencies
include 30 minutes, 1 hour, 3 hours, and 1 day. Choose a frequency that aligns with the distribution of your interactions
data. Missing data over the interval you choose can reduce recommendation accuracy. If you import zero interactions
over the last two time intervals, Amazon Personalize recommends only popular items instead of trending items.

With Trending-Now, you call the [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") operation or get recommendations on the **Test campaign** page of the Amazon Personalize
console. Amazon Personalize returns the top trending items. You pass a `userId` in your request only if you apply a filter that requires it. With the GetRecommendations API, you can configure the number
of trending items returned with the `numResults` parameter. You can't get batch recommendations with the Trending-Now recipe.

To use Trending-Now, you must create an Item interactions dataset with at least 1000 unique
historical and event interactions combined (after filtering by eventType and eventValueThreshold, if provided).
When generating trending item recommendations, Trending-Now
doesn't use data in Items or Users datasets. However, you can still filter recommendations
based on data in these datasets. For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

###### Topics

- [Properties and
  hyperparameters](#trending-now-hyperparameters "#trending-now-hyperparameters")
- [Creating a solution (SDK for Python (Boto3))](#trending-now-python "#trending-now-python")
- [Sample Jupyter
  notebook](#trending-now-sample-notebooks "#trending-now-sample-notebooks")

## Properties and

hyperparameters

The Trending-Now recipe has the following properties:

- Name –
  `aws-trending-now`
- Recipe Amazon Resource Name
  (ARN) –
  `arn:aws:personalize:::recipe/aws-trending-now`
- Algorithm ARN –
  `arn:aws:personalize:::algorithm/aws-trending-now-custom`

For more information, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

The following table describes the hyperparameters for the Trending-Now recipe. A _hyperparameter_ is an algorithm parameter that you can adjust to improve model performance. Algorithm
hyperparameters control how the model performs. The process of choosing the best value for a hyperparameter is called
hyperparameter optimization (HPO). For more information, see [Hyperparameters and
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

| Name                                       | Description |
| ------------------------------------------ | ----------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Feature transformation hyperparameters** |             | `Trend discovery frequency` | Specify how often Amazon Personalize evaluates your interactions data and identifies trending items. For example, if you specify `30 minutes` for `Trend discovery frequency`, every 30 minutes Amazon Personalize identifies items with the greatest rate of increase in interactions over 30-minute intervals. Available frequencies include 30 minutes, 1 hour, 2 hours, 3 hours, and 1 day. Choose a frequency that aligns with the distribution of your interactions data. Missing data over the interval you choose can reduce recommendation accuracy. If you use the CreateSolution API operation and don't specify a value, the default is every 2 hours. NoteFor any parameter values that are greater than 2 hours, Amazon Personalize automatically refreshes the trending item recommendations every 2 hours to account for new interactions and new items. Default value: 2 hours Possible values: 30 minutes, 1 hour, 2 hours, 3 hours, and 1 day. Value type: String HPO tunable: No | ## Creating a solution (SDK for Python (Boto3)) The following code shows how to create a solution with the Trending-Now recipe using the SDK for Python (Boto3). Possible values for `trend_discovery_frequency` are `30 minutes`, `1 hour`, `3 hours`, and `1 day`. For information about creating a solution with the console, see [Creating a solution (console)](create-solution.md#configure-solution-console "create-solution.md#configure-solution-console"). ``import boto3 personalize = boto3.client("personalize") create_solution_response = personalize_client.create_solution( name="`solution name`", recipeArn="arn:aws:personalize:::recipe/aws-trending-now", datasetGroupArn="`dataset group ARN`", solutionConfig={ "featureTransformationParameters": { "trend_discovery_frequency": "1 hour" } } ) print(create_solution_response['solutionArn'])`` ## Sample Jupyter notebook For a sample Jupyter notebook that shows how to use the Trending-Now recipe, see [trending_now_example.ipynb](https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/trending_now/trending_now_example.ipynb "https://github.com/aws-samples/amazon-personalize-samples/blob/master/next_steps/core_use_cases/trending_now/trending_now_example.ipynb") in the Amazon Personalize samples GitHub repository. |

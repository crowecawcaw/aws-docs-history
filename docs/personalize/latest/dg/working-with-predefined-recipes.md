# Choosing a

recipe

When you create a custom solution, you specify a recipe and configure training parameters. _Recipes_ are Amazon Personalize
algorithms that are prepared for specific use cases. Amazon Personalize provides recipes, based on common use cases, for
training models.
When you create a solution version for the solution, Amazon Personalize trains the models backing the solution version based on the recipe and
training configuration.

Amazon Personalize recipes use the following during training:

- Predefined attributes of your data
- Predefined feature transformations
- Predefined algorithms
- Initial parameter settings for the algorithms
  To optimize your model, you can override many of these parameters when
  you create a solution. For more information, see [Hyperparameters and
  HPO](customizing-solution-config-hpo.md "customizing-solution-config-hpo.md").

###### Topics

- [Amazon Personalize recipe types by use case](#use-cases "#use-cases")
- [Amazon Personalize recipes](#recipe-categories "#recipe-categories")
- [Viewing available Amazon Personalize recipes](#listing-recipes "#listing-recipes")
- [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
- [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Trending-Now
  recipe](native-recipe-trending-now.md "native-recipe-trending-now.md")
- [Popularity-Count recipe](native-recipe-popularity.md "native-recipe-popularity.md")
- [Personalized-Ranking-v2 recipe](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md")
- [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md")
- [Similar-Items
  recipe](native-recipe-similar-items.md "native-recipe-similar-items.md")
- [SIMS recipe](native-recipe-sims.md "native-recipe-sims.md")
- [Next-Best-Action recipe](native-recipe-next-best-action.md "native-recipe-next-best-action.md")
- [Item-Affinity recipe](item-affinity-recipe.md "item-affinity-recipe.md")
- [Item-Attribute-Affinity recipe](item-attribute-affinity-recipe.md "item-attribute-affinity-recipe.md")
- [Legacy HRNN recipes](legacy-user-personalization-recipes.md "legacy-user-personalization-recipes.md")

## Amazon Personalize recipe types by use case

To choose your recipe, first choose your use case from the following and note its corresponding recipe type.

- Recommending items for users (USER_PERSONALIZATION recipes)

To provide personalized recommendations for your users, train your model with a
USER_PERSONALIZATION recipe. Personalized recommendations help drive better engagement and conversion.

- Ranking items for a user (PERSONALIZED_RANKING recipes)

To personalize the order of curated lists or search results for your users, train your
model with a PERSONALIZED_RANKING recipe. PERSONALIZED_RANKING recipes create a
personalized list by re-ranking a collection of input items based on predicted interest level
for a given user. Personalized lists improve the customer experience and increase customer
loyalty and engagement.

- Recommending trending or popular items (POPULAR_ITEMS recipes)

To recommend trending or popular items use a
POPULAR_ITEMS recipe. You might use a POPULAR_ITEMS if your customers highly value what other
users are interacting with. Common uses include recommending viral social media content, breaking news articles, or recent sports videos.

- Recommending similar items (RELATED_ITEMS recipes)

To recommend similar items, such as items frequently bought together or movies that other users have also watched,
you should use a RELATED_ITEMS recipe. Recommending similar
items can help your customers discover items and can increase user conversion rate.

- Recommending the next best action (PERSONALIZED_ACTIONS recipes)

To recommend the next best action for your users in real time, such as
signing up for your loyalty program or applying for a credit card,
you should use a PERSONALIZED_ACTIONS recipe. Recommending the next best action
can increase customer loyalty, generate more revenue, and improve your users' experience.

- Getting user segments (USER_SEGMENTATION recipes)

To get segments of users based on item input data, such as users who will most likely interact with items with a certain attribute,
you should use a USER_SEGMENTATION recipe. Getting user segments can help you create advanced marketing campaigns that promote
different items to different user segments based on the likelihood that they will take an action.

## Amazon Personalize recipes

Amazon Personalize provides the following types of recipes. Besides behavioral
differences, each type has different requirements for getting
recommendations, as shown in the following table.

| Recipe type          | Recipes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | API                                                                                                 | API requirements                                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| USER_PERSONALIZATION | [User-Personalization-v2](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")<br>[User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")<br>[HRNN recipe (legacy)](native-recipe-hrnn.md "native-recipe-hrnn.md")<br>[HRNN-Metadata recipe (legacy)](native-recipe-hrnn-metadata.md "native-recipe-hrnn-metadata.md")<br>[HRNN-Coldstart recipe (legacy)](native-recipe-hrnn-coldstart.md "native-recipe-hrnn-coldstart.md") | [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")                   | `userId`: Required<br>`itemId`: Not used<br>`inputList`: NA                                                                                   |
| POPULAR_ITEMS        | [Trending-Now](native-recipe-trending-now.md "native-recipe-trending-now.md")<br>[Popularity-Count](native-recipe-popularity.md "native-recipe-popularity.md")                                                                                                                                                                                                                                                                                                                                                                | [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")                   | `userId`: Required only if you apply a filter that requires it<br>`itemId`: Not used<br>`inputList`: NA                                       |
| PERSONALIZED_RANKING | [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md")<br>[Personalized-Ranking](native-recipe-search.md "native-recipe-search.md")                                                                                                                                                                                                                                                                                                                                   | [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md")       | `userId`: Required<br>`itemId`: NA<br>`inputList`: list of itemId's                                                                           |
| RELATED_ITEMS        | [Similar-Items](native-recipe-similar-items.md "native-recipe-similar-items.md")<br>[SIMS](native-recipe-sims.md "native-recipe-sims.md")                                                                                                                                                                                                                                                                                                                                                                                     | [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")                   | `userId`: Required only if you apply a filter that requires it<br>`itemId`: Required<br>`inputList`: NA                                       |
| PERSONALIZED_ACTIONS | [Next-Best-Action](native-recipe-next-best-action.md "native-recipe-next-best-action.md")                                                                                                                                                                                                                                                                                                                                                                                                                                     | [GetActionRecommendations](API_RS_GetActionRecommendations.md "API_RS_GetActionRecommendations.md") | `userId`: Required<br>`actionId`: Not used<br>`itemId`: Not used<br>`inputList`: NA                                                           |
| USER_SEGMENTATION    | [Item-Affinity](item-affinity-recipe.md "item-affinity-recipe.md")<br>[Item-Attribute-Affinity](item-attribute-affinity-recipe.md "item-attribute-affinity-recipe.md")                                                                                                                                                                                                                                                                                                                                                        | [CreateBatchSegmentJob](API_CreateBatchSegmentJob.md "API_CreateBatchSegmentJob.md")                | For batch workflow requirements, see [Getting user segments with a batch segment job](creating-batch-seg-job.md "creating-batch-seg-job.md"). |

## Viewing available Amazon Personalize recipes

To see a list of available recipes:

- In the Amazon Personalize console, choose a dataset group. From the navigation
  pane, choose **Solutions and recipes**, and choose
  the **Recipes** tab.
- With the AWS SDK for Python (Boto3), call the [ListRecipes](API_ListRecipes.md "API_ListRecipes.md") API.
- With the AWS CLI, use the following command.

```
aws personalize list-recipes
```

To get information about a recipe using the SDK for Python (Boto3), call the [DescribeRecipe](API_DescribeRecipe.md "API_DescribeRecipe.md") API.
To get information about a recipe using the AWS CLI, use the following
command.

```
aws personalize describe-recipe --recipe-arn `recipe_arn`
```

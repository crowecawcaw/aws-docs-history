# Maintaining recommendation relevance

Relevant recommendations can increase user engagement, click-through rate, and conversion rate for your application
as your catalogue grows.
To maintain and improve the relevance of Amazon Personalize recommendations for your users, keep your data and custom resources up to date.
This allows Amazon Personalize to learn from your user’s most recent behavior and include your newest items in recommendations.

###### Topics

- [Keeping datasets current](#updating-data "#updating-data")
- [Maintaining domain recommenders](#maintain-recommender-relevance "#maintain-recommender-relevance")
- [Maintaining custom solutions](#retraining-model "#retraining-model")

## Keeping datasets current

As your catalog grows, update your historical data with bulk or individual data import operations. For more information
about importing historical data, see [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md"). For information on how data you import after training a model influences recommendations,
see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

For use cases and recipes that provide personalized real-time recommendations, keep your Item interactions dataset up to
date with your users' behavior. Do this by recording item interactions with an event tracker and the PutEvents API operation. Amazon Personalize updates recommendations based on your user's most recent activity as
they interact with your catalog. For information about real-time personalization, see [Real-time personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization").
For more information on recording real-time events, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

## Maintaining domain recommenders

Amazon Personalize automatically retrains the models backing your recommenders every 7 days. This is a
full retraining that creates entirely new models based on the entirety of the data in your datasets.
If you modify the columns used in training, Amazon Personalize automatically starts a full retraining of
the models backing your recommender.

- For
  _Top picks for you_ and _Recommended for you_ use cases, Amazon Personalize updates your recommender to consider new items for
  recommendations. Automatic updates are not a full
  retraining where the model learns from your users' behavior.
  Instead, automatic updates allow Amazon Personalize to feature your new items in recommendations before the recommender's next full retraining.
  For information about automatic updates, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates").
- If you use the _Trending now_ use case,
  Amazon Personalize automatically evaluates your interactions data every two hours and identifies trending items. You don't have to wait
  for your recommender to retrain.

While recommender retraining is in progress, you can still get recommendations from the recommender. Until the retraining
completes, the recommender uses the previous configuration and models. To track
updates, you can view the timestamp for the latest recommender update on the **Recommender details** page in the Amazon Personalize console. Or you can view the
`latestRecommenderUpdate` details from the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") operation.

## Maintaining custom solutions

By default, all new solutions use automatic training to create a new solution version every
7 days. Training continues until you delete the solution.

When you create a solution, we recommend that you use automatic training to manage solution version creation. This makes
maintaining your solution easier. It removes the manual training required for the solution to learn from your more recent
data. Without automatic training, you must manually create new solution versions for the solution to learn from your most
recent data. For more information about configuring automatic training, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

Your training frequency depends on your business requirements, the recipe that you use, and how frequently you import
data. For all recipes, we recommend training at least weekly. With automatic training, this is the default training
frequency. If you frequently add new items or actions, you might want to have a higher training frequency, depending on your
recipe.

- If you use User-Personalization-v2, User-Personalization, or Next-Best-Action, the solution automatically updates to consider new items or actions for
  recommendations. Automatic updates aren't the same as automatic training. An automatic update doesn't create a
  completely new solution version, and the model doesn't learn from your latest data. To maintain your solution, your
  training frequency should still be at least weekly. For more formation about automatic updates, including additional
  guidelines and requirements, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates").
- If you use Trending-Now, Amazon Personalize automatically identifies the top trending items in your interactions data over a configurable interval of time.
  Trending-Now can recommend items added since the last training through bulk or streaming interactions data. Your training frequency should still be at least weekly. For more information,
  see [Trending-Now
  recipe](native-recipe-trending-now.md "native-recipe-trending-now.md").
- If you don't use a recipe with automatic updates or the Trending-Now recipe, Amazon Personalize considers new items
  for recommendations only after the next training. For example, if you use the Similar-Items recipe, and you add new
  items daily, you must use a daily training frequency for these items to appear in recommendations that same day.

# How new data influences batch recommendations (custom resources)

After you create a custom solution version, how new data influences batch recommendations depends the data's type, the
method of import, and the custom recipe you use.

For user segments, Amazon Personalize generates segments using only the data present at
the last full solution version training. And Amazon Personalize uses only bulk data that you imported with an import mode of FULL
(replacing existing data). For more information about user segments, see [Getting batch user segments with custom resources](getting-user-segments.md "getting-user-segments.md").

When generating batch item recommendations, Amazon Personalize considers all bulk data present at the time of latest solution version creation.
This data can be imported with an import mode of FULL or INCREMENTAL. For newer bulk records to influence batch recommendations, you must create a new solution version and then create the batch inference job.

The following sections explain how individual imports influence batch item recommendations.

###### Topics

- [New interactions](#batch-new-interactions "#batch-new-interactions")
- [New users](#batch-new-users "#batch-new-users")
- [New items](#batch-new-items "#batch-new-items")

## New interactions

If you use a USER_PERSONALIZATION or PERSONALIZED_RANKING recipe, Amazon Personalize considers new item interactions data with existing
items and users within about 15 minutes from data import. These items and users must have been present at the latest training.
To make sure events are considered, we recommend you wait at
minimum 15 minutes before you start a batch inference job.
For all other recipes, and for events with new items or users, you must create a new solution version for the streamed events to
influence batch recommendations.

## New users

For users without interactions data, recommendations are initially for only popular items. If you use a
USER_PERSONALIZATION or PERSONALIZED_RANKING recipe and you record events for the user, their recommendations might become
more relevant within about 15 minutes after import without retraining. To make sure events are considered, we recommend you
wait at minimum 15 minutes before you start a batch inference job. For all other recipes, you must create a new
solution version for streamed events to influence batch recommendations for users without interactions data.

## New items

With User-Personalization-v2 and User-Personalization, when you create a batch inference job and specify the latest fully trained solution version for your solution,
Amazon Personalize automatically updates the solution version to include new items in recommendations with
exploration. If you don't specify the latest solution version, no update occurs. For any other recipe, you must create a new solution version for new items to be featured in batch recommendations.
For more information about exploration, see [Exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration").

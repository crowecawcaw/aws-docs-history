# How new data influences real-time recommendations

After you create a recommender or custom solution version, how new data
influences real-time recommendations depends on the data's type, the method of import, and the domain use case or custom recipe you use. The following sections
explain how new data influences real-time recommendations before the next training.

Training can be
a recommender's weekly automatic training, or automatic or manual solution version creation.
For manual training with User-Personalization, omit the `trainingMode` to use the default `FULL` training mode.

###### Topics

- [New interactions](#new-interactions "#new-interactions")
- [New items](#new-items "#new-items")
- [New users](#new-users "#new-users")
- [New actions](#new-actions "#new-actions")

## New interactions

New interactions are item or action interactions that you import after the latest training. For both real-time and
bulk data, if interactions involve a new item or action, Amazon Personalize might consider it for recommendations without training if your recipe or use case
features exploration. For more information, see [New items](#new-items "#new-items") or [New actions](#new-actions "#new-actions").

**Real-time events**

For use cases and recipes that feature real-time personalization, Amazon Personalize immediately uses real-time interactions
between a user and items or actions present at the latest training. When generating recommendations for the user in the
vent, Amazon Personalize uses these real-time interactions. For more information about real-time personalization, see [Real-time personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization").

For any domain use cases and custom recipes that don't feature real-time personalization, such as recommending similar items, your model learns from real-time interactions data only
after training.

**Bulk interactions**

For _bulk interactions_,
for both incremental _and_ full dataset import jobs, your model learns from bulk item interaction or action interaction
data only after the next training. Bulk data isn't used to update recommendations for real-time personalization.

For more information about importing more bulk data, see [Importing bulk data into Amazon Personalize with a
dataset import job](bulk-data-import-step.md "bulk-data-import-step.md").

## New items

New items are items that you import after the latest training.
They can come from either interactions data or item metadata in an Items dataset.

New items are considered for recommendations as follows:

- For _Top picks for you_ and _Recommended for you_ domain cases or User-Personalization-v2, User-Personalization, or Next-Best-Action recipes,
  Amazon Personalize automatically updates the model every two hours. After each update, Amazon Personalize
  considers new items for recommendations as part of exploration. When considering the new item, Amazon Personalize considers
  any metadata for the item. However this data will have a greater effect on recommendations only
  after you record interactions for the item and train a new model.
  For information about updates, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates").
- If you use the _Trending now_ use case,
  Amazon Personalize automatically evaluates your interactions data every two hours and identifies trending items. You don't have to wait
  for your recommender to train. If you use the _Trending-Now recipe_, Amazon Personalize automatically considers all new items over
  configurable intervals without training. For information about configuring intervals, see [Trending-Now
  recipe](native-recipe-trending-now.md "native-recipe-trending-now.md").
- If you don't use the Trending-Now recipe or your use case or recipe doesn't support automatic updates,
  Amazon Personalize will consider new items only after the next training.

## New users

New users are users that you import after the latest training.
They can come from either interactions data or user metadata in a Users dataset. For new, anonymous users (users without a userId),
you can record events for the user with a `sessionId` and Amazon Personalize will
associate events with the user before they log in. For more information, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

Amazon Personalize generates recommendations for new users as follows:

- If you use the Trending now domain use case or Trending-Now custom recipe, new users immediately receive
  recommendations for the top trending items. If you use the Popularity-Count recipe, new users immediately receive
  recommendations for items with the most interactions.
- For recipes or use cases that provide personalized recommendations for users,
  recommendations for new users are based on the early interaction histories of your existing users. The first items
  or actions these existing users interacted with are more likely to be recommended to new users. For the User-Personalization or
  Personalized-Ranking recipes, if you set `recency_mask` to `true`, recommendations also include
  items based on the latest popularity trends in your interactions data.

The following can increase recommendation relevance for new users:

- Interactions data – The primary way to improve recommendation relevance for a new user is to import data from their interactions with your items.
  For information about how new interactions data influences
  recommendations, see [New interactions](#new-interactions "#new-interactions").
- User metadata – Importing user metadata, such as GENDER or MEMBERSHIP_STATUS, can improve recommendations. For metadata to influence
  recommendations, you must wait for your domain recommender's weekly automatic retraining to complete. Or you must manually create a new solution version.
- Contextual metadata – If your use case or recipe supports
  contextual metadata and your Item interactions dataset has metadata fields for contextual data, you can provide the user's context in your request for recommendations. This does not require retraining. For more information, see
  [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md").

## New actions

New actions are actions that you import since the latest training. They can come
from either action interaction data or actions in an Actions dataset.

With the Next-Best-Action recipe, Amazon Personalize automatically updates a solution version every two hours. After
each update, Amazon Personalize considers new actions for recommendations as part of exploration. When considering the new action,
Amazon Personalize considers any metadata for the action. However, this data will have a greater effect on recommendations only after you
record action interactions for the action and fully retrain. For information about updates, see [Automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates")

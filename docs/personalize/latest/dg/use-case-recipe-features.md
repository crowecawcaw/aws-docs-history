# Use case and recipe features

With some use case and recipes, Amazon Personalize uses the following features to generate more relevant recommendations and improve item discovery
and engagement.

###### Topics

- [Real-time personalization](#about-real-time-personalization "#about-real-time-personalization")
- [Exploration](#about-exploration "#about-exploration")
- [Automatic updates](#automatic-updates "#automatic-updates")

## Real-time personalization

With some use cases and recipes, Amazon Personalize uses real-time personalization to update and adapt recommendations according
to a user's evolving interest. It updates recommendations for a user as you record their interactions with items or actions present at the latest full training.
You record these interactions
with an event tracker and the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") operation or, for interactions with actions, the PutActionInteractions operation.

For more information about recording events, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").
For information about new data influences real-time recommendations, including real-time personalization,
see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

The following use cases and recipes support real-time personalization:

- [Recommended for you (ECOMMERCE use case)](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case")
- [Top picks for you (VIDEO_ON_DEMAND use case)](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case")
- [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
- [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Personalized-Ranking-v2 recipe](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md")
- [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md")
- [Next-Best-Action recipe](native-recipe-next-best-action.md "native-recipe-next-best-action.md")

## Exploration

For some domain use cases and custom recipes, Amazon Personalize uses
exploration when recommending items. With exploration, recommendations include some items or actions that would be typically less likely to be recommended for the user,
such as new items or actions, items or actions with few interactions, or items or actions less relevant for the user based on their previous behavior.
This improves item discovery and engagement when you have a fast-changing catalog, or when new items, such as
news articles or promotions, are more relevant to users because they are fresh.

### Configuring exploration

If you use the User-Personalization-v2 recipe, Amazon Personalize handles exploration configuration for you
and items included through exploration have `Exploration` for the `Reason` in
the recommendation response. To make sure new items are included in recommendations, you can use a promotion filter
to promote new items based on creation timestamp.
For more information about promotions, see [Promoting items in real-time recommendations](promoting-items.md "promoting-items.md").

For all other use cases or recipes that use exploration, when you create a recommender or custom campaign, or when you create a
batch inference job (custom resources), you can configure exploration with the following fields:

- Emphasis on exploring less relevant items (exploration weight) – Configure how
  much to explore. Specify a decimal value between 0 to 1. The default is 0.3. The closer the value is to 1, the more exploration. With more exploration,
  recommendations include more items with less item interactions data or relevance based on previous behavior. At zero, no
  exploration occurs and recommendations are based on current data
  (relevance).
- Exploration item age cutoff – Specify the maximum item age in days since
  the latest interaction across all items in the Item interactions dataset. This defines the scope of item exploration based on
  item age. Amazon Personalize determines item age based on its creation timestamp or, if creation timestamp data is missing, item interactions data. For
  more information how Amazon Personalize determines item age, see [Creation timestamp data](items-datasets.md#creation-timestamp-data "items-datasets.md#creation-timestamp-data").

To increase the items Amazon Personalize considers
during exploration, enter a greater value. The minimum is 1 day and the default is 30 days. Recommendations might include items
that are older than the item age cut off you specify. This is because these items are
relevant to the user and exploration didn't identify them.

### Use cases and recipes that use exploration

For more information about each use case or recipe that uses exploration, see the following:

- [Recommended for you (ECOMMERCE use case)](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case")
- [Top picks for you (VIDEO_ON_DEMAND use case)](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case")
- [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
- [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Next-Best-Action recipe](native-recipe-next-best-action.md "native-recipe-next-best-action.md")

## Automatic updates

For some use cases and custom recipes, Amazon Personalize automatically updates your recommender or solution version to consider new items or actions
for recommendations.
There is no cost for automatic updates. For a list of use cases and recipes with automatic updates, see
[Domain use cases and custom recipes with automatic updates](#use-case-recipes-with-auto-update "#use-case-recipes-with-auto-update").

Automatic updates work as follows:

- When Amazon Personalize automatically updates your solution version or recommender depends on how you get recommendations:
  - For real-time recommendations,
    Amazon Personalize updates the solution version or recommender every two hours.
  - For batch item recommendations, when you create a batch inference job and specify the latest fully trained solution
    version for your solution, Amazon Personalize automatically updates the solution version to consider new items during exploration. If you don't specify the latest solution version, no update occurs.

- With each update, Amazon Personalize starts including new items in recommendations using [Exploration](#about-exploration "#about-exploration"). When considering a new item or action, Amazon Personalize considers any metadata for the
  item. However, this data will have a greater effect on recommendations only after you record interactions for the item
  and fully retrain.
- For an update to occur, you must provide new action, item, or interactions data since the last automatic update or
  retraining.
- Amazon Personalize considers new items until you import 750,000 items. This is the maximum number of items considered during training.

### Additional guidelines and requirements for custom resources

If you use custom resources, the following are guidelines and requirements for auto updates:

- Your solution version must be deployed in a campaign. Your campaign automatically uses the updated solution
  version.
- Automatic updates aren't the same as automatic training. An automatic update
  doesn't create a completely new solution version. And the model doesn't learn from your latest data. To maintain
  your solution, your automatic training frequency should still be at
  least weekly.
- After your solution automatically creates a new solution version or you manually create a new one,
  Amazon Personalize will not automatically update older solution versions, even
  if you deployed them in a campaign.
- If every two hours is not frequent enough, with User-Personalization you can manually create a solution version with
  `trainingMode` set to `UPDATE` to include those new items in recommendations. Just remember
  that Amazon Personalize automatically updates only your latest _fully_ trained solution version. The manually
  updated solution version won't be automatically updated in the future.
  If your solution uses automatic training, auto updates will resume for the next solution version. If not, manually create a new solution with
  training mode set to `FULL` and deploy it in a campaign.

### Domain use cases and custom recipes with automatic updates

For more information about each use case or recipe that features automatic updates, see the following:

- [Recommended for you (ECOMMERCE use case)](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case")
- [Top picks for you (VIDEO_ON_DEMAND use case)](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case")
- [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
- [User-Personalization recipe](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Next-Best-Action recipe](native-recipe-next-best-action.md "native-recipe-next-best-action.md")

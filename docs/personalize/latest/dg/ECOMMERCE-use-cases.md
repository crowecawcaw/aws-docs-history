# ECOMMERCE use cases

The following sections list the requirements and Amazon Resource Name
(ARN) for each ECOMMERCE use case.
For all use cases,
your interactions data must have the following:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.
  For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.

###### Note

If you use the [CreateRecommender](API_CreateRecommender.md "API_CreateRecommender.md") API, provide the ARN listed
here for the recipe ARN.

###### Topics

- [Most viewed](#most-viewed-use-case "#most-viewed-use-case")
- [Best sellers](#best-sellers-use-case "#best-sellers-use-case")
- [Frequently bought
  together](#frequently-bought-together-use-case "#frequently-bought-together-use-case")
- [Customers who viewed X
  also viewed](#customers-also-viewed-use-case "#customers-also-viewed-use-case")
- [Recommended for
  you](#recommended-for-you-use-case "#recommended-for-you-use-case")

## Most viewed

Get recommendations for popular items based on how many times your customers viewed an item.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-ecomm-popular-items-by-views`
- **GetRecommendations requirements:**

`userId`: Required

`itemId`: Not used

`inputList`: NA

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `View` events.

## Best sellers

Get recommendations for popular items based on how many times your customers purchased an item.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-ecomm-popular-items-by-purchases`
- **GetRecommendations requirements:**

`userId`: Required

`itemId`: Not used

`inputList`: NA

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `Purchase` events.

## Frequently bought

together

Get recommendations for items that customers frequently buy together
along with an item that you specify.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-ecomm-frequently-bought-together`
- **GetRecommendations requirements:**

`userId`: Required only if you filter by CurrentUser

`itemId`: Required

`inputList`: NA

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `Purchase` events.

## Customers who viewed X

also viewed

Get recommendations for items that customers also viewed based on an
item that you specify. With this use case, Amazon Personalize automatically filters
items the user purchased based on the userId that you specify and
`Purchase` events. If you apply your own filter, your filter is applied after the items the user already purchased
are filtered out.

When filtering, Amazon Personalize considers at most 100 item interactions per user per event type. This
applies to any automatic or custom filters. You can use the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") to request an increase for this limit. For more information, see the [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") section of the _Service Quotas User Guide_. If you don't import item interactions for a user for three months, your filters no longer
consider the user's historical data. To consider this data, you must import the user's entire event history again.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-ecomm-customers-who-viewed-x-also-viewed`
- **GetRecommendations requirements:**

`userId`: Required

`itemId`: Required

`inputList`: NA

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `View` events.
- **Recommended event
  types:**
  `Purchase` events.

## Recommended for

you

Get personalized recommendations for items based on a user that you specify. With this use case, Amazon Personalize automatically
filters out items the user purchased based on the userId that you specify and `Purchase` events.
If you apply your own filter, your filter is applied after the items the user already purchased
are filtered out.

When filtering, Amazon Personalize considers at most 100 item interactions per user per event type. This
applies to any automatic or custom filters. You can use the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") to request an increase for this limit. For more information, see the [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") section of the _Service Quotas User Guide_. If you don't import item interactions for a user for three months, your filters no longer
consider the user's historical data. To consider this data, you must import the user's entire event history again.

When recommending items, this use case uses [real-time-personalization](use-case-recipe-features.md#about-real-time-personalization "use-case-recipe-features.md#about-real-time-personalization") and
[exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration"). And it uses [automatic updates](use-case-recipe-features.md#automatic-updates "use-case-recipe-features.md#automatic-updates")
to consider new items for recommendations.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-ecomm-recommended-for-you`
- **GetRecommendations requirements:**

`userId`: Required

`itemId`: Not used

`inputList`: NA

- **Datasets used when training:**
  - Interactions (required)
  - Items (optional)
  - Users (optional)

- **Required number of events:** At
  minimum, 1000 events.
- **Recommended event
  types:** `View` and
  `Purchase` events.
- **Exploration configuration parameters:** When you create a recommender,
  you can configure exploration with the following.
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

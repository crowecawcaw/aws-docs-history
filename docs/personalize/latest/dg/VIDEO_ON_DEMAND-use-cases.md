# VIDEO_ON_DEMAND use

cases

The following sections list the requirements and Amazon Resource Name
(ARN) for each VIDEO_ON_DEMAND use case.
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

- [Because you watched
  X](#because-you-watched-use-case "#because-you-watched-use-case")
- [More like X](#more-like-y-use-case "#more-like-y-use-case")
- [Most popular](#hot-picks-use-case "#hot-picks-use-case")
- [Trending now](#trending-now-use-case "#trending-now-use-case")
- [Top picks for you](#top-picks-use-case "#top-picks-use-case")

## Because you watched

X

Get recommendations for videos that other users also watched based
on a video that you specify. With this use case, Amazon Personalize automatically
filters videos the user watched based on the userId you specify and `Watch`
events. If you apply your own filter, your filter is applied after the videos the user watched
are filtered out.

When filtering, Amazon Personalize considers at most 100 item interactions per user per event type. This
applies to any automatic or custom filters. You can use the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") to request an increase for this limit. For more information, see the [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") section of the _Service Quotas User Guide_. If you don't import item interactions for a user for three months, your filters no longer
consider the user's historical data. To consider this data, you must import the user's entire event history again.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-vod-because-you-watched-x`
- **GetRecommendations API requirements:**

`userId`: Required

`itemId`: Required

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `Watch` events.

## More like X

Get recommendations for videos that are similar to a video that you
specify. With this use case, Amazon Personalize automatically filters videos the
user watched based on the userId that you specify and `Watch`
events. If you apply your own filter, your filter is applied after the videos the user watched
are filtered out.

When filtering, Amazon Personalize considers at most 100 item interactions per user per event type. This
applies to any automatic or custom filters. You can use the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") to request an increase for this limit. For more information, see the [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") section of the _Service Quotas User Guide_. If you don't import item interactions for a user for three months, your filters no longer
consider the user's historical data. To consider this data, you must import the user's entire event history again.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-vod-more-like-x`
- **GetRecommendations API requirements:**

`userId`: Required

`itemId`: Required

- **Datasets used when training:**
  - Interactions (required)
  - Items (required)

- **Required number of events:** At
  minimum, 1000 events of any type.
- **Recommended event
  types:** `Watch` and
  `Click` events.

## Most popular

Get recommendations for videos that have been watched by the most
users.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-vod-most-popular`
- **GetRecommendations
  requirements:**

`userId`: Required

`itemId`: Not used

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required event types:** At
  minimum, 1000 `Watch` events.

## Trending now

Get recommendations for videos that are currently trending. Trending videos are items
that are rapidly becoming more popular with your users. Every two hours, Amazon Personalize
automatically evaluates your interactions data and identifies trending items.

- **Recipe ARN:**
  `arn:aws:personalize:::recipe/aws-vod-trending-now`
- **GetRecommendations API requirements:**

`userId`: Required only if you filter by CurrentUser or by items
a user has interacted with

`itemId`: Not used

- **Datasets used when training:** Only Item interactions dataset (required)
- **Required number of events:** At
  minimum, 1000 events of any type.

## Top picks for you

Get personalized content recommendations for a user that you
specify. With this use case, Amazon Personalize automatically filters videos the
user watched based on the userId that you specify and `Watch`
events. If you apply your own filter, your filter is applied after the videos the user watched
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
  `arn:aws:personalize:::recipe/aws-vod-top-picks`
- **GetRecommendations requirements:**

`userId`: Required

`itemId`: Not used

- **Datasets used when training:**
  - Interactions (required)
  - Items (optional)
  - Users (optional)

- **Required number of events:** At
  minimum, 1000 events.
- **Recommended event
  types:**
  `Click` and `Watch` events.
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

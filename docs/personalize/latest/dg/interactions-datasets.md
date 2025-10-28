# Preparing item interaction data for training

An _item interaction_ is a positive interaction event between a user and an item in your catalogue.
For example, a user watching a movie, viewing a listing, or purchasing a pair of shoes.
You import data about your users' interactions with your items into a _Item interactions dataset_.
You can
record multiple event types, such as _click_, _watch_ or
_purchase_.

For example, if a
user _clicks_ a particular item and then _likes_ the item,
you can have Amazon Personalize use these events as training data. For each event, you would record the
user's ID, the item's ID, the timestamp (in Unix time epoch format), and the event type
(_click_ and _like_). You
would then add both item interaction events to an _Item interactions dataset_.

For all domain use cases and custom recipes, your bulk item interactions data must be in a CSV file. Each row should represent
a single interaction between a user and an item.
After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

The following sections provide more information on how to prepare your item interaction data for Amazon Personalize. For
bulk data format guidelines for all types of data, see [bulk data format guidelines](preparing-training-data.md#general-formatting-guidelines "preparing-training-data.md#general-formatting-guidelines")

###### Topics

- [Item interaction data requirements](#item-interaction-requirements "#item-interaction-requirements")
- [Timestamp data](#timestamp-data "#timestamp-data")
- [Event type and event value data](#event-type-and-event-value-data "#event-type-and-event-value-data")
- [Contextual metadata](#interactions-contextual-metadata "#interactions-contextual-metadata")
- [Impressions data](#interactions-impressions-data "#interactions-impressions-data")
- [Interactions data example](#interactions-data-schema-example "#interactions-data-schema-example")

## Item interaction data requirements

The following
sections list item interaction data requirements for Amazon Personalize. For additional quotas, see [Amazon Personalize endpoints and quotas](limits.md "limits.md").

### Minimum training requirements

For all domain use cases and custom recipes, your bulk item interactions data must have the following:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.

For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.

To create a recommender or a custom solution, you must at minimum create an _Item interactions dataset_.

### Column requirements

Your item interactions data must have the following columns.

- USER_ID – The unique identifier of the user who interacted with the item. Every event must have an USER_ID. It must be a `string` with a max length of 256 characters.
- ITEM_ID – The unique identifier of the item that the user interacted with. Every event must have an item ID. It must be a `string` with a max length of 256 characters.
- TIMESTAMP – The time the event occurred (in Unix epoch time format in seconds). Every interaction must have an TIMESTAMP.
  For more information, see [Timestamp data](#timestamp-data "#timestamp-data").
- EVENT_TYPE – The nature of item interaction event, such as _click_, _watch_ or
  _purchase_. For domain recommenders, you must have an event type column and every
  interaction must have an event type. For all custom recipes, an EVENT_TYPE column is recommended but optional. If you add it, every
  event must have an event type. For more information see [Event type and event value data](#event-type-and-event-value-data "#event-type-and-event-value-data").

You are free to add additional custom columns depending on your use case and
your data. The maximum number of optional metadata columns is 5. These columns can include empty/null values.
We recommend that these columns be at minimum 70 percent complete.

## Timestamp data

Timestamp data must be in Unix epoch time format in seconds. For example, the Epoch timestamp in seconds for date
July 31, 2020 is 1596238243. To convert dates to Unix epoch timestamps, use an [Epoch converter - Unix timestamp converter](https://www.epochconverter.com "https://www.epochconverter.com").

Amazon Personalize uses timestamp data to calculate recency and identify any time-based patterns.
It helps Amazon Personalize keep recommendations up-to-date with users' evolving preferences.

## Event type and event value data

An Item interactions dataset can store event type and event value data for each interaction.
Only custom resources use event value data.

### Event type data

An item interaction's event type provides context about its nature and significance.
Event type examples might be _click_, _watch_ or
_purchase_. Amazon Personalize uses event type data, such as _click_ or _purchase_ data, to identify
user intent and interest. The maximum number of distinct event types combined with total number of optional metadata columns in an Item interactions dataset
is 10.

For domain recommenders, you must have an event type column and every
interaction must have an event type. For all custom recipes, an EVENT_TYPE column is recommended but optional. If you add it, every
event must have an event type.

If you create custom resources, you can choose the events used for training by event type.If your dataset has
multiple event types in an EVENT_TYPE column, and you do not provide an event type when you configure a custom solution,
Amazon Personalize uses all item interactions data for training with equal weight regardless of type. For more information, see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md").

If you have multiple event types and use the User-Personalization-v2 recipe or Personalized-Ranking-v2 recipe,
when you configure a custom solution you can specify different weights for different types. For example, you can
configure a solution to give more weight to purchase events than click events.
For more information, see [Optimizing a solution with events configuration](optimizing-solution-events-config.md "optimizing-solution-events-config.md").

The following use cases have specific
event type requirements:

VIDEO_ON_DEMAND domain use cases

- Because you watched X requires at minimum 1000 `Watch` events.
- Most popular requires at minimum 1000 `Watch` events.

ECOMMERCE domain use cases

- Most viewed requires at minimum 1000 `View` events.
- Best sellers requires at minimum 1000 `Purchase` events.

#### Positive and negative event types

Amazon Personalize assumes any interaction is a positive one. Interactions with a negative event type, such as
_dislike_, won't necessarily keep the item from appearing in the user's future
recommendations.

The following are ways to have negative events and users' disinterest influence recommendations:

- For all domain use cases and the [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") recipe, Amazon Personalize can use impressions data. When
  an item appears in impressions data and a user doesn't choose it, the item is less likely to appear in
  recommendations. For more information, see [Impressions data](#interactions-impressions-data "#interactions-impressions-data").
- If you use custom resources and import positive and negative event types, you can train on only positive event
  types and then filter out items the user interacted with negatively. For more information, see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md") and [Filtering recommendations and user segments](filter.md "filter.md").

### Event value data (custom resources)

Event value data might be the percentage of a movie that a user watched or a rating out of 10. If you create custom solutions,
you can choose records used for training
based on data in EVENT_TYPE and EVENT_VALUE columns.
With domain recommenders, Amazon Personalize doesn't use event value data and you can't filter events before
training.

To choose records based on type and value, record event type and event value data for events. Not all events must have an event value.
The value you choose
for each event depends on what data you want to exclude and what event types you are recording. For example, you might
match the user activity, such as the percentage of video the user watched for _watch_ event types.

When you configure a solution, you set a specific value as a threshold to exclude records from training. For example,
if your EVENT_VALUE data for events with an EVENT_TYPE of _watch_ is the percentage of a video that a
user watched, if you set the event value threshold to 0.5, and the event type to _watch_, Amazon Personalize trains
the model using only _watch_ interaction events with an EVENT_VALUE greater than or equal to 0.5.

For more information, see [Choosing the item interaction data used for training](event-values-types.md "event-values-types.md")

## Contextual metadata

With certain recipes and recommender use cases, Amazon Personalize can use contextual metadata when identifying underlying
patterns that reveal the most relevant items for your users. Contextual metadata is interactions data you collect on the
user's environment at the time of an event, such as their location or device type. You can also specify a user's
context when you get recommendations for the user.

Include contextual metadata to provide a more personalized experience for your users and
decrease the cold-start phase for new users. The cold-start phase is when recommendations are less relevant due
to a lack of historical user data.

For example, if your item interactions CSV file includes a DEVICE_TYPE column with `tablet` and `phone` values,
Amazon Personalize can learn how customers shop differently with different devices. When you get recommendations for a user,
you can specify their device and recommendations will be more relevant, even if the user has no interaction history.

The following shows how you would format a item interactions CSV file with a DEVICE_TYPE column as contextual metadata.

```
ITEM_ID,USER_ID,TIMESTAMP,DEVICE_TYPE,EVENT_TYPE
shoe12345,12,1428624000,Tablet,CLICK
shoe12346,12,1420416000,Tablet,CLICK
shoe12347,12,1410652800,Tablet,BUY
shoe4444,13,1409961600,Phone,CLICK
shoe4445,13,1402876800,Phone,BUY
shoe4336,13,1402185600,Phone,CLICK
.....
```

For Domain dataset groups, the following recommender use cases can use contextual metadata:

- [Recommended for
  you](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case") (ECOMMERCE domain)
- [Top picks for you](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case") (VIDEO_ON_DEMAND domain)

For custom resources, recipes that use contextual metadata include the following:

- [User-Personalization-v2](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md") and [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md") and [Personalized-Ranking](native-recipe-search.md "native-recipe-search.md")

For information about including context when you get recommendations, see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md").
For an end to end example that shows how to use contextual metadata, see the following AWS Machine Learning Blog post: [Increasing the relevance of your Amazon Personalize recommendations by leveraging contextual information](https://aws.amazon.com/blogs/machine-learning/increasing-the-relevance-of-your-amazon-personalize-recommendations-by-leveraging-contextual-information/ "https://aws.amazon.com/blogs/machine-learning/increasing-the-relevance-of-your-amazon-personalize-recommendations-by-leveraging-contextual-information/").

## Impressions data

Impressions are lists of items that were visible to a user when they interacted with (for example, clicked or watched) a
particular item. If you use a domain use case that provides personalization or the [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
recipe, Amazon Personalize can use impressions data to guide exploration.

With exploration, recommendations include some items or actions that would be typically less likely to be recommended for the user,
such as new items or actions, items or actions with few interactions, or items or actions less relevant for the user based on their previous behavior. The more frequently an
item occurs in impressions data, the less likely it is that Amazon Personalize includes the item in exploration.

When you create a recommender or solution, Amazon Personalize always excludes impressions data from training. This is because Amazon Personalize
doesn't train your models with impressions data. Instead, it uses it when you get recommendations to guide exploration for
the user.

Impression values can have at most 1000 characters (including the vertical bar character).
For Domain dataset groups, the following recommender use cases can use impressions data:

- [Recommended for
  you](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case") (ECOMMERCE domain)
- [Top picks for you](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case") (VIDEO_ON_DEMAND domain)

For more information about exploration see [Exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration").
Amazon Personalize can model two types of impressions: [Implicit impressions](#implicit-impressions-info "#implicit-impressions-info") and [Explicit impressions](#explicit-impressions-info "#explicit-impressions-info").

### Explicit impressions

_Explicit impressions_ are impressions that you manually record and send to Amazon Personalize.
Use explicit impressions to manipulate results from Amazon Personalize. The order of the items has no impact.

For example, you might have a shopping application that provides recommendations for shoes. If you only recommend
shoes that are currently in stock, you can specify these items using explicit impressions. Your recommendation workflow
using explicit impressions might be as follows:

1. You request recommendations for one of your users using the Amazon Personalize [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")
   API.
2. Amazon Personalize generates recommendations for the user using your model (solution version) and returns them in the API
   response.
3. You show the user only the recommended shoes that are in stock.
4. For real-time incremental data import, when your user interacts with (for example, clicks) a pair of shoes, you
   record the choice in a call to the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API and
   list the recommended items that are in stock in the `impression` parameter. For a code sample see [Recording
   item interaction events with impressions data](putevents-including-impressions-data.md "putevents-including-impressions-data.md").

For importing impressions in historical item interactions data, you can list explicit impressions in your csv
file and separate each item with a '|' character. The vertical bar character counts towards the 1000
character limit. For an example see [Formatting explicit impressions](#data-prep-including-explicit-impressions "#data-prep-including-explicit-impressions"). 5. Amazon Personalize uses the impression data to guide exploration, where future recommendations include new shoes with less
interactions data or relevance.

#### Formatting explicit impressions

To include explicit impressions in your CSV file, add an IMPRESSION column. For each item interaction, add list of
itemIds separated with a vertical bar, '|', character. The vertical bar character counts toward the 1000
character limit for impressions data. If you include explicit impressions in [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") operation, you specify the items in an array of strings.

The following is a short excerpt from a CSV file that includes explicit impressions in the
`IMPRESSION` column.

| EVENT_TYPE | IMPRESSION | ITEM_ID | TIMESTAMP | USER_ID |
| ---------- | ---------- | ------- | --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ |
| click      | 73         | 70      | 17        | 95      | 96                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 73  | 1586731606 | USER_1 |
| click      | 35         | 82      | 78        | 57      | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 63  | 1          | 90     | 76  | 75  | 49  | 71  | 26  | 24  | 25  | 6   | 35  | 1586735164 | USER_2 |
| ...        | ...        | ...     | ...       | ...     | The application showed user `USER_1` items `73`, `70`, `17`, `95`, and `96` and the user ultimately chose item `73`. When you create a new solution version based on this data, items `70`, `17`, `95`, and `96` will be less frequently recommended to user `USER_1`. ### Implicit impressions _Implicit impressions_ are the recommendations, retrieved from Amazon Personalize, that you show the user. Your CSV file doesn't need to include IMPRESSION or RECOMMENDATION_ID columns to use implicit impressions. Instead, you include the `RecommendationId` (returned by the [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") and [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md") operations) in [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") requests. Amazon Personalize derives the implicit impressions based on your recommendation data. For example, you might have an application that provides recommendations for streaming video. Your recommendation workflow using implicit impressions might be as follows: 1. You request video recommendations for one of your users using the Amazon Personalize [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") API operation. 2. Amazon Personalize generates recommendations for the user using your model (solution version) and returns them with a `recommendationId` in the API response. 3. You show the video recommendations to your user in your application. 4. When your user interacts with (for example, clicks) a video, record the choice in a call to the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") API and include the `recommendationId` as a parameter. For a code sample see [Recording item interaction events with impressions data](putevents-including-impressions-data.md "putevents-including-impressions-data.md"). 5. Amazon Personalize uses the `recommendationId` to derive the impression data from the previous video recommendations, and then uses the impression data to guide exploration, where future recommendations include new videos with less interactions data or relevance. For more information on recording events with implicit impression data, see [Recording item interaction events with impressions data](putevents-including-impressions-data.md "putevents-including-impressions-data.md"). ## Interactions data example The following interactions data represents historical user activity from a streaming video website. You might use the data to train a model that provides movie recommendations based on users' interaction data. Note that some values for EVENT_VALUE are null. `USER_ID,ITEM_ID,EVENT_TYPE,EVENT_VALUE,TIMESTAMP 196,242,watch,.50,881250949 186,302,watch,.75,891717742 22,377,click,,878887116 244,51,click,,880606923 166,346,watch,.50,886397596 298,474,watch,.25,884182806 115,265,click,,881171488 253,465,watch,.50,891628467 305,451,watch,.75,886324817` Amazon Personalize requires the `USER_ID`, `ITEM_ID`, and `TIMESTAMP` column. `USER_ID` is the identifier for a user of your application. `ITEM_ID` is the identifier for a movie. `EVENT_TYPE` and `EVENT_VALUE` are the identifiers for user interactions. In the sample data, the events are `watch` and `click` events and the values are the percentage of a video that a user watched. The `TIMESTAMP` represents the Unix epoch time that the movie purchase took place. After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). This is what the schema JSON file would look like for the sample data. `{ "type": "record", "name": "Interactions", "namespace": "com.amazonaws.personalize.schema", "fields": [ { "name": "USER_ID", "type": "string" }, { "name": "ITEM_ID", "type": "string" }, { "name": "EVENT_TYPE", "type": "string" }, { "name": "EVENT_VALUE", "type": "float" }, { "name": "TIMESTAMP", "type": "long" } ], "version": "1.0" }` |

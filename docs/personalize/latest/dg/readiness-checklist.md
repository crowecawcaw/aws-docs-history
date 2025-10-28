# Readiness checklist

This checklist provides lists of Amazon Personalize features, requirements, and data guidance. It can help you plan,
or you can use it as a reference as you create resources in Amazon Personalize.

###### Topics

- [Have you matched your use cases to Amazon Personalize resources?](#readiness-usecases "#readiness-usecases")
- [Do you have enough item interaction data?](#readiness-interact-data "#readiness-interact-data")
- [Do you have a real-time event streaming architecture in place?](#readiness-events "#readiness-events")
- [Is your data optimized for Amazon Personalize?](#readiness-data-prep "#readiness-data-prep")
- [Do you collect optional data that can improve recommendations?](#readiness-optional-data "#readiness-optional-data")
- [Do you have a plan to test your recommendations?](#readiness-ab-testing "#readiness-ab-testing")
- [Do you have additional business goals?](#readiness-business-goals "#readiness-business-goals")

## Have you matched your use cases to Amazon Personalize resources?

Amazon Personalize recommendations can address the following use cases:

- Generating personalized recommendations for a user
- Recommending similar or related items
- Recommending trending or popular items
- Recommending the next best actions for a user
- Re-ordering by relevance (only with custom resources)
- Generating user segments (only with custom resources)

Amazon Personalize features domain based resources and custom resources configured for these use cases. You start by creating a
Domain dataset group or a Custom dataset group:

- With a _Domain dataset group_, you create resources that are pre-configured and optimized for
  for the VIDEO_ON_DEMAND or ECOMMERCE domains.

If you have a streaming video or e-commerce application, we recommend that you start with a Domain dataset group. You
can still add custom resources, such as solutions and solution versions trained for custom use cases. And you can still
use custom resources to get batch recommendations. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group.

- With a _Custom dataset group_, you choose a recipe that matches your use case. You then train
  and deploy only configurable solutions and solution versions (trained Amazon Personalize recommendation models). When ready,
  you can deploy the solution version in a campaign for real-time recommendations. Or you can get
  batch recommendations without a campaign.

If you don't have a
streaming video or e-commerce application, we recommend that you create a Custom dataset group. Otherwise, start with
a Domain dataset group and adding custom resources as necessary.

For information on the use cases and custom recipes available in Amazon Personalize, see [Matching your use case to Amazon Personalize resources](use-cases-and-recipes.md "use-cases-and-recipes.md").

## Do you have enough item interaction data?

For all use cases and recipes, you must have at
minimum 1,000 item interactions for 25 unique users with at least two interactions each. For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.

If you aren't sure
if you have enough data, you can import and analyze it with the Amazon Personalize console. For more information, see [Analyzing quality and quantity of data in Amazon Personalize datasets](analyzing-data.md "analyzing-data.md").

## Do you have a real-time event streaming architecture in place?

If you don't have enough
item interaction data, you can use Amazon Personalize to collect additional real-time event data. With some recipes and use cases, Amazon Personalize
can learn from your user’s most recent activity and update recommendations as they use your application.

For information about recording events, including how events impact recommendations, a list of third-party event
tracking services, and sample implementations, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

## Is your data optimized for Amazon Personalize?

We recommend you check for the following in your data:

- Check for missing values. We recommend that a minimum of 70% of your records have data for every attribute. We
  recommend columns that allow null values be at least 70% complete.
- Fix any inaccuracies or issues in your data, such as inconsistent naming conventions, duplicate categories for an
  item, mismatched IDs across datasets, or duplicate IDs. These issues can negatively impact recommendations or lead to
  unexpected behavior. For example, you might have both “N/A” and “Not Applicable” in your data, but filter out
  recommendations based on only “N/A”. Items marked "Not Applicable" would not be removed by the filter.
- If an item, user, or action can have multiple categories, such as a movie with multiple genres, combine the categorical
  values into one attribute and separate each value with the | operator. For example, a movie’s GENRES data might be
  Action | Adventure | Thriller.
- Avoid having more than 1000 possible categories for a column (unless the column contains data for only filtering
  purposes).

For a complete list of data recommendations, and instructions on how you can use Amazon Personalize to identify issues, see [Analyzing quality and quantity of data in Amazon Personalize datasets](analyzing-data.md "analyzing-data.md").

## Do you collect optional data that can improve recommendations?

The following data can help improve your recommendation relevance.

- Event type (required for all Domain dataset group use cases)
- Event value
- Contextual metadata
- Item and user metadata
- Action interaction data (used by only PERSONALIZED_ACTIONS recipes)

For more information on the types of data Amazon Personalize can use, see [Types of data Amazon Personalize can use](datasets.md "datasets.md").

## Do you have a plan to test your recommendations?

You can use A/B testing to compare
the results of different groups of users interacting with recommendations from different models. A/B testing can help you
compare different recommendation strategies and see if recommendations are helping you achieve your business goals.
For more information, see [Measuring recommendation impact with A/B testing](ab-testing-recommendations.md "ab-testing-recommendations.md").

## Do you have additional business goals?

In some cases, you might have goals in
addition to generating relevant recommendations for your users. For example, you might want to maximize revenue, or
promote certain types of items from a certain category. The following Amazon Personalize features can help:

- Promotions: You can use promotions to make sure a certain percentage of items satisfy your business requirements.
  For more information, see [Promoting items in real-time recommendations](promoting-items.md "promoting-items.md").
- Optimizing for business objective: For some Custom dataset group recipes, you can optimize a solution for a
  custom objective, such as maximizing streaming minutes or increasing revenue. For more information, see [Optimizing a solution for an additional
  objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").
- Filtering recommendations. Use filters to apply business rules to recommendations. You can use filters to include
  or exclude certain types of items from recommendations. For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

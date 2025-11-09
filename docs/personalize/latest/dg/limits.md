# Amazon Personalize endpoints and quotas

The following sections contain information about Amazon Personalize guidelines,
quotas, and endpoints. For adjustable quotas, you can request a quota
increase using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For more information, see [Requesting a quota
increase](#requesting-limit-increase "#requesting-limit-increase").

###### Topics

- [Amazon Personalize endpoints and regions](#regions "#regions")
- [Compliance](#compliance "#compliance")
- [Service quotas](#limits-table "#limits-table")
- [Requesting a quota
  increase](#requesting-limit-increase "#requesting-limit-increase")

## Amazon Personalize endpoints and regions

For a list of Amazon Personalize endpoints by region, see [AWS regions and endpoints](../../../general/latest/gr/personalize.md "../../../general/latest/gr/personalize.md") in the _Amazon Web Services General Reference_.

## Compliance

For information about Amazon Personalize compliance programs, see [AWS compliance](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/"), [AWS compliance
programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"), and [AWS services in
scope by compliance program](https://aws.amazon.com/compliance/services-in-scope "https://aws.amazon.com/compliance/services-in-scope").

## Service quotas

Your AWS account has the following quotas for Amazon Personalize.

| Resource                                                                                                                                                                                                                     | Quota                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Item interactions**                                                                                                                                                                                                        |
| Minimum number of unique item interactions required to create a solution version or recommender.<br>For a custom solution, you must have this many records after any filtering by event type or event value before training. | 1000                                                                                            |
| For User-Personalization-v2 and Personalized-Ranking-v2 recipes, the maximum number of item interactions that are considered by a model<br>during training.                                                                  | 3 billion                                                                                       |
| For all domain use cases and custom recipes other than User-Personalization-v2 or Personalized-Ranking-v2,<br>the maximum number of item interactions that are considered by a model<br>during training.                     | 500 million (adjustable)                                                                        |
| Maximum number of distinct event types combined with total<br>number of optional metadata columns in an Item interactions dataset.                                                                                           | 10                                                                                              |
| Maximum number of metadata columns, excluding reserved<br>fields, in an Item interactions dataset.                                                                                                                           | 5                                                                                               |
| Maximum number of characters for categorical data and impression<br>values.                                                                                                                                                  | 1000                                                                                            |
| Maximum amount of bulk item interactions data per dataset import job with FULL import mode.                                                                                                                                  | 100 GB (increases to 1TB with any increase to _Item interactions considered by a model_)        |
| Maximum amount of bulk item interactions data per dataset import job with INCREMENTAL import mode.                                                                                                                           | 1 GB                                                                                            |
| Minimum number of item interactions records per dataset import job with FULL or INCREMENTAL import mode.                                                                                                                     | 1000                                                                                            |
| **Users**                                                                                                                                                                                                                    |
| Minimum number of unique users in item interactions data, with at minimum 2 item interactions<br>each, required to create a domain recommender or custom solution version.                                                   | 25                                                                                              |
| Minimum percentage of total users that must have<br>at minimum 2 item interactions or more before you can<br>create a domain recommender or custom solution version.                                                         | 1 percent                                                                                       |
| Maximum number of metadata fields for a Users<br>dataset.                                                                                                                                                                    | 25                                                                                              |
| Maximum number of characters for USER_ID data values.                                                                                                                                                                        | 256                                                                                             |
| Maximum number of characters for categorical data<br>values.                                                                                                                                                                 | 1000 characters                                                                                 |
| Maximum amount of bulk user data per dataset import job with FULL import mode.                                                                                                                                               | 100 GB                                                                                          |
| Maximum amount of bulk user data per dataset import job with INCREMENTAL import mode.                                                                                                                                        | 1 GB                                                                                            |
| **Items**                                                                                                                                                                                                                    |
| For User-Personalization-v2 or Personalized-Ranking-v2, the maximum number of items that are considered by a model<br>during training. These items are from both the Items and Item interactions dataset.                    | 5 million                                                                                       |
| For all domain use cases and custom recipes other than User-Personalization-v2 and Personalized-Ranking-v2, the maximum number of items that are considered by a model during<br>training and generating recommendations.    | 750,000                                                                                         |
| Maximum number of metadata fields for an Items<br>dataset.                                                                                                                                                                   | 100                                                                                             |
| Maximum number of characters for ITEM_ID data values.                                                                                                                                                                        | 256                                                                                             |
| Maximum number of characters for categorical and non-categorical string data<br>values.                                                                                                                                      | 1000 characters                                                                                 |
| Maximum number of textual fields for an Items dataset.                                                                                                                                                                       | 1                                                                                               |
| Maximum number of characters for textual data values for<br>Chinese and Japanese languages.                                                                                                                                  | 7,000 characters                                                                                |
| Maximum number of characters for textual data values for all<br>other languages.                                                                                                                                             | 20,000 characters                                                                               |
| Maximum amount of bulk items data per dataset import job with BULK import mode.                                                                                                                                              | 100 GB                                                                                          |
| Maximum amount of bulk item data per dataset import job with INCREMENTAL import mode.                                                                                                                                        | 1 GB                                                                                            |
| **Actions**                                                                                                                                                                                                                  |
| Maximum number of actions that are considered by a model during<br>training and generating recommendations.                                                                                                                  | 1000                                                                                            |
| Maximum number of metadata fields for an Actions<br>dataset.                                                                                                                                                                 | 10                                                                                              |
| Maximum number of characters for ACTION_ID data values.                                                                                                                                                                      | 256                                                                                             |
| Maximum number of characters for categorical data<br>values.                                                                                                                                                                 | 1000 characters                                                                                 |
| Maximum amount of bulk actions data per dataset import job with BULK import mode.                                                                                                                                            | 100 GB                                                                                          |
| Maximum amount of bulk actions data per dataset import job with INCREMENTAL import mode.                                                                                                                                     | 1 GB                                                                                            |
| **Action interactions**                                                                                                                                                                                                      |
| Maximum number of action interactions that are considered by a model<br>during training.                                                                                                                                     | 500 million                                                                                     |
| Maximum number of metadata columns, excluding reserved<br>fields, in a Action interactions dataset.                                                                                                                          | 5                                                                                               |
| Maximum amount of bulk interactions data per dataset import job with FULL import mode.                                                                                                                                       | 100 GB (increases to 1TB with any increase to _Action item interactions considered by a model_) |
| Maximum amount of bulk interactions data per dataset import job with INCREMENTAL import mode.                                                                                                                                | 1 GB                                                                                            |
| **Individual record<br>import APIs**                                                                                                                                                                                         |
| Maximum rate of `PutEvents` requests per dataset group.                                                                                                                                                                      | 1000/second                                                                                     |
| Maximum number of events in a `PutEvents`<br>call.                                                                                                                                                                           | 10                                                                                              |
| Maximum size of an event.                                                                                                                                                                                                    | 10 KB                                                                                           |
| Maximum rate of `PutActionInteractions` requests per dataset group.                                                                                                                                                          | 1000/second                                                                                     |
| Maximum number of action interaction events in a `PutActionInteractions`<br>call.                                                                                                                                            | 10                                                                                              |
| Maximum size of an action interaction event.                                                                                                                                                                                 | 10 KB                                                                                           |
| Maximum rate of `PutItems` requests per dataset group.                                                                                                                                                                       | 10/second                                                                                       |
| Maximum number of items in a `PutItems`<br>call.                                                                                                                                                                             | 10                                                                                              |
| Maximum rate of `PutUsers` requests per dataset group.                                                                                                                                                                       | 10/second                                                                                       |
| Maximum number of users in a `PutUsers`<br>call.                                                                                                                                                                             | 10                                                                                              |
| Maximum rate of `PutActions` requests per dataset group.                                                                                                                                                                     | 10/second                                                                                       |
| Maximum number of users in a `PutActions`<br>call.                                                                                                                                                                           | 10                                                                                              |
| **Legacy recipes**                                                                                                                                                                                                           |
| Maximum amount of combined data for Users and Items datasets<br>for HRNN-metadata and HRNN-Coldstart recipes.                                                                                                                | 5 GB                                                                                            |
| Maximum number of cold start items the HRNN-Coldstart recipe<br>supports to train a model (create a solution version).                                                                                                       | 80000                                                                                           |
| Minimum number of cold start items the HRNN-Coldstart recipe<br>requires to train a model (create a solution version).                                                                                                       | 100                                                                                             |
| **Filters**                                                                                                                                                                                                                  |
| Total number of filters per dataset group.                                                                                                                                                                                   | 30 (adjustable)                                                                                 |
| Maximum number of distinct dataset fields for a filter.                                                                                                                                                                      | 10                                                                                              |
| Total number of distinct dataset fields across all filters in a dataset group.                                                                                                                                               | 20                                                                                              |
| Maximum number of item interactions per user per event type considered<br>by a filter.                                                                                                                                       | 100 interactions (adjustable)                                                                   |
| Maximum number of action interactions per user per event type considered<br>by a filter.                                                                                                                                     | 300 action interactions (adjustable)                                                            |
| **GetRecommendations / GetPersonalizedRanking / GetActionRecommendations<br>requests**                                                                                                                                       |
| Maximum transaction rate for `GetRecommendations`, `GetActionRecommendations` and<br>`GetPersonalizedRanking` requests.                                                                                                      | 2500/sec                                                                                        |
| Maximum number of `GetRecommendations` requests<br>per second per campaign.                                                                                                                                                  | 500/sec                                                                                         |
| Maximum number of `GetActionRecommendations` requests<br>per second per campaign.                                                                                                                                            | 500/sec                                                                                         |
| Maximum number of `GetPersonalizedRanking`<br>requests per second per campaign.                                                                                                                                              | 500/sec.                                                                                        |
| Maximum number of metadata columns per `GetRecommendations` or `GetPersonalizedRanking`<br>request.                                                                                                                          | 10                                                                                              |
| Maximum number of recommendation results for a `GetRecommendation` request without<br>metadata.                                                                                                                              | 500                                                                                             |
| Maximum number of recommendation results for a `GetRecommendation` request with<br>metadata.                                                                                                                                 | 50                                                                                              |
| Maximum number of items for ranking in a `GetPersonalizedRanking` request without<br>metadata.                                                                                                                               | 500                                                                                             |
| Maximum number of items for ranking in a `GetPersonalizedRanking` request with<br>metadata.                                                                                                                                  | 50                                                                                              |
| **Metric attribution quotas**                                                                                                                                                                                                |
| Maximum number of metrics for a metric attribution                                                                                                                                                                           | 10                                                                                              |
| Maximum number of unique event attribution sources                                                                                                                                                                           | 100                                                                                             |
| **Batch inference jobs**                                                                                                                                                                                                     |
| Maximum number of input files for a batch inference<br>job.                                                                                                                                                                  | 1000                                                                                            |
| Maximum size of batch inference job input.                                                                                                                                                                                   | 1 GB                                                                                            |
| Maximum number of records per input file for a batch inference<br>job without themes.                                                                                                                                        | 50 million                                                                                      |
| Maximum number of records per input file for a batch inference<br>job with themes.                                                                                                                                           | 100                                                                                             |
| **Batch segment jobs**                                                                                                                                                                                                       |
| Maximum number of input files for a batch segment<br>job.                                                                                                                                                                    | 1000                                                                                            |
| Maximum size of batch segment job input.                                                                                                                                                                                     | 1 GB                                                                                            |
| Maximum number of queries per input file for Item-Affinity<br>recipe.                                                                                                                                                        | 500                                                                                             |
| Maximum number of queries per input file for<br>Item-Attribute-Affinity recipe.                                                                                                                                              | 10                                                                                              |
| Maximum number of users per segment                                                                                                                                                                                          | 5 million                                                                                       |
| **Data deletion jobs**                                                                                                                                                                                                       |
| Maximum number of data deletion jobs for a dataset group with a status of PENDING.                                                                                                                                           | 5 (adjustable)                                                                                  |
| Maximum total size of your data deletion input file or files                                                                                                                                                                 | 100 MB                                                                                          |

Your AWS account has the following quotas for each region.

| Resource                                                        | Quota           |
| --------------------------------------------------------------- | --------------- |
| Total number of active schemas.                                 | 500             |
| Total number of active dataset groups.                          | 5 (adjustable)  |
| Total number of pending or in progress dataset import<br>jobs.  | 5               |
| Total number of pending or in progress batch inference<br>jobs. | 5 (adjustable)  |
| Total number of pending or in progress batch segment<br>jobs.   | 5               |
| Total number of pending or in progress solution<br>versions.    | 20 (adjustable) |

Each dataset group has the following quotas.

| Resource                                                                         | Quota           |
| -------------------------------------------------------------------------------- | --------------- |
| Total number of active solutions.                                                | 10 (adjustable) |
| Total number of active campaigns.                                                | 5 (adjustable)  |
| Total number of recommenders.                                                    | 5               |
| Total number of filters.                                                         | 30 (adjustable) |
| Total number of distinct dataset fields across all filters.                      | 20              |
| Total number of data deletion jobs for a dataset group with a status of PENDING. | 5               |

## Requesting a quota

increase

For adjustable quotas, you can request a quota increase using the
[Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). The following Amazon Personalize quotas are adjustable:

- Maximum number of item interactions that are considered by a model
  during training.
- Active campaigns per dataset group
- Active dataset groups
- Active filters per dataset group
- Active solutions per dataset group
- Amount of data per incremental import
- Maximum number of item interactions per user per event type considered by a filter
- Total number of pending or in progress batch inference jobs
- Total number of pending or in progress solution versions
- Maximum rate of `PutEvents` or `PutActionInteraction` requests

To request a quota increase, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") and follow the steps
in the [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") section of the _Service
Quotas User Guide_.

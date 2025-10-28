# Frequently asked questions for Amazon Personalize

The following are answers to frequently asked questions related to importing data,
training, model deployment, recommendations, and filters in Amazon Personalize.

For more questions and answers, see the [Amazon Personalize Cheat Sheet](https://github.com/aws-samples/amazon-personalize-samples/blob/master/PersonalizeCheatSheet2.0.md "https://github.com/aws-samples/amazon-personalize-samples/blob/master/PersonalizeCheatSheet2.0.md") in the [Amazon Personalize samples](https://github.com/aws-samples/amazon-personalize-samples "https://github.com/aws-samples/amazon-personalize-samples")
repository.

###### Topics

- [Data import and management](#data-import-questions "#data-import-questions")
- [Creating a custom solution and solution version](#training-questions "#training-questions")
- [Model deployment (custom campaigns)](#deployment-questions "#deployment-questions")
- [Recommendations](#recommendations-questions "#recommendations-questions")
- [Filtering recommendations](#filters-questions "#filters-questions")

## Data import and management

_What format should my bulk data be in?_

Your bulk data must be in comma-separated
values (CSV) format. The first row of your CSV file must contain column headers. The column headers in your CSV file need to map to
the schema to create the dataset. If your data includes any non-ASCII encoded characters, your CSV file
must be encoded in UTF-8 format. Don't enclose headers in quotation marks
("). `TIMESTAMP` and `CREATION_TIMESTAMP` data must be
in _UNIX epoch_ time format. For more information on timestamp data, see
[Timestamp data](interactions-datasets.md#timestamp-data "interactions-datasets.md#timestamp-data").
For more information about schemas, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

For complete data format guidelines, see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md"). If you're not sure how to format your data, you can use
Amazon SageMaker AI Data Wrangler (Data Wrangler) to prepare your data. For more information, see [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](preparing-importing-with-data-wrangler.md "preparing-importing-with-data-wrangler.md").

_How much training data do I need?_

For all use cases (Domain dataset groups) and custom recipes,
your interactions data must have the following:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.

For quality recommendations, we recommend that you have at minimum 50,000 item interactions from at least 1,000 users with two or more item interactions each.

You can start out with an empty Item interactions dataset and, when you
have recorded enough data, create your recommender (Domain dataset group) or custom solution version using only new recorded events.
Some recipes and use cases may have additional data requirements. For information on use case requirements, see [Choosing a use case](domain-use-cases.md "domain-use-cases.md").
For information on recipe requirements, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

_How do I update an item or user's
attributes?_

Use the Amazon Personalize console or the [PutItems](API_UBS_PutItems.md "API_UBS_PutItems.md") or [PutUsers](API_UBS_PutUsers.md "API_UBS_PutUsers.md") operations to import an item or user with the same
item ID but with the modified attributes.

_How do I delete an item or user?_

Amazon Personalize doesn't support deleting a specific item or user. To make sure that an item or
user doesn't appear in recommendations, use a filter to exclude items. For more
information, see [Filtering recommendations and user segments](filter.md "filter.md").

_How do I delete a schema?_

You can delete a schema only with the [DeleteSchema](API_DeleteSchema.md "API_DeleteSchema.md") operation. You can't use the Amazon Personalize console to delete
a schema.

## Creating a custom solution and solution version

_What recipe should I use?_

The Amazon Personalize recipe that you use depends on your use case. For information on matching
use cases to recipes, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md"). The [Amazon Personalize Cheat Sheet](https://github.com/aws-samples/amazon-personalize-samples/blob/master/PersonalizeCheatSheet2.0.md "https://github.com/aws-samples/amazon-personalize-samples/blob/master/PersonalizeCheatSheet2.0.md") also includes use case and recipe information.

_How often should I train?_

We recommend using automatic training with at least a weekly training frequency.
Automatic training makes it easier for you to maintain recommendation relevance.
Your training frequency depends on your business
requirements, the recipe that you use, and how frequently you import data. For more information, see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md"). For information about
maintaining relevance, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").

_Should I use AutoML?_

No, instead we recommend that you match your use case to different Amazon Personalize recipes and
choose a recipe. For information on matching use cases to recipes, see [Choosing a
recipe](working-with-predefined-recipes.md "working-with-predefined-recipes.md").

## Model deployment (custom campaigns)

_What should I set for my campaign's minProvisionedTPS?_

A high `minProvisionedTPS` will increase your cost. We recommend starting with 1 for
`minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the
`minProvisionedTPS` as necessary.

_How do I monitor the cost of my campaigns?_

The Amazon Personalize Monitor project provides a CloudWatch dashboard, custom metrics, utilization alarms, and cost optimization
functions for Amazon Personalize campaigns. See the [Amazon Personalize
Monitor](https://github.com/aws-samples/amazon-personalize-monitor "https://github.com/aws-samples/amazon-personalize-monitor") in the [Amazon Personalize samples](https://github.com/aws-samples/amazon-personalize-samples "https://github.com/aws-samples/amazon-personalize-samples")
repository.

_How do I set a maximum transaction throughput for a campaign?_

You can only set the _minimum_ throughput for a campaign. When you create an Amazon Personalize campaign, you
specify a dedicated transaction capacity for creating real-time recommendations for your application users. If your TPS
increases beyond `minProvisionedTPS`, Amazon Personalize auto-scales the provisioned capacity up and down, but never
below the `minProvisionedTPS`. For more information, see [Minimum provisioned transactions per second and auto-scaling](campaigns.md#min-tps-auto-scaling "campaigns.md#min-tps-auto-scaling").

## Recommendations

_How can I tell if my Amazon Personalize model is generating quality
recommendations?_

Evaluate the performance of your solution version with offline and online metrics
(see [Evaluating an Amazon Personalize solution version with metrics](working-with-training-metrics.md "working-with-training-metrics.md")) and online testing (such as A/B
testing). For more information about A/B testing, see
[Measuring recommendation impact with A/B testing](ab-testing-recommendations.md "ab-testing-recommendations.md").

_How do I delete my batch inference job and why is its status
"active"?_

You can't delete batch inference jobs. When a batch inference job's status is
_active_, the job is complete. You can access your recommendations in
the output Amazon S3 bucket or folder. You won't incur additional cost from the batch inference
job once the job is complete. However you may incur additional charges from other services
such as Amazon S3 for input and output data storage.

_Why does my SIMS-backed campaign recommend items that are not
similar based on metadata?_

SIMS uses your Item interactions dataset to determine similarity; not item metadata such as
color or price. SIMS identifies the co-occurrence of the item in user histories in your
Interaction dataset to recommend similar items. For more information, see [SIMS recipe](native-recipe-sims.md "native-recipe-sims.md").

_Can I get more than 500 items from a single
GetRecommendations API operation?_

500 is the maximum number of items that you can retrieve in a single [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md"). This
value cannot be increased.

## Filtering recommendations

_Why aren't my recommendations filtered as
expected?_

This can occur for a variety of reasons:

- There may be issue with the format or syntax of your filter expression. For
  examples of correctly formatted filter expressions, see [Filter expression examples](filter-expression-examples.md "filter-expression-examples.md").
- Amazon Personalize considers up to 100
  of the most recent interactions per user per event type.
  This is an adjustable quota.
  You can request a quota increase using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). If you don't import item interactions for a user for three months, your filters no longer
  consider the user's historical data. To consider this data, you must import the user's entire event history again.

For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

_How can I remove already purchased items from
recommendations?_

For ECOMMERCE Domain dataset groups, if you create a recommender with the [Recommended for
you](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case") or
[Customers who viewed X
also viewed](ECOMMERCE-use-cases.md#customers-also-viewed-use-case "ECOMMERCE-use-cases.md#customers-also-viewed-use-case") use case,
Amazon Personalize automatically filters items the user
purchased based on the userId that you specify and `Purchase`
events.

For other Domain dataset group use cases or custom resources, use a filter to remove purchased items. Add a `Purchased` event type attribute to your data, record
_Purchase_ events with the `PutItems` operation, and create a
filter that removes purchased items from recommendations. For example:

```
EXCLUDE ItemID WHERE Interactions.EVENT_TYPE IN ("purchased")
```

For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

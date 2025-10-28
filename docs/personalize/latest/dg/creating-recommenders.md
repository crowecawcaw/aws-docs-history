# Domain recommenders in Amazon Personalize

If you created a Domain dataset group, after you [import data](import-data.md "import-data.md") you are ready
to create recommenders for your domain use cases. A _recommender_ is a
Domain dataset group resource that generates recommendations. You use a recommender in your
application to get real-time recommendations with the [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") operation.

When you create a recommender, you specify a use case and Amazon Personalize trains the models backing
the recommender with the best configurations for the use case. Each use case has different API
requirements for getting recommendations. For a list of recommender use cases by domain, see
[Choosing a use case](domain-use-cases.md "domain-use-cases.md"). You can create at most
15 recommenders per region.

Amazon Personalize automatically retrains the models backing your recommenders every 7 days. This is a full retraining that creates entirely new models based on
the entirety of the data in your datasets. With _Top picks for you_ and _Recommended for you_ use cases, Amazon Personalize updates the existing models every two hours
to include new items in recommendations with exploration.

When you create a recommender, you can do the following:

- Enable item metadata in recommendations.
  For more information, see [Enabling metadata in recommendations](create-recommender-return-metadata.md "create-recommender-return-metadata.md").
- Configure the columns used when training the models backing your recommender. For more information, see [Configuring columns used when creating an Amazon Personalize domain
  recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md").
- For _Top picks for your_ or _Recommended for you_ use cases, you can configure exploration. For
  more information, see [Configuring exploration for a domain recommender](create-recommender-configure-exploration.md "create-recommender-configure-exploration.md").
  After you create a recommender, you can do the following:

- Evaluate the recommender – You can evaluate the performance of your recommender through offline and online metrics.
  For more information, see [Evaluating an Amazon Personalize domain recommender](evaluating-recommenders.md "evaluating-recommenders.md").
- Stop and restart the recommender – If you want to pause billing for an active recommender, you can stop the
  recommender and restart it later. For more information, see [Stopping a recommender](stopping-starting-recommender.md "stopping-starting-recommender.md").
- Update the recommender's configuration – You can update the columns the recommender uses in training and update
  the recommender's request capacity. For more information, see [Updating a recommender](updating-recommender.md "updating-recommender.md").
- Delete the recommender – You can delete recommenders with the [DeleteRecommender](API_DeleteRecommender.md "API_DeleteRecommender.md") operation. Or you can delete a recommender from the recommender details page in
  the Amazon Personalize console.

###### Topics

- [Recommender statuses](#recommender-statuses "#recommender-statuses")
- [Minimum recommendation requests per second and
  auto-scaling](#min-rrps-auto-scaling "#min-rrps-auto-scaling")
- [Creating domain recommenders in Amazon Personalize](creating-domain-recommenders.md "creating-domain-recommenders.md")
- [Enabling metadata in recommendations for a domain recommender in Amazon Personalize](create-recommender-return-metadata.md "create-recommender-return-metadata.md")
- [Configuring columns used when creating an Amazon Personalize domain
  recommender](create-recommender-configure-columns.md "create-recommender-configure-columns.md")
- [Configuring exploration for a domain recommender](create-recommender-configure-exploration.md "create-recommender-configure-exploration.md")
- [Evaluating an Amazon Personalize domain recommender](evaluating-recommenders.md "evaluating-recommenders.md")
- [Updating a recommender](updating-recommender.md "updating-recommender.md")
- [Stopping a recommender](stopping-starting-recommender.md "stopping-starting-recommender.md")

## Recommender statuses

A recommender can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

To get the recommender status, navigate to the Recommenders page in the Amazon Personalize console or use the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") operation.

## Minimum recommendation requests per second and

auto-scaling

###### Important

A high `minRecommendationRequestsPerSecond` will increase your bill. We
recommend starting with 1 for `minRecommendationRequestsPerSecond` (the default).
Track your usage using Amazon CloudWatch metrics, and increase the
`minRecommendationRequestsPerSecond` as necessary.

When you create a recommender, you can configure the recommender's minimum recommendation
requests per second. The minimum recommendation requests per second
(`minRecommendationRequestsPerSecond`) specifies the baseline recommendation
request throughput provisioned by Amazon Personalize. The default minRecommendationRequestsPerSecond is
`1`. A recommendation request is a single `GetRecommendations`
operation. Request throughput is measured in requests per second and Amazon Personalize uses your requests
per second to derive your requests per hour and the price of your recommender usage.

If your requests per second increases beyond
`minRecommendationRequestsPerSecond`, Amazon Personalize auto-scales the provisioned capacity
up and down, but never below `minRecommendationRequestsPerSecond`. There's a short
time delay while the capacity is increased that might cause loss of requests.

Your bill is the greater of either the minimum requests per hour (based on
minRecommendationRequestsPerSecond) or the actual number of requests. The actual request
throughput used is calculated as the average requests/second within a one-hour window. We
recommend starting with the default `minRecommendationRequestsPerSecond`, track
your usage using Amazon CloudWatch metrics, and then increase the
`minRecommendationRequestsPerSecond` as necessary.

# Measuring recommendation impact with a metric attribution

To measure the impact of item recommendations, you can create a metric attribution. A _metric attribution_
creates reports based on the item interactions and items data that you import, and the metrics that you specify. For example, the
total length of movies watched by users, or the total number of click events. Amazon Personalize aggregates calculations over a 15-minute window. For
streamed interaction data and incremental bulk data, Amazon Personalize automatically sends metric reports to Amazon CloudWatch. For bulk data, you can choose
to publish reports to an Amazon S3 bucket.

For each interaction that you import, include source data to compare different campaigns, recommenders, and third parties. You can include the recommendation ID of the recommendations you showed the user
or the event source, such as a third party.

For example, you might have a video streaming app that shows movie recommendations from two different Amazon Personalize recommenders.
If you wanted to see which recommender generates the most watch events,
you could create a metric attribution that tracks the total number of watch events. Then you could record watch events as
users interact with recommendations, and include
the `recommendationId` in each event. Amazon Personalize uses the `recommendationId` to identify each recommender.
As you record events, you can view the watch event totals aggregated over every 15 minutes for both recommenders in CloudWatch. For code samples that show
how to include a `recommendationId` or an `eventAttributionSource` for an event, see [Event metrics and attribution reports](event-metrics.md "event-metrics.md").

###### Topics

- [Guidelines and requirements for a metric attribution](metric-attribution-requirements.md "metric-attribution-requirements.md")
- [Creating an Amazon Personalize metric attribution](creating-metric-attribution.md "creating-metric-attribution.md")
- [Updating an Amazon Personalize metric attribution](updating-metric-attribution.md "updating-metric-attribution.md")
- [Deleting an Amazon Personalize metric attribution](deleting-metric-attribution.md "deleting-metric-attribution.md")
- [Viewing graphs of metric data in CloudWatch](metric-attribution-results-cloudwatch.md "metric-attribution-results-cloudwatch.md")
- [Publishing metric attribution reports to Amazon S3](metric-attribution-results-s3.md "metric-attribution-results-s3.md")

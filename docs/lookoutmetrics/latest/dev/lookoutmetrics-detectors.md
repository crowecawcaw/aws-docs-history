Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Working with detectors

In Amazon Lookout for Metrics, a _detector_ is a resource that monitors a dataset and identifies
_anomalies_ (data that falls outside of the expected range). Detectors use
machine learning (ML) to find patterns in business data, and to distinguish between expected variations in data and
legitimate anomalies. A detector can monitor a dataset that contains metrics data that you manage in Amazon Simple Storage Service
(Amazon S3), live data from another service such as Amazon CloudWatch, or events from a database. When new data points fall
outside of the expected range, the detector records the anomaly and sends an alert.

A [dataset](detectors-dataset.md "detectors-dataset.md") is a collection of timestamped data points that can each have
multiple metrics and attributes. You choose one of the metrics to be the _measure_, which is the primary metric
that the detector monitors for anomalies.

You can also configure up to 10 additional attributes as _dimensions_. Dimensions are additional information that the detector uses to segment anomalies, filter the dataset, and identify contributing factors.

For example, you can choose a field named `availability` for a measure. If you don't choose a
dimension, the detector monitors availability across all records. If you choose a field named `country`
for a dimension, then the detector monitors availability in each country as a separate metric:
_availability in Canada_, _availability in Italy_, and so on.

Alternately, you can create a filter on `country` that includes only the countries that you are interested in monitoring. In this case, `availability` is monitored only in the countries that are included in the filter.

Detectors primarily work against live data. A detector analyzes new data periodically to find anomalies in
measure values. The _interval_ at which it analyzes data can be between 5 minutes and 1 day. To
allow time for the datasource to collect all data before analysis starts, you also configure a
_delay_ on the dataset. At the end of an interval, the detector waits for the duration of the
delay before analyzing data.

When you create a detector, you can also provide _historical data_. If you provide historical
data, the detector uses it to learn patterns and relationships between fields in your data. If not, the detector
spends several intervals learning on live data.

Every time it runs, the detector analyzes all of the data generated during the interval, identifies anomalous
data points, and assigns a severity score to each. If the severity of an anomaly exceeds a
_threshold_, the detector sends an _alert_. You can [configure alerts](detectors-alerts.md "detectors-alerts.md") to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic, or to
invoke an AWS Lambda function. If you get too many or too few results, you can change the threshold that triggers the
alert.

###### Topics

- [Setting up a detector](detectors-setup.md "detectors-setup.md")
- [Managing detectors](detectors-manage.md "detectors-manage.md")
- [Managing a dataset in Amazon S3](detectors-dataset.md "detectors-dataset.md")
- [Working with anomalies](detectors-anomalies.md "detectors-anomalies.md")
- [Working with alerts](detectors-alerts.md "detectors-alerts.md")
- [Tagging Lookout for Metrics resources](detectors-tags.md "detectors-tags.md")
- [Working with filters](detectors-filters.md "detectors-filters.md")

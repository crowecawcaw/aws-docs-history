Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Monitoring Lookout for Metrics with Amazon CloudWatch

When an anomaly detector processes data or sends an alert, Amazon Lookout for Metrics sends metrics to Amazon CloudWatch. You can build
graphs and dashboards with these metrics in the CloudWatch console to monitor detector activity, and set alarms that
notify you when there are errors in alert delivery or anomaly detection. To filter and sort metrics, use the
`AlertArn` and `AnomalyDetectorArn` Amazon CloudWatch dimensions.

###### To view metrics in the CloudWatch console

1. Open the [Amazon CloudWatch
   console Metrics page](<https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();namespace=~'AWS*2fLookoutMetrics> "https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();namespace=~'AWS*2fLookoutMetrics") (`AWS/LookoutMetrics` namespace).
2. Choose a dimension schema.
   - **AlertArn** – To view metrics for an alert channel.
   - **AnomalyDetectorArn** – To view processing metrics for a
     detector.

3. Choose metrics to add them to the graph.
4. To choose a different statistic and customize the graph, use the options on the **Graphed
   metrics** tab. By default, graphs use the `Average` statistic for all metrics.

###### Pricing

CloudWatch has an Always Free tier. Beyond the free tier threshold, CloudWatch charges for metrics, dashboards, alarms,
logs, and insights. For details, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For more information about CloudWatch, see the [_Amazon CloudWatch User Guide_](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md").

###### Sections

- [Using processing metrics](#monitoring-cloudwatch-processing "#monitoring-cloudwatch-processing")
- [Using alert metrics](#monitoring-cloudwatch-alerts "#monitoring-cloudwatch-alerts")
- [Configuring alarms](#monitoring-cloudwatch-alarms "#monitoring-cloudwatch-alarms")

## Using processing metrics

When a detector processes data at the end of each interval, it sends metrics to Amazon CloudWatch. You can use these
metrics to monitor detector activity and trigger an alarm if a detector fails to process data.

There are three processing metrics:

- `ExecutionsStarted` – The number of times the detector looked for anomalies. For an
  active detector, this metric is sent once per interval.
- `ExecutionsSucceeded` – The number of processing attempts that succeeded.
- `ExecutionsFailed` – The number of processing attempts that failed.

View the processing metrics with the `Sum` statistic.

## Using alert metrics

When a detector finds an anomaly, it sends [anomaly alerts](detectors-alerts.md "detectors-alerts.md") to alert
channels that you configure. Each time it sends an anomaly alert, the detector sends a metric to indicate whether
the alarm was sent successfully.

There are two alert metrics:

- `Delivered` – An anomaly alert was sent successfully.
- `Undelivered` – An anomaly alert could not be delivered.

View the alert metrics with the `Sum` statistic.

## Configuring alarms

To get notifications when a metric exceeds a threshold, create an alarm. For example, you can create an alarm
that sends a notification when the sum of the `ExecutionsFailed` metric exceeds 1 for an hour.

###### To create an alarm

1. Open the [Amazon CloudWatch console Alarms
   page](https://console.aws.amazon.com/cloudwatch/home#alarmsV2: "https://console.aws.amazon.com/cloudwatch/home#alarmsV2:").
2. Choose **Create alarm**.
3. Choose **Select metric** and locate a metric for your detector, such as
   `ExecutionsFailed` for `my-detector`.
4. Follow the instructions to configure a condition, action, and name for the alarm.

For detailed instructions, see [Create a CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
_Amazon CloudWatch User Guide_.

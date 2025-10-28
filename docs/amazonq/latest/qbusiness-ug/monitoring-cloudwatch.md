# Monitoring Amazon Q Business and Amazon Q Apps

with Amazon CloudWatch

You can monitor Amazon Q Business and Amazon Q Apps with Amazon CloudWatch, which collects raw data and
processes it into readable, near real-time metrics. These statistics are kept for 15 months,
so that you can access historical information and gain a better perspective on how your web
application or service is performing. You can also set alarms that watch for certain
thresholds, and send notifications or take actions when those thresholds are met. For more
information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Topics

- [Using CloudWatch Metrics](#using-metrics "#using-metrics")
- [Viewing metrics](#how-to-access "#how-to-access")
- [Creating a CloudWatch alarm](alarms.md "alarms.md")
- [Amazon Q Business chat metrics](qbusiness-metrics-chat.md "qbusiness-metrics-chat.md")
- [Amazon Q Business API operation metrics](qbusiness-metrics-api.md "qbusiness-metrics-api.md")
- [Amazon Q Business index metrics](qbusiness-metrics-index.md "qbusiness-metrics-index.md")
- [Amazon Q Apps metrics](qapps-metrics.md "qapps-metrics.md")

## Using CloudWatch Metrics

To use metrics, you must specify the following information:

- The metric namespace. A _namespace_ is a CloudWatch container Amazon Q uses to publish its metrics into. If you are using the CloudWatch [ListMetrics](../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md "../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md") API or the [list-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metrics.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metrics.html") command to view the metrics for Amazon Q Business or
  Amazon Q Apps, specify `AWS/QBusiness` or `AWS/QApps` for the
  namespace.
- The metric dimension. A _dimension_ is a name-value pair that
  helps you to uniquely identify a metric. Common dimension names include:
  - `ApplicationId` - Identifies the specific Amazon Q Business application
  - `IndexId` - Identifies the specific index (for index-related metrics)
  - `DataSourceId` - Identifies the specific data source (for data source metrics)
  - `PluginId` - Identifies the specific plugin (for plugin-related metrics)
  - `API name` - Identifies the specific API operation (for performance metrics like Chat)
  - `MethodType` - Identifies the specific method being called (for API operation metrics)
  - `UsefulnessReason` - Identifies feedback categories (for feedback metrics)

- The metric name. For example, `DocumentsIndexed`.

You can get monitoring data for Amazon Q Business or Q Apps with the AWS Management Console, the AWS CLI, or the
CloudWatch API. You can also use the CloudWatch API through one of the AWS SDKs or the CloudWatch API tools.
The console displays a series of graphs based on the raw data from the CloudWatch API. Depending
on your needs, you might prefer to use either the graphs displayed in the console or
retrieved from the API.

###

The following table shows some common uses for the metrics. These are suggestions to
get you started, not a comprehensive list.

| How do I?                                                    | Relevant metrics                                                                        |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How do I track how many documents were indexed successfully? | Use the `DocumentsIndexed` metrics.                                                     |
| How do I monitor end user experience for Amazon Q Business?  | Use the `ThumbsUpCount` and `ThumbsDownCount` metrics.                                  |
| How do I track how many users used Q Apps                    | Use the `ActiveUsers` metric.                                                           |
| How do I track API operation success rates?                  | Use the `success` and `failure` metrics with appropriate `MethodType` dimensions.       |
| How do I monitor individual API operation performance?       | Use the `latency` metric with specific `MethodType` dimensions.                         |
| How do I monitor chat response performance and latency?      | Use the `TimeToFirstToken` and `Latency` metrics with API name dimension set to "Chat". | You must have the appropriate CloudWatch permissions to monitor Amazon Q Business with CloudWatch. For more information, see [Identity and access management for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _Amazon CloudWatch User Guide_. ## Viewing metrics The following steps show how to access Amazon Q Business or Amazon Q Apps metrics using the CloudWatch console. ###### To view metrics (console) 1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch"). 2. Choose **Metrics**, choose the **All Metrics** tab, and then choose **AWS/QBusiness** or **AWS/QApps**. ###### Note Some Q Apps metrics might be emitted using a different namespace. 3. Choose the metric dimension. 4. Choose the metric that you want from the list, and choose a time period for the graph. ###### Note You can use the `Sum` statistic to aggregate all metrics with the unit `Count`. For more information on CloudWatch statistics and how to use them, see [CloudWatch statistics definitions](../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md "../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md") in the _Amazon CloudWatch User Guide_. |

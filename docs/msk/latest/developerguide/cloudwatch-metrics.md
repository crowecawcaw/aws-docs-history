# View Amazon MSK metrics using CloudWatch

You can monitor metrics for Amazon MSK using the CloudWatch console, the command line, or
the CloudWatch API. The following procedures show you how to access metrics using these
different methods.

###### To access metrics using the CloudWatch console

Sign in to the AWS Management Console and open the CloudWatch console at
[https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

1. In the navigation pane, choose **Metrics**.
2. Choose the **All metrics** tab, and then choose
   **AWS/Kafka**.
3. To view topic-level metrics, choose **Topic, Broker ID, Cluster
   Name**; for broker-level metrics, choose **Broker ID,
   Cluster Name**; and for cluster-level metrics, choose
   **Cluster Name**.
4. (Optional) In the graph pane, select a statistic and a time period, and then
   create a CloudWatch alarm using these settings.

###### To access metrics using the AWS CLI

Use the [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") and [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") commands.

###### To access metrics using the CloudWatch CLI

Use the [mon-list-metrics](../../../AmazonCloudWatch/latest/cli/cli-mon-list-metrics.md "../../../AmazonCloudWatch/latest/cli/cli-mon-list-metrics.md") and [mon-get-stats](../../../AmazonCloudWatch/latest/cli/cli-mon-get-stats.md "../../../AmazonCloudWatch/latest/cli/cli-mon-get-stats.md") commands.

###### To access metrics using the CloudWatch API

Use the [ListMetrics](../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md "../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md") and
[GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") operations.

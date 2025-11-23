# View Direct Connect CloudWatch metrics

Direct Connect sends the following metrics about your Direct Connect connections. Amazon CloudWatch
then aggregates these data points to 1-minute or 5-minute intervals. By default,
Direct Connect metric data is written to CloudWatch at 5-minute intervals.

###### Note

When monitoring Direct Connect through CloudWatch, you can request metrics at 1-minute intervals.
However, the actual update frequency is controlled by CloudWatch. Because CloudWatch controls the
interval, Direct Connect can't always guarantee intervals shorter than five minutes.

You can use the following procedures to view the metrics for Direct Connect
connections.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace. For more information about using
Amazon CloudWatch to view Direct Connect metrics, including adding math
functions or prebuilt queries, see [Using
Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working-with-metrics.md "../../../AmazonCloudWatch/latest/monitoring/working-with-metrics.md") in the
_Amazon CloudWatch User Guide_.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
   choose **All metrics**.
3. In the **Metrics** section, choose
   **DX**.
4. Choose a **ConnectionId** or **Metric
   name**, and then choose any of the following to further define
   the metric:
   - **Add to search** — Adds this metric to your
     search results.
   - **Search for this only** — Searches only for this
     metric.
   - **Remove from graph** — Removes this metric from
     the graph.
   - **Graph this metric only** — Graphs only this
     metric.
   - **Graph all search results** — Graphs all
     metrics.
   - **Graph with SQL query** — Opens
     **Metric Insights -query builder**, allowing
     you to choose what you want to graph by creating an SQL query. For
     more information on using Metric Insights, see [Query your metrics
     with CloudWatch Metrics Insights](../../../AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.md "../../../AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.md") in the
     _Amazon CloudWatch User Guide_.

###### To view metrics using the Direct Connect console

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Connections**.
3. Select your connection.
4. Choose the **Monitoring** tab to display the metrics for
   your connection.

###### To view metrics using the AWS CLI

At a command prompt, use the following command.

```
`aws cloudwatch list-metrics --namespace "AWS/DX"`
```

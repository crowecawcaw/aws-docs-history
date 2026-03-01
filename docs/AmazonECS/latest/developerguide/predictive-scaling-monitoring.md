# Monitor predictive scaling metrics for Amazon ECS with CloudWatch

You can use Amazon CloudWatch to monitor your data for predictive scaling. A predictive scaling policy collects
data that is used to forecast your future load. The data collected is automatically stored in CloudWatch at
regular intervals and can be used to visualize how well the policy performs over time. You can also create
CloudWatch alarms to notify you when performance indicators change beyond the limits that you defined.

## Visualize historical forecast data

Load forecast data for a predictive scaling policy can be viewed in CloudWatch and can be useful when
visualizing forecasts against other CloudWatch metrics in a single graph. You can also see trends over time
by viewing a broader time range. You can access up to 15 months of historical metrics to get a better
perspective on how your policy is performing.

###### To view historical forecast data using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics** and then **All
   metrics**.
3. Choose the **Application Auto Scaling** metric namespace.
4. Choose **Predictive Scaling Load Forecasts**.
5. In the search field, enter the name of the predictive scaling policy or the name of the Amazon ECS
   service group, and then press Enter to filter the results.
6. To graph a metric, select the check box next to the metric. To change the name of the graph,
   choose the pencil icon. To change the time range, select one of the predefined values or choose
   **custom**. For more information, see [Graphing a metric](../../../AmazonCloudWatch/latest/monitoring/graph_a_metric.md "../../../AmazonCloudWatch/latest/monitoring/graph_a_metric.md") in
   the _Amazon CloudWatch User Guide_.
7. To change the statistic, choose the **Graphed metrics** tab. Choose the
   column heading or an individual value, and then choose a different statistic. Although you can
   choose any statistic for each metric, not all statistics are useful for
   **PredictiveScalingLoadForecast** metrics. For example, the
   **Average**, **Minimum**, and
   **Maximum** statistics are useful, but the **Sum**
   statistic is not.
8. To add another metric to the graph, under **Browse**, choose
   **All**, find the specific metric, and then select the check box next to
   it. You can add up to 10 metrics.
9. (Optional) To add the graph to a CloudWatch dashboard, choose **Actions**,
   **Add to dashboard**.

## Create accuracy metrics using metric math

With metric math, you can query multiple CloudWatch metrics and use math expressions to create new time
series based on these metrics. You can visualize the resulting time series on the CloudWatch console and add
them to dashboards. For more information about metric math, see [Using metric math](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md") in the
_Amazon CloudWatch User Guide_.

Using metric math, you can graph the data that service auto scaling generates for predictive scaling
in different ways. This helps you monitor policy performance over time, and helps you understand
whether your combination of metrics can be improved.

For example, you can use a metric math expression to monitor the [mean absolute percentage
error](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error "https://en.wikipedia.org/wiki/Mean_absolute_percentage_error") (MAPE). The MAPE metric helps monitor the difference between the forecasted values
and the actual values observed during a given forecast window. Changes in the value of MAPE can
indicate whether the policy's performance is degrading over time as the nature of your application
changes. An increase in MAPE signals a wider gap between the forecasted values and the actual values.

**Example: Metric math expression**

To get started with this type of graph, you can create a metric math expression like the one shown in
the following example.

Instead of a single metric, there is an array of metric data query structures for
`MetricDataQueries`. Each item in `MetricDataQueries` gets a metric or
performs a math expression. The first item, `e1`, is the math expression. The designated
expression sets the `ReturnData` parameter to `true`, which ultimately produces a
single time series. For all other metrics, the `ReturnData` value is `false`.

In the example, the designated expression uses the actual and forecasted values as input and returns
the new metric (MAPE). `m1` is the CloudWatch metric that contains the actual load values
(assuming CPU utilization is the load metric that was originally specified for the policy named
`my-predictive-scaling-policy`). `m2` is the CloudWatch metric that contains the
forecasted load values. The math syntax for the MAPE metric is as follows:

_Average of (abs ((Actual - Forecast)/(Actual)))_

### Visualize your accuracy metrics and set alarms

To visualize the accuracy metric data, select the **Metrics** tab in the CloudWatch
console. You can graph the data from there. For more information, see [Adding a math expression to a CloudWatch graph](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#adding-metrics-expression-console "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#adding-metrics-expression-console") in the
_Amazon CloudWatch User Guide_.

You can also set an alarm on a metric that you're monitoring from the
**Metrics** section. While on the **Graphed metrics** tab,
select the **Create alarm** icon under the **Actions** column.
The **Create alarm** icon is represented as a small bell. For more information and
notification options, see [Creating a
CloudWatch alarm based on a metric math expression](../../../AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.md "../../../AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.md") and [Notifying users on
alarm changes](../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md "../../../AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.md") in the _Amazon CloudWatch User Guide_.

Alternatively, you can use [GetMetricData](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricData.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricData.md") and
[PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md") to perform calculations using metric math and create alarms based on
the output.

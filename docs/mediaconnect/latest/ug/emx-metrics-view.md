# Viewing metrics for a MediaConnect flow

You can view some metrics in the MediaConnect console. You can view all metrics in the
CloudWatch console. You can also retrieve metrics using the CLI, the REST API, or any
AWS SDK.

On the CloudWatch console, the minimum refresh rate for metrics is 30 seconds.

###### To view metrics on the MediaConnect console

You can view some metrics in the MediaConnect console. You can view the current
metrics, going back from 1 hour to 1 week. (To view other metrics or to view
historical metrics, you must use the CloudWatch console.)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Flows**. On the
   **Flows** page, choose the flow you want. The
   **Details** page appears.
3. Choose the **Health** tab. The metrics that MediaConnect
   supports on this tab appears.
4. Choose the period and time range. For example, **Past 1 day (5 min
   period)**.

###### To view metrics using the CloudWatch console

On the CloudWatch console you can view all MediaConnect metrics for any range of time — the
current metrics or historical metrics. There is a charge to view metrics on the
CloudWatch console.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, then choose
   **All metrics**. In the bottom half of the page, the
   **Browse** tab shows cards with names.

No cards appear if you are completely new to AWS, and you haven't
performed an action that creates metrics in any service. 3. Select the card that is named **AWS/MediaConnect**.

This card appears only if you have started at least one flow in the last
15 months in the AWS Region that is currently selected for CloudWatch. This card
won't appear if have never started a MediaConnect flow. In this case, come back to
this procedure after you have created and started a flow.

(A card named **MediaConnect** might appear in the custom
namespace section of the page. This card is for the old namespace for MediaConnect
metrics. The two namespaces became duplicates of each other in September of
2022, so there is no advantage to choosing this card. Always choose
**AWS/MediaConnect**.) 4. The **Browse** tab in the bottom half of the page now
shows dimensions. Choose a metric dimension. For example, choose
**Flow ARN**.

The **Browse** tab now shows a table with one column that
shows the chosen dimension (for example, Flow ARN) and one column that shows
all the metrics. You can sort the table. 5. Select one or more rows. As soon as you select a row, it appears in the
graph in the top half of the page. 6. In the bottom half of the page, choose the **Graphed
metrics** tab. 7. On the choices on the right of the tab, specify the
**Statistic** and the **Period**.

When you choose the period, the graph refreshes to show the [maximum time range for that
period](monitor-with-cloudwatch-metric-info.md#emx-metrics-about-time-range "monitor-with-cloudwatch-metric-info.md#emx-metrics-about-time-range"). If the graph is now empty on the left, you can adjust the
timeline in the choices at the top right of the graph. Choose a lower number
so that the full space is filled up. For example, change
**1w** to **1d**.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command:

```
aws cloudwatch list-metrics --namespace "AWS/MediaConnect"
```

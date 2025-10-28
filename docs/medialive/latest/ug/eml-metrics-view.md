# Viewing metrics

You can view some metrics in the MediaLive console. You can view all
metrics in the CloudWatch console. You can also retrieve metrics using the
CLI, the REST API, or any AWS SDK.

On the CloudWatch console, the minimum refresh rate for metrics is 30
seconds.

###### To view metrics on the MediaLive console

You can view some metrics in the MediaLive console. You can view
those metrics for a range from the last hour up to the last
week. (To view other metrics or to view historical metrics, you
must use the CloudWatch console.)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose
   **Channels**. In the
   **Channels** page, choose the channel
   you want. The **Channel details** page
   appears.
3. Choose the **Health** tab. The metrics
   that MediaLive supports on this tab appears.
4. Choose the period and time range. For example,
   **Past 1 day (5 min period)**.

###### To view metrics using the CloudWatch console

On the CloudWatch console you can view all MediaLive metrics for any
range of time — the current metrics or historical metrics. There
is a charge to view metrics on the CloudWatch console.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose
   **Metrics**, then choose **All
   metrics**. In the bottom half of the page, the
   **Browse** tab shows cards with names.

No cards appear if you are completely new to AWS, and
you haven't performed an action that creates metrics in any
service. 3. Select the card that is named
**AWS/MediaLive**.

This card appears only if you have started at least one
channel in the last 15 months in the AWS Region that is
currently selected for CloudWatch. This card won't appear if have
never started a MediaLive channel. In this case, come back to
this procedure after you have created and started a
channel.

(A card named **MediaLive** might appear
in the custom namespace section of the page. This card is
for the old namespace for MediaLive metrics. The two namespaces
became duplicates of each other in September of 2022, so
there is no advantage to choosing this card. Always choose
**AWS/MediaLive**.) 4. The **Browse** tab in the bottom half of
the page now shows dimensions. Choose a metric dimension.
For example, choose **Channel ID**.

The **Browse** tab now shows a table with
one column that shows the chosen dimension (for example,
channel IDs) and one column that shows all the metrics. You
can sort the table. 5. Select one or more rows. As soon as you select a row, it
appears in the graph in the top half of the page. 6. In the bottom half of the page, choose the
**Graphed metrics** tab. 7. On the choices on the right of the tab, specify the
**Statistic** and the
**Period**.

When you choose the period, the graph refreshes to show
the [maximum
time range for that period](eml-metrics-gen-info.md#eml-metrics-about-time-range "eml-metrics-gen-info.md#eml-metrics-about-time-range"). If the graph is now
empty on the left, you can adjust the timeline in the
choices at the top right of the graph. Choose a lower number
so that the full space is filled up. For example, change
**1w** to
**1d**.

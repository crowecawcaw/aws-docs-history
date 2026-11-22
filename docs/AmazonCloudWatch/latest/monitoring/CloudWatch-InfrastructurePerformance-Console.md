

# Monitor using the console

View the network performance between two Regions, between two Availability Zones, or within an Availability Zone. After you choose a starting and ending date, and a period by which to aggregate performance, the network performance metrics display in the **Health status timeline** and **Network latency timeline** for that time period. You can also subscribe to or unsubscribe from Amazon CloudWatch metrics. When you subscribe, you can view performance metrics in CloudWatch.

**Note**  
Enabling subscriptions with CloudWatch might incur a charge. For more information about CloudWatch pricing guidelines, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**To choose a Region or Availability Zone**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**.

1. On the **Infrastructure Performance** tab, for **Select connection type**, choose **Inter-Region**, **Inter-Availability Zone**, or **Intra-Availability Zone**.

   By default, the table lists all source and destination pairs. You can sort by **Source**, **Destination**, or **Subscription**.

1. Scroll through the pages and choose one or more pairs.

1. (Optional) To choose specific Regions or Availability Zones, choose **Find metrics**. For example, filter for Source=us-east-1 and Destination=eu-central-1.

   1. In the **Find metrics** field, choose one of the following properties: **Source**, **Destination**, or **Subscription**.

   1. For the property operator, choose `=` or `!=`.

   1. From the **Source Values** list, choose the value.

   1. To add more filters, repeat these steps.

   1. By default, filters are joined with "and". To use "or", choose it from the list.

1. Choose a time range, and then choose **Apply**. The following options are available:
   + **Relative**: Last 30 minutes, Last 1 hour, Last 6 hour, Last 1 day, Last 1 week, or a custom range. For a custom range, enter a duration and choose a unit (seconds, minutes, hours, days, weeks, or years).
   + **Absolute**: A specific start and end date and time. The range can't exceed 30 days.

1. Choose an aggregation period: 5M (default), 15M, 1H, 1D, or 1W.

## Health status timeline
<a name="CloudWatch-InfrastructurePerformance-Console-Health"></a>

The **Health status timeline** shows a consolidated view of network performance. The following statuses are available:
+ **Healthy**: Network performance is within the expected range.
+ **Degraded**: Network performance is below the expected range.

Hover over the timeline for details.

## Network latency timeline
<a name="CloudWatch-InfrastructurePerformance-Console-Latency"></a>

The **Network latency timeline** shows actual network performance speed. Latency ranges from 0 ms to 160 ms. Each pair is represented as an individual line. Hover over the timeline for a comprehensive list and actual latency.
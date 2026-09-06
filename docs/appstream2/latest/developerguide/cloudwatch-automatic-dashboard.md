

# Monitor your WorkSpaces Applications health using the CloudWatch automatic dashboard
<a name="cloudwatch-automatic-dashboard"></a>

You can monitor WorkSpaces Applications using the CloudWatch automatic dashboard, which collects raw data and processes it into readable, near real-time metrics. The metrics are kept for 15 months to access historical information and to monitor the performance of your fleets, instances, and sessions. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

The CloudWatch automatic dashboard is created when you use your AWS account to configure your WorkSpaces Applications. The dashboard allows you to monitor your WorkSpaces Applications metrics across Regions, including:
+ **Capacity metrics** — Monitor overall fleet capacity status, including capacity utilization, actual capacity, available capacity, desired capacity, in-use capacity, pending capacity, and running capacity. Track insufficient capacity errors to identify scaling issues.
+ **Performance metrics** — View fleet, instance, and session performance data including CPU utilization, memory utilization, disk utilization, paging file utilization, and disk I/O operations.
+ **Session quality metrics** — Monitor in-session latency, frames per second (FPS), and bandwidth to assess streaming performance and user experience.

You can use the dashboard for the following purposes:
+ Identify fleets experiencing capacity constraints or insufficient capacity errors.
+ Monitor resource utilization (CPU, memory, disk) over time to optimize instance sizing.
+ Track session quality metrics to identify performance degradation or network issues.
+ Identify anomalies to help with troubleshooting streaming or connectivity problems.
+ View metrics by fleet to compare performance across different configurations.

The automatic dashboard provides time range filters (1 hour, 3 hours, 12 hours, 1 day, 1 week, or custom) and displays metrics in UTC timezone by default.

**To use the WorkSpaces Applications CloudWatch automatic dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Dashboards**.

1. Choose the **Automatic dashboards** tab.

1. Choose **AppStream**.
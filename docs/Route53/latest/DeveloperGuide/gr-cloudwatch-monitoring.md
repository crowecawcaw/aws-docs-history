

# Monitoring Route 53 Global Resolver with Amazon CloudWatch
<a name="gr-cloudwatch-monitoring"></a>

Route 53 Global Resolver DNS publishes query log data directly to Amazon CloudWatch Logs. With CloudWatch Logs, you can search and analyze your log data, create metric filters that define patterns to look for in the data, and set alarms that send notifications based on those metric filters. For more information about Amazon CloudWatch Logs, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

You can process Route 53 Global Resolver DNS query log records as you would with any other log events that CloudWatch Logs collects. For more information about monitoring log data and metric filters, see [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*.

**Topics**
+ [Example: Create a Amazon CloudWatch metric filter and alarm for blocked DNS queries](#gr-cloudwatch-example-metric-filter-alarm)
+ [Example metric filters](gr-cloudwatch-metric-filters.md)
+ [IAM role for publishing CloudWatch metrics from DNS query logs](gr-cloudwatch-metrics-iam-role.md)
+ [Using Amazon CloudWatch Contributor Insights with Route 53 Global Resolver data](gr-cloudwatch-contributor-insights.md)
+ [Analyzing Route 53 Global Resolver logs with Amazon CloudWatch Logs Insights](gr-cloudwatch-logs-insights.md)

## Example: Create a Amazon CloudWatch metric filter and alarm for blocked DNS queries
<a name="gr-cloudwatch-example-metric-filter-alarm"></a>

The following example shows you how to create a metric filter that counts blocked DNS queries in your Route 53 Global Resolver logs. It also shows you how to create an alarm that notifies you when 10 or more blocked queries occur within a 1-hour period.

**Step 1: Create the metric filter**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, then **Log groups**.

1. Select your Route 53 Global Resolver log group, which is located in the observability Region that you set for Route 53 Global Resolver, and then choose **Actions**, **Create metric filter**.

1. For **Filter pattern**, enter the following. This matches any log entry in which a firewall rule blocked the DNS query: `{ $.disposition = "Blocked" }`

1. To verify the pattern works, select a log stream under **Select log data to test** and choose **Test pattern**.

1. Choose **Next**.

1. Provide a filter name, set the metric namespace to `Route53GlobalResolver`, and provide a metric name.

1. Set the metric value to 1 so that each blocked query increments the count.

1. Choose **Dimensions** and add a custom dimension. The dimension name and value can be one of the following.


**Metric filter dimensions for Route 53 Global Resolver logs**  
<a name="gr-metric-filter-dimensions"></a>
<table>
<thead>
  <tr><th>Dimension name</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td><code>DNSViewId</code></td><td><code>$.enrichments[0].data.dns_view_id</code></td></tr>
  <tr><td><code>AccessTokenId</code></td><td><code>$.enrichments[0].data.token_id</code></td></tr>
  <tr><td><code>AccessSourceCidr</code></td><td><code>$.enrichments[0].data.access_source_cidr</code></td></tr>
  <tr><td><code>GlobalResolverId</code></td><td><code>$.enrichments[0].value</code></td></tr>
</tbody>
</table>


1. Choose **Next**, then **Create metric filter**.

**Step 2: Create the alarm**

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Find and select the metric you created, then choose **Select metric**.

1. Configure the alarm as follows, then choose **Next**:
   + For **Statistic**, choose **Sum** to count all blocked queries in the window.
   + For **Period**, choose **1 hour**.
   + For **Whenever**, choose **Greater/Equal** and enter 10 for the threshold.
   + For **Additional configuration**, **Datapoints to alarm**, leave the default of 1.

1. Choose or create an Amazon SNS topic to receive the notification. Choose **Next**.

1. Enter a name and description for the alarm and choose **Next**.

1. Review the configuration and choose **Create alarm**.
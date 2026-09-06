

# Analyzing log data with CloudWatch Log Analytics
<a name="LogAnalytics"></a>

Log Analytics is a unified console experience in Amazon CloudWatch Logs that brings together log analysis capabilities in one place. You can query and analyze log data with CloudWatch Logs Insights, stream logs in real time with Live Tail, and identify your top contributors with CloudWatch Contributor Insights. Log Analytics is the default experience for analyzing logs in the CloudWatch Logs console.

## What you can do with Log Analytics
<a name="LogAnalytics-capabilities"></a>

Log Analytics brings together the following capabilities:
+ **Query and analyze log data** – Run queries against your log groups with CloudWatch Logs Insights. You can run multiple queries in different tabs, save and reuse queries with parameters, explore your data with facets, generate queries using natural language, and visualize results. For more information, see [Analyzing log data with CloudWatch Logs Insights](AnalyzingLogData.md).
+ **Stream logs in near real time** – Use Live Tail to view a streaming list of log events as they are ingested, and filter or highlight the events that matter to you. For more information, see [Troubleshoot with CloudWatch Logs Live Tail](CloudWatchLogs_LiveTail.md).
+ **Identify top contributors** – Use CloudWatch Contributor Insights to analyze high-cardinality log data and see the contributors that have the greatest impact on your system. For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html).

## Get started with Log Analytics
<a name="LogAnalytics-getting-started"></a>

To use Log Analytics, sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), and choose **Log Analytics** under **Logs** in the navigation pane.

Log Analytics is the default experience. If you opt out, you can continue to use CloudWatch Logs Insights, Live Tail, and Contributor Insights as distinct experiences alongside Log Analytics, and you can switch back at any time to Log Analytics.

Log Analytics uses the same pricing as its underlying capabilities: CloudWatch Logs Insights queries, Live Tail, and Contributor Insights. For pricing details, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).
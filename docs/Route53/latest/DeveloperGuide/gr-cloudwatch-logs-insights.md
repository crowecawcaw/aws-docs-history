

# Analyzing Route 53 Global Resolver logs with Amazon CloudWatch Logs Insights
<a name="gr-cloudwatch-logs-insights"></a>

With Amazon CloudWatch Logs Insights, you can interactively search and analyze your Route 53 Global Resolver log data with queries. You can run queries to respond to operational issues and identify patterns in your DNS traffic. For more information, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

1. Before you begin, configure DNS query logging for your global resolver to deliver query logs to Amazon CloudWatch Logs. For more information, see [Configure DNS monitoring and logging with Route 53 Global Resolver](gr-configure-dns-monitoring.md).

1. In the console, navigate to **Route 53**, **Route 53 Global Resolver**, then **Global Resolvers**. Select the global resolver you want, choose the **Analytics** tab, and then choose **Logs Insights**.

1. Select one or more log groups that you want to analyze. When you configure DNS query logging, your global resolver delivers query logs to these log groups.

1. Choose the dimensions to analyze. You can choose from two dimensions: **Metric** and **Action**. Alternatively, you can enter your own CloudWatch Logs Insights query to analyze the log data in other ways.
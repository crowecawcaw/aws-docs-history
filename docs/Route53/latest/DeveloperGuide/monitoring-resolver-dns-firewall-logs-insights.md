

# Analyzing DNS Firewall logs with Amazon CloudWatch Logs Insights
<a name="monitoring-resolver-dns-firewall-logs-insights"></a>

With Amazon CloudWatch Logs Insights, you can interactively search and analyze your DNS Firewall query log data. For more information, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

**To analyze DNS Firewall logs with Amazon CloudWatch Logs Insights**

1. From the **Analytics** tab, choose **Logs Insights**.

1. Select one or more log groups to analyze. These are the log groups that you created for Route 53 VPC Resolver query logging. For more information about selecting fields to index, see [Create field indexes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Field-Indexing-Selection.html).

1. Choose the dimensions to analyze. You can choose from three dimensions: **Resource**, **Metric**, and **Action**.

1. Run the query.
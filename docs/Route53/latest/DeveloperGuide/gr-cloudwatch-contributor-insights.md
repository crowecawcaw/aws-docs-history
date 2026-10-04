

# Using Amazon CloudWatch Contributor Insights with Route 53 Global Resolver data
<a name="gr-cloudwatch-contributor-insights"></a>

Amazon CloudWatch Contributor Insights analyzes log data to create time series that display contributor data. You can see metrics about the top-N contributors, the total number of unique contributors, and their usage. This information helps you find the highest-impact contributors to a system. With Route 53 Global Resolver DNS query logs, you can use Contributor Insights to identify your top query sources, the most-blocked domains, the noisiest access tokens, and other high-impact contributors to your DNS traffic. For more information, see [Using Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html).

1. Before you begin, configure DNS query logging for your global resolver to deliver query logs to Amazon CloudWatch Logs. For more information, see [Configure DNS monitoring and logging with Route 53 Global Resolver](gr-configure-dns-monitoring.md).

1. In the console, navigate to **Route 53**, **Route 53 Global Resolver**, then **Global Resolvers**. Select the global resolver you want, and then choose the **Analytics** tab.
**Note**  
You can access both Contributor Insights and Logs Insights from the **Analytics** tab. You can also select an individual rule group to view its analytics.

1. Choose **Contributor Insights**, then **Create rule**. For more information, see [Create a Contributor Insights rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html).

1. Choose the log group or log groups that contain your Route 53 Global Resolver query logs.

1. For **Rule type**, choose **Sample rule**. Then choose **Select sample rule**, and choose one of the Route 53 Global Resolver Logs sample rules.
**Note**  
Include the global resolver ID in the rule name so that you can identify which global resolver the rule applies to.

1. Selecting one of the sample rules populates all the required fields on the CloudWatch rule page.

1. To view the resulting metrics, open the CloudWatch console, choose **Metrics**, then **All metrics**, and look for the Route 53 Resolver namespace, which includes DNS Firewall metrics.
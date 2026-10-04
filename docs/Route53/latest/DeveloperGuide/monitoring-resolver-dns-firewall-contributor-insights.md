

# Using Amazon CloudWatch Contributor Insights with DNS Firewall data
<a name="monitoring-resolver-dns-firewall-contributor-insights"></a>

Amazon CloudWatch Contributor Insights analyzes log data to create time series that display contributor data. For example, you can view the rule groups and VPCs that produce the most blocked or allowed DNS queries. You can use this data to identify which rule groups, domains, or VPCs generate the most filtered traffic. For more information, see [Using Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html).

**To use Amazon CloudWatch Contributor Insights with DNS Firewall data**

1. Contributor Insights requires Route 53 VPC Resolver query logging for the VPC that you want to analyze. If you haven't enabled query logging for your target VPC, complete the following step to enable it.

1. In the Amazon VPC console, open the Route 53 VPC Resolver query logging page and create a query logging configuration. For the destination, choose an existing CloudWatch Logs log group, or create one (you can create a log group directly from the query logging console). Then associate the configuration with your target VPC. For more information, see [Managing Resolver query logging configurations](resolver-query-logging-configurations-managing.md).

1. In the Amazon VPC DNS Firewall console, open the **Analytics** tab, or open the Amazon CloudWatch Contributor Insights console.
**Note**  
You can access both Contributor Insights and Logs Insights from the **Analytics** tab. You can also select an individual rule group that you're interested in and view its analytics.

1. Choose **Contributor Insights**, then **Create rule**. For more information, see [Create a Contributor Insights rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html).

1. For **Rule type**, choose **Sample rule**. Then choose **Select sample rule** and choose one of the Route 53 DNS Firewall Logs sample rules.
**Note**  
Include the firewall rule group ID in the rule name so that you can identify which rule group the rule applies to.

1. After you select a sample rule, CloudWatch populates all the required fields on the rule page.

1. To view the resulting metrics, open the CloudWatch console. Choose **Metrics**, then **All metrics** (classic metrics), and look for the Route 53 VPC Resolver namespace, which already includes DNS Firewall metrics.
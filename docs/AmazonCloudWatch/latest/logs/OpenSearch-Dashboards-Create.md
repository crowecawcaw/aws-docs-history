# Step 2: Create vended logs dashboards

After you have created the integration, you can create dashboards. Dashboards are
available for Amazon VPC flow logs, CloudTrail logs, and AWS WAF logs.

###### To create a vended log dashboard with metrics derived by OpenSearch Service

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs Insights** and
   then choose the **Analyze with OpenSearch** tab.
3. Choose **Create dashboard**.
4. Choose which type of logs to create the dashboard for, AWS WAF, Amazon VPC flow logs,
   CloudTrail, or AWS Network Firewall.
5. Enter a name for the dashboard, and optionally enter a description.
6. For **Data synchronization frequency**, enter how often that
   you want OpenSearch Service to query CloudWatch so the metrics and indexes created in OpenSearch Service can be
   synchronized and updated with new data. OpenSearch Service creates metrics and indexes on
   your logs for rendering the dashboard.

Choosing a shorter time keeps the data more up to date and incurs higher
costs. 7. Select the log groups to collect data from for this dashboard. Be sure to
select log groups that match the type of dashboard that you are creating.

You can use the **Browse log groups** button and the
**View log samples from selected log groups** option as you
make these choices, to make sure that you get the log groups that you
want. 8. Choose **Create dashboard**.

At first, the dashboard appears without any data. After a few minutes, data
will appear in the dashboard. When the data first appears, it will be for the
most recent 15 minutes of log entries.

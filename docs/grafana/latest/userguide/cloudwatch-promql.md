# Query Amazon CloudWatch metrics using PromQL

You can query Amazon CloudWatch metrics using PromQL by configuring an Amazon Managed Service for Prometheus data
source that points to the CloudWatch PromQL endpoint. This approach lets you use
PromQL syntax to query metrics that are ingested into CloudWatch through OpenTelemetry
Protocol (OTLP).

AWS resource enrichment automatically adds labels such as
`aws_account_id`, `aws_region`, and resource tags to
your metrics. You can use these labels in your PromQL queries for filtering and
aggregation.

Before you configure the CloudWatch PromQL data source, verify the following
requirements:

- [OpenTelemetry metrics in CloudWatch](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.md") ingestion is enabled in your CloudWatch
  account.
- Amazon Managed Grafana workspace version 12.4 or later.
- Amazon Managed Service for Prometheus plugin version 3.0.0 or later.
- IAM permissions for
  `cloudwatch:GetMetricData` and
  `cloudwatch:ListMetrics`.

###### To configure the CloudWatch PromQL data source

1. In your Amazon Managed Grafana workspace, choose
   **Connections** in the navigation pane, then
   choose **Data sources**.
2. Choose **Add data source**, then choose
   **Amazon Managed Service for Prometheus**.
3. For **Prometheus server URL**, enter the CloudWatch
   PromQL endpoint for your Region:
   `https://monitoring.`region`.amazonaws.com`.
4. Under **Authentication**, choose
   **SigV4** as the authentication method.
5. Under **SigV4 Auth Details**, for
   **Service**, enter
   `monitoring`.
6. Choose **Save & test** to verify the
   connection.
   After you save the data source, you can use PromQL queries in Explore and
   dashboards to query CloudWatch metrics that are ingested through OTLP.

![Amazon Managed Grafana Explore view showing a PromQL query for container CPU usage rate with enriched AWS labels available as filters](images/grafana-cloudwatch-promql.png)
For more information about OpenTelemetry metrics ingestion and PromQL queries
in Amazon CloudWatch, see [Introducing OpenTelemetry and PromQL support in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/introducing-opentelemetry-promql-support-in-amazon-cloudwatch/ "https://aws.amazon.com/blogs/mt/introducing-opentelemetry-promql-support-in-amazon-cloudwatch/") on the
AWS Cloud Operations Blog.

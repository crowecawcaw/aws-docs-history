

# Get started with ElastiCache Insights
<a name="ElastiCache-Insights-Get-Started"></a>

ElastiCache Insights requires no setup. As soon as a node‐based Valkey cluster is running, ElastiCache emits a core set of vended OpenTelemetry metrics automatically, at 60‐second granularity and at no additional cost, and the dashboard runs on these metrics. To open the dashboard, see [How to access](ElastiCache-Insights.md#ElastiCache-Insights-access).

**Prerequisites**
+ A node‐based Amazon ElastiCache for Valkey cluster that emits OpenTelemetry metrics. For eligibility, see [Supported configurations](ElastiCache-Insights.md#ElastiCache-Insights-supported).
+ The `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` IAM permissions to view metrics in the dashboard.

To emit additional metrics at 15‐second granularity, select them with a resource metrics configuration. For more information, see [CloudWatch detailed monitoring for OpenTelemetry metrics](resource-metrics-configuration.md).
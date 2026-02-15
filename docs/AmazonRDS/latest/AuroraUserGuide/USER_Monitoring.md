# Viewing metrics in the Amazon RDS console

Amazon RDS integrates with Amazon CloudWatch to display a variety of Aurora DB cluster metrics in the RDS console. Some
metrics are apply at the cluster level, whereas others apply at the instance level. For descriptions of
the instance-level and
cluster-level metrics, see [Metrics reference for Amazon Aurora](metrics-reference.md "metrics-reference.md").

For your Aurora DB cluster, the following categories of metrics are monitored:

- **CloudWatch** – Shows the Amazon CloudWatch metrics for Aurora
  that you can access in the RDS console. You can also access
  these metrics in the CloudWatch console. Each metric includes a graph that shows the metric monitored over
  a specific time span. For a list of CloudWatch metrics,

see [Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.md "Aurora.AuroraMonitoring.md").

- **Enhanced monitoring** – Shows a summary of
  operating-system metrics when your Aurora DB
  cluster has
  turned on Enhanced Monitoring. RDS delivers the metrics from Enhanced Monitoring to
  your Amazon CloudWatch Logs account. Each OS metric includes a graph showing
  the metric monitored over a specific time span. For an overview, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md"). For a list of
  Enhanced Monitoring metrics, see [OS metrics in Enhanced Monitoring](USER_Monitoring-Available-OS-Metrics.md "USER_Monitoring-Available-OS-Metrics.md").
- **OS Process list** – Shows details for each process running in your DB cluster.
- **Performance Insights** – Opens the Amazon RDS Performance Insights dashboard
  for a DB instance in your Aurora DB cluster.
  Performance Insights isn't supported at the cluster level.
  For an overview of Performance Insights, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md"). For a list of Performance Insights metrics, see [Amazon CloudWatch metrics for Amazon RDS Performance Insights](USER_PerfInsights.md "USER_PerfInsights.md").
  Amazon RDS now provides a consolidated view of Performance Insights and CloudWatch metrics in the Performance Insights dashboard.
  Performance Insights must be turned on for your DB cluster to use this view. You can choose the new monitoring
  view in the **Monitoring** tab or **Performance Insights** in the
  navigation pane. To view the instructions for choosing this view, see [Viewing combined metrics with the Performance Insights dashboard](Viewing_Unifiedmetrics.md "Viewing_Unifiedmetrics.md").
